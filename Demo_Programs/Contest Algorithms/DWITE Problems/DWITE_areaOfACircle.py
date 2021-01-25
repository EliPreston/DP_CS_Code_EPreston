import math


def findArea(x1, x2, y1, y2):

    # Contest Stategy 1 - just set variable values and take inputs after
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    #r = ((y2 - y1)**(2) + (x2 - x1)**(2))**(1/2)

    # sqrt is a static/class function contained in the math module.
    # static function does not require an implied object.
    # word = "Emanuel"
    # word.upper() #word is the implied object meaning upper is an instance or non-static method
    # math.sqrt(7) #math is a modeule containing a bunch of function - no implied object is needed for sqrt
    # 			 #to run.  Therefore we invoke the method with the name of the modele (or nothing). The
    # 			 #method runs purley on the parameters that are passed

    r = math.sqrt((y2 - y1)**(2) + (x2 - x1)**(2))
    a = 3.14159*r*r
    a = round(a, 3)

    print(a)


# Contest Strategy 2 - Write the problem as a function


x1 = input()
x2 = input()
y1 = input()
y2 = input()

findArea(x1, x2, y1, y2)
