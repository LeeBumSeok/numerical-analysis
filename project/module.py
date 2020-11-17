import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import unittest

plt.rc('font', family='NanumGothic')
plt.rc('axes', unicode_minus=False)


class optimization:
    def __init__(self, start_x, start_y, i_max, alpha, eps, m):
        self.start_x = start_x
        self.start_y = start_y
        self.i_max = i_max
        self.alpha = alpha
        self.eps = eps
        self.m = m

    def f2(self, x, y):
        # 2차원 로젠브록 함수
        return (1 - x)**2 + 100.0 * (y - x**2)**2

    def f2g(self, x, y):
        # 2차원 로젠브록 함수의 도함수
        return np.array(
            (2.0 * (x - 1) - 400.0 * x * (y - x**2), 200.0 * (y - x**2)))

    def rosenbrock_momentum(self):
        w_init = [self.start_x, self.start_y]
        w_i = np.zeros([self.i_max, 2])
        w_i[0, :] = w_init
        x = w_init[0]
        y = w_init[1]
        vx = 0
        vy = 0
        XY = list()
        XY.append([x, y])
        cnt = 0
        for i in range(1, self.i_max):
            fdx = self.f2g(x, y)
            vx = self.m * vx - self.alpha * fdx[0]
            vy = self.m * vy - self.alpha * fdx[1]
            x += vx
            y += vy
            cnt = i
            w_i[i, 0] = x
            w_i[i, 1] = y
            XY.append([x, y])
            if self.f2(x, y) < self.eps:
                break
        print(cnt)
        print(XY)
        return np.array(XY)

    def show_contour(self):
        XY = self.rosenbrock_momentum()
        xx = np.linspace(-4, 4, 800)
        yy = np.linspace(-3, 3, 600)
        X, Y = np.meshgrid(xx, yy)
        Z = self.f2(X, Y)

        levels = np.logspace(-1, 3, 10)
        plt.contourf(X, Y, Z, alpha=0.2, levels=levels)
        plt.contour(X,
                    Y,
                    Z,
                    colors="gray",
                    levels=[0.4, 3, 15, 50, 150, 500, 1500, 5000])
        plt.plot(XY[:, 0], XY[:, 1], 'g.-')
        plt.plot(1, 1, 'ro', markersize=10)

        plt.xlim(-4, 4)
        plt.ylim(-3, 3)
        plt.xticks(np.linspace(-4, 4, 9))
        plt.yticks(np.linspace(-3, 3, 7))
        plt.xlabel("$x$")
        plt.ylabel("$y$")
        plt.title("2차원 로젠브록 함수 $f(x,y)$")
        plt.show()

    def show_3d(self):
        XY = self.rosenbrock_momentum()
        x = np.linspace(-2, 2, 200)
        y = np.linspace(-2, 2, 200)
        X, Y = np.meshgrid(x, y)
        Z = self.f2(X, Y)
        fig = plt.figure(figsize=(5, 5))
        ax = fig.gca(projection='3d')
        ax.view_init(45, 230)
        ax.plot_surface(X, Y, Z, color='g', alpha=0.7)
        ax.scatter(1, 1, 0, 'ro')
        ax.scatter(self.start_x, self.start_y,
                   self.f2(self.start_x, self.start_y), 'ro')
        ax.plot(XY[:, 0], XY[:, 1], [self.f2(x, y) for x, y in XY], color='r')
        plt.show()


start_x = float(input("시작점 x값 : "))
start_y = float(input("시작점 y값 : "))
i_max = int(input("실행 횟수 : "))
alpha = float(input("학습률 : "))
eps = float(input("오차율 : "))
m = float(input("모멘텀 계수 : "))

a = optimization(start_x, start_y, i_max, alpha, eps, m)
# a = optimization(-2, -2, 10000, 0.00089, 0.000001, 0.7)

a.show_contour()
a.show_3d()