# MuJoCo シミュレーション用のロボット準備

## OnShape で設計した場合

### onshape-to-robot の制約に従って設計されていることを確認
https://onshape-to-robot.readthedocs.io/en/latest/design.html


URDF には `closing_<...>_1` と `closing_<...>_2` という名前のフレームが含まれます。これを使って MJCF ファイルでループを閉じることができます。

### OnShape から URDF を取得

以下を実行:

```bash
$ onshape-to-robot robots/bd1/
```

#### (オプション) 閉ループがある場合は onshape-to-robot のドキュメントに従って処理した後:

`robot.urdf` に以下を追加:
```xml
<robot name="...">
    <mujoco>
        <compiler fusestatic="false"/>
    </mujoco>
	...
</robot>
```

# URDF を MJCF (MuJoCo) に変換

## MuJoCo バイナリの取得

MuJoCo のバイナリを任意の場所にダウンロード: https://github.com/google-deepmind/mujoco/releases

展開して以下を実行:

```bash
$ ./compile robot.urdf robot.xml
```

## robot.xml にアクチュエータを追加:
例:
```xml
	<actuator>
		<position name="left_hip_yaw"    joint="left_hip_yaw"    inheritrange="1"/>
		<position name="left_hip_roll"   joint="left_hip_roll"   inheritrange="1"/>
		<position name="left_hip_pitch"  joint="left_hip_pitch"  inheritrange="1"/>
		<position name="left_knee"       joint="left_knee"       inheritrange="1"/>
		<position name="left_ankle"      joint="left_ankle"      inheritrange="1"/>
		<position name="right_hip_roll"  joint="right_hip_roll"  inheritrange="1"/>
		<position name="right_hip_yaw"   joint="right_hip_yaw"   inheritrange="1"/>
		<position name="right_hip_pitch" joint="right_hip_pitch" inheritrange="1"/>
		<position name="right_knee"      joint="right_knee"      inheritrange="1"/>
		<position name="right_ankle"     joint="right_ankle"     inheritrange="1"/>
		<position name="head_pitch1"     joint="head_pitch1"     inheritrange="1"/>
		<position name="head_pitch2"     joint="head_pitch2"     inheritrange="1"/>
		<position name="head_yaw"        joint="head_yaw"        inheritrange="1"/>
	</actuator>
```

## freejoint の追加

body を freejoint で囲む:
```xml
<worldbody>
	<body>
		<freejoint />
		...
		...
	</body>
</worldbody>
```

## (オプション) 閉ループの拘束

MJCF ファイルに以下を追加:
```xml
<equality>
    <connect body1="closing_<...>_1" body2="closing_<...>_2" anchor="x y z" />
</equality>
```

x, y, z の値は `.urdf` 内で確認できる:

```xml
<joint name="closing_<...>_1_frame" type="fixed">
	<origin xyz="x y z" rpy="r p y" />
	...
</joint>
```

## 衝突グループ、ダンピング、摩擦の設定
/!\ ジョイントの actuatorfrcrange を削除すること。
以下を `<mujoco>` タグ内に配置:
```xml
<mujoco>
  <default>
    <geom contype="1" conaffinity="1" solref=".004 1" />
    <joint damping="0.09" frictionloss="0.1"/>
    <position kp="10" forcerange="-5.0 5.0"/>
  </default>
	...
	...
</mujoco>
```

まだ必要な作業:
- frame を site に変更


## 可視化

```bash
$ python3 -m mujoco.viewer --mjcf=<path>/scene.xml
```

または

```bash
$ <path_to_mujoco_bin>/bin/simulate <path>/scene.xml
```
