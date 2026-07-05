> まだ最終版ではありません

# 実機に転移する方策の学習 (sim2real)

実機にうまく転移する方策を学習したい。これが sim2real 問題です。特に安価で制御精度の高くないサーボモーターを使用している我々にとっては難しい問題です。

以下では、我々がそこに到達するまでの手順をおおまかに説明しますが、各プロセスの結果は提供しているため、すべてを自分でやり直す必要はありません。

## ロボットの正確なモデルを作る (URDF/MJCF)

### ロボットの構造

[OnShape ドキュメント](https://cad.onshape.com/documents/64074dfcfa379b37d8a47762/w/3650ab4221e215a4f65eb7fe/e/0505c262d882183a25049d05)で各部品のマテリアルを指定しています。ただし、インフィルを使用して印刷するため、スライサーの (かなり正確な) 質量推定値で部品の質量を上書きしています。

[onshape-to-robot](https://github.com/Rhoban/onshape-to-robot) を使用して URDF/MJCF 記述をエクスポートしています。MJX 用には軽量モデルを作る必要があります。我々の [config.json](https://github.com/apirrone/Open_Duck_Playground/blob/main/playground/open_duck_mini_v2/xmls/config.json) を参照してください。

これにより、ロボットの質量と慣性モーメントを記述する MJCF (MuJoCo フォーマット) [ロボット記述](https://github.com/apirrone/Open_Duck_Playground/blob/main/playground/open_duck_mini_v2/xmls/open_duck_mini_v2.xml)が得られます。

### モーター

正確なモデルを作るもう一つの非常に重要な要素はモーターの挙動のモデリングです。これには [BAM](https://github.com/Rhoban/bam/) を使用しています。同定プロセスを自分で行う必要はなく、結果は[ここ](https://github.com/Rhoban/bam/tree/main/params/feetech_sts3215_7_4V)で提供しています。

シミュレータがモーターを正確にシミュレートすることは極めて重要です。方策 (ニューラルネットワーク) はセンサ入力 (モーター位置/速度、IMU、足センサ) に基づいてモーター位置を出力するように学習するためです。シミュレーションと実機でモーターの挙動が異なると、方策は機能しないか、最悪の場合カオス的な動きを生み出します。

`BAM` は同定した主要パラメータを MuJoCo 単位にエクスポートできます (`bam.to_mujoco` を使用)。これらの値を MJCF モデルのアクチュエータおよびジョイント特性に設定します。

- damping
- kp
- frictionloss
- armature
- forcerange

## 方策の学習

我々独自の [mujoco playground](https://github.com/google-deepmind/mujoco_playground) ベースのフレームワーク、[Open Duck Playground](https://github.com/apirrone/Open_Duck_Playground) を使用しています。

[joystick](https://github.com/apirrone/Open_Duck_Playground/blob/main/playground/open_duck_mini_v2/joystick.py) 環境では、異なる報酬の有効化/無効化、独自の報酬の作成、重みやノイズ、ランダム化のパラメータ調整を試すことができます。

Disney が [BDX 論文](https://github.com/apirrone/Open_Duck_Playground/blob/main/playground/open_duck_mini_v2/joystick.py)で説明している模倣報酬を実装することで良好な結果を得ました。

この報酬を使用するにはリファレンスモーションが必要です。パラメトリック歩行エンジンを使ってこのようなモーションを生成する[リポジトリ](https://github.com/apirrone/Open_Duck_reference_motion_generator)を作成しました。そこの手順に従って `polynomial_coefficients.pkl` ファイルを生成できます。playground リポジトリの `data/` ディレクトリにはすでにこのファイルが含まれています。

方策の学習が完了したら、Runtime リポジトリの[このスクリプト](https://github.com/apirrone/Open_Duck_Mini_Runtime/blob/v2/scripts/v2_rl_walk_mujoco.py)を使って実機で動かすことができます。実行前に[チェックリスト](https://github.com/apirrone/Open_Duck_Mini_Runtime/blob/v2/checklist.md)のすべてのステップを完了していることを確認してください。
