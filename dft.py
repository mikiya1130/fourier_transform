"""フーリエ変換"""

import numpy as np


def dft(x):
    N = len(x)
    W = np.array(
        [
            [
                complex(np.cos(i * j * 2 * np.pi / N), -np.sin(i * j * 2 * np.pi / N))
                for j in range(N)
            ]
            for i in range(N)
        ]
    )

    return np.array([w * x for w in W]).sum(axis=1)
