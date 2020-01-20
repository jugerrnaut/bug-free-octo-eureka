from flask import Flask,request, url_for, redirect, render_template
import joblib
import pandas as pd
import numpy as np
import math

model = joblib.load("/Users/athreya/desktop/nFl/NFL_Data/nfl-model.sav")


data2 = pd.read_csv("/Users/athreya/Desktop/nFl/NFL_Data/pbp-2019.csv")
drop_columns = ["Description","PlayType","Unnamed: 12","GameId","GameDate","Quarter","Minute","Second","NextScore","TeamWin","SeasonYear","Yards","IsIncomplete","IsRush","IsPass","IsTouchdown","PassType","IsSack","IsChallenge","IsChallengeReversed","Challenger","IsMeasurement","IsInterception","IsFumble","IsPenalty","IsTwoPointConversion","IsTwoPointConversionSuccessful","RushDirection","YardLineFixed","YardLineDirection","IsPenaltyAccepted","PenaltyTeam","IsNoPlay","PenaltyType","PenaltyYards","Unnamed: 10","Unnamed: 16", "Unnamed: 17"]

data2 = data2.loc[data2["Down"] == 4]
data2 = data2.drop(drop_columns, axis = 1)
#baseline for the renaming
o_list = list(data2.OffenseTeam.unique())
f_list = list(data2.Formation.unique())
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

app = Flask(__name__)

@app.route("/",methods = ['GET', 'POST'])
def hello():
  return render_template('main.html')


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


@app.route("/p",methods = ['GET','POST'])
def p():
    OT = request.form['OT']
    DT  = request.form['DT']
    DOWN = request.form['Down']
    TG = request.form['TG']
    YL = request.form['YL']
    FORM = request.form['Formation']
    num = [[OT,DT,DOWN,TG,YL,FORM]]
    columns = ["OffenseTeam","DefenseTeam","Down","ToGo","YardLine","Formation"]
    test_df = pd.DataFrame(num, columns = columns)
    insertdatatodf(test_df,actualnaming(test_df,"OffenseTeam"))
    insertdatatodf(test_df,actualnaming(test_df,"DefenseTeam"))
    insertformationdatatodf(test_df,formationnaming(test_df))
    pred = model.predict_proba(test_df)
    return render_template('p.html',prediction = pred[0])
if __name__ == "__main__":
  app.run()
