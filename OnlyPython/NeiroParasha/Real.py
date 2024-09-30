import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense

c = np.array([-40, -10, 0, 8, 15, 22, 38])
f = np.array([-40, 14, 32, 46, 59, 72, 100])

model = keras.Sequential() #Создание всесвязанной
model.add(Dense(units = 1, input_shape =(1,), activation = 'linear'))#1 нейрон, 1 вход активационная функция ч

model.compile(loss ='mean_squared_error', optimizer = keras.optimizers.Adam(0.1))#Компиляция, способ оптимизации + критерий качества

history = model.fit(c, f, epochs=500, verbose= 0)#Входные, выходные, число эпох, не вывод служебной информации
# plt.plot(history.history['loss'])#все ошибки
# plt.grid(True)
# plt.show()
input_data = np.array([[-40], [-10], [0]])  # Создание массива для предсказания (размерность 2D) d
predictions = model.predict(input_data)

print(predictions)
