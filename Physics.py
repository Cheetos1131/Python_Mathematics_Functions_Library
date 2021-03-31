import math

def Linear_noD():
    selector = int(input("Enter 1 to solve for Vf, 2 for Vo, 3 for a, or 4 for t. "))
    if (selector == 1): 
        Vo = float(input("Enter initial velocity in terms of m/s. "))
        a = float(input("Enter acceleration in terms of m/s^2. "))
        t = int(input("Enter total time in terms of seconds. "))
        Vf = (Vo + a) * t
        print("The final velocity is " + str(Vf) + " m/s.")
    elif (selector == 2):
        Vf = float(input("Enter the final velocity in terms of m/s. "))
        a = float(input("Enter the acceleration in terms of m/s^2. "))
        t = int(input("Enter the time in terms of seconds. "))
        Vo = -Vf + a * t 
        print(Vo)
    elif (selector == 3): 
        Vf = float(input("Enter the final velocity in terms of m/s. "))
        Vo = float(input("Enter the initial velocity in terms of m/s. "))
        t = int(input("Enter time in terms of seconds. "))
        a = (Vf - Vo) / t
        print(a)
    elif (selector == 4):
        Vf = float(input("Enter the final velocity in terms of m/s. "))
        Vo = float(input("Enter the initial velocity in terms of m/s. "))
        a = float(input("Enter the acceleration in terms of m/s^2. "))
        t = (Vf - Vo) / a
        print(t)
    else: 
        print("Retry and enter one of the variables.")

def Linear_noT():
    selector = int(input("Enter 1 to solve for Vf, 2 for Vo, 3 for a, or 4 for d. ")) 
    if (selector == 1):
        Vo = float(input("Enter in the initial velocity in terms of m/s. "))
        a = float(input("Enter in the acceleration in terms of m/s^2. "))
        d = float(input("Enter in the distance in terms of m. "))
        Vf = Vo + math.sqrt(2 * a * d)
        print(Vf)
    elif (selector == 2):
        Vf = float(input("Enter in the final velocity in terms of m/s. "))
        a = float(input("Enter in the acceleration in terms of m/s^2. "))
        d = float(input("Enter in the distance in terms of m. "))
        Vo = Vf - math.sqrt(2 * a * d) 
        print(Vo)
    elif (selector == 3):
        Vf = float(input("Enter in the final velocity in terms of m/s. "))
        Vo = float(input("Enter in the initial velocity in terms of m/s. "))
        d = float(input("Enter in the distance in terms of m. "))
        a = math.sqrt((pow(Vf, 2) - pow(Vo, 2)) / (2 * d)) 
        print(a)
    elif (selector == 4):
        Vf = float(input("Enter in the final velocity in terms of m/s. "))
        Vo = float(input("Enter in the initial velocity in terms of m/s. "))
        a = float(input("Enter in the acceleration in terms of m/s^2. "))
        d = math.sqrt((pow(Vf, 2) - pow(Vo, 2)) / (2 * a)) 
        print(d)
    else: 
        print("Retry and enter one of the variables.")

def Linear_NoVf(): 
    selector = int(input("Enter 1 to solve for Vo, 2 for t, 3 for a, or 4 for d. "))
    if (selector == 1):
        d = float(input("Enter in the distance in terms of m. "))
        a = float(input("Enter in the acceleration in terms of m/s^2. "))
        t = int(input("Enter time in terms of seconds. "))
        Vo = (d - ((1 / 2) * a * pow(t, 2))) / t
        print(Vo)
    elif (selector == 2): 
        print(t)
    elif (selector == 3):
        d = float(input("Enter in the distance in terms of m. "))
        Vo = float(input("Enter in initial velocity in terms of m/s. "))
        t = int(input("Enter time in terms of seconds. "))
        a = (d - (Vo * t)) / ((1 / 2) * pow(t, 2))
        print(a)
    elif (selector == 4): 
        Vo = float(input("Enter in the initial velocity in terms of m/s. "))
        a = float(input("Enter in the acceleration in terms of m/s^2. "))
        t = int(input("Enter in the time in terms of seconds. "))
        d = (Vo * t) + ((1 / 2) * a * pow(t, 2))
        print(d)
    else: 
        print("Retry and enter one of the variables. ")

  
Linear_noT()
Linear_noD()
Linear_noVf()
