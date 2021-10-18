 from math import *
  2 import matplotlib.pyplot as plt
  3 import numpy as np
  4 
  5 def gradient(f,x):
  6     return (eval(f.replace('x', '('+str(x+0.00001)+')')) - eval(f.replace('x', '('+str(x)+')'))) / 0.00001
  7 
  8 def points(x, rate):
  9     return [x+i/10 for i in range(-10, 10)]
 10 
 11 def plot(x, f):
 12     r = np.arange(min(x), max(x), 0.1)
 13     y = np.array([eval(f.replace('x', '('+str(p)+')')) for p in r])
 14 
 15     plt.plot(r, y)
 16     for i in x:
 17         plt.plot(i, eval(f.replace('x', '('+str(i)+')')), marker="o", markersize=5, markerfacecolor="green")
 18 
 19     plt.show(block=False)
 20     plt.pause(0.5)
 21     plt.close()
 22 
 23 def optimize(f, x, rate, iters):
 24     x = points(x, rate)
 25     delta = [0 for i in range(-10, 10)]
 26     for i in range(iters):
 27         for p in range(len(x)):
 28             delta[p] = gradient(f, x[p]) * rate + 0.9 * delta[p]
 29             x[p] -= delta[p]
 30         plot(x, f)
 31     return x
 32 
 33 f = input('Function: ')
 34 x = float(input('Guess: '))
 35 rate = float(input('Rate: '))
 36 iters = int(input('Iterations: '))
 37 
 38 x = optimize(f, x, rate, iters)
