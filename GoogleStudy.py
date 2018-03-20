#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format


def studypd():
    city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
    population = pd.Series([852469, 1015785, 485199])
    cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
    cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
    series_bool = cities['City name'].apply(lambda string: string.startswith('San')) & cities['Area square miles'].apply(lambda area: area > 50)
    cities['City Bool'] = series_bool
    print(cities)


def studytf():
    california_housing_dataframe = pd.read_csv(r"C:\Users\WEB_PC_X1\Downloads\california_housing_train.csv", sep=",")

    # 对数据进行随机化（乱序）
    california_housing_dataframe = california_housing_dataframe.reindex(np.random.permutation(california_housing_dataframe.index))

    # 对median_house_value的值除以1000
    california_housing_dataframe["median_house_value"] /= 1000.0

    # 选择total_rooms作为特征列（x)，用于估计平均房价
    my_feature = california_housing_dataframe[["total_rooms"]]

    # 给线性回归模型定义一个特征列，类型是list，这个列子里只有一列，如果有多个变量，可以将list扩展到高维度
    feature_columns = [tf.feature_column.numeric_column("total_rooms")]

    # 定义median_house_value为标签列（目标列，y），用于与total_rooms对应分析房价变化因素
    targets = california_housing_dataframe["median_house_value"]

    # 配置线性回归模型，GradientDescentOptimizer函数实现小批量随机梯度下降法SGD
    ## 先定义梯度下降算法的参数：学习率learning_rate定义梯度步长，clip_gradients_by_norm函数防止梯度过大
    my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0000001)
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)

    # 定义了一个线性回归模型
    linear_regressor = tf.estimator.LinearRegressor(
        feature_columns=feature_columns,
        optimizer=my_optimizer
    )

    # my_input_fn函数中定义了一个给linear_regressor提供输入的函数

    # 训练模型
    _ = linear_regressor.train(
        input_fn=lambda: my_input_fn(my_feature, targets),
        steps=100
    )

    # 评估模型
    # Create an input function for predictions.
    # Note: Since we're making just one prediction for each example, we don't
    # need to repeat or shuffle the data here.
    prediction_input_fn = lambda: my_input_fn(my_feature, targets, num_epochs=1, shuffle=False)

    # Call predict() on the linear_regressor to make predictions.
    predictions = linear_regressor.predict(input_fn=prediction_input_fn)

    # Format predictions as a NumPy array, so we can calculate error metrics.
    predictions = np.array([item['predictions'][0] for item in predictions])

    # Print Mean Squared Error and Root Mean Squared Error.
    mean_squared_error = metrics.mean_squared_error(predictions, targets)
    root_mean_squared_error = math.sqrt(mean_squared_error)
    print("Mean Squared Error (on training data): %0.3f" % mean_squared_error)
    print("Root Mean Squared Error (on training data): %0.3f" % root_mean_squared_error)

    # 评估模型均方差的基本质量
    min_house_value = california_housing_dataframe["median_house_value"].min()
    max_house_value = california_housing_dataframe["median_house_value"].max()
    min_max_difference = max_house_value - min_house_value

    print("Min. Median House Value: %0.3f" % min_house_value)
    print("Max. Median House Value: %0.3f" % max_house_value)
    print("Difference between Min. and Max.: %0.3f" % min_max_difference)
    print("Root Mean Squared Error: %0.3f" % root_mean_squared_error)

    calibration_data = pd.DataFrame()
    calibration_data["predictions"] = pd.Series(predictions)
    calibration_data["targets"] = pd.Series(targets)
    print(calibration_data.describe())

    sample = california_housing_dataframe.sample(n=300)
    x_0 = sample["total_rooms"].min()
    x_1 = sample["total_rooms"].max()

    # Retrieve the final weight and bias generated during training.
    weight = linear_regressor.get_variable_value('linear/linear_model/total_rooms/weights')[0]
    bias = linear_regressor.get_variable_value('linear/linear_model/bias_weights')
    #打印w和b
    print('weight = %0.5f' %weight)
    print('bias = %0.5f' %bias)

    # Get the predicted median_house_values for the min and max total_rooms values.
    y_0 = weight * x_0 + bias
    y_1 = weight * x_1 + bias

    # Plot our regression line from (x_0, y_0) to (x_1, y_1).
    plt.plot([x_0, x_1], [y_0, y_1], c='r')

    # Label the graph axes.
    plt.ylabel("median_house_value")
    plt.xlabel("total_rooms")

    # Plot a scatter plot from our data sample.
    plt.scatter(sample["total_rooms"], sample["median_house_value"])

    # Display graph.
    plt.show()

#定义输入函数
def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    """
    Trains a linear regression model of one feature.

    Args:
      features: pandas DataFrame of features
      targets: pandas DataFrame of targets
      batch_size: Size of batches to be passed to the model
      shuffle: True or False. Whether to shuffle the data.
      num_epochs: Number of epochs for which data should be repeated. None = repeat indefinitely
    Returns:
      Tuple of (features, labels) for next data batch
    """

    # 将DataFrame转换为{'total_rooms': array([5612., 7650.,  720., ..., 2677., 2672., 1820.])}的形式
    features = {key: np.array(value) for key, value in dict(features).items()}

    # 构造机器学习的数据集
    ds = Dataset.from_tensor_slices((features, targets))  # warning: 2GB limit
    ds = ds.batch(batch_size).repeat(num_epochs)

    # 数据重新乱序
    if shuffle:
        ds = ds.shuffle(buffer_size=10000)

    # Return the next batch of data
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels



if __name__ == '__main__':
    studytf()