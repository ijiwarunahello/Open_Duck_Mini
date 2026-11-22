# 組み立てガイド

> 組み立てを始める前に、まず[モーターの設定](./configure_motors.md)を完了してください。

## 必要なもの:

以下を用意してください:
- はんだごて、基本的な電子工作工具と技能
- M3 ネジ各種 (TODO: 正確な本数を追加)
- ワイヤー
- Loctite ネジロック剤 青243

> 一般的な注意: モーターに金属ネジを金属に対してねじ込む際は、少量のネジロック剤を使用してください。これはロボット動作中の振動によるネジの緩みを防止します。ビルドに少し時間がかかりますが、やっておいて良かったと思えるはずです ;)
>
> プラスチックネジにはネジロック剤を使わないでください。

> いつでも CAD を参照できます: https://cad.onshape.com/documents/64074dfcfa379b37d8a47762/w/3650ab4221e215a4f65eb7fe/e/0505c262d882183a25049d05

## 手順:

### トランク (胴体) の組み立て

`trunk_bottom` にベアリングを以下のように配置し、これらの穴に M3 インサートを挿入します。後でボディパーツを取り付けるために、この部品の底面にある 4 つの M3 インサート穴にも今のうちに挿入しておきましょう。

<img src="https://github.com/user-attachments/assets/9ed8591a-7c96-4410-8d7e-9b7d88c6bd1f" alt="1" width="500px" >

次に `trunk_bottom` と `trunk_top` を組み合わせ、これらの穴を通して `M3x10` ネジ 2 本で固定します。

<img src="https://github.com/user-attachments/assets/ae36b396-a34a-4691-8e62-fd916cd1f76c" alt="1" width="500px" >

中央モーターを以下のように取り付け、モーター付属のプラスチックネジで固定します:

<img src="https://github.com/user-attachments/assets/d4a6ba6c-852f-440e-afb7-3b9ca66ad3dc" alt="1" width="500px" >

`roll_motor_bottom` を以下のように挿入します。

<img src="https://github.com/user-attachments/assets/31c031b7-58b8-4c4c-a3fa-1f14a310c2f2" alt="1" width="500px" >


### 足の組み立て

両足とも同じ構造です。

まず `foot_bottom_tpu` と `foot_bottom_pla` を組み合わせます。以下の穴に M3 インサートを挿入:

<img src="https://github.com/user-attachments/assets/6749a5ba-cea9-4b0a-ac32-f32e130fd057" alt="1" width="500px" >

`M3x6` ネジ 2 本で 2 つの部品を固定します。

次に `foot_top` の以下の穴に M3 インサートを挿入:

<img src="https://github.com/user-attachments/assets/1a77f2f8-56ea-43d2-91c7-78130456c45b" alt="1" width="500px" >

以下のようにすべてを組み立てます。モーターのドライバ側が `foot_top` パーツ側に来るようにしてください:

<table>
  <tr>
    <td> <img src="https://github.com/user-attachments/assets/197cd9b7-05a6-46ed-9af5-d2def37970c8" alt="1" width="500px" > </td>
    <td> <img src="https://github.com/user-attachments/assets/f532fbcc-100b-4715-96a8-66697e4fda26" alt="1" width="500px" > </td>
   </tr> 
</table>

フットスイッチもここで取り付けます:

> 足が地面に接触した時にスイッチが作動するように圧入します。

<table>
  <tr>
    <td> <img src="https://github.com/user-attachments/assets/71b9ad91-864e-423f-97a3-911d65182ab9" alt="1" width="500px" > </td>
    <td> <img src="https://github.com/user-attachments/assets/59e15c7c-3515-4408-bfe9-80e30c4cd007" alt="1" width="500px" > </td>
   </tr> 
</table>


### 脛 (シン) の組み立て

`leg_spacer` の以下の穴に M3 インサートを挿入します (両側。合計 4 つの M3 インサートを挿入):

<img src="https://github.com/user-attachments/assets/41eb01a2-d6f9-43b1-a83e-d14785907425" alt="1" width="500px" >

次に、まず足のモーターにモーターケーブルを接続し、以下のように `right_sheet` を通します。

<img src="https://github.com/user-attachments/assets/a1432505-6b6c-4765-aea6-0a7a0b8b220b" alt="1" width="500px" >

以下のように組み立てます:

<img src="https://github.com/user-attachments/assets/54615217-fec9-46dd-8b40-e21a4f527b55" alt="1" width="500px" >

### 腿 (サイ) の組み立て

腿は基本的に脛と同じですが、`hip_pitch` モーターの取り付け方向が異なります (ゼロ位置にとって重要):

<img src="https://github.com/user-attachments/assets/951157a4-26dc-41bb-b97f-18dbbb0c1cd3" alt="1" width="500px" >

### ヒップの組み立て

`left_roll_to_pitch` または `right_roll_to_pitch` を取り付けます。これらは対称パーツなので正しい側のものを使用してください。

<img src="https://github.com/user-attachments/assets/368a85ad-1c58-4db2-bdd0-812334b6c784" alt="1" width="500px" >

`roll_motor_top` を `hip_yaw` サーボに取り付けます (底面からネジ止め)。まだサーボをトランクには取り付けないでください。


<img src="https://github.com/user-attachments/assets/768f1664-030c-4432-9071-c52d79d3ef6b" alt="1" width="500px" >

次に `hip_roll` を以下のように取り付けます。

<img src="https://github.com/user-attachments/assets/e1287f67-320c-42cf-a5dc-84f4c64abb17" alt="1" width="500px" >

サブアセンブリを以下のように挿入します。

<img src="https://github.com/user-attachments/assets/dba458ae-e9cb-4e16-a82e-cbe74d2350fa" alt="1" width="500px" >

固定できるところをすべてネジ止めします (サーボ付属のプラスチックネジを使用)。

脚を以下のように取り付けます:

<img src="https://github.com/user-attachments/assets/a7169791-9f0a-4827-aea7-00ab1d0f6212" alt="1" width="500px" >

反対側の脚も同様に行います :)

ダックはこのような状態になっているはずです:

<img src="https://github.com/user-attachments/assets/4921b29b-b38b-423d-9da1-1c8f84689e84" alt="1" width="500px" >

### 首の組み立て

手順は同じ要領です。

<img src="https://github.com/user-attachments/assets/f96fe44f-a7bc-423e-a925-4aef3e7bf568" alt="1" width="500px" >

### ヘッド機構の組み立て

まず `head_pitch_to_yaw` を以下のように取り付けます。

<img src="https://github.com/user-attachments/assets/a4dba395-eb0d-4150-8980-8e14f1173d02" alt="1" width="500px" >

次に、`head_yaw_to_roll` と `head_roll_mount` を独立して `head_roll dof` に取り付けます。

<img src="https://github.com/user-attachments/assets/4648cd6c-391e-41e4-9617-4ecebfa9215b" alt="1" width="500px" >

(後でヘッドを分解せずに済むよう、ここで `head_bot_plate` と `body_middle_top` も挿入しておくとよいです)

次に:

<img src="https://github.com/user-attachments/assets/03f3bdae-06c3-4c37-b68f-14587edd6123" alt="1" width="500px" >

次に:

<img src="https://github.com/user-attachments/assets/04a219d8-bbaf-4910-b5d3-7ca67bce466c" alt="1" width="500px" >

ダックはこのような状態になっているはずです:

<img src="https://github.com/user-attachments/assets/71545d40-f0f5-411d-a8d5-1cd676a74e75" alt="1" width="500px" >

### サーボドライバーボードの取り付け

TODO: 写真を撮る

### IMU の取り付け

以下のように:

> 実際には IMU を正しい自然な向き (下の写真から X 軸方向に反転) で取り付ける方が良いです。
> 下の写真では IMU が逆さまに取り付けられています。
> 逆さまに取り付けてもそこまで大きな問題にはなりません。取り付け向きは後でソフトウェアで設定できます。

<table>
  <tr>
    <td> <img src="https://github.com/user-attachments/assets/8772996d-5906-48fa-8cbe-6b6823982375" alt="1" width="500px" ></td>
    <td> <img src="https://github.com/user-attachments/assets/172f44c7-c7c6-47f8-894a-14024abd24f4" alt="2" width="500px" ></td>
   </tr> 
</table>

## 電子部品

全体の電子配線図を参考として示します。

<table>
  <tr>
    <td> <img src="open_duck_mini_v2_wiring_diagram.png" alt="1" width="500px" ></td>
    <td> <img src="wiring.png" alt="2" width="500px" ></td>
   </tr> 
</table>

足の配線方法:

![feet](https://github.com/user-attachments/assets/d3376494-4690-4484-8352-132e6284731a)

Pi Zero ヘッダーのピンマッピング:

|       **LED**       | **Pi Zero ヘッダーピン** | **Pi Zero 機能** |
|:-------------------:|:----------------------:|:--------------------:|
|  左目 アノード (+)  |           16           |        GPIO 23       |
| 右目 アノード (+)   |           18           |        GPIO 24       |
| プロジェクタ アノード (+) |           22           |        GPIO 25       |
|  共通カソード (-)   |            6           |          GND         |
|                     |                        |                      |
|     **アンテナ**    |                        |                      |
|       左 PWM        |           32           |     GPIO 12 (PWM)    |
|       右 PWM        |           33           |     GPIO 13 (PWM)    |
|          5V         |            2           |          5V          |
|         GND         |            6           |          GND         |
|                     |                        |                      |
|  **フットスイッチ** |                        |                      |
|       左足          |           15           |        GPIO 22       |
|       右足          |           13           |        GPIO 27       |
|         GND         |            9           |          GND         |
|                     |                        |                      |
|      **BNO055**     |                        |                      |
|         VIN         |            1           |          3V3         |
|         3VO         |           NC           |           -          |
|         GND         |            9           |          GND         |
|         SDA         |            3           |        GPIO 2        |
|         SCL         |            5           |        GPIO 3        |
|         RST         |           NC           |           -          |
|                     |                        |                      |
|    **MAX98357A**    |                        |                      |
|         LRC         |           35           |        GPIO 19       |
|         BCLK        |           12           |        GPIO 18       |
|         DIN         |           40           |        GPIO 21       |
|         GAIN        |           NC           |           -          |
|          SD         |           NC           |           -          |
|         GND         |            6           |          GND         |
|         VIN         |            2           |          5V          |

### バッテリーパック

> 安全のため、セルをホルダーに入れる前に同じ電圧まで充電されていることを確認してください。

<table>
  <tr>
    <td> <img src="https://github.com/user-attachments/assets/371db809-7cb3-47e1-b277-7fc2bdf21025" alt="1" width="500px" ></td>
    <td> <img src="https://github.com/user-attachments/assets/3acfa4e6-ecf7-41f6-a965-35a3040f52fb" alt="2" width="500px" ></td>
   </tr> 
</table>


### ヘッド

まず、以下のすべての穴に M3 インサートを挿入します。

![image](https://github.com/user-attachments/assets/ef4cd513-6b8d-41fa-9cc3-149fc8333d3e)

> TODO: 表情機能 (カメラ、アンテナ、目の LED、プロジェクタ、スピーカー) の手順を追加

次にベアリングを挿入し、耳のモーターと Raspberry Pi Zero 2W を取り付けます。

参考: ヘッドの内部は現在このようになっています。

![image](https://github.com/user-attachments/assets/91284081-a563-4c02-bb3d-194b3afbc25c)


首とヘッドを以下のように接続します。

![image](https://github.com/user-attachments/assets/96fd5347-bff7-47e9-a7bd-fde17ab1bcd2)


## ボディ

まず `body_middle_bottom` をネジ止めします。

![Capture d'écran du 2025-02-09 12-10-00](https://github.com/user-attachments/assets/081d8840-8e88-4938-9d9a-4d97614e6261)

次に `body_middle_bottom` と `body_middle_top` のすべての穴に M3 インサートを挿入します。ここにバッテリーパックと `body_front` を取り付けます。

`body_middle_top`、`body_front`、バッテリーパックを取り付けます。

<table>
  <tr>
    <td> <img src="https://github.com/user-attachments/assets/679a9cd2-89ca-41e8-9d03-f93fc040068b" alt="1" width="500px" ></td>
    <td> <img src="https://github.com/user-attachments/assets/ca292c48-1c72-4649-b7d1-4d3c9eac62ac" alt="2" width="500px" ></td>
   </tr> 
</table>

完成です :)

<table>
  <tr>
    <td> <img src="https://github.com/user-attachments/assets/312ec747-8eb4-4145-92eb-c1c3ddba80da" alt="1" width="500px" ></td>
    <td> <img src="https://github.com/user-attachments/assets/864d9dd7-3daf-4e63-913c-2e99157e4aaf" alt="2" width="500px" ></td>
   </tr> 
</table>


> ダックの組み立てが完了したら、Raspberry Pi とランタイムソフトウェアのセットアップを[こちら](https://github.com/apirrone/Open_Duck_Mini_Runtime)で行ってください。
