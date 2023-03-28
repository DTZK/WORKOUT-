import math


def workout_1(ask_age):
    if ask_age <= 60:
        #compare var is fixed here since there is no calc
        compare = 1
        number_20 = 20
        number_15 = 15
        number_10 = 10
    elif 60 < ask_age <= 65:
        compare = ask_age - 60
        # _ ignores the value of that specific variable of the cal function
        number_20, _, number_15, _, number_10, _ = cal(compare, 1, 0.01)
    elif 65 < ask_age <= 75:
        compare = ask_age - 65
        number_20, _, number_15, _, number_10, _ = cal(compare, 0.95, 0.02)

    elif 75 < ask_age <= 80:
        compare = ask_age - 75
        number_20, _, number_15, _, number_10, _ = cal(compare, 0.75, 0.03)
    elif 80 < ask_age < 100:
        compare = ask_age - 80
        number_20, _, number_15, _, number_10, _ = cal(compare, 0.6, 0.04)
    else:
        compare = 1
        number_20, _, number_15, _, number_10, _ = cal(compare, 0.2, 0)

    workout = f"Gym workout for fat loss\n\
\n\
Plate thrusters ({number_15} reps x 3 sets)\n\
Mountain climbers ({number_20} reps x 3 sets)\n\
Box jumps ({number_10} reps x 3 sets)\n\
Lunges ({number_10} reps x 3 sets)\n\
Renegade rows ({number_10} reps x 3 sets)\n\
Press ups ({number_15} reps x 3 sets)\n\
Treadmill ({number_10} mins x 3 sets)\n\
Supermans ({number_10} reps x 3 sets)\n\
Crunches ({number_10} reps x 3 sets)"

    print(workout)

def workout_2(ask_age):
    if ask_age <= 60:
        compare = 1
        number_2 =2
        number_3 = 3
    elif 60 < ask_age <= 65:
        compare = ask_age - 60
        _, _, _, _, _, number_2 = cal(compare, 1, 0.01)
        number_3 = math.ceil(3*(1-(compare*0.01)))
    elif 65 < ask_age <= 75:
        compare = ask_age - 65
        _, _, _, _, _, number_2 = cal(compare, 0.95, 0.02)
        number_3 = math.ceil(3 * (0.95- 0.02*(compare)))

    elif 75 < ask_age <= 80:
        compare = ask_age - 75
        _, _, _, _, _, number_2 = cal(compare, 0.75, 0.03)
        number_3 = math.ceil(3 * (0.75- 0.03*(compare)))
    elif 80 < ask_age < 100:
        compare = ask_age - 80
        _, _, _, _, _, number_2 = cal(compare, 0.6, 0.04)
        number_3 = math.ceil(3 * (0.4- 0.04*(compare)))
    else:
        compare = 1
        _, _, _, _, _, number_2 = cal(compare, 0.2, 0)
        number_3 = math.ceil(3 * 0.2)
    workout = f"Gym workout for stretch and relax\n\
\n\
Quad stretchs ({number_2} mins x 3 sets)\n\
Hamstring stretchs ({number_2} mins x 3 sets)\n\
Chest and shoulder stretchs ({number_2} mins x 2 sets)\n\
Upper back stretchs ({number_3} mins x 2 sets)\n\
Biceps stretchs ({number_2} mins x 2 sets)\n\
Triceps stretchs ({number_2} mins x 3 sets)\n\
Hip flexors ({number_2} mins x 3 sets)\n\
Calf stretchs ({number_2} mins x 3 sets)\n\
Lower back stretchs ({number_2} mins x 3 sets)"

    print(workout)

def workout_3(ask_age):
    if ask_age <= 60:
        compare = 1
        number_20 =20
        number_15 = 15
    elif 60 < ask_age <= 65:
        compare = ask_age - 60
        number_20, _, number_15, _, _,_  = cal(compare, 1, 0.01)
    elif 65 < ask_age <= 75:
        compare = ask_age - 65
        number_20, _, number_15, _, _,_  = cal(compare, 0.95, 0.02)

    elif 75 < ask_age <= 80:
        compare = ask_age - 75
        number_20, _, number_15, _, _,_  = cal(compare, 0.75, 0.03)
    elif 80 < ask_age < 100:
        compare = ask_age - 80
        number_20, _, number_15, _, _,_  = cal(compare, 0.6, 0.04)
    else:
        compare = 1
        number_20, _, number_15, _, _,_  = cal(compare, 0.2, 0)
    workout = f"Gym workout for high-intensity exercises\n\
\n\
Jumping jacks ({number_20} reps x 4 sets)\n\
Sprints ({number_20} reps x 3 sets)\n\
Mountain climbers ({number_20} reps x 4 sets)\n\
Squat jumps ({number_20} reps x 4 sets)\n\
Lunges ({number_20} reps x 3 sets)\n\
Crunches ({number_20} reps x 3 sets)\n\
Treadmill ({number_15} mins x 2 sets)\n\
Side planks ({number_15} reps x 3 sets)\n\
Burpees ({number_15} reps x 3 sets)"

    print(workout)

def workout_4(ask_age):
    if ask_age <= 60:
        compare = 1
        number_20 =20
        number_15 = 15
        number_12 = 12
        number_10 = 10
    elif 60 < ask_age <= 65:
        compare = ask_age - 60
        number_20, _, number_15, number_12, number_10,_ = cal(compare, 1, 0.01)
    elif 65 < ask_age <= 75:
        compare = ask_age - 65
        number_20, _, number_15, number_12, number_10,_ = cal(compare, 0.95, 0.02)

    elif 75 < ask_age <= 80:
        compare = ask_age - 75
        number_20, _, number_15, number_12, number_10,_ = cal(compare, 0.75, 0.03)
    elif 80 < ask_age < 100:
        compare = ask_age - 80
        number_20, _, number_15, number_12, number_10,_ = cal(compare, 0.6, 0.04)
    else:
        compare = 1
        number_20, _, number_15, number_12, number_10,_ = cal(compare, 0.2, 0)
    workout = f"Gym workout for strong legs\n\
\n\
Back squats ({number_10} reps x 5 sets)\n\
Hip thrusts ({number_12} reps x 3 sets)\n\
Overhead presses ({number_10} reps x 5 sets)\n\
Rack pulls ({number_10}reps x 5 sets)\n\
Squats ({number_10} reps x 4 sets)\n\
Dumbbell lunges ({number_10} reps x 3 sets)\n\
Leg curls ({number_15} reps x 3 sets)\n\
Standing calf raises ({number_20} reps x 2 sets)"

    print(workout)

def workout_5(ask_age):
    if ask_age <= 60:
        compare = 1

        number_15 = 15
        number_12 = 12
        number_10 = 10
    elif 60 < ask_age <= 65:
        compare = ask_age - 60
        _, _, number_15, number_12, number_10,_ = cal(compare, 1, 0.01)
    elif 65 < ask_age <= 75:
        compare = ask_age - 65
        _, _, number_15, number_12, number_10,_ = cal(compare, 0.95, 0.02)

    elif 75 < ask_age <= 80:
        compare = ask_age - 75
        _, _, number_15, number_12, number_10,_ = cal(compare, 0.75, 0.03)
    elif 80 < ask_age < 100:
        compare = ask_age - 80
        _, _, number_15, number_12, number_10,_ = cal(compare, 0.6, 0.04)
    else:
        compare = 1
        _, _, number_15, number_12, number_10,_ = cal(compare, 0.2, 0)
    workout = f"Gym workout for strong ABS\n\
    \n\
    Cross crunchs ({number_12} reps x 3 sets)\n\
    Knee ups ({number_15} reps x 5 sets)\n\
    Hip thrusts ({number_15} reps x 3 sets)\n\
    Mountain climbers ({number_15} reps x 3 sets)\n\
    Vertical hip thrusts ({number_12} reps x 3 sets)\n\
    Bicycles ({number_15} mins x 2 sets)\n\
    Front planks ({number_15} mins x 3 sets)\n\
    Dragon flags ({number_12} reps x 4 sets)\n\
    Reverse crunches ({number_10} reps x 3 sets)"

    print(workout)

def workout_6(ask_age):
    if ask_age <= 60:
        compare = 1
        number_15 = 15
        number_12 = 12
        number_10 = 10
    elif 60 < ask_age <= 65:
        compare = ask_age - 60
        _, _, number_15, number_12, number_10,_ = cal(compare, 1, 0.01)
    elif 65 < ask_age <= 75:
        compare = ask_age - 65
        _, _, number_15, number_12, number_10,_ = cal(compare, 0.95, 0.02)

    elif 75 < ask_age <= 80:
        compare = ask_age - 75
        _, _, number_15, number_12, number_10,_ = cal(compare, 0.75, 0.03)
    elif 80 < ask_age < 100:
        compare = ask_age - 80
        _, _, number_15, number_12, number_10,_ = cal(compare, 0.6, 0.04)
    else:
        compare = 1
        _, _, number_15, number_12, number_10,_ = cal(compare, 0.2, 0)
    workout = f"Gym workout for strong shoulder and arms\n\
\n\
Bench presses ({number_10} reps x 5 sets)\n\
Triceps dips ({number_10} reps x 5 sets)\n\
Incline dumbbell presses ({number_12} reps x 3 sets)\n\
dumbbell flyes ({number_15} reps x 3 sets)\n\
Triceps extensions ({number_15} reps x 3 sets)\n\
Pull ups ({number_10} reps x 5 sets)\n\
Treadmill ({number_15} mins x 2 sets)\n\
Bent over rows ({number_10} reps x 5 sets)\n\
Chin ups ({number_10} reps x 3 sets)"

    print(workout)

def workout_m_18_lower():
    workout = f"Gym workout for a male younger than 18 years old\n\
\n\
High knees (20 reps x 3 sets)\n\
Squats (10 reps x 3 sets)\n\
Calf raises (10 reps x 3 sets)\n\
Scissor jumps (12 reps x 3 sets)\n\
Burpees (10 reps x 3 sets)\n\
Treadmill (10 mins x 2 sets)"

    print(workout)

def workout_f_18_lower():
    workout = f"Gym workout for a female younger than 18 years old\n\
\n\
Squats (10 reps x 3 sets)\n\
Crunches (10 reps x 2 sets)\n\
Jumping jacks (10 reps x 3 sets)\n\
Push ups (10 reps x 2 sets)\n\
Burpees (10 reps x 3 sets)\n\
Treadmill (10 mins x 2 sets)"

    print(workout)

def workout_m_18_upper(ask_age):
    if ask_age <= 60:
        compare = 1
        number_20 = 20
        number_18 = 18
        number_15 = 15
        number_12 = 12
        number_10 = 10
    elif 60 < ask_age <= 65:
        compare = ask_age - 60
        # _, passes the variables in the position of the function returning
        number_20, number_18, number_15, number_12, number_10, _ = cal(compare, 1, 0.01)
    elif 65 < ask_age <= 75:
        compare = ask_age - 65
        number_20, number_18, number_15, number_12, number_10, _  = cal(compare, 0.95, 0.02)

    elif 75 < ask_age <= 80:
        compare = ask_age - 75
        number_20, number_18, number_15, number_12, number_10, _  = cal(compare, 0.75, 0.03)
    elif 80 < ask_age < 100:
        compare = ask_age - 80
        number_20, number_18, number_15, number_12, number_10, _ = cal(compare, 0.6, 0.04)
    else:
        compare = 1
        number_20, number_18,number_15, number_12, number_10, _ = cal(compare, 0.2, 0)
    workout = f"Gym workout for a male at least 18 years old\n\
\n\
Standing biceps curls ({number_20} reps x 3 sets)\n\
Seated incline curls ({number_18} reps x 3 sets)\n\
Seated dumbbell presses ({number_12} reps x 3 sets)\n\
Leg presses ({number_15} reps x 3 sets)\n\
Bench presses ({number_10} reps x 4 sets)\n\
Tricep kickbacks ({number_15} reps x 3 sets)\n\
Hip thrusts ({number_12} reps x 3 sets)\n\
Seated rows ({number_10} reps x 4 sets)"

    print(workout)


def workout_f_18_upper(ask_age):
    if ask_age <= 60:
        compare = 1
        number_15 = 15
        number_12 = 12
        number_10 = 10
    elif 60 < ask_age <= 65:
        compare = ask_age - 60
        #_, passes the variables in the position of the function returning
        _, _, number_15, number_12, number_10, _ = cal(compare, 1, 0.01)
    elif 65 < ask_age <= 75:
        compare = ask_age - 65
        _, _, number_15, number_12, number_10, _  = cal(compare, 0.95, 0.02)

    elif 75 < ask_age <= 80:
        compare = ask_age - 75
        _, _, number_15, number_12, number_10, _  = cal(compare, 0.75, 0.03)
    elif 80 < ask_age < 100:
        compare = ask_age - 80
        _, _, number_15, number_12, number_10, _ = cal(compare, 0.6, 0.04)
    else:
        compare = 1
        _, _,number_15, number_12, number_10, _ = cal(compare, 0.2, 0)
        
    workout = f"Gym workout for a female at least 18 years old\n\
\n\
Lateral raises ({number_15} reps x 3 sets)\n\
Reverse flyes ({number_12} reps x 3 sets)\n\
Hip thrusts ({number_12} reps x 3 sets)\n\
Incline dumbbell presses ({number_15} reps x 3 sets)\n\
Squats ({number_10} reps x 4 sets)\n\
Dumbbell lunges ({number_10} reps x 3 sets)\n\
Leg presses ({number_12} reps x 3 sets)\n\
Dumbbell presses ({number_10} reps x 4 sets)"

    print(workout)

def cal(compare, percentage, decrease_rate):
    number_20 = math.ceil(20* (percentage - decrease_rate*compare))
    number_18 = math.ceil(18* (percentage - decrease_rate*compare))
    number_15 = math.ceil(15 * (percentage - decrease_rate*compare))
    number_12 = math.ceil(12 * (percentage - decrease_rate*compare))
    number_10 = math.ceil(10 * (percentage - decrease_rate*compare))
    number_2 = math.ceil(2* (percentage - decrease_rate*compare))
    return number_20, number_18, number_15, number_12, number_10, number_2


#This function checks the age
def get_age():
    # Ensures the user's age is between 0 and 110
    while True:
        ask_age = input("\nPlease enter your age: ").strip()
        if ask_age.isnumeric() and (0 <= int(ask_age) <= 110):
                return int(ask_age)
        else:
            print("Error: The age is a number between 0 to 110")

#This function checks the name
def get_name():
    x = True
    name = input("Please enter your name: ")
    while x == True:
        counter = 0
        while name == "":
            print("Error: Only accept alphabetical characters and spaces for name\n")
            name = input("Please enter your name: ")
    
        while name.isspace():
            print("Error: Only accept alphabetical characters and spaces for name\n")
            name = input("Please enter your name: ")

        while counter < len(name):            
            if name[counter].isalpha() or name[counter].isspace():
                counter += 1
                if counter == len(name) and counter != 0:
                    x = False
                    return(name)
            # ensures the variable name only has letters and spaces in it
            else:
                print("Error: Only accept alphabetical characters and spaces for name\n")
                name = input("Please enter your name: ")
                break


def name_exist(name):
    while name == "":
        print("Error: Only accept alphabetical characters and spaces for name\n")
        name = input("Please enter your name: ")

#This function checks the gender
def get_gender():
    # Ensures that the variable ask_gender either has string "female" or "male"
    while True:
        ask_gender = input("\nPlease enter your biological sex (female/male): ")
        if ask_gender == "female" or ask_gender == "male":
            return ask_gender
        else:
            print("Error: Please enter valid input")

#This function is about setting the user's exercise aim
def get_exercise_goals():
    while True:
        print("\nWhat do you want to get out of your training? \n\
    1. Your goal is losing weight\n\
    2. Your goal is to staying calm and relax\n\
    3. Your goal is increasing your heart rate\n\
    4. Your goal is having stronger legs\n\
    5. Your goal is having stronger ABS\n\
    6. Your goal is having stronger shoulders and arms")
        aim = input("Choose a number between 1 to 6: ")
        if 1 <= int(aim) <= 6:
            return int(aim)
        else:
            print("Error - It can only be a number between 1 to 6")
            

def get_training_days(): 
    while True:
        training_days = input("\nHow many days per week you can train: ")
        while True:
                if 1 <= int(training_days) <= 7:
                        return int(training_days)
                else:
                        print("Error: It can only be a number between 1 to 7\n")
                        training_days = input("How many days per week you can train: ")

def female_workout(ask_age):
    # to separate the age between under 18 and 18 and over
    if ask_age < 18:
        workout_f_18_lower()

    else:
        workout_f_18_upper(ask_age)

def male_workout(ask_age):
    if ask_age < 18:
        workout_m_18_lower()
    else:
        workout_m_18_upper(ask_age)

if __name__ == "__main__":
    name = get_name()
    ask_age = get_age()
    ask_gender = get_gender()
    exercise_goals = get_exercise_goals()
    training_days = get_training_days()
    # day_counter is 1 since it starts on the first Day
    day_counter = 1
    print(f"\nHello {name}! Here is your training:\n\
-------------------------------------------------------------------------------------")
    while day_counter <= training_days:
       print(f"Day {day_counter}")
       if day_counter % 2 == 0:
            # to differentiate for each gender
            if ask_gender == "female":
                female_workout(ask_age)
            else:
                male_workout(ask_age)
       else:
            # for each target, it will output a different menu 
            if exercise_goals == 1:
                workout_1(ask_age)
            elif exercise_goals == 2:
                workout_2(ask_age)
            elif exercise_goals == 3:
                workout_3(ask_age)
            elif exercise_goals == 4:
                workout_4(ask_age)
            elif exercise_goals == 5:
                workout_5(ask_age)
            else:
                workout_6(ask_age)
       print("-------------------------------------------------------------------------------------")
       day_counter += 1
    print(f"\nBye {name}.")