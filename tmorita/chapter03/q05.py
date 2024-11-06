#0度から360度まで1度刻みの三角関数の値をまとめた三角関数表を画面に出力するプログラムを作成
import numpy as np

#角度を0度から360度まで1度刻みで生成
angles = np.arange(0, 361, 1)

print(f"{'角度':>6} {'sin':>10} {'cos':>10} {'tan':>10}")
print("-" * 36)

#各角度に対してsin, cos, tanを計算し出力
for angle in angles:
    radian = np.radians(angle)  # 角度をラジアンに変換
    sin_val = np.sin(radian)
    cos_val = np.cos(radian)
    tan_val = np.tan(radian) if cos_val != 0 else None  # cosが0の場合はtanは定義されない

    if tan_val is None:
        print(f"{angle:>6} {sin_val:>10.4f} {cos_val:>10.4f} {'undefined':>10}")
    else:
        print(f"{angle:>6} {sin_val:>10.4f} {cos_val:>10.4f} {tan_val:>10.4f}")