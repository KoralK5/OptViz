from math import *
import matplotlib.pyplot as plt
import numpy as np

def func(f, x):
    return eval(f.replace('x', '('+str(x)+')'))

def gradient(f,x):
    return (func(f, x+0.00001) - func(f, x)) / 0.00001

def points(x, rate):
    return [x+i/10 for i in range(-10, 10)]

def plot(x, f, it, sleep=0.5):
    if len(x) == 1:
        r = np.arange(-10, 10, 0.1)
    else:
        r = np.arange(min(x), max(x), 0.1)

    y = np.array([func(f, p) for p in r])
    plt.plot(r, y)
    miny = float('inf')
    for i in x:
        fi = func(f, i)
        miny = min(miny, fi)
        plt.plot(i, fi, marker="o", markersize=5)

    plt.legend([it, f'y = {f}', f'y = {"{0:.2f}".format(miny)}', f'{len(x)} balls'], loc='upper right')
    plt.show(block=False)
    plt.pause(sleep)

def filter(f, x, delta, rate):
    i = 0
    while True:
        try: x[i+1]
        except: break
        if abs(x[i] - x[i+1]) < rate:
            a, b = func(f, x[i]), func(f, x[i+1])
            if a < b:
                x.pop(i+1)
                delta.pop(i+1)
            else:
                x.pop(i)
                delta.pop(i)
        i += 1
    return x, delta

def optimize(f, x, initRate, decay, iters):
    rate = initRate
    x = points(x, rate)
    delta = [0 for i in range(-10, 10)]
    for i in range(iters):
        for p in range(len(x)):
            delta[p] = gradient(f, x[p]) * rate + delta[p] * decay
            x[p] -= delta[p]
        plot(x, f, i+1)
        plt.close()
        x, delta = filter(f, x, delta, rate)
        rate *= 1/(1+decay*i)
    return x

f = input('Function: ')
x = float(input('Guess: '))
rate = float(input('Rate: '))
decay = float(input('Decay: '))
iters = int(input('Iterations: '))

x = optimize(f, x, rate, decay, iters)
y = [func(f, p) for p in x]

miny = min(y)
minx = x[y.index(miny)]

print('\nx =', minx, '\ny =', miny)

plot([minx], f, iters, sleep=float('inf'))
