from json.tool import main
import habit_tracking

def test_func(name='pre_defined'):

    h=habit_tracking.Habit_Tracker(name)

    result=h.analyze_habit()

    return result



def main_func(order=0,name='pre_defined'):
    
    
    if order=='0':
        
        h=habit_tracking.Habit_Tracker(name)

        h.analyze_habit()

        return 
        
    else:

        h=habit_tracking.Habit_Tracker(name)
        
        while True:

            if order=='6':
                print('application stoped')
                break
            else:
                

                if order=='1':
                    h.create_habit()

                if order=='2':
                    h.update_habit()

                if order=='3':
                    h.delete_habit()

                if order=='4':
                    h.analyze_habit()

                if order=='5':
                    h.update_habit(check_off=True)

            con=input('do you want to continue y/n : ')
            if con=='n':
                print('application stoped')
                break
            if con=='y':
                order=input('choose one of the numbers to start 1)create habit_list 2)update a habit 3)delete a habit 4)analyze habits 5)quit')
                continue

if __name__=='__main__':
    name=input('please enter your name without space : ')

    order=input('choose one of the numbers to start\n 0)see pre_defined habits\n 1)create habit\n 2)update habit\n 3)delete habit\n 4)analyze habits\n 5)check_off habit 6)quit : ')
    
    main_func(order,name)
         


