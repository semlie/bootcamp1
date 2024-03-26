# import datetime
# import os
# import re
# import sys
# import numpy as np
import pickle
import pandas as pd
# import seaborn as sns
"""import"""
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from sklearn.feature_extraction.text import (CountVectorizer, TfidfTransformer,
                                             TfidfVectorizer)
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

load_dotenv()

mongo_connection = os.environ.get("MONGO_DB")
client = MongoClient(mongo_connection)
db = client.get_database()
collection = db["items"] 


def get_X_Y_data(df, x_col, y_col):
    sub_df = df[[x_col, y_col]]
    sub_df = sub_df.dropna()
    return sub_df[x_col], sub_df[y_col]


def generate_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)
    pred_model = Pipeline(
        [('vect', CountVectorizer()),
         ('tfidf', TfidfTransformer()),
         ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3,
          random_state=42, max_iter=5, tol=None)),  # hinge
         ])
    
    pred_model.fit(X_train, y_train)
    y_pred = pred_model.predict(X_test)
    print('accuracy %s' % accuracy_score(y_pred, y_test))
    # print(classification_report(y_test, y_pred))
    return pred_model
    
def get_error_analysis(df, pred_model, x_col, y_col):
    X, y = get_X_Y_data(df, x_col, y_col)
    y_pred = pred_model.predict(X)
    df["y_pred"] = y_pred
    df["y"] = y
    df["error"] = df["y"] != df["y_pred"]
    return df
def get_confusion_matrix(df, y, y_pred):
    Y = df[y]
    Y_pred = df[y_pred]
    return confusion_matrix(Y, Y_pred)
def get_top_features(model, n):
    feature_names = model.named_steps['vect'].get_feature_names_out()
    coefs = model.named_steps['clf'].coef_[0]
    top_features = [(feature_names[i], coefs[i]) for i in coefs.argsort()]
    return top_features


# run the model again


if "__main__" == __name__:
    # connect to mongdb and read all the docs
    pipeline = [
    {"$group": {"_id": "$category", "messages": {"$push": "$message_content"}}}
    ]

    result = collection.find()
    categories_messages_list = list(result)

    # make as pandas dataframe call in df 

    df = pd.DataFrame.from_dict( categories_messages_list)
    
    X,y = get_X_Y_data(df.copy(),'massage_content','category')

    model = generate_model(X,y )
    # errors_df =get_error_analysis(df,model,'massage_content','category')
    with open('class_model.pkl',"wb" ) as p:
        pickle.dump(model,p)

    pred = model.predict(df['massage_content'])
    df['y_pred'] = pred
    
    print(pred)