import numpy as np

from dft import dft
from fft import fft

# ndarray 型 print() 時の表示設定
np.set_printoptions(precision=3, floatmode="fixed")  # 小数点以下3桁で0埋め
np.set_printoptions(suppress=True)  # 指数表記しない

# 対象データ
f = np.array(
    [
        complex(0, 2**0.5),
        complex(-1, 1),
        complex(-(2**0.5), 0),
        complex(-1, -1),
        complex(0, -(2**0.5)),
        complex(1, -1),
        complex(2**0.5, 0),
        complex(1, 1),
    ]
)

# 計算結果
print("DFT:")
print(dft(f))
print("-" * 80)
print("FFT:")
print(fft(f))
