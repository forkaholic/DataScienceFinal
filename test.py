import pandas as pd
import numpy as np
from joblib import load

model = load('Static/followers_prediction.joblib')  #load
#6196161750	215250	222720	27716	3246298	1734810	93036735	1	0

x = np.array([6196161750,	215250,		27716,	3246298	,	1,	0])
print(model.predict(x.reshape(1,-1))[0])
print("1734810")