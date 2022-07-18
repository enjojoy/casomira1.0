import mysql.connector

mydb = mysql.connector.connect(host='localhost',user = 'root',passwd='01041976', database='casomira')

mycursor = mydb.cursor()

# def new_person():
#     #INSERT NEW VALUE TO THE PEOPLE TABLE
#     id = input('What their ID will bee?')
#     f_name = input('What is their first name?')
#     l_name = input('What is their last name?')
#     mycursor.execute(f"insert into people values ('{id}','{f_name}','{l_name}')")
#     mycursor.execute("select * from people")
#     result = mycursor.fetchall()
#
#     for i in result:
#         print(i)

def new_aircraft():
    #INSERT NEW VALUE TO THE AIRCRAFT TABLE
    aircraft_reg = input('Aircraft registration please:')
    model = input('Aircraft model:')
    mycursor.execute(f"insert into aircraft values ('{aircraft_reg}','{model}', 0)")
    mycursor.execute("select * from aircraft")
    result = mycursor.fetchall()

    for i in result:
        print(i)

def new_flight():
    #INSERT NEW FLIGHT INFORMATION
    print('New flight created')

    #COUNTING FLIGHT NUMBER
    last_flight_no = mycursor.execute()

class People:
    def  __init__(self, id, first_n, last_n, minutes_flied ):
        self.id = id
        self.first_n = first_n
        self.last_n = last_n
        self.minutes_flied = minutes_flied

    def new_person(self):
        # INSERT NEW VALUE TO THE PEOPLE TABLE
        id = input('What their ID will bee?')
        first_n = input('What is their first name?')
        last_n = input('What is their last name?')
        mycursor.execute(f"insert into people values ('{id}','{first_n}','{last_n}')")
        mycursor.execute("select * from people")
        result = mycursor.fetchall()

        for i in result:
            print(i)











