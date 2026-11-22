# モーターの設定

> この作業はダックを組み立てる**前**に、各モーターに対して個別に行う必要があります。
>
> 設定中にモーターがゼロ位置に移動します。その状態でホーンを取り付け、下の写真のようにできるだけ正確に位置合わせしてください。(完璧でなくても後でソフトウェアで補正できます)

![Capture d'écran du 2025-04-25 09-55-34](https://github.com/user-attachments/assets/e3c4aefa-5e0a-4d4e-89f4-82df9bf30e29)


Runtime リポジトリの `v2` ブランチをクローンしてインストール (`pip install -e .`) してください: `https://github.com/apirrone/Open_Duck_Mini_Runtime`

設定作業は PC でも Raspberry Pi でも実行できます。サーボに電力を供給する手段 (バッテリーパック等) があれば大丈夫です。


各モーターに対して以下のコマンドを実行します:

```bash
python configure_motor.py --id <id>
```

モーター ID の一覧:

```python
{
    "left_hip_yaw": 20,
    "left_hip_roll": 21,
    "left_hip_pitch": 22,
    "left_knee": 23,
    "left_ankle": 24,
    "neck_pitch": 30,
    "head_pitch": 31,
    "head_yaw": 32,
    "head_roll": 33,
    "right_hip_yaw": 10,
    "right_hip_roll": 11,
    "right_hip_pitch": 12,
    "right_knee": 13,
    "right_ankle": 14,
}
```
