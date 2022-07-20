import mysql.connector
from datetime import date
from datetime import datetime
import time

mydb = mysql.connector.connect(host='localhost',user = 'root',passwd='01041976', database='casomira1')


def let_user_pick(options):
    for idx, element in enumerate(options):
        print("{}) {}".format(idx + 1, element))

    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            return int(i) - 1
    except:
        pass
    return None

#ADD NEW DATA TO THE DATABASE
def new_person():
    #INSERT NEW VALUE TO THE PEOPLE TABLE

    mycursor = mydb.cursor()
    f_name = input('What is their first name?')
    l_name = input('What is their last name?')
    mycursor.execute(f"insert into people (first_name,last_name) values ('{f_name}','{l_name}')")
    mycursor.execute("select * from people")
    result = mycursor.fetchall()
    mydb.commit()
    for i in result:
        print(i)
    mycursor.close()
def new_aircraft():
    mycursor = mydb.cursor()
    #INSERT NEW VALUE TO THE AIRCRAFT TABLE
    aircraft_reg = input('Aircraft registration please:')
    model = input('Aircraft model:')
    mycursor.execute(f"insert into aircraft values ('{aircraft_reg}','{model}', 0)")
    mycursor.execute("select * from aircraft")
    result = mycursor.fetchall()
    mydb.commit()
    for i in result:
        print(i)

#ADD NEW FLIGHT INFO
def new_flight():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='01041976', database='casomira1')
    mycursor = mydb.cursor()
    #INSERT NEW FLIGHT INFORMATION
    print('New flight created')

    def let_user_pick(options):

        for idx, element in enumerate(options):
            print("{}) {}".format(idx + 1, element))

        i = input("Enter number: ")
        try:
            if 0 < int(i) <= len(options):
                return int(i) - 1
        except:
            pass
        return None

    #CHOOSE FROM A LIST OF AIRCRAFTS

    def choose_aircraft():
        list_of_aircrafts = []
        mycursor.execute("select * from aircraft")
        result = mycursor.fetchall()
        for i in result:
            i = list(i)
            list_of_aircrafts.append(i)
        active_aircraft = list_of_aircrafts[let_user_pick(list_of_aircrafts)]
        active_aircraft_id = active_aircraft[0]
        mycursor.close()
        return active_aircraft_id

    #COUNTING FLIGHT NUMBER

    def aircraft_flight_no():
        #returns flight_no
        mycursor = mydb.cursor(buffered=True)
        try:
            mycursor.execute(f"select max(aircraft_flight_no) from flights where aircraft_registration ='{active_aircraft_id}'")
            result = list(mycursor.fetchone())
            flight_no = result[0]
            mycursor.close()
            if flight_no is None:
                flight_no = 1
            else:
                flight_no = int(flight_no) + 1
        except:
            flight_no = 1


        return flight_no

    #CHOOSE CAPITAN FROM A LIST OF PEOPLE
    def choose_capitan():
        mycursor = mydb.cursor(buffered=True)
        list_of_people = []
        mycursor.execute("select * from people")
        result = mycursor.fetchall()
        for i in result:
            i = list(i)
            list_of_people.append(i)
        active_capitan = list_of_people[let_user_pick(list_of_people)]
        mycursor.close()
        return active_capitan[0]

    #CHOOSE STUDENT FROM A LIST OF PEOPLE
    def choose_student():
        mycursor = mydb.cursor(buffered=True)
        list_of_stu = []
        mycursor.execute("select * from people")
        result = mycursor.fetchall()
        for i in result:
            i = list(i)
            list_of_stu.append(i)
        active_student = list_of_stu[let_user_pick(list_of_stu)]
        mycursor.close()
        return active_student[0]

    #CHOOSE START TYPE
    def choose_start_type():
        start_types_list = ['M', 'A']
        active_start_type = start_types_list[let_user_pick(start_types_list)]
        return active_start_type

    print("Please choose an aircraft:")
    active_aircraft_id = choose_aircraft()
    aircraft_flight_no = aircraft_flight_no()
    print("Please choose a capitan:")
    capitan_id = choose_capitan()
    print("Please choose a student:")
    student_id = choose_student()
    print("Please choose a start type:")
    start_type = choose_start_type()
    date_today = date.today()
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute(f"INSERT INTO flights (date, aircraft_registration, aircraft_flight_no, capitan_id, student_id, start_type) VALUES (SYSDATE(), '{active_aircraft_id}', '{aircraft_flight_no}', '{capitan_id}', '{student_id}', '{start_type}');")
    mycursor.close()
    mydb.commit()









    #INSERT NEW FLIGHT COUNT

#ADD TAKEOFF TIME FOR THE CHOOSEN FLIGHT
def time_of_flight():
    def choose_flight():
        mycursor = mydb.cursor()
        list_of_flights = []
        mycursor.execute("select * from flights where flight_takeoff is null or flight_landing is null")
        result = mycursor.fetchall()
        for i in result:
            i = list(i)
            list_of_flights.append(i)
        active_flight = list_of_flights[let_user_pick(list_of_flights)]

        print(f"Active flight is : {active_flight}")
        mycursor.close()
    choose_flight()



    # def time_convert(sec):
    #     mins = sec // 60
    #     sec = sec % 60
    #     hours = mins // 60
    #     mins = mins % 60
    #     return("Time Lapsed = {1} minutes".format(int(mins)))
    #
    # input('Press ENTER to START the flight')
    # takeoff_time = datetime.now()
    # print(f"Takeoff time is {takeoff_time}")
    #
    #
    # input('Press ENTER to END the flight for the towplain')
    # towplain_landing_time = time.time()
    #
    # input('Press ENTER to END the flight for the glider')
    # glider_landing_time = time.time()
    #
    # print("")
    #

#CASOMIRA PROGRAM LOGIC
def menu():
    print('Hello and welcome to  CASOMIRA')
    #CHOICE OF AN OPTION
    def main_menu():

        menu_options = {
            1: 'Add new person to the database',
            2: 'Add new aircraft to the database',
            3: 'Work with casomira',
            4: 'Exit',
        }

        while True:
            try:
                print(menu_options)
                opt = int(input('What do you want to do?'))
            except ValueError:
                print('Please enter a valid choice!')
            else:
                break

        print(f'Your choice is: {menu_options[opt]}')
        if opt == 1:
            new_person()
        if opt == 2:
            new_aircraft()
        # if opt == 3:

work_with_flights_options = {
    1: 'Add new flight',
    2: 'Add time to the existing flights',
    3: 'Go back to the main menu'
}


new_flight()