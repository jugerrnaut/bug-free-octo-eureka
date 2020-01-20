import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import sklearn
from sklearn.preprocessing import OneHotEncoder
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from keras import optimizers
import xgboost
from xgboost import XGBClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import joblib
onehotencoder = OneHotEncoder(categorical_features = [0])
# all parameters not specified are set to their defaults
logisticRegr = LogisticRegression()

data2 = pd.read_csv("pbp-2019.csv")
drop_columns = ["Description","PlayType","Unnamed: 12","GameId","GameDate","Quarter","Minute","Second","NextScore","TeamWin","SeasonYear","Yards","IsIncomplete","IsRush","IsPass","IsTouchdown","PassType","IsSack","IsChallenge","IsChallengeReversed","Challenger","IsMeasurement","IsInterception","IsFumble","IsPenalty","IsTwoPointConversion","IsTwoPointConversionSuccessful","RushDirection","YardLineFixed","YardLineDirection","IsPenaltyAccepted","PenaltyTeam","IsNoPlay","PenaltyType","PenaltyYards","Unnamed: 10","Unnamed: 16", "Unnamed: 17"]

data2 = data2.loc[data2["Down"] == 4]
data2 = data2.drop(drop_columns, axis = 1)
#baseline for the renaming
o_list = list(data2.OffenseTeam.unique())
def formatforrenaming(frame,column):
	result = list(frame["{}".format(column)])
	return result
#the function that names the teams as integers
def actualnaming(frame,column):
	inputlist = []
	inputlist= formatforrenaming(frame,column)
	outputlist = []
	for i in range(0,len(inputlist)):
		a = inputlist[i]
		if a == o_list[0]:
			a = 0
			outputlist.append(a)
		if a == o_list[1]:
			a = 1
			outputlist.append(a)
		if a == o_list[2]:
			a = 2
			outputlist.append(a)
		if a == o_list[3]:
			a = 3
			outputlist.append(a)
		if a == o_list[4]:
			a = 4
			outputlist.append(a)
		if a == o_list[5]:
			a = 5
			outputlist.append(a)
		if a == o_list[6]:
			a = 6
			outputlist.append(a)
		if a == o_list[7]:
			a = 7
			outputlist.append(a)
		if a == o_list[8]:
			a = 8
			outputlist.append(a)
		if a == o_list[9]:
			a = 9
			outputlist.append(a)
		if a == o_list[10]:
			a = 10
			outputlist.append(a)
		if a == o_list[11]:
			a = 11
			outputlist.append(a)
		if a == o_list[12]:
			a = 12
			outputlist.append(a)
		if a == o_list[13]:
			a = 13
			outputlist.append(a)
		if a == o_list[14]:
			a = 14
			outputlist.append(a)
		if a == o_list[15]:
			a = 15
			outputlist.append(a)
		if a == o_list[16]:
			a = 16
			outputlist.append(a)
		if a == o_list[17]:
			a = 17
			outputlist.append(a)
		if a == o_list[18]:
			a = 18
			outputlist.append(a)
		if a == o_list[19]:
			a = 19
			outputlist.append(a)
		if a == o_list[20]:
			a = 20
			outputlist.append(a)
		if a == o_list[21]:
			a = 21
			outputlist.append(a)
		if a == o_list[22]:
			a = 22
			outputlist.append(a)
		if a == o_list[23]:
			a = 23
			outputlist.append(a)
		if a == o_list[24]:
			a = 24
			outputlist.append(a)
		if a == o_list[25]:
			a = 25
			outputlist.append(a)
		if a == o_list[26]:
			a = 26
			outputlist.append(a)
		if a == o_list[27]:
			a = 27
			outputlist.append(a)
		if a == o_list[28]:
			a = 28
			outputlist.append(a)
		if a == o_list[29]:
			a = 29
			outputlist.append(a)
		if a == o_list[30]:
			a = 30
			outputlist.append(a)
		if a == o_list[31]:
			a = 31
			outputlist.append(a)
	return list([outputlist,column])
def getrows(frame):
	rowlist = []
	for row in frame.index: 
		rowlist.append(row)
	return rowlist
def insertdatatodf(frame,insertdata):
	currentpos = 0
	rows = getrows(frame)
	for i in range(0,frame.shape[0]):
		frame.at[rows[currentpos],"{}".format(insertdata[1])] = insertdata[0][currentpos]
		currentpos +=1
insertdatatodf(data2,actualnaming(data2,"OffenseTeam"))
insertdatatodf(data2,actualnaming(data2,"DefenseTeam"))
f_list = list(data2.Formation.unique())
def formationrenaming(frame,column = "Formation"):
	result = list(frame["{}".format(column)])
	return result
def formationnaming(frame,column = "Formation"):
	inputlist = []
	inputlist= formatforrenaming(frame,column)
	outputlist = []
	for i in range(0,len(inputlist)):
		a = inputlist[i]
		if a == f_list[0]:
			a = 0
			outputlist.append(a)
		if a == f_list[1]:
			a = 1
			outputlist.append(a)
		if a == f_list[2]:
			a = 2
			outputlist.append(a)
		if a == f_list[3]:
			a = 3
			outputlist.append(a)
		if a == f_list[4]:
			a = 4
			outputlist.append(a)
		if a == f_list[5]:
			a = 5
			outputlist.append(a)
	return list([outputlist,column])
def insertformationdatatodf(frame,insertdata):
	currentpos = 0
	rows = getrows(frame)
	for i in range(0,frame.shape[0]):
		frame.at[rows[currentpos],"Formation"] = insertdata[0][currentpos]
		currentpos +=1
insertformationdatatodf(data2,formationnaming(data2))
X = data2.copy()
X = X.drop(["SeriesFirstDown"],axis = 1)
y = data2.copy()
y = y["SeriesFirstDown"]

logisticRegr.fit(X, y)

test_data = [["SF","NO",4,2,34,"UNDER CENTER"]]
test_cols = ['OffenseTeam','DefenseTeam',"Down","ToGo","YardLine","Formation"]
test_df = pd.DataFrame(test_data, columns = test_cols)
insertdatatodf(test_df,actualnaming(test_df,"OffenseTeam"))
insertdatatodf(test_df,actualnaming(test_df,"DefenseTeam"))
insertformationdatatodf(test_df,formationnaming(test_df))
joblib.dump(logisticRegr,"nfl-model.sav")
print("model dumped")
#judged on a basis of [fail,success]
#options for formation are SHOTGUN, UNDER CENTER, NO HUDDLE SHOTGUN
print(logisticRegr.predict_proba(test_df))
