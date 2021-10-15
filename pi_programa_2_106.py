# Victoria Rodríguez de León A01656328
# Moisés Adame Aguilar A01660927


from os import read
import pandas as pd
import sys
from PIL import Image 
from math import floor


# .jpg file is stored on "img" variable using Image import from Pillow library
img = Image.open('supercoolbearwow.jpg') 
# csv file database is stored on 'read_doc' so it can be accessed to perform
# the functions' tasks.
read_doc = pd.read_csv('shootings_wash_post.csv')
# Global variable for percentage calculations
total_global = 5557

# Function 1: Return to Home Screen
def home_screen():
    print()
    home = input('Do you want to return to the home screen? Input "yes" or "no": ')
    if home == 'yes':
        # return to main()
        print()
        main()
    elif home == 'no':
        # Display super cool bear saying "goodbye"
        print('Goodbye, user...')
        img.show()
        sys.exit()

# Function 2: Tasks based on database
def values(specific_values):
    which_one = 0
    if specific_values == 'yes':
        while which_one == '1' or '2' or '3' or '4' or '5' or '6' or\
            '7' or '8' or '9' or '10' or '11' or '12' or '13':
            # User is asked their category of interest:
            print('''
Specify: 
1 -  Gender
2 -  Name
3 -  Age
4 -  Date
5 -  Manner of death
6 -  Armed
7 -  Race
8 -  City
9 -  State
10 - Signs of mental illness
11 - Threat level
12 - Flee
13 - Body camera

Extra:
14 - Highlighted categories in relation to race

Input "home" to return to the home screen
Input "exit" to end program.
''')
            which_one = input('Specify: ')
        # For gender
            if which_one == '1':
                # From the database:
                # Sum all the values that correspond to string 'M' in 
                # the column titled 'gender'. Store result in 'm'.
               
                m = (read_doc['gender']=='M').sum()

                # Sum all the values that correspond to string 'F' in 
                # the column titled 'gender'. Store result in 'w'.
                w = (read_doc['gender']=='F').sum()

                # Output
                # 'm' and 'w' variables are transformed to str so they 
                # can be concatenated. 
                print()
                print(f'Total: {str(m+w)}')
                print(f'# of Men: {str(m)}')
                print(f'# of Women: {str(w)}')

                print(f'Male prevalence: {str(round((m*100)/(m+w)))}%')
                print(f'Women prevalence: {str(round((w*100)/(m+w)))}%')
                
            # For name
            elif which_one == '2':
                inp = input('Inserta el nombre del que te gustaría obtener información (e.g; "Brock Nichols"): ')
               
                # If user's input exists on the database, follow algorithm:
                if inp in read_doc.values:
                    # With pandas .loc() property, user's input is searched in the column 'name'.
                    index = read_doc.loc[read_doc['name'] == inp].index[0]
                    # If it's found, all the available information corresponding to the row where 
                    # it is located will be displayed in the terminal. 
                    print(read_doc.loc[index])

                # Else, tell the user there was an input error. 
                else:
                    print('Input error: Name was not found on database. ')
                    # Ask user if they want to return to home screen:
                    home_screen()
           
            
            # For age
            elif which_one == '3':
                # From all the values in the database's column "age", the maximum value is 
                # obtained and stored in max_age.
                max_age = read_doc['age'].max()
                # From all the values in the database's column "age", the minimum value is 
                # obtained and stored in min_age.
                min_age = read_doc['age'].min()
                # Mean is automatically calculated from all the values in the database's column 
                # "age" and stored in mean_age.
                mean_age = read_doc['age'].mean()

                # Output:
                print()
                print(f"Edad promedio:  {str(int(floor(mean_age)))} años")
                print(f"Edad máxima: {str(int(max_age))} años")
                print(f"Edad mínima: {str(int(min_age))} años")
                #Range is directly calculated.
                print(f"Rango:  {str(int(max_age-min_age))} años")

            # For date
            elif which_one == '4':
                # Create new column named 'Year' based on pandas DatetimeIndex attribute to
                # get only the year from the original date.
                read_doc['Year'] = pd.DatetimeIndex(read_doc['date']).year

                # Create new column named 'Month' based on pandas DatetimeIndex attribute to 
                # get only the month from the original date.
                read_doc['Month'] = pd.DatetimeIndex(read_doc['date']).month

                # In the database's "Year" column (created manually on line 120), values with the 
                # specified equivalence (e.g. ['Year']==2015) are searched. If found, they are added
                # and the result is stored in the corresponding variable (e.g. "y_2015").

                y_2015 = (read_doc['Year']==2015).sum()
                y_2016 = (read_doc['Year']==2016).sum()           
                y_2017 = (read_doc['Year']==2017).sum()                
                y_2018 = (read_doc['Year']==2018).sum()                
                y_2019 = (read_doc['Year']==2019).sum()              
                y_2020 = (read_doc['Year']==2020).sum()

                # In the database's "Month" column (created manually on line 124), values with 
                # the specified equivalence (e.g. ['Month']==1) are searched. If found, they are added 
                # and the result is stored in the corresponding variable (e.g. "jan"). 

                jan = (read_doc['Month']==1).sum()
                feb = (read_doc['Month']==2).sum()              
                mar = (read_doc['Month']==3).sum()           
                apr = (read_doc['Month']==4).sum()          
                may = (read_doc['Month']==5).sum()           
                jun = (read_doc['Month']==6).sum()           
                jul = (read_doc['Month']==7).sum()             
                aug = (read_doc['Month']==8).sum()           
                sep = (read_doc['Month']==9).sum()           
                oct = (read_doc['Month']==10).sum()            
                nov = (read_doc['Month']==11).sum()            
                dec = (read_doc['Month']==12).sum()

            # Input: menu with code of letters is presented to the user.
                choose_letter = 0
                print('''

Choose a letter to obtain the information of your interest:
a - Shootings per year
b - Shootings per month
c - Both
Input "x" when you are done.
''')
                
                # Output if user wants to know shootings per year:
                while choose_letter == 'a' or 'b' or 'c':
                    choose_letter = input('Input letter: ')

                    if choose_letter == 'a':
                        print(f'''

Shootings per year:
2015 = {y_2015} shootings.
2016 = {y_2016} shootings.
2017 = {y_2017} shootings.
2018 = {y_2018} shootings.
2019 = {y_2019} shootings.
2020 = {y_2020} shootings.
''')

                # Output if user wants to know shootings per month:
                    elif choose_letter == 'b':
                        print(f'''

Shootings per month:
January = {jan} shootings.
February = {feb} shootings.
March = {mar} shootings.
April = {apr} shootings.
May = {may} shootings.
June = {jun} shootings.
July = {jul} shootings.
August = {aug} shootings.
September = {sep} shootings.
October = {oct} shootings.
November = {nov} shootings.
December = {dec} shootings.
''')
                    # Output if user wants to know both shootings per year and shootings per month:
                    elif choose_letter == 'c':
                        print(f'''

Shootings per year:
2015 = {y_2015} shootings.
2016 = {y_2016} shootings.
2017 = {y_2017} shootings.
2018 = {y_2018} shootings.
2019 = {y_2019} shootings.
2020 = {y_2020} shootings.

Shootings per month:
January = {jan} shootings.
February = {feb} shootings.
March = {mar} shootings.
April = {apr} shootings.
May = {may} shootings.
June = {jun} shootings.
July = {jul} shootings.
August = {aug} shootings.
September = {sep} shootings.
October = {oct} shootings.
November = {nov} shootings.
December = {dec} shootings.
''')
                    # Break loop if user's input is equal to 'x'
                    elif choose_letter == 'x':
                        break

                    else:
                    # Else, tell user the input is invalid and ask them if they want to return 
                    # to the home screen
                        print('Invalid input.')
                        home_screen()
                        
                
            # For manner of death:
            elif which_one == '5':
                shot = (read_doc['manner_of_death']=='shot').sum()

                # Sum all the values corresponding to string 'shot and Tasered' in the database's column 
                # titled 'manner_of_death'. Store result in "shot_and_tasered" variable.
                shot_and_tasered = (read_doc['manner_of_death'] =='shot and Tasered').sum()

                # Calculate percentages (values are rounded).
                shot_per = round((shot*100)/(shot+shot_and_tasered))
                shot_tasered_per = round((shot_and_tasered*100)/(shot+shot_and_tasered))

                # Output: 'shot' and 'shot_and_tasered' variables are transformed to str so they can 
                # be concatenated.
                print(f'# of shot citizens: {str(shot)}')
                print(f'# of shot and tasered citizens: {str(shot_and_tasered)}')
                print(f'% of shot citizens: {shot_per}%')
                print(f'% of shot and tasered citizens: {shot_tasered_per}%')
                print('Related to race:')
                

            # For armed:
            elif which_one == '6':
                # Sum all the values that correspond to string 'gun' in the database's column titled 
                # "armed". Store result in "gun" variable.
                # Same case for variables "knife", "toy_weapon", "vehicle" and "unarmed"; making
                # the equivalence with the corresponding string (e.g. 'knife' for "knife"). 

                gun = (read_doc['armed']=='gun').sum()
                knife = (read_doc['armed']=='knife').sum()
                toy_weapon = (read_doc['armed']=='toy weapon').sum()
                vehicle = (read_doc['armed']=='vehicle').sum()
                unarmed = (read_doc['armed']=='unarmed').sum()
                others = total_global-(gun+knife+toy_weapon+unarmed+vehicle)
                
                # Output:
                print()
                print(f'Gun armed: {gun}')
                print(f'Toy weapon armed: {toy_weapon}')
                print(f'Knife armed: {knife}')
                print(f'Vehicle armed: {vehicle}')
                print(f'Unarmed: {unarmed}')
                print(f'Others: {others}') 
                print()

                # Output (Values of percentages are rounded).
                print(f'% Gun armed: {round((gun*100)/total_global)}%')
                print(f'% Toy weapon armed: {round((toy_weapon*100)/total_global)}%')
                print(f'% Knife armed: {round((knife*100)/total_global)}%')
                print(f'% Vehicle armed: {round((vehicle*100)/total_global)}%')
                print(f'% Unarmed: {round((unarmed*100)/total_global)}%')
                print(f'% Others: {round((others*100)/total_global)}%')

            # For race:    
            elif which_one == '7':
                # For all cases, in the database's column titled 'race', look for specified 
                # string (e.g. 'W') and sum all found values, storing them after in the 
                # corresponding variable (e.g. "w")

                #white, non-hispanic
                w = (read_doc['race']=='W').sum()
                #black, non hispanic 
                b = (read_doc['race']=='B').sum()
                #asian
                a = (read_doc['race']=='A').sum()
                #native american
                n = (read_doc['race']=='N').sum()
                #hispanic
                h = (read_doc['race']=='H').sum()
                #others
                o = total_global - (w+b+a+n+h)
                
                # Output:
                print()
                print(f'White, non-Hispanic: {w}')
                print(f'Black, non-Hispanic: {b}')
                print(f'Asian: {a}')
                print(f'Native American: {n}')
                print(f'Hispanic: {h}')
                print(f'Others: {o}')
                print('')

                # Output (values of percentages are rounded):
                print(f'% White, non-Hispanic: {round((w*100)/total_global)}%')
                print(f'% Black, non-Hispanic: {round((b*100)/total_global)}%')
                print(f'% Asian: {round((a*100)/total_global)}%')
                print(f'% Native American: {round((n*100)/total_global)}%')
                print(f'% Hispanic: {round((h*100)/total_global)}%')
                print(f'% Others: {round((o*100)/total_global)}%')
                
            # For city:
            elif which_one == '8':

                select_city = input('Input the name of the city of your interest. (p.ej; "Austin"): ')
                want_to = input('Do you want to see all the data or specific data. Input "all" or "specific": ')

                # If user's input exists on the database, follow algorithm
                if select_city in read_doc.values:

                    # If user's input is equal to 'all':
                    if want_to == 'all':
                    # A list that contains all the values of the database's columns titles 
                    # is stored in variable "lst".
                        lst = ['id','city','name','date', 'armed', 'gender', 'state',\
                            'signs_of_mental_illness','flee','body_camera', 'age',\
                            'race', 'manner_of_death', 'threat_level']

                        all_or_not = input('Display all columns? Input "yes" or "no": ')

                        # Display all columns
                        if all_or_not == 'yes':
                            # Display all rows and columns
                            pd.set_option('display.max_rows', None, 'display.max_columns', None)
                            # From the column 'city' in the database, search all the values that are equal to
                            # the user's input ("select_city"). If found, print the values of the categories 
                            # specified in lst according to each row's index. 
                            print(read_doc[read_doc['city'] == select_city] [lst])

                        # Don't display all columns
                        elif all_or_not == 'no':
                            # Reset maximum # of rows and columns to pandas' default 
                            # mode (truncated DataFrame)
                            pd.reset_option('all', silent=True)
                            print(read_doc[read_doc['city'] == select_city] [lst])

                        # Else, tell user the input is invalid and ask them if they want to return 
                        # to the home screen
                        else:
                            print('Invalid input')
                            home_screen()     
                              

                    # If user's input is equal to 'specific':
                    elif want_to == 'specific':
                    # Code of numbers presented to the user for efficiency. Each number corresponds 
                    # to a column's title on the database. 
                        print('''

Input the categories of your interest using the following code of numbers:
1 - id
2 - name
3 - date
4 - manner of death
5 - armed 
6 - age
7 - gender
8 - race
9 - state  
10 - signs of mental illness
11 - threat level
12 - flee
13 - body camera?
Input "x" when you are finished.
''')

                    # "lst" variable is initialized with the a list that contains the default 
                    # string 'city'. As the user is asking about the city, it's not logical 
                    # to present it in the code of numbers.
                        lst = ['city']
                    # "specify" is initialized to be used in while loop
                        specify = 0
                    
                    # while specify is not equal to 'x' (meaning that the user has finished):
                        while specify != 'x':
                            specify = input('Input: ')
                            # Evaluate input if specify is not equal to "x"
                            if specify != 'x':
                                # For all numbers and their corresponding string, evaluate if the 
                                # equivalance is correct. If it is, append value to the list in "lst"
                                if specify == '1':
                                    specify = 'id'
                                    lst.append(specify)
                                elif specify == '2':
                                    specify = 'name'
                                    lst.append(specify)
                                elif specify == '3':
                                    specify = 'date'
                                    lst.append(specify)
                                elif specify == '4':
                                    specify = 'manner_of_death'
                                    lst.append(specify)
                                elif specify == '5':
                                    specify = 'armed'
                                    lst.append(specify)
                                elif specify == '6':
                                    specify = 'age'
                                    lst.append(specify)
                                elif specify == '7':
                                    specify = 'gender'
                                    lst.append(specify)
                                elif specify == '8':
                                    specify = 'race'
                                    lst.append(specify)
                                elif specify == '9':
                                    specify = 'state'
                                    lst.append(specify)
                                elif specify == '10':
                                    specify = 'signs_of_mental_illness'
                                    lst.append(specify)
                                elif specify == '11':
                                    specify = 'threat_level'
                                    lst.append(specify)
                                elif specify == '12':
                                    specify = 'flee'
                                    lst.append(specify)
                                elif specify == '13':
                                    specify = 'body_camera'
                                    lst.append(specify)
                                else:
                                    print("Invalid input. We won't take it into account. ")
                                    pass

                            # if "specify" is equal to 'x' (meaning the user has finished):
                            if specify == 'x':
                                #Display all rows and columns
                                pd.set_option('display.max_rows', None, 'display.max_columns', None)
            
                                # Search all values equal to user's input in "select_city" and, 
                                # based on the row index, print only the values corresponding to
                                # the columns' titles stored in "lst". 
                                print(read_doc[read_doc['city'] ==select_city] [lst])

                            else:
                                pass
                    
                    else:
                        print('Invalid input')
                        # Return to home screen?
                        home_screen()
                else:
                    print('City input was not found on the database.')
                    home_screen()
                   

            # For state:     
            elif which_one == '9':

                choose_letter = 0
                while choose_letter == 'a' or 'b' or 'c' or 'd':
                    print('''
Choose an option:
a - Consult general data about specific states. 
b - Consult specific data about specific states.
c - Consult number of deaths of all the available states. 
d - Consult number of deaths of specific states. 
Input 'x' when you are finished.
''')
                    choose_letter = input('Input letter: ')

                    # If user wants to consult general data about specific states:
                    if  choose_letter == 'a':
                        # Ask state to the user:
                        select_state = input('Input the abbreviation of your state of interest (e.g. "RI" for Rhode Island.): ')
                        # Display all rows and columns
                        pd.set_option('display.max_rows', None, 'display.max_columns', None)

                        # If user's input exists on the database, follow algorithm
                        if select_state in read_doc.values:
                    
                            # List with the titles of all the database's categories is created and stored in lst. 
                            lst = ['id', 'name', 'date', 'manner_of_death', 'armed', 'age', 'gender',\
                                  'race', 'city', 'state','signs_of_mental_illness', 'threat_level',\
                                  'flee', 'body_camera']

                            # From the column 'state' in the database, search all the values that are equal to
                            # the user's input. If found, print the values of all the categories corresponding 
                            # to each row's index. 
                            print(read_doc[read_doc['state'] == select_state] [lst])

                        # Else, tell user the user was not found and ask them if they want to return to 
                        # the homescreen
                        else: 
                            print('State input was not found on the database.')
                            pass


                    # If user wants to consult specific data about specific states:
                    elif choose_letter == 'b':
                        select_state = input('Input the abbreviation of your state of interest (e.g. "IA" for Iowa.): ')

                        # If user's input exists on the database, follow algorithm
                        if select_state in read_doc.values:
                            print('''

Input the categories of your interest using the following code of numbers:
1  - id
2  - name
3  - date
4  - manner of death
5  - armed  
6  - age
7  - gender
8  - race
9  - city  
10 - signs of mental illness
11 - threat level 
12 - flee
13 - body camera
Input "x" when you are finished.
''')

                            # "lst" is initialized with the default string 'state'. As the user is asking 
                            # about the state, it's not logical to present it in the code of numbers.
                            lst = ['state']
                            # variable 'specify' is initialized to be used in while loop. 
                            specify = 0

                            while specify != 'x': 
                                specify = input('Input: ')
                                
                                if specify != 'x':
                                # For all numbers and their corresponding string, evaluate if the 
                                # equivalance is correct. If it is, append value to the list in "lst"
                                    if specify == '1':
                                        specify = 'id'
                                        lst.append(specify)
                                    elif specify == '2':
                                        specify = 'name'
                                        lst.append(specify)
                                    elif specify == '3':
                                        specify = 'date'
                                        lst.append(specify)
                                    elif specify == '4':
                                        specify = 'manner_of_death'
                                        lst.append(specify)
                                    elif specify == '5':
                                        specify = 'armed'
                                        lst.append(specify)
                                    elif specify == '6':
                                        specify = 'age'
                                        lst.append(specify)
                                    elif specify == '7':
                                        specify = 'gender'
                                        lst.append(specify)
                                    elif specify == '8':
                                        specify = 'race'
                                        lst.append(specify)
                                    elif specify == '9':
                                        specify = 'city'
                                        lst.append(specify)
                                    elif specify == '10':
                                        specify = 'signs_of_mental_illness'
                                        lst.append(specify)
                                    elif specify == '11':
                                        specify = 'threat_level'
                                        lst.append(specify)
                                    elif specify == '12':
                                        specify = 'flee'
                                        lst.append(specify)
                                    elif specify == '13':
                                        specify = 'body_camera'
                                        lst.append(specify)
                                    else:
                                        print("Invalid input. We won't take it into account. ")
                                        pass

                                # If "specify" is equal to "x", meaning that the user has finished:
                                if specify == 'x':
                                    #Display all rows and columns
                                    pd.set_option('display.max_rows', None, 'display.max_columns', None)
                                    # From the state the user specified in "select_state", print the values
                                    # that correspond to the user's input in relation to the state they selected.
                                    print(read_doc[read_doc['state'] == select_state] [lst])

                        else:
                            print('Value was not found on the database.')
                            pass
                                

                    # Consult number of deaths of all the available states     
                    elif choose_letter == 'c':
                        # In the column 'state', classify all the unique values counting the number
                        # of times each is repeated; presenting them from highest to lowest.
                        count_items = read_doc['state'].value_counts()
                        print('Number of deaths per state (From highest to lowest):')
                        print(count_items)
                    
                    # Consult number of deaths of specific states. 
                    elif choose_letter == 'd':
                        print('Input the abbreviation of your state of interest (e.g. "CA" for Caliornia.). Input "x" when you are finished.')
                        # Initialized variables for while loop
                        inp = 0 
                        read_state = 0
                        # While the user's input is not equal to "x", keep asking state and printing the 
                        # corresponding number of deaths if the condition is met.
                        while inp != 'x':
                            inp = input('State: ')

                            # if the value inp is not equal to 'x' (meaning the user has finished) and if 
                            # inp exists on the database, follow algorithm:

                            if inp != 'x' and inp in read_doc.values:
                                # From the column titled 'state' on the database, search values
                                # that are equal to the user's input, if found, add them and store the result
                                # in the variable read_state. Then print it.
                                read_state = (read_doc['state'] == inp).sum()
                                print(f'Number of deaths: {read_state}')

                            elif inp == 'x':
                                break

                            else:
                                print('State input was not found on the database')
                                pass
                                
                        else:
                            break
                    
                    elif choose_letter == 'x':
                        break

                    else:
                        print('Invalid input')
                        home_screen()
                       

            # For signs of mental illness
            elif which_one == '10':
                # From the column titled 'armed' on the database, search all the values 
                # that are equal to the string 'gun' and add them if found. Then, store
                # the result in variable "gun".
                gun = (read_doc['armed']=='gun').sum()

                print(''' 
Choose a number:
1 - Signs of mental illness per state
2 - Signs of mental illness per city
Input 'x' when you are finished
                ''')
                inp = 0

                while inp == '1' or '2':
                    inp = input('Input: ')
                    #For signs of mental illness per state
                    if inp == '1':
                        # Display all rows
                        pd.set_option('display.max_rows', None)

                        # Create a pandas dataframe which contains an aggrupation of the True/False cases 
                        # number that corresponds to the signs of mental illness per state
                        group_data = pd.DataFrame(read_doc.groupby(['state', "signs_of_mental_illness"]).size())
                        print(group_data)
                    
                        # For both cases (true and false), in the dataframe's column titled 
                        # "signs_of_mental_illness", search the corresponding values 
                        # (True or False). If found, add them and store the result in the corresponding 
                        # variable (true for True, false for False).
                        true = (read_doc['signs_of_mental_illness'] == True).sum()
                        false = (read_doc['signs_of_mental_illness'] == False).sum()

                        # Rounded percentage:
                        true_per = round((true*100)/total_global)
                        false_per = round((false*100)/total_global)

                        print(f'''
General:
True: {true} cases, {true_per}%
False: {false} cases, {false_per}%
''')

                    # For signs of mental illness per city
                    elif inp == '2':
                        # User is asked their city of interest for further calculations.
                        select_city = input('Input the name of the city of your interest (e.g. "Orlando"): ')

                        if select_city in read_doc.values:
                        
                            # Using as a reference the column titled "city" on the dataframe, read all values that
                            # are equal to the user's input. Then, on the row's index of each, read the values of
                            # only the columns titled "city" and "signs_of_mental_illness". Finally, with pd.DataFrame, 
                            # convert all into a dataframe and store it in the df variable.
                            df = pd.DataFrame(read_doc[read_doc['city'] ==select_city] [['city', 'signs_of_mental_illness']])

                            # On the dataframe's column titled 'signs_of_mental_illness', add all values that
                            # are False and store the result in the "false" variable.
                            false = (df['signs_of_mental_illness']==False).sum()

                            # On the dataframe's column titled 'signs_of_mental_illness', add all values that
                            # are True and store the result in the "false" variable.
                            true = (df['signs_of_mental_illness']==True).sum()

                            # Rounded percentage:
                            total = false+true
                            true_per = round((true*100)/total)
                            false_per = round((false*100)/total)

                            print(f'''
General info:
Cases with mental illness in {select_city}: {true} ({true_per})%
Cases without mental illness in {select_city}: {false} ({false_per})%
''')
                        else:
                            print('Input was not found on database.')
                            print()
                            pass

                    elif inp == 'x':
                        break

                    # Else, tell user input is invalid and ask them if they want to return to the home screen
                    else:
                        print('Invalid input')
                        home_screen()
                        
                
            
            # For threat level
            elif which_one == '11':
                state_or_city = 0
                while state_or_city == 'state' or 'city':
                    print('To know about the threat level, input "state" or "city": ')
                    print('Input "x" when you are done. ')
                    print()
                    state_or_city = input('Input: ')

                    if state_or_city == 'state':
                        # User is asked their abbreviated state of interest for further calculations.
                        name_state = input('Input the state as an abbreviation (e.g. "UT for Utah"): ')
                        if name_state in read_doc.values:
                            # From the database's column titled 'state', search the string value of name_state
                            df = (read_doc[read_doc['state'] == name_state])
                            # Using the the 'state values' of df as a reference, for each, make an aggrupation of
                            # threat level in relation to race and store everything in the "group" variable 
                            group = df.groupby(['state', 'race', 'threat_level']).size()
                            # Do the same but for all states and not the one specified by the user
                            group_all = (read_doc.groupby(['state', 'race', 'threat_level']).size())     

                            # Considering all the columns that were grouped in group, find max value and store it
                            # in max_threat. Same for min_threat but with the min value.
                            max_threat = group.idxmax()
                            min_threat = group.idxmin()

                            # Do the same but for all the states.
                            general_max_threat = group_all.idxmax()
                            general_min_threat = group_all.idxmin()   

                            print (group)
                            print(f'''
In the format of (state, race, threat type):

From specified state:
Maximum threat: {max_threat}
Minimum threat: {min_threat}

From all states:
Maximum threat: {general_max_threat}
Minimum threat: {general_min_threat}
''')
                            # User's input for further calculations
                            summary = input('Do you want a summary of all states? Input "yes" or "no": ')
                            if summary == 'yes':
                                pd.set_option('display.max_rows', None, 'display.max_columns', None)
                                # Create a pandas dataframe with an aggrupation of the columns of state, race and 
                                # threat_level. Then print it.
                                summary_data = pd.DataFrame(read_doc.groupby(['state', 'race', 'threat_level']).size())
                                print()
                                print(summary_data)
                            else:
                                print('Ok. ')
                                print()
                                pass
                        else:
                            print('Value was not found on the database.')
                            home_screen()
                            

                    elif state_or_city == 'city':
                        # User's input is asked for further calculations.
                        name_city = input('Input the name of the city (e.g. "El Paso"): ')
                        if name_city in read_doc.values:
                            # From the database's column titled 'city', search the string value of name_city
                            df = (read_doc[read_doc['city'] == name_city])

                            # Using the the 'city' values of df as a reference, for each, make an aggrupation of
                            # threat level in relation to race and store everything in the "group" variable 
                            group = df.groupby(['city', 'race', 'threat_level']).size()

                            # Do the same but for all states and not the one specified by the user.
                            group_all = (read_doc.groupby(['city', 'race', 'threat_level']).size())    

                            # Considering all the columns that were grouped in group, find max value and store it
                            # in max_threat. Same for min_threat but with the min value.
                            max_threat = group.idxmax()
                            min_threat = group.idxmin()

                            # Do the same but for all the states
                            general_max_threat = group_all.idxmax()
                            general_min_threat = group_all.idxmin()
                            print()
                            print(group)
                            print(f'''

 In the format of (city, race, threat type):

For specified city:
Maximum threat: {max_threat}
Minimum threat: {min_threat}

For all cities:
Maximum threat: {general_max_threat}
Minimum threat: {general_min_threat}

''')
                    
                        else:
                            print('Value was not found on database.')
                            home_screen()
                           
                    else:
                        if state_or_city == 'x':
                            break
                
                        else:
                            print('Invalid input')
                            home_screen()
                            
            # For flee
            elif which_one == '12':
                # From the column titled 'flee' on the database, search all values
                # that are equal to the string 'Car'. If found, add them and store the result
                # in the variable car. 
                # Do the same for the variables "foot", "not_fleeing" and "other" with their
                # corresponding equivalences.
                car = (read_doc['flee']=='Car').sum()
                foot =  (read_doc['flee']=='Foot').sum()
                not_fleeing =  (read_doc['flee']=='Not fleeing').sum()
                other =  (read_doc['flee']=='Other').sum()
                
                # Percentage calculation
                per_car = (car*100)/total_global
                per_foot = (foot*100)/total_global
                per_not_fleeing = (not_fleeing*100)/total_global
                per_other = (other*100)/total_global
                
                print(f'''
Car: {car} cases, {round(per_car)}%.
Foot: {foot} cases, {round(per_foot)}%.
Others: {other} cases, {round(per_other)}%.
Not fleeing: {not_fleeing} cases, {round(per_not_fleeing)}%.
''')

            # For body camera:
            elif which_one == '13':
                # From the database's column titled 'body_camera', search all True values and
                # add them. Store result in "true" variable.
                true = (read_doc['body_camera']==True).sum()

                # Same case but for False values
                false = (read_doc['body_camera']==False).sum()

                # Percentage calculation (result is rounded)
                true_per = round((true*100)/total_global)
                false_per = round((false*100)/total_global)

                print(f'''
Use of body camera:
True:  {true_per} %
False: {false_per} %
''')

                see_all = input('Do you want to see the True/False values of all states? Input "yes" or "no": ')
                if see_all == 'yes':
                    # Display all rows
                    pd.set_option('display.max_rows', None)
                    df = pd.DataFrame(read_doc.groupby(['state', "body_camera"]).size())
                    print()
                    print(df) 

                elif see_all == 'no':
                    print('ok')     
                    pass      

                else:
                    print('Invalid input.')
                    home_screen()

            # for race related to highlighted categories
            elif which_one == '14':
                choose = 0
                print('''
Choose an option. Input "x" when you're finished.

Race related to:
1 - Manner of death
2 - Unarmed cases
3 - Cities
4 - States
5 - Threat level
6 - Flee?
''')
                while choose != 'x':
                    choose = input('Input: ')
                    # For manner of death related to race
                    if choose == '1':
                        print()
                        manner_of_death = read_doc.groupby(['race', 'manner_of_death']).size()
                        print(manner_of_death.to_string())
                        print()

                    # For unarmed cases related to race
                    elif choose == '2':
                        print()
                        # Create pandas DataFrame from armed and race columns. Only store
                        # store rows that contain the 'unarmed' string in the "armed" column
                        df = pd.DataFrame(read_doc[read_doc['armed']=='unarmed'][['armed', 'race']])
                        # Group them and add them. Print result.
                        unarmed = df.groupby(['race', 'armed']).size()
                        print(unarmed.to_string())
                        print()

                    # City with most killings of black race and white race (predominant)
                    elif choose == '3':
                        # For each, create pandas DataFrame from armed and race columns. Only store
                        # rows that contain the specified string ('B' or 'W')in the "race" column. 
                        # Count values from highest to lowest with .value_counts(). For every case,
                        # print head and tail to get max and min values per city in relation to race
                        print()
                        df_black = pd.DataFrame(read_doc[read_doc['race']=='B'][['city','race']]).value_counts()
                        print('City with the highest killings of black citizens: ')
                        b = df_black.head(1)
                        print(b.to_string())
                        print()

                        print('City with the fewest killings of black citizens: ')
                        b_less = df_black.tail(1)
                        print(b_less.to_string())
                        print()

                        df_white = pd.DataFrame(read_doc[read_doc['race']=='W'][['city','race']]).value_counts()
                        print('City with the highest killings of white citizens: ')
                        w = df_white.head(1)
                        print(w.to_string())
                        print()
                        print('City with the fewest killings of white citizens: ')
                        w_less = df_white.tail(1)
                        print(w_less.to_string())
                        print()
                     
                    # States with most and least killings for each race
                    elif choose == '4':
                        # For each, create pandas DataFrame from armed and race columns. Only store
                        # rows that contain the specified string ('B','W','H','N' or 'A') in the "race"
                        # column. Count values from highest to lowest with .value_counts(). For every 
                        # case, print head and tail to get max and min values per city in relation to race.
                        df_black = pd.DataFrame(read_doc[read_doc['race']=='B'][['state','race']]).value_counts()
                        df_white = pd.DataFrame(read_doc[read_doc['race']=='W'][['state','race']]).value_counts()
                        df_hispanic = pd.DataFrame(read_doc[read_doc['race']=='H'][['state','race']]).value_counts()
                        df_native_american = pd.DataFrame(read_doc[read_doc['race']=='N'][['state','race']]).value_counts()
                        df_asian = pd.DataFrame(read_doc[read_doc['race']=='A'][['state','race']]).value_counts()
                        
                        # black
                        b = df_black.head(1)
                        b_less = df_black.tail(1)
                        print()
                        print(f'''
State with the highest killings of black citizens: 
{b.to_string()}''')
                        print()
                        print(f'''
State with the fewest killings of black citizens: 
{b_less.to_string()}''')
                        # white
                        w = df_white.head(1)
                        w_less = df_white.tail(1)
                        print(f'''
State with the highest killings of white citizens: 
{w.to_string()}''')
                        print()
                        print(f'''
State with the fewest killings of white citizens: 
{w_less.to_string()}''')
                        # hispanic
                        h = df_hispanic.head(1)
                        h_less = df_hispanic.tail(1)
                        print(f'''
State with the highest killings of hispanic citizens: 
{h.to_string()}''')
                        print(f'''
State with the fewest killings of hispanic citizens: 
{h_less.to_string()}''')
                        # native american
                        n_a = df_native_american.head(1)
                        n_a_less = df_native_american.tail(1)
                        print(f'''
State with the highest killings of native american citizens: 
{n_a.to_string()}''')
                        print(f'''
State with the fewest killings of native american citizens: 
{n_a_less.to_string()}''')
                        # asian
                        a = df_asian.head(1)
                        a_less = df_asian.tail(1)
                        print(f'''
State with the highest killings of asian citizens: 
{a.to_string()}''')
                        print(f'''
State with the fewest killings of asian citizens: 
{a_less.to_string()}''')
                        print()

                    # For threat level related to race 
                    elif choose == '5':
                        print()
                        # Display all rows and columns
                        pd.set_option('display.max_rows', None, 'display.max_columns', None)
                        # Group database's race and threat_level columns and count them
                        threat_level = read_doc.groupby(['race', 'threat_level']).size()
                        print(threat_level.to_string())
                        # Reset rows and columns to pandas' default
                        pd.reset_option('all', silent=True)
                        print()
                        
                    # For flee related to race 
                    elif choose == '6':
                        print()
                        # Display all rows and columns
                        pd.set_option('display.max_rows', None, 'display.max_columns', None)
                        # Group database's race and flee columns and count them
                        flee_race = read_doc.groupby(['race', 'flee']).size()
                        print(flee_race.to_string())
                        # Reset rows and columns to pandas' default
                        pd.reset_option('all', silent=True)
                        print()
                   
                    # Exit loop
                    elif choose == 'x':
                        break

                    # Exit loop
                    else:
                        print('Invalid input')
                        break
                    
                else:
                    break
            
            elif which_one == 'home':
                main()

            elif which_one == 'exit':
                print('Goodbye, user...')
                img.show()
                sys.exit()
            
            else:
                print('Invalid input')
                home_screen()
                
        else:
            print('Invalid input.')
            home_screen()
            

    elif specific_values == 'no':
        print('Goodbye, user...')
        img.show()
        sys.exit()

    else:
        print('Invalid input')
        home_screen()
        

# Function 4: Tasks based on Pandas' library:
def functions(pandas_functions):
    if pandas_functions == 'yes':
         
        # "inp" variable is initialized for further use in while loop:
        inp = 0
        while inp == "1" or "2" or "3" or "4" or "5":
            print('''

Select needed computation using the following code of numbers:
1 - Display first "n" values of DataFrame
2 - Display last "n" values of DataFrame 
3 - Show dimensionality of DataFrame
4 - Show concise summary of DataFrame
5 - Show quick statistics of DataFrame
    
Input "x" when you are finished.
''')
   
            inp = input('Specify: ')
            #head: displays the first "n" values (specified by user) of the database.
            
            if inp == '1':
                n = input('Enter "n" value: ')
                see_all_columns = input('Do you want all the columns to be displayed? Input "yes" or "no": ')
                if n.isdigit():
                    if see_all_columns == 'yes':
                        # Display all rows and all columns
                        pd.set_option('display.max_rows', None, 'display.max_columns', None)

                        # Print .head() using as a parameter the value obtained from user's input in "n"
                        print(read_doc.head(int(n)))

                    elif see_all_columns == 'no':
                        # Reset maximum # of rows and columns to pandas' default mode (truncated DataFrame)
                        pd.reset_option('all', silent=True)
                        # Print .head() using as a parameter the value obtained from user's input in "n"
                        print(read_doc.head(int(n)))

                    else:
                        print('Invalid input')
                        home_screen()
                        
                        
                else:
                    print('Invalid input')
                    home_screen()
                    
                
            #tail: displays the last "n" values (specified by user) of the database.
            elif inp == '2':
                n = input('Enter "n" value: ')
                see_all_columns = input('Do you want all the columns to be displayed? Input "yes" or "no": ')
                if n.isdigit():
                    if see_all_columns == 'yes':
                        # Display all rows and all columns
                        pd.set_option('display.max_rows', None, 'display.max_columns', None)

                        # Print .tail() using as a parameter the value obtained from user's input in "n"
                        print(read_doc.tail(int(n)))

                    elif see_all_columns == 'no':
                        # Reset maximum # of rows and columns to pandas' default mode (truncated DataFrame)
                        pd.reset_option('all', silent=True)

                        # Print .tail() using as a parameter the value obtained from user's input in "n"
                        print(read_doc.tail(int(n)))
                    
                    else:
                        print('Invalid input')
                        home_screen()
                       
                else:
                    print('Invalid input')
                    home_screen()
                 
                 
            # Shape returns a tuple representing the dimensionality of the DataFrame
            elif inp == '3':
                print (str(read_doc.shape) + ' in terms of (rows, columns)')

            # Info prints a concise summary of DataFrame
            elif inp == '4':
                print (read_doc.info())
            
            # Describe generates descriptive statistics
            elif inp == '5':
                print('"Describe" indicates a quick statistic summary of your data.')
                print (read_doc.describe())

            elif inp == 'x':
                home_screen()

            else:
                print('Invalid input')
    else:
        pass
    
def main():
    print('--------Welcome to the home screen---------')

    pandas_functions = input('Do you want to use pandas functions? Input "yes" or "no": ')

    # If user's input == 'yes', functions(pandas_functions) is called in main()
    if pandas_functions == 'yes':
        functions(pandas_functions)

    # If user's input == "no" (the user doesn't want to use pandas' functions):
    elif pandas_functions == 'no':
        # The program requests the following input:
        specific_values = input('Do you want to obtain specific values from the database? Input "yes" or "no": ')
        # "values(specific_values) is called in main()
        values(specific_values)

    else:
        print('Invalid input.')
        home_screen()
    

if __name__ == '__main__':
    main()