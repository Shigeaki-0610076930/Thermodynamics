import numpy as np

# パラメータ設定
a = 0.1  # 温度伝導率
dt = 5  # 時間刻み幅
dx = 1  # 空間刻み幅

# グリッドの設定
nx = 6  # 座標点の数
nt = 100  # タイムステップ数

# 初期条件の設定
T = 20 * np.ones(nx)
T[0] = 0
T[-1] = 20

# 陽解法による数値解法
for n in range(nt):
    Tn = T.copy()
    for i in range(1, nx - 1):
        T[i] = Tn[i] + a * dt / dx**2 * (Tn[i+1] - 2*Tn[i] + Tn[i-1])

    # 安定時刻までの各座標T[i]の値をプリントアウト
    print(f"Time step {n}: {T}")
