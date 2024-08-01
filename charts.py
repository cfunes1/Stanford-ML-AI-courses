import numpy as np
import matplotlib.pyplot as plt
# plt.style.use('./deeplearning.mplstyle')

# # x_train is the input variable (size in 1000 square feet)
# # y_train is the target (price in 1000s of dollars)
# x_train = np.array([1.0, 2.0])
# y_train = np.array([300.0, 500.0])
# print(f"x_train = {x_train}")
# print(f"y_train = {y_train}")

# # m is the number of training examples
# print(f"x_train.shape: {x_train.shape}")
# m = x_train.shape[0]
# print(f"Number of training examples is: {m}")

# # m is the number of training examples
# m = len(x_train)
# print(f"Number of training examples is: {m}")

# i = 1 # Change this to 1 to see (x^1, y^1)

# x_i = x_train[i]
# y_i = y_train[i]
# print(f"(x^({i}), y^({i})) = ({x_i}, {y_i})")

# # Plot the data points
# plt.scatter(x_train, y_train, marker='x', c='b')
# # Set the title
# plt.title("Housing Prices")
# # Set the y-axis label
# plt.ylabel('Price (in 1000s of dollars)')
# # Set the x-axis label
# plt.xlabel('Size (1000 sqft)')
# plt.show()

# w = 100
# b = 100
# print(f"w: {w}")
# print(f"b: {b}")

# def compute_model_output(x, w, b):
#     """
#     Computes the prediction of a linear model
#     Args:
#       x (ndarray (m,)): Data, m examples 
#       w,b (scalar)    : model parameters  
#     Returns
#       f_wb (ndarray (m,)): model prediction
#     """
#     m = x.shape[0]
#     f_wb = np.zeros(m)
#     for i in range(m):
#         f_wb[i] = w * x[i] + b
        
#     return f_wb

# tmp_f_wb = compute_model_output(x_train, w, b,)

# # Plot our model prediction
# plt.plot(x_train, tmp_f_wb, c='b',label='Our Prediction')

# # Plot the data points
# plt.scatter(x_train, y_train, marker='x', c='r',label='Actual Values')

# # Set the title
# plt.title("Housing Prices")
# # Set the y-axis label
# plt.ylabel('Price (in 1000s of dollars)')
# # Set the x-axis label
# plt.xlabel('Size (1000 sqft)')
# plt.legend()
# plt.show()

# w = 200                         
# b = 100    
# x_i = 1.2
# cost_1200sqft = w * x_i + b    

# print(f"${cost_1200sqft:.0f} thousand dollars")


import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Create the plot
plt.plot(x, y)

# Add a title
plt.title("Basic Line Plot")

# Add labels to the axes
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Display the plot
plt.show()

# Sample data
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Create a scatter plot
plt.scatter(x, y)

# Add a title and labels
plt.title("Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Display the plot
plt.show()


# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# Create a bar chart
plt.bar(categories, values)

# Add a title and labels
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

# Display the plot
plt.show()

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Create a histogram
plt.hist(data, bins=4)

# Add a title and labels
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("Frequency")

# Display the plot
plt.show()


# Customizing a line plot
plt.plot(x, y, linestyle='--', color='r', marker='o')

# Adding grid lines
plt.grid(True)

# Adding a legend
plt.legend(["Line 1"])

# Adjusting axis limits
plt.xlim(0, 5)
plt.ylim(0, 35)

# Display the plot
plt.show()

# Create subplots
fig, axs = plt.subplots(2, 2)

# First subplot
axs[0, 0].plot(x, y)
axs[0, 0].set_title("Plot 1")

# Second subplot
axs[0, 1].scatter(x, y)
axs[0, 1].set_title("Plot 2")

# Third subplot
axs[1, 0].bar(categories, values)
axs[1, 0].set_title("Plot 3")

# Fourth subplot
axs[1, 1].hist(data, bins=4)
axs[1, 1].set_title("Plot 4")

# Display the plots
plt.tight_layout()
plt.show()
