#0度から360度まで1度刻みの三角関数の値をまとめた三角関数表を画面に出力するプログラムを作成してください． 三角関数表は，例えば以下のようなものになります．
import math
#mathモジュールをインポートし、三角関数や度からラジアンへの変換を行う
print("θ[°]\tsin(θ)\t\tcos(θ)\t\ttan(θ)")
#表のヘッダーを出力
for θ in range(5):         #0度から4度までの範囲でループを回す
    rad = math.radians(θ)  #角度をラジアンに変換(三角関数は度単位ではなくラジアン単位で計算されるため)
    sin_val = math.sin(rad)
    cos_val = math.cos(rad)#sin,cos,tanの値を計算し、格納
    tan_val = math.tan(rad) if cos_val != 0 else float('無限')
    #tanの場合、cosが0になると値が無限大になるため、cos==0の時に無限を表示
    print(f"{θ} \t{sin_val:.5f} \t{cos_val:.5f} \t{tan_val:.5f}")
    #小数点以下5桁まで表示する
