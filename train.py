from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd
import csv
from joblib import dump

data = None

#drop 0 3 10
#save 6 7

with open('twitchdata-update.csv', newline='') as file:
    reader = csv.reader(file)
    c=0
    temp = []
    for row in reader:
        if c == 0:
            c = 1
            continue
        del(row[10])
        del(row[0])
        temp.append(row)
    data = pd.DataFrame(np.array(temp).astype(np.int64))

# Columns to del get shifted because of for loop
# Columns remaining (all shifted by 1 when referencing)
# 1,2,3,4,5,6,7,8,9
y = data[[5]] # Followers gained (year) actually column 6
# y = data[[6]] # Views gained (year) actually column 7
data.drop(columns=[2,5,6],inplace=True)

# remaining columns
# 1, 3, 4, 7, 8, 9

# split the data with 50% in each set
X1, X2, y1, y2 = train_test_split(data, y, random_state=0,
                                  train_size=0.75)

# fit the model on one set of data

pipeline = Pipeline([
    ("Standard Scaling", StandardScaler()),
    ("Lasso", linear_model.Lasso())
])
pipeline.fit(X1,y1)
#.values.ravel()

# evaluate the model on the second set of data
y2_model = pipeline.predict(X2)
print(r2_score(y2, y2_model))

# Model/pipeline predicts followers gained in a year

dump(pipeline,'Static/followers_prediction.joblib')