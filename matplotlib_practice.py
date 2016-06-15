#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)  # type: np.array
    C, S = np.cos(x), np.sin(x)
    plt.plot(x, C, color='red', linewidth='2.4', linestyle='--', label='cosine')
    plt.plot(x, S, color='blue', label='sine')
    plt.xlim(x.min() * 1.1, x.max() * 1.1)
    plt.ylim(C.min() * 1.1, C.max() * 1.1)
    plt.xticks(np.linspace(-np.pi, np.pi, 5, endpoint=True),
               [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
    axis = plt.gca()
    axis.spines['right'].set_color('none')
    axis.spines['top'].set_color('none')
    axis.xaxis.set_ticks_position('bottom')
    axis.spines['bottom'].set_position(('data', 0))
    axis.yaxis.set_ticks_position('left')
    axis.spines['left'].set_position(('data', 0))
    plt.legend(loc='upper left')
    t = 2 * np.pi / 3
    plt.plot([t, t], [0, np.cos(t)], color='red', linestyle='--')
    plt.scatter([t, ], [np.cos(t), ], 50, color='red')
    plt.annotate(r'$\cos(\frac{2\pi}{3})=\frac{1}{2}$', xy=(t, np.cos(t)), xycoords='data', xytext=(10, 30),
                 textcoords='offset points', fontsize='16', color='red',
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=0.2', color='red'))
    plt.show()
