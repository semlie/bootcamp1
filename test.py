import os
import pickle

file_path = '../data/filterd.txt'

if os.path.exists(file_path):
    with open(file_path, 'rb') as file:
        obj = pickle.load(file)
    print(obj)
else:
    print("File not found:", file_path)

