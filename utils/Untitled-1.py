import numpy as np

img = np.random.randint(1, 256, (3, 416, 416))
mean = [80.2324447631836, 80.93988037109375, 54.676353454589844]
std = [53.057960510253906, 53.754241943359375, 45.067726135253906]
img = (img[:, ...] - np.asarray(mean[:])[:, np.newaxis, np.newaxis]) / np.asarray(std[:])[:, np.newaxis, np.newaxis]
print(img.shape)