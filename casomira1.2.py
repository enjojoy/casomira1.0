import mysql.connector

mydb = mysql.connector.connect(host='localhost',user = 'root',passwd='01041976', database='casomira')

mycursor = mydb.cursor(buffered = True)

def new_person():
    #INSERT NEW VALUE TO THE PEOPLE TABLE
    id = input('What their ID will bee?')
    f_name = input('What is their first name?')
    l_name = input('What is their last name?')
    mycursor.execute(f"insert into people values ('{id}','{f_name}','{l_name}')")
    mycursor.execute("select * from people")
    result = mycursor.fetchall()

    for i in result:
        print(i)

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

    #NEW FLIGHT ID FOR TODAY
    def new_flight_id():
        new_flight_id = 0
        last_flight_id = mycursor.execute("select flight_id from flights where date = SYSDATE()", multi = True)
        if str(type(last_flight_id)) == "<class 'NoneType'>":
            new_flight_id = 1
        else:
            last_flight_id += 1
        return new_flight_id

    def let_user_pick(options):
        print("Please choose:")

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
    list_of_aircrafts = []
    mycursor.execute("select * from aircraft")
    result = mycursor.fetchall()
    for i in result:
        i = list(i)
        list_of_aircrafts.append(i)
    def choose_aircraft():
        # list_of_aircrafts = []
        # mycursor.execute("select * from aircraft")
        # result = mycursor.fetchall()
        # for i in result:
        #     i = list(i)
        #     list_of_aircrafts.append(i)
        active_aircraft = list_of_aircrafts[let_user_pick(list_of_aircrafts)]
        active_aircraft_id = active_aircraft[0]
        return active_aircraft_id

    new_flight_id = new_flight_id()
    active_aircraft_id = choose_aircraft()

    #COUNTING FLIGHT NUMBER
    mycursor.execute(
        f"select max(aircraft_flight_no) from flights where aircraft_registration ='{active_aircraft_id}'")
    result = mycursor.fetchone()

    def aircraft_flight_no():
        # last_flight_no = mycursor.execute(f"select max(aircraft_flight_no) from flights where aircraft_registration ='{active_aircraft_id}'")
        if str(type(result)) == "<class 'NoneType'>":
            last_flight_no = 1
        else:
            last_flight_no = result + 1
        return last_flight_no

    #CHOOSE CAPITAN FROM A LIST OF PEOPLE
    def choose_capitan():
        list_of_people = []
        mycursor.execute("select * from people")
        result = mycursor.fetchall()
        for i in result:
            i = list(i)
            list_of_people.append(i)
        active_capitan = list_of_people[let_user_pick(list_of_people)]
        return active_capitan[0]

    #CHOOSE STUDENT FROM A LIST OF PEOPLE
    def choose_student():
        list_of_people = []
        mycursor.execute("select * from people")
        result = mycursor.fetchall()
        for i in result:
            i = list(i)
            list_of_people.append(i)
        active_student = list_of_people[let_user_pick(list_of_people)]
        return active_student[0]

    #CHOOSE START TYPE
    def choose_start_type():
        start_types_list = ['M', 'A']
        active_start_type = start_types_list[let_user_pick(start_types_list)]
        return active_start_type

    # new_flight_id = new_flight_id()
    # active_aircraft_id = choose_aircraft()
    aircraft_flight_no = aircraft_flight_no()



new_flight()
    #INSERT NEW FLIGHT COUNT



# def let_user_pick(options):
#         print("Please choose:")
#
#         for idx, element in enumerate(options):
#             print("{}) {}".format(idx + 1, element))
#
#         i = input("Enter number: ")
#         try:
#             if 0 < int(i) <= len(options):
#                 return int(i) - 1
#         except:
#             pass
#         return None
# def choose_aircraft():
#     list_of_aircrafts = []
#     mycursor.execute("select * from aircraft")
#     result = mycursor.fetchall()
#     for i in result:
#         i = list(i)
#         list_of_aircrafts.append(i)
#     active_aircraft = list_of_aircrafts[let_user_pick(list_of_aircrafts)]
#     active_aircraft_id = active_aircraft[0]
#     return active_aircraft_id
#
# lala = choose_aircraft()
# print(lala)













# list_of_aircrafts = []
# mycursor.execute("select * from aircraft")
# result = mycursor.fetchall()
# for i in result:
#     i = list(i)
#     list_of_aircrafts.append(i)
# active_aircraft = let_user_pick(list_of_aircrafts)
# res = let_user_pick(options)
#
# print(options[res])

# list_of_people = []
# mycursor.execute("select * from people")
# result = mycursor.fetchall()
# for i in result:
#     i = list(i)
#     list_of_people.append(i)
# active_capitan = let_user_pick(list_of_people)
# print(active_capitan)

#
# def let_user_pick(options):
#     print("Please choose:")
#
#     for idx, element in enumerate(options):
#         print("{}) {}".format(idx + 1, element))
#
#     i = input("Enter number: ")
#     try:
#         if 0 < int(i) <= len(options):
#             return int(i) - 1
#     except:
#         pass
#     return None
#
# list_of_people = []
# mycursor.execute("select * from people")
# result = mycursor.fetchall()
# for i in result:
#     i = list(i)
#     list_of_people.append(i)
# active_capitan = list_of_people[let_user_pick(list_of_people)]
# print(active_capitan[2])
