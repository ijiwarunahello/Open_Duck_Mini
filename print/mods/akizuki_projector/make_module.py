"""Generate a flash light module that holds the Akizuki power LED reflector kit (106077).

The kit is a star board LED + BJB 47.313.1000 connector + BJB 47.313.-320 lens holder
+ Nakaza 20 mm aluminium reflector. The stock module bore (D21.9-23.2, 12.7 deep) takes
neither the holder (D22.2) nor the connector ears (25.1 across). This script edits the
stock STL with booleans so the head-side mounting surface stays exactly as upstream.

Run:  uv run --no-project --with trimesh --with manifold3d --with shapely \
          --with networkx --with scipy python make_module.py
All coordinates are the upstream assembly frame (mm). The projector axis is +x.
"""

from pathlib import Path

import numpy as np
import trimesh
from shapely.geometry import Point, Polygon, box
from shapely.ops import unary_union

HERE = Path(__file__).resolve().parent
PRINT = HERE.parent.parent
SRC = PRINT / "flash_light_module.stl"
HEAD = PRINT / "head.stl"

# --- projector axis (measured from the stock part) ---
CY, CZ = 99.093, 144.540  # axis centre in y/z
FLOOR_X = 101.3  # stock bore floor
FRONT_X = 114.0  # stock front face

# --- kit, measured with calipers (2026-11-21) ---
KIT_HEIGHT = 12.7  # a: board back -> holder front
EAR_SPAN = 25.1  # b1: ear tip to ear tip
BODY_WIDTH = 20.3  # b2: width across the ear axis
HOLDER_D = 22.2  # c
WIRE_HEIGHT = 3.6  # d: board back -> wire centre
WIRE_STICKOUT = 5.0  # d': wire beyond the outline, bent
CONNECTOR_TOP = 7.2  # f: board back -> connector top
EAR_PITCH = 19.2  # datasheet: ear hole spacing
EAR_TO_U = 120.0  # datasheet: ear axis vs. the connector's 20.4 mm side (u), deg
# datasheet top view, (u, v) from centre: terminal blocks sit in the +u+v and -u-v corners
BODY_HALF = (10.2, 4.5)  # main body between the side rails
TERMINALS = [(-1.6, 5.0, 10.2, 10.1), (-10.2, -10.1, 1.6, -5.0)]  # u0, v0, u1, v1
WIRE_MOUTH = (10.1, 6.7)  # datasheet scale: terminal mouth (u, v) from centre

# --- design choices ---
CLEAR = 0.2  # radial clearance per side
ALPHA = 35.0  # angle of the connector u axis (deg from +y toward +z)
BOSS_R = 17.0  # added outer material on the free (non-head) side
BOSS_FROM, BOSS_TO = 255.0, 495.0  # boss sector, deg (stays clear of the head)
BOSS_BACK_X = 96.0
CHANNEL_D = 2.8  # wire channel through the body
EXIT_X = 92.0  # wires leave toward the head here (same spot as the stock-head plan)
EXIT_D = 4.0
EXIT_ANGLE = 180.0
PILOT_D = 2.2  # M2.6 self-tapping screw pilot
PILOT_DEPTH = 6.0

TO_WORLD = np.array(
    [[0, 0, 1, 0], [1, 0, 0, CY], [0, 1, 0, CZ], [0, 0, 0, 1]], dtype=float
)  # local (X, Y, Z=axis) -> world (x, y, z)


def rot(p, deg):
    t = np.radians(deg)
    c, s = np.cos(t), np.sin(t)
    return (p[0] * c - p[1] * s, p[0] * s + p[1] * c)


def prism(poly, x0, x1):
    m = trimesh.creation.extrude_polygon(poly, x1 - x0)
    m.apply_translation([0, 0, x0])
    m.apply_transform(TO_WORLD)
    return m


def rod(p0, p1, d):
    """Cylinder between two world points."""
    p0, p1 = np.asarray(p0, float), np.asarray(p1, float)
    seg = trimesh.creation.cylinder(radius=d / 2, segment=[p0, p1], sections=48)
    return seg


def world(x, local_xy):
    return (x, CY + local_xy[0], CZ + local_xy[1])


def sector(r, a0, a1, n=96):
    ts = np.radians(np.linspace(a0, a1, n))
    pts = [(0, 0)] + [(r * np.cos(t), r * np.sin(t)) for t in ts]
    return Polygon(pts)


def build():
    module = trimesh.load(SRC)
    floor = FLOOR_X - 0.3  # a little deeper than the stock floor for the board
    front = floor + KIT_HEIGHT + 0.3
    ear_axis = ALPHA + EAR_TO_U
    ear_r = (EAR_SPAN - EAR_PITCH) / 2

    # added material on the free side
    boss = prism(sector(BOSS_R, BOSS_FROM, BOSS_TO), BOSS_BACK_X, FRONT_X)
    body = trimesh.boolean.union([module, boss], engine="manifold")

    cuts = []
    # holder bore, through the front
    cuts.append(prism(Point(0, 0).buffer(HOLDER_D / 2 + CLEAR, 128), floor, FRONT_X + 1))
    # connector with ears
    core = Point(0, 0).buffer(7.0, 64)
    ears = [unary_union([core, Point(*rot((s * EAR_PITCH / 2, 0), EAR_TO_U)).buffer(ear_r, 64)]).convex_hull for s in (-1, 1)]
    parts = [box(-BODY_HALF[0], -BODY_HALF[1], BODY_HALF[0], BODY_HALF[1]), *[box(*t) for t in TERMINALS], *ears]
    local = unary_union(parts).buffer(CLEAR, join_style=2)
    local = unary_union([local, Point(0, 0).buffer(BODY_WIDTH / 2 + CLEAR, 128)])
    conn = Polygon([rot(p, ALPHA) for p in local.exterior.coords])
    # the connector goes in from the front, so its outline runs through to the front face
    cuts.append(prism(conn, floor, FRONT_X + 1))

    wire_x = floor + 0.3 + WIRE_HEIGHT
    for s in (-1, 1):
        mu, mv = s * WIRE_MOUTH[0], s * WIRE_MOUTH[1]
        # pocket where the wire leaves the terminal and bends back
        u0, u1 = sorted((mu - s * 1.0, mu + s * 2.6))
        pocket = Polygon([rot(p, ALPHA) for p in [(u0, mv - 1.6), (u1, mv - 1.6), (u1, mv + 1.6), (u0, mv + 1.6)]])
        cuts.append(prism(pocket, floor, FRONT_X + 1))  # the bent wire stub passes down from the front
        # channel from the bend down through the body to the exit point on the axis
        bend = rot((mu + s * 1.5, mv), ALPHA)
        cuts.append(rod(world(wire_x, bend), world(EXIT_X, (0, 0)), CHANNEL_D))
        cuts.append(trimesh.creation.icosphere(radius=CHANNEL_D / 2, subdivisions=3).apply_translation(world(wire_x, bend)))
        # screw pilots in the ear positions
        ear_c = rot((s * EAR_PITCH / 2, 0), ear_axis)
        cuts.append(rod(world(floor - PILOT_DEPTH, ear_c), world(floor + 0.1, ear_c), PILOT_D))

    # exit toward the head
    exit_dir = rot((25.0, 0), EXIT_ANGLE)
    cuts.append(rod(world(EXIT_X, (0, 0)), world(EXIT_X, exit_dir), EXIT_D))

    cut = trimesh.boolean.union(cuts, engine="manifold")
    out = trimesh.boolean.difference([body, cut], engine="manifold")
    return out, cut, front


def main():
    out, cut, front = build()
    out.export(HERE / "flash_light_module_akizuki.stl")
    box = trimesh.creation.box(bounds=[[98.0, 60, 100], [130, 140, 190]])
    test = trimesh.boolean.intersection([out, box], engine="manifold")
    test.export(HERE / "flash_light_module_akizuki_test.stl")

    head = trimesh.load(HEAD)
    stock = trimesh.load(SRC)
    def overlap(a):
        i = trimesh.boolean.intersection([a, head], engine="manifold")
        return 0.0 if i.is_empty else i.volume
    print(f"watertight={out.is_watertight} volume={out.volume:.0f} (stock {stock.volume:.0f})")
    print(f"test piece watertight={test.is_watertight} volume={test.volume:.0f}")
    print(f"head overlap: stock={overlap(stock):.2f} new={overlap(out):.2f} mm^3")
    print(f"holder front at x={front:.2f} (module front {FRONT_X})")


if __name__ == "__main__":
    main()
