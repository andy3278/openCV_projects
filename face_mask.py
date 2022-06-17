import cv2 
import numpy as np
import pandas as pd
import os
# Preprocessing
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, label_binarize
# Machine learning
import catboost
from sklearn.model_selection import train_test_split
from sklearn import model_selection, tree, preprocessing, metrics, linear_model
from sklearn.svm import LinearSVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression, LogisticRegression, SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from catboost import CatBoostClassifier, Pool, cv
from sklearn.preprocessing import StandardScaler
from keras.layers.advanced_activations import ReLU
from keras.models import Sequential, Model
from keras.layers import Activation, Convolution2D, MaxPooling2D, BatchNormalization, Flatten,Dense, Dropout, Conv2D,MaxPool2D, ZeroPadding2D
import keras
import cv2
import tensorflow
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint

train_path = './face_mask/Train'
test_path = './face_mask/Test'
img_size = 100

categories=os.listdir(train_path)
print('Categories Name :' ,categories)
labels=[i for i in range(len(categories))]
print('After convert it to 0,1 :',labels)