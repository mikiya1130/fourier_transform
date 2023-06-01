"""高速フーリエ変換"""

import numpy as np


def is_pow2(x):
    if x <= 0:
        return False
    return (x & (x - 1)) == 0


def fft(x):
    def _fft(x):
        n = len(x)
        x1 = x[: n // 2]
        x2 = x[n // 2 :]
        w = np.array(
            [complex(np.cos(i * 2 * np.pi / n), -np.sin(i * 2 * np.pi / n)) for i in range(n // 2)]
        )
        x = np.concatenate((x1 + x2, (x1 - x2) * w))
        return x

    n = len(x)
    if not is_pow2(n):
        raise ValueError("高速フーリエ変換はデータ数が2の累乗の場合のみ")

    for i in range(int(np.log2(n))):
        x = np.concatenate(
            [_fft(x[j * (n // (2**i)) : (j + 1) * (n // (2**i))]) for j in range(2**i)]
        )

    x = x.reshape(*((2,) * int(np.log2(n)))).T.flatten()

    return x
