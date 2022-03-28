
import Analyzer
import json
from pandas import json_normalize
import os.path
class Habit_Tracker():

    def __init__(self,name) :
        self.name=name
        

    
    def create_habit(self):
        if os.path.isfile(self.name+'.json')!=True :
            print('please enter your first habit properties')
            category=input('please input habit category : ')
            habit=input('please input your habit : ')
            habit_number=input('please input your habit number : ')
            start_date=input('please input the habit start date :')
            end_date=input('please input the habit end date : ')
            habit_dict={ 
                self.name:{
                    habit:
                    {

                    'category':category,
                    'habit_number':habit_number,
                    'habit_name':habit,
                    'start_date':start_date,
                    'end_date':end_date
                    }
                        }
                        }
                    
            if self.name!='pre_defined':
                
                with open(self.name+'.json','w+') as outfile:
                    json.dump(habit_dict,outfile)
        else:
            print('you have created a list before use update to change or add new habit')       
    
    def delete_habit(self):

        if os.path.isfile(self.name+'.json')!=True :

            print('please create a habit_list first')

        else:

            
            habit=input('please input your habit : ')


            with open(self.name+'.json', "r") as outfile:
                data=json.load(outfile)
            data=data[self.name]

            data.pop(habit)

            with open(self.name+'.json', "w") as outfile:
                data=json.dump(data,outfile)


    def update_habit(self,check_off=False):

        

        if os.path.isfile(self.name+'.json')!=True :

            print('please create a habit_list first')

        else:

            category=input('please input habit category : ')
            habit=input('please input your habit : ')
            habit_number=input('please input your habit number : ')
            start_date=input('please input the habit start date :')
            end_date=input('please input the habit end date : ')
            if check_off==True:
                habit='checked '+habit
                status='checked off'
            else:
                status=''
            habit_dict={ 
                habit:
                 {

                'category':category,
                'habit_number':habit_number,
                'habit_name':habit,
                'start_date':start_date,
                'end_date':end_date,
                'status':status
                 }
                        }
            
            with open(self.name+'.json', "r") as outfile:
                data=json.load(outfile)
            
            data[self.name].update(habit_dict)

            with open(self.name+'.json', "w") as outfile:
                data=json.dump(data,outfile)

    def analyze_habit(self):

        if self.name=='pre_defined':
           return Analyzer.analyze(self.name) 
        else:
            
            Analyzer.analyze(self.name)
            
        


        pass

