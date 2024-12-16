import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2, figsize=(16, 9))
plt.suptitle('Plot Examples', fontsize=20)

covariance_matrix = [[1, 0.7], [0.7, 1]]
mean_values = [20, 10]
scatter_data = np.random.multivariate_normal(mean_values, covariance_matrix, size=1000)
axs[0, 0].scatter(scatter_data[:, 0], scatter_data[:, 1], color='#4169E1', edgecolors='#000000')
axs[0, 0].set_title('Scatter Plot Example')

histogram_data = np.random.geometric(p=0.1, size=3000)
axs[0, 1].hist(histogram_data, bins=40, color='#FF0000')
axs[0, 1].set_title('Histogram Example')

x_values = np.linspace(0.01, 6, 1000)
y_values_log_x = np.log(x_values)
y_values_log_2x = np.log(x_values * 2)
axs[1, 0].plot(x_values, y_values_log_x, color='#000000', label='log(x)')
axs[1, 0].plot(x_values, y_values_log_2x, color='#FF0000', label='log(2x)')
axs[1, 0].set_title('Line Plot Example')
axs[1, 0].legend()

bar_values = np.random.normal(5, size=14)
bar_labels = [
    '2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',
    '2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08',
    '2021-01-09', '2021-01-10', '2021-01-11', '2021-01-12',
    '2021-01-13', '2021-01-14'
]
axs[1, 1].bar(bar_labels, bar_values)
axs[1, 1].tick_params(axis='x', labelrotation=90)
axs[1, 1].set_title('Bar Plot Example')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
