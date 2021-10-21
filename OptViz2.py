  1 from math import *
  2 import matplotlib.pyplot as plt
  3 import numpy as np
  4 
  5 def func(f, x):
  6     return eval(f.replace('x', '('+str(x)+')'))
  7 
  8 def gradient(f,x):
  9     return (func(f, x+0.00001) - func(f, x)) / 0.00001
 10 
 11 def points(x, rate):
 12     return [x+i/10 for i in range(-10, 10)]
 13 
 14 def plot(x, f, it, sleep=0.5):
 15     if len(x) == 1:
 16         r = np.arange(-10, 10, 0.1)
 17     else:
 18         r = np.arange(min(x), max(x), 0.1)
 19 
 20     y = np.array([func(f, p) for p in r])
 21     plt.plot(r, y)
 22     miny = float('inf')
 23     for i in x:
 24         fi = func(f, i)
 25         miny = min(miny, fi)
 26         plt.plot(i, fi, marker="o", markersize=5)
 27 
 28     plt.legend([it, f'y = {f}', f'y = {"{0:.2f}".format(miny)}', f'{len(x)} balls'], loc='upper right')
 29     plt.show(block=False)
 30     plt.pause(sleep)
 31 
 32 def filter(f, x, delta, rate):
 33     i = 0
 34     while True:
 35         try: x[i+1]
 36         except: break
 37         if abs(x[i] - x[i+1]) < rate:
 38             a, b = func(f, x[i]), func(f, x[i+1])
 39             if a < b:
 40                 x.pop(i+1)
 41                 delta.pop(i+1)
 42             else:
 43                 x.pop(i)
 44                 delta.pop(i)
 45         i += 1
 46     return x, delta
 47 
 48 def optimize(f, x, initRate, decay, iters):
 49     rate = initRate
 50     x = points(x, rate)
 51     delta = [0 for i in range(-10, 10)]
 52     for i in range(iters):
 53         for p in range(len(x)):
 54             delta[p] = gradient(f, x[p]) * rate + delta[p] * decay
 55             x[p] -= delta[p]
 56         plot(x, f, i+1)
 57         plt.close()
 58         x, delta = filter(f, x, delta, rate)
 59         rate *= 1/(1+decay*i)
 60     return x
 61 
 62 f = input('Function: ')
 63 x = float(input('Guess: '))
 64 rate = float(input('Rate: '))
 65 decay = float(input('Decay: '))
 66 iters = int(input('Iterations: '))
 67 
 68 x = optimize(f, x, rate, decay, iters)
 69 y = [func(f, p) for p in x]
 70 
 71 miny = min(y)
 72 minx = x[y.index(miny)]
 73 
 74 print('\nx =', minx, '\ny =', miny)
 75 
 76 plot([minx], f, iters, sleep=float('inf'))
