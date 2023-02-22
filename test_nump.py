import numpy as np

weight = [1.11, 2.43, 2.55, 5.65]
height = [6, 8, 7, 6]

np_weight = np.array(weight)
np_height = np.array(height)
weight_mean = np.mean(weight)
height_mean = np.mean(height)
weight_sum = np.sum(weight)
height_sum = np.sum(height)

bmi = np_weight / np_height ** 2

print(bmi)
print(weight_mean)
print(height_mean)
print(weight_sum)
print(height_sum)


random_num = np.arange(0, 100, 10)
print(random_num)

is_2d = np.random.random((3,3))
mean_is_2d = np.mean(is_2d)
print(is_2d)
print(mean_is_2d)