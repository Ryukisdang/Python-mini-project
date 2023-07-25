from sklearn.linear_model import LinearRegression

# Create an instance of the Linear Regression model
model = LinearRegression()

# Train the model using the training data
model.fit(X_train, y_train)
from sklearn.metrics import mean_squared_error

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
# Make predictions on new data
new_data = [...]  # Features of new data
predicted_price = model.predict([new_data])
