

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import GRU, Dense

# Generate synthetic time series data (you can replace this with your real data)
def generate_synthetic_data(num_points):
    x = np.linspace(0, 10, num_points)
    y = np.sin(x) + np.random.normal(0, 0.1, num_points)
    return y

# Sample data generation
def predictfn(y,num_of_days):

        data = np.array(y)



        # Normalize the data
        scaler = MinMaxScaler()
        data = scaler.fit_transform(data.reshape(-1, 1))

        # Split the data into training and testing sets
        train_size = int(len(data) * 0.8)
        train_data, test_data = data, data

        # Create sequences for the GRU model
        def create_sequences(data, look_back):
            X, y = [], []
            for i in range(len(data) - look_back):
                X.append(data[i:i+look_back])
                y.append(data[i+look_back])
            return np.array(X), np.array(y)

        look_back = 3  # You can adjust this parameter to change the sequence length
        train_X, train_y = create_sequences(train_data, look_back)
        test_X, test_y = create_sequences(test_data, look_back)

        # Build the GRU model
        model = Sequential()
        model.add(GRU(units=50, input_shape=(look_back, 1)))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mean_squared_error')

        # Train the model
        model.fit(train_X, train_y, epochs=100, batch_size=64)

        # Make predictions
        train_predict = model.predict(train_X)
        # test_predict = model.predict(test_X)
        while True:
            print(len(train_predict),"====",int(num_of_days))
            if len(train_predict)<int(num_of_days):
                data=list(data)
                for i in train_predict:
                    data.append(i)
                data=np.asanyarray(data)
                train_X, train_y = create_sequences(data, look_back)
                train_predict = model.predict(train_X)
            else:
                break



        # Inverse transform the predictions to original scale
        train_predict = scaler.inverse_transform(train_predict)
        # test_predict = scaler.inverse_transform(test_predict)
        print(train_predict,"test_predict")
        print(train_predict,"test_predict")
        print(train_predict,"test_predict")
        # Plot the results
        return train_predict
