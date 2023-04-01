import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import t, norm
from sklearn.linear_model import LinearRegression


class part():
    def __init__(self, shape, size):
        self.shape = shape
        self.size = size

    def get_part(self):
        print(self.shape)
        print(self.size)


class eye(part):
    def __init__(self, shape, size, color):
        super().__init__(shape, size)
        self.color = color

    def get_eye(self):
        self.get_part()
        print(self.color)

    def set_color(self, other_color):
        self.color = other_color


e = eye("round", "medium", "blue")
e.get_eye()
e.set_color("green")
e.get_eye()
