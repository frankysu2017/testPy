#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

def runplt():
    plt.figure()
    plt.title(u'diameter-cost curver')
    plt.xlabel(u'diameter')
    plt.ylabel(u'cost')
    plt.axis([-5, 30, -5, 30])
    plt.grid(True)
    return plt

if __name__ == "__main__":
    X = [[6], [8], [10], [14], [18]]
    y = [[7], [9], [13], [17.5], [18]]

    plt = runplt()
    X2 = [[0], [10], [14], [25]]
    model = LinearRegression()
    model.fit(X, y)
    y2 = model.predict(X2)
    plt.plot(X, y, 'k.')
    plt.plot(X2, y2, 'g-')
    plt.show()

    quadratic_featurizer = PolynomialFeatures(degree=4)
    X_train_quadratic = quadratic_featurizer.fit_transform(X2)

    print(X_train_quadratic)


