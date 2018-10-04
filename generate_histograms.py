import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


class HistogramsGenerator:
    channels = [0, 1, 2]
    bins_rgb = [8, 8, 8]
    ranges = [0, 256, 0, 256, 0, 256]

    bins_hue = [10, 1, 1]
    bins_sv = [1, 5, 5]

    dominant_color = None
    number_of_images_for_color_clustering = 210
    number_of_clusters = 5

    figure_size = (20, 20)

    def __init__(self, set_mask=False, crop_coefficient=None):
        self.set_mask = set_mask
        self.crop_coefficient = crop_coefficient

    def get_representations(self, files):
        if self.set_mask:
            self.dominant_color = self.get_dominant_color(files)
        return [self.get_histogram(self.preprocess_image(cv2.imread(file))) for file in files]

    def preprocess_image(self, image):
        if self.set_mask:
            image = self.cut_dominant_color(image, self.dominant_color)
        if self.crop_coefficient:
            image = self.crop_image(image)
        return image

    def get_histogram(self, image):
        return

    def crop_image(self, image):
        k = self.crop_coefficient
        h, w, _ = image.shape
        return image[int(k * h): int((1 - k) * h), int(k * w): int((1 - k) * w)]

    def cut_dominant_color(self, image, dominant_color, color_eps=25):
        b, g, r = dominant_color
        blue, green, red = image[:, :, 0], image[:, :, 1], image[:, :, 2]
        mask = (abs(blue - b) < color_eps) & (abs(green - g) < color_eps) & (abs(red - r) < color_eps)
        image[mask] = [255, 255, 255]
        return image

    def get_dominant_color(self, files, plot_images=True):
        images = []
        for i in range(self.number_of_images_for_color_clustering):
            image = cv2.imread(files[i])
            image = cv2.resize(image, (25, 40))
            images.append(image)
        images = np.hstack(images)
        if plot_images:
            plt.figure(figsize=self.figure_size)
            plt.imshow(images)
        images = images.reshape(-1, 3)
        kmeans = KMeans(max_iter=300, n_clusters=self.number_of_clusters, random_state=1232).fit(images)
        labels = kmeans.labels_
        counts, bins = np.histogram(labels, len(set(kmeans.labels_)))
        dominant_color = kmeans.cluster_centers_[counts.argmax()]
        print(f'most frequent is {dominant_color}')
        return dominant_color

    def show_images(self, files):
        fig = plt.figure(figsize=self.figure_size)
        for i, file in enumerate(files):
            image = cv2.imread(file)
            image = self.preprocess_image(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            fig.add_subplot(1, len(files), i + 1)
            plt.imshow(image)

    def show_histograms(self, files):
        plt.figure(figsize=(self.figure_size[0], self.figure_size[1] // 5))
        histograms = [self.get_histogram(self.preprocess_image(cv2.imread(file))) for file in files]
        plt.plot(np.array(histograms).T)
        plt.show()


class RgbHistogramsGenerator(HistogramsGenerator):
    def get_histogram(self, image):
        histogram = cv2.calcHist([image], self.channels, None, self.bins_rgb, self.ranges).flatten()
        return histogram / histogram.sum()


class HsvHistogramsGenerator(HistogramsGenerator):
    def get_histogram(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        histogram_hue = cv2.calcHist([image], self.channels, None, self.bins_hue, self.ranges).flatten()
        histogram_sv = cv2.calcHist([image], self.channels, None, self.bins_sv, self.ranges).flatten()
        histogram = np.hstack((histogram_hue, histogram_sv))
        return histogram / histogram.sum()


class OnPartsHistogramsGenerator(HistogramsGenerator):
    def get_histogram(self, image):
        h = image.shape[0]
        histogram_bottom = cv2.calcHist(
            [image[int(0.5 * h):]], self.channels, None, self.bins_rgb, self.ranges).flatten()
        histogram_top = cv2.calcHist(
            [image[:int(0.5 * h)]], self.channels, None, self.bins_rgb, self.ranges).flatten()
        histogram = np.hstack((histogram_bottom, histogram_top))
        return histogram / histogram.sum()
