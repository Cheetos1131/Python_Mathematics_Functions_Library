import math

def Linear_noD(): # This is the Linear Equation without Distance as a variable
    selector = int(input("Enter 1 to solve for Vf, 2 for Vo, 3 for a, or 4 for t. ")) # This asks the user for what variable they are missing and selects an equation based on this input
    if (selector == 1): # Equation to solve final velocity
        Vo = float(input("Enter initial velocity in terms of m/s. "))
        a = float(input("Enter acceleration in terms of m/s^2. "))
        t = int(input("Enter total time in terms of seconds. "))
        Vf = (Vo + a) * t
        print("The final velocity is " + str(Vf) + " m/s. ")
    elif (selector == 2): # Equation to solve initial velocity
        Vf = float(input("Enter the final velocity in terms of m/s. "))
        a = float(input("Enter the acceleration in terms of m/s^2. "))
        t = int(input("Enter the time in terms of seconds. "))
        Vo = -Vf + a * t 
        print("The initial velocity is " + str(Vo) + " m/s. ")
    elif (selector == 3): # Equation to solve acceleration
        Vf = float(input("Enter the final velocity in terms of m/s. "))
        Vo = float(input("Enter the initial velocity in terms of m/s. "))
        t = int(input("Enter time in terms of seconds. "))
        a = (Vf - Vo) / t
        print("The acceleration is " + str(a) + " m/s^2. ")
    elif (selector == 4): # Equation to solve time
        Vf = float(input("Enter the final velocity in terms of m/s. "))
        Vo = float(input("Enter the initial velocity in terms of m/s. "))
        a = float(input("Enter the acceleration in terms of m/s^2. "))
        t = (Vf - Vo) / a
        print("The time elapsed was " + str(t) + " seconds. ")
    else: # In case the user input something that was not in the program
        print("Retry and enter one of the variables.")

def Linear_noT(): # This is the Linear Equation without Time as a variable
    selector = int(input("Enter 1 to solve for Vf, 2 for Vo, 3 for a, or 4 for d. ")) # This asks the user for what variable they are missing and selects an equation based on this input
    if (selector == 1): # Equation to solve final velocity
        Vo = float(input("Enter in the initial velocity in terms of m/s. "))
        a = float(input("Enter in the acceleration in terms of m/s^2. "))
        d = float(input("Enter in the distance in terms of m. "))
        Vf = Vo + math.sqrt(2 * a * d)
        print("The final velocity is " + str(Vf) + " m/s. ")
    elif (selector == 2): # Equation to solve initial velocity
        Vf = float(input("Enter in the final velocity in terms of m/s. "))
        a = float(input("Enter in the acceleration in terms of m/s^2. "))
        d = float(input("Enter in the distance in terms of m. "))
        Vo = Vf - math.sqrt(2 * a * d) 
        print("The initial velocity is " + str(Vo) + " m/s. ")
    elif (selector == 3): # Equation to solve acceleration
        Vf = float(input("Enter in the final velocity in terms of m/s. "))
        Vo = float(input("Enter in the initial velocity in terms of m/s. "))
        d = float(input("Enter in the distance in terms of m. "))
        a = math.sqrt((pow(Vf, 2) - pow(Vo, 2)) / (2 * d)) 
        print("The acceleration is " + str(a) + " m/s^2. ")
    elif (selector == 4): # Equation to solve distance
        Vf = float(input("Enter in the final velocity in terms of m/s. "))
        Vo = float(input("Enter in the initial velocity in terms of m/s. "))
        a = float(input("Enter in the acceleration in terms of m/s^2. "))
        d = math.sqrt((pow(Vf, 2) - pow(Vo, 2)) / (2 * a)) 
        print("The distance travelled is " + str(d) + " meters. ")
    else: # In case the user input something that was not in the program
        print("Retry and enter one of the variables.")

def Linear_noVf(): # This is the Linear Equation without Final Velocity as a variable
    selector = int(input("Enter 1 to solve for Vo, 2 for t, 3 for a, or 4 for d. ")) # This asks the user for what variable they are missing and selects an equation based on this input
    if (selector == 1): # Equation to solve initial velocity
        d = float(input("Enter in the distance in terms of m. "))
        a = float(input("Enter in the acceleration in terms of m/s^2. "))
        t = int(input("Enter time in terms of seconds. "))
        Vo = (d - ((1 / 2) * a * pow(t, 2))) / t
        print("The initial velocity is " + str(Vo) + " m/s. ")
    elif (selector == 2): # Equation to solve time
        d = float(input("Enter in the distance in terms of m. "))
        Vo = float(input("Enter in the initial velocity in terms of m/s. "))
        a = float(input("Enter in the acceleration in terms of m/s^2. "))
        t = (2*(d - Vo)) / a
        print("The time elapsed was " + str(t) + " seconds. ")
    elif (selector == 3): # Equation to solve acceleration
        d = float(input("Enter in the distance in terms of m. "))
        Vo = float(input("Enter in initial velocity in terms of m/s. "))
        t = int(input("Enter time in terms of seconds. "))
        a = (d - (Vo * t)) / ((1 / 2) * pow(t, 2))
        print("The acceleration is " + str(a) + " m/s^2. ")
    elif (selector == 4): # Equation to solve distance
        Vo = float(input("Enter in the initial velocity in terms of m/s. "))
        a = float(input("Enter in the acceleration in terms of m/s^2. "))
        t = int(input("Enter in the time in terms of seconds. "))
        d = (Vo * t) + ((1 / 2) * a * pow(t, 2))
        print("The distance travelled is " + str(d) + " meters. ")
    else: # In case the user input something that was not in the program
        print("Retry and enter one of the variables. ")
        
def Linear_noA(): # This is the Linear Equation without Acceleration as a variable
    selector = int(input("Enter 1 to solve for d, 2 for Vo, 3 for Vf, or 4 for t. ")) # This asks the user for what variable they are missing and selects an equation based on this input
    if (selector == 1): # Equation to solve distance
        Vo = float(input("Enter in the initial velocity in terms of m/s. "))
        Vf = float(input("Enter in the final velocity in terms of m/s. "))
        t = float(input("Enter in the time in terms of seconds. "))
        d = ((1 / 2) * (Vo + Vf)) * t
        print("The distance travelled is " + str(d) + " meters. ")
    elif (selector == 2): # Equation to solve initial velocity
        d = float(input("Enter in the distance in terms of m. "))
        t = float(input("Enter in the time in terms of seconds. "))
        Vf = float(input("Enter in the final velocity in terms of m/s. "))
        Vo = (2 * (d / t)) - Vf
        print("The initial velocity is " + str(Vo) + " m/s. ")
    elif (selector == 3): # Equation to solve final velocity
        d = float(input("Enter in the distance in terms of m. "))
        t = float(input("Enter in the time in terms of seconds. "))
        Vo = float(input("Enter in the initial velocity in terms of m/s. "))
        Vf = (2 * (d / t)) - Vo
        print("The final velocity is " + str(Vf) + " m/s. ")
    elif (selector == 4): # Equation to solve time
        d = float(input("Enter in the distance in terms of m. "))
        Vo = float(input("Enter in the initial velocity in terms of m/s. "))
        Vf = float(input("Enter in the final velocity in terms of m/s. "))
        t = ((2 * d) / (Vo + Vf))
        print("The time elapsed was " + str(t) + " seconds. ") 
    else: # In case the user input something that was not in the program
        print("Retry and enter one of the variables. ")

eqSelect = int(input("Enter in a 1 for and equation without distance, 2 for without time, 3 for no final velocity, or 4 for no acceleration. ")) # Equation selector based on user input
if (eqSelect == 1): 
    Linear_noD()
elif (eqSelect == 2): 
    Linear_noT()
elif (eqSelect == 3): 
    Linear_noVf()
elif (eqSelect == 4): 
    Linear_noA()
else: # In case the user input something that was not in the program
    print("Retry and enter a number from 1 to 4. ") 