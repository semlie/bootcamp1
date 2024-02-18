import pandas as pd
import pickle


def hello():
    return 'Hello, World from ather file imported!'

with open(r'data/filterd.pkl', 'r', encoding='utf-8') as f:
    obj = f.read()
    print(obj[:1000])






