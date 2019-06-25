#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from matplotlib import pyplot


def runplt(title):

    return pyplot


def dataSample(datalist, samplePoint=500):
    samp = random.sample(datalist, samplePoint)
    x_sample = [[item[0]] for item in samp]
    y_sample = [[item[1]] for item in samp]
    return x_sample, y_sample


def polyRegression(data, plotpos, sampleRate=500, showPoint=True):

    sample_distance, sample_timecost = dataSample(data, samplePoint=sampleRate)
    xx = np.linspace(0, 27, 50000)

    #Polynomial Linear Regression
    polynomic_featurizer = PolynomialFeatures(degree=5)
    sample_distance_polynomic = polynomic_featurizer.fit_transform(sample_distance)
    regressor = LinearRegression()
    regressor.fit(sample_distance_polynomic, sample_timecost)
    xx_polynomic = polynomic_featurizer.transform(xx.reshape(-1, 1))
    yy = regressor.predict(xx_polynomic)
    pyplot.subplot(plotpos)
    pyplot.title("Sample Rate = %d" %sampleRate)
    pyplot.xlabel(u'Distance')
    pyplot.ylabel(u'Time Cost')
    pyplot.axis([0, 26, 0, 110])
    pyplot.grid(True)
    if showPoint == True:
        pyplot.plot(sample_distance, sample_timecost, 'k.')
    pyplot.plot(xx, yy, 'r-')

if __name__ == "__main__":

    #Generate simulating data
    distance = np.linspace(0, 27, 50000)
    costtime = distance * (1 + np.random.randn(50000) / 8) * 4
    pair = list(zip(distance, costtime))
    sampleRates = [5, 10, 30, 500]
    positions = [221, 222, 223, 224]

    pyplot.figure(u"Windshield Time Cost")
    for i in range(4):
        polyRegression(pair, positions[i], sampleRates[i], True)
        print(positions[i], sampleRates[i])

    pyplot.show()
