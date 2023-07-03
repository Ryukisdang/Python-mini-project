#building a simple calculator taking user input and printing output
# head are global variable or description
def Calculator_Start():
    Start = str(input("Press enter to start the calculator..........plsss"))
    if Start=="start":
        print("                THIS calculator sucks            ")
        print("Timer begin on")
        print()
        print("6")
        print("5")
        print("4")
        print("3")
        print("2")
        print("1")
        print("0")
        print("Your Calculator Started")
        return Calculator()
    
#body



def Add():# function to add two number
    add1 = float(input("enter number a number...*_*...pls: "))
    add2 = float(input("enter number a number...*_*...pls: "))
    adding = add1+add2
    return adding
def Subtract():# function to subtract two number
    sub1 =  float(input("enter number a number...*_*...pls: "))
    sub2 =  float(input("enter number a number...*_*...pls: "))
    subtracting = sub1 - sub2
    return subtracting
def Comparison():#function to compare two digit
    x = float(input("enter number a number...*_*...pls: "))
    y = float(input("enter number a number...*_*...pls: "))
    if x > y:
        print(f'Your x digit {x} is greater than y digit {y}')
    elif x <y:
        print(f'Your x digit {x} is less than y digit {y}')
    elif x==y:
        print(f'Your x digit {x} is equal to  y digit {y}')
def Divide():
    method = str(input("Enter a divide method to get remainder or qoutient: "))
    div1 =  float(input("enter number a number...*_*...pls: "))
    div2 =  float(input("enter number a number...*_*...pls: "))
    if method == "remainder":
        dividing1 = div1//div2
        return dividing1
    elif method =="qoutient":
        dividing2 = div1%div2
        return dividing2
def Square_Root():
    sqrt1 = float(input("enter number a number...*_*...pls: "))
    sqrt = sqrt1**2
    return sqrt
def Product():
    pro1 = float(input("enter number a number...*_*...pls: "))
    pro2 = float(input("enter number a number...*_*...pls: "))
    multiplied = pro1*pro2
    return multiplied
def Percentage():
    Per1 = float(input("Enter a number you want to find % of : "))
    Per2 = float(input("Enter how many percentage you want to see of it: "))
    per1 = Per1/100
    per2 = per1*Per2
    percent = per2
    return percent
def Cubic():
    cube = int(input("Enter a number you wanna find cubic value: "))
    cubing = cube**3
    return cubing

            

#END-------of my user defined function------ just a curious person trying to write it own code playing around with functions and trying to link it 
# Hope you like my simple program as it is not complex one yet with more functionality and user interface and user friendly

        

#foot
def Calculator():
    #divided,subtracted,product,sqaure_root,cubic):
 
    #call out this function why typing add or subtract
    #assign variable for checking
    added = "add"
    subtracted = "subtract"
    compared = "comparison"
    divided = "divide"
    Sqrted = "sqaure root"
    producted = "product"
    percented = "percentage"
    cubed = "cubic"
    
    
    
    
    
    user_input = input("Enter WHAT Operation you wanna do in calculator Choose, add, divide, subtract, product, sqaure root, cubic, comparison, percentage: ")
    if user_input == added:
        add = Add()
        return add
    
    elif user_input == subtracted:
        sub = Subtract()
        return sub
    
    elif user_input == compared:
        compare = Comparison()
        return compare
    
    elif user_input == divided:
        Divided = Divide()
        return Divided
    
    elif user_input == Sqrted:
        SQRT = Square_Root()
        return SQRT
    
    elif user_input == producted:
        Producted =  Product()
        return Producted
    
    elif user_input == percented:
        Percented = Percentage()
        return Percentage
    
    elif user_input == cubed:
        Cubed =  Cubic()
        return Cubed
        
        
        


 
    #product = multiply
    #percentage
    #cubic = cube|
#Calculator()
Calculator_Start()
    