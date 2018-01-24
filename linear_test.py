#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline

def genData(amount):
    x = np.arange(0, 30, 30/amount)
    y = norm.rvs(0, size = amount, scale=3)
    y = y + 3*x
    return x.reshape(-1,1), y.reshape(-1,1)

def genPlot(amount, showPots=True):
    a, b = genData(amount)
    x = np.arange(0,30,1/1000).reshape(-1,1)
    poly = make_pipeline(PolynomialFeatures(degree=6), Ridge())
    poly.fit(a, b)
    print(poly.named_steps['ridge'].coef_)
    y = poly.predict(x)
    plt.figure()
    plt.title(u'Time Costing prediction')
    plt.xlabel(u'Distance')
    plt.ylabel(u'Using time')
    plt.grid(True)
    plt.plot(x, y, 'r-')
    if showPots == True:
        plt.plot(a, b, 'k.')
    plt.show()

if __name__ == "__main__":
    genPlot(5000, False)