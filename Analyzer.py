import pandas as pd 
import json


def analyze(name):
#analyzing the pre defined file
    if name=="pre_defined":
        with open(name+'.json', "r") as outfile:
            data=json.load(outfile)
        habits=list(data[name].keys())
        habit_list=list(data[name].values())
        print('current pre_defined habits: ',habits)
        return True
    habit_name=input('if you want to analyze a specific habit enter the habits name : ')
    with open(name+'.json', "r") as outfile:
        data=json.load(outfile)
    habits=list(data[name].keys())
    #get habit list
    habit_list=list(data[name].values())
    same_habit=set()
    #get same period for habits
    for i in range(0,len(habit_list)-1):
        h1=pd.to_datetime(habit_list[i]['start_date'])
        h2=pd.to_datetime(habit_list[i]['end_date'])
        h3=pd.to_datetime(habit_list[i+1]['start_date'])
        h4=pd.to_datetime(habit_list[i+1]['end_date'])
        if (h2-h1)==(h4-h3):
            same_habit.add(habit_list[i]['habit_name'])
            same_habit.add(habit_list[i+1]['habit_name'])
    #get the longest period
    for i in range(0,len(habit_list)-1):
        l_period=habit_list[i]['habit_name']
        h1=pd.to_datetime(habit_list[i]['start_date'])
        h2=pd.to_datetime(habit_list[i]['end_date'])
        h3=pd.to_datetime(habit_list[i+1]['start_date'])
        h4=pd.to_datetime(habit_list[i+1]['end_date'])
        if (h2-h1)<(h4-h3):
            l_period=habit_list[i+1]['habit_name']

        else:
            continue
    #get the longest period for a specific habit
    count=0
    for key,value in data['james_william'].items():
        if value['habit_name']==habit_name and count==0:
            l_period=pd.to_datetime(value['end_date'])-pd.to_datetime(value['start_date'])
            count+=1
        elif value['habit_name']==habit_name and count!=0:
            period=pd.to_datetime(value['end_date'])-pd.to_datetime(value['start_date'])
            if period>l_period:
                l_period=period
    


    print('current habits: ',habits)
    print('the longest period habit is: ',l_period)
    print('habits with the same periods is: ',same_habit)
