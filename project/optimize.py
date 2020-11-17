import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='NanumGothic')
plt.rc('axes', unicode_minus=False)

np.random.seed(seed=1)
X_min = 4
X_max = 30
X_n = 16
X = 5 + 25 * np.random.rand(X_n)
Prm_c = [170, 108, 0.2]
T = Prm_c[0] - Prm_c[1] * np.exp(-Prm_c[2] * X) \
    + 4 * np.random.randn(X_n)


def dmse_line(x, t, w):
    y = w[0] * x + w[1]
    d_w0 = 2 * np.mean((y - t) * x)
    d_w1 = 2 * np.mean(y - t)
    return d_w0, d_w1


# 경사하강법
def fit_line_num(x, t):
    w_init = [10.0, 165.0]
    alpha = 0.001  # 학습률
    i_max = 100000
    eps = 0.1  # 종료 판정
    w_i = np.zeros([i_max, 2])  # w0, w1을 넣을 리스트
    w_i[0, :] = w_init  # 최초의 10, 165 를 0번째 자리에 넣음
    for i in range(1, i_max):
        dmse = dmse_line(x, t, w_i[i - 1])  # X, T와 i(10, 165) 저장
        w_i[i, 0] = w_i[i - 1, 0] - alpha * dmse[0]  # a
        w_i[i, 1] = w_i[i - 1, 1] - alpha * dmse[1]  # b
        if max(np.absolute(dmse)) < eps:
            break
    w0 = w_i[i, 0]
    w1 = w_i[i, 1]
    w_i = w_i[:i, :]
    return w0, w1, dmse, w_i  # w0 = 기울기, w1 = 절편


def mse_line(x, t, w):
    y = w[0] * x + w[1]
    mse = np.mean((y - t)**2)
    return mse


def f1(x):
    # x^2 -4x + 6
    return (x - 2)**2 + 2


def f1d(x):
    # 2x - 4
    return 2 * (x - 2.0)


W0, W1, dMSE, W_history = fit_line_num(X, T)


def show_line(w):
    xb = np.linspace(X_min, X_max, 100)
    y = w[0] * xb + w[1]
    plt.plot(xb, y, color=(.5, .5, .5), linewidth=4)


plt.figure(figsize=(4, 4))
W = np.array([W0, W1])
mse = mse_line(X, T, W)
print("w0={0:.3f}, w1={1:.3f}".format(W0, W1))
print("SD={0:.3f} cm".format(np.sqrt(mse)))
show_line(W)
plt.plot(X,
         T,
         marker='o',
         linestyle='None',
         color='cornflowerblue',
         markeredgecolor='black')
plt.xlim(X_min, X_max)
plt.grid(True)
plt.show()


# 2차원 로젠브록 함수
def f2(x, y):
    return (1 - x)**2 + 100.0 * (y - x**2)**2


def f2g(x, y):
    """f2(x, y)의 도함수"""
    # 2차원 로젠브록 함수의 도함수
    # (1 - x)**2 + 100.0 * (y - x**2)**2
    return np.array(
        (2.0 * (x - 1) - 400.0 * x * (y - x**2), 200.0 * (y - x**2)))


def momentum():
    i_max = 10000  # 실행 횟수
    alpha = 0.00089  # 학습률
    eps = 0.000001  # 오차 범위
    m = 0.7  # 모멘텀 계수

    w_init = [-2, -2]
    w_i = np.zeros([i_max, 2])
    w_i[0, :] = w_init
    x = w_init[0]
    y = w_init[1]
    vx = 0
    vy = 0
    XY = list()
    XY.append([x, y])
    iter = 0
    for i in range(1, i_max):
        fdx = f2g(x, y)
        vx = m * vx - alpha * fdx[0]
        vy = m * vy - alpha * fdx[1]
        x += vx
        y += vy
        iter = i
        w_i[i, 0] = x
        w_i[i, 1] = y
        XY.append([x, y])
        if f2(x, y) < eps:
            break

    print(x, y)
    print(iter)
    print(XY)

    XY = np.array(XY)
    return XY


def show_contour():
    xx = np.linspace(-4, 4, 800)
    yy = np.linspace(-3, 3, 600)
    X, Y = np.meshgrid(xx, yy)
    Z = f2(X, Y)

    levels = np.logspace(-1, 3, 10)
    plt.contourf(X, Y, Z, alpha=0.2, levels=levels)
    plt.contour(X,
                Y,
                Z,
                colors="gray",
                levels=[0.4, 3, 15, 50, 150, 500, 1500, 5000])
    plt.plot(XY[:, 0], XY[:, 1], 'g*-')
    plt.plot(1, 1, 'ro', markersize=10)

    plt.xlim(-4, 4)
    plt.ylim(-3, 3)
    plt.xticks(np.linspace(-4, 4, 9))
    plt.yticks(np.linspace(-3, 3, 7))
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.title("모멘텀 알고리즘")
    plt.show()


def show_3d():
    x = np.linspace(-2, 2, 200)
    y = np.linspace(-2, 2, 200)
    X, Y = np.meshgrid(x, y)
    Z = f2(X, Y)
    fig = plt.figure(figsize=(5, 5))
    ax = fig.gca(projection='3d')
    ax.view_init(45, 230)
    ax.plot_surface(X, Y, Z, color='g', alpha=0.7)
    ax.scatter(1, 1, 0, 'ro')
    ax.scatter(-2, -2, f2(-2, -2), 'ro')
    ax.plot(XY[:, 0], XY[:, 1], [f2(x, y) for x, y in XY], color='r')
    plt.show()


XY = momentum()
show_contour()
show_3d()

import unittest


class test(unittest.TestCase):
    def testMomentum(self):
        momentum()


if __name__ == '__main__':
    unittest.main()
