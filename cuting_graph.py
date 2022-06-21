import matplotlib.pyplot as plt
import numpy as np
import itertools
import pickle

from sklearn.model_selection import train_test_split
from sklearn import preprocessing

from tensorflow.keras import layers
from tensorflow import keras
import tensorflow as tf
import os

EPOCH = 200
KERNEL_SIZE = 3
POOLING_SIZE = 2
BATCH_SIZE = 10

SAVE_PATH = "./graph_data/"
DATA_PATH = "./mit_data/"

def list_to_list(input_list):
    input_list_to_list = list(itertools.chain(*input_list))
    return input_list_to_list

# 경로에 폴더가 없으면 폴더 만들기
def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

# Dataload part
le = preprocessing.LabelEncoder()

record_list = []
pickle_input = dict()
X, y = [], []

print("[INFO] Read records file from ", DATA_PATH)
with open(DATA_PATH + 'RECORDS') as f:
    record_lines = f.readlines()

for i in range(len(record_lines)):
    record_list.append(str(record_lines[i].strip()))

for j in range(len(record_list)):
    temp_path = DATA_PATH + "mit" + record_list[j] + ".pkl"
    with open(temp_path, 'rb') as f:
        pickle_input = pickle.load(f)
        for i in range(len(pickle_input[0])):
            X.append(pickle_input[0][i])
            plt.title(pickle_input[1][i])
            plt.plot(X[-1])

            check_ann = pickle_input[1][i]
            temp_ann_list = list()
            if check_ann == "N":            # Normal
                temp_ann_list.append(0)
                annotation_path = SAVE_PATH + str(pickle_input[1][i]) + "/"
                plt.title(pickle_input[1][i])

            elif check_ann == "S":          # Supra-ventricular
                temp_ann_list.append(1)
                annotation_path = SAVE_PATH + str(pickle_input[1][i]) + "/"
                plt.title(pickle_input[1][i])

            elif check_ann == "V":          # Ventricular
                temp_ann_list.append(2)
                annotation_path = SAVE_PATH + str(pickle_input[1][i]) + "/"
                plt.title(pickle_input[1][i])

            elif check_ann == "F":          # False alarm
                temp_ann_list.append(3)
                annotation_path = SAVE_PATH + str(pickle_input[1][i]) + "/"
                plt.title(pickle_input[1][i])

            else:                           # Unclassed 
                temp_ann_list.append(4)
                annotation_path = SAVE_PATH + "Q" + "/"
                plt.title("Q")
            
            createDirectory(annotation_path)
            save_file_name = annotation_path + str(record_list[j]) + "__" + str(i) + str(pickle_input[1][i]) + ".png"

            plt.savefig(save_file_name)
            plt.clf()

        print("[INFO] {}".format(temp_path))
            
        for z in range(len(pickle_input[1])):
            check_ann = pickle_input[1][z]
            temp_ann_list = list()
            if check_ann == "N":            # Normal
                temp_ann_list.append(0)
                plt.title("N")

            elif check_ann == "S":          # Supra-ventricular
                temp_ann_list.append(1)
                plt.title("S")

            elif check_ann == "V":          # Ventricular
                temp_ann_list.append(2)
                plt.title("V")

            elif check_ann == "F":          # False alarm
                temp_ann_list.append(3)
                plt.title("F")

            else:                           # Unclassed 
                temp_ann_list.append(4)
                plt.title("Q")

            print(check_ann + str(record_list[j]) + "__" + str(i) + str(pickle_input[1][i]) + ".png")
            y.append(temp_ann_list)