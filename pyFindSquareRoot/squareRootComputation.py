#note: this is just an algorithm test
#to calc sqrt use math or use ->  25**.5 = 5

print("Program to find the square root of a number.")
print("Enter a number that you want to know the square root of:")

#create a flag var to check if a number is entered
flag = True
icount = 0
#try except statment here, if not able to convert to float, then NaN
try:
    value = float(raw_input())
    if value > 0:
        flag = True
except:
    flag = False
    
    
#program logic here after the try..except    
if (flag == True):
    print("Finding the square root...")    
    guess = value/6 #get a better calc to find the initial guess value
    check = False  
    while (check == False):
        if (guess*guess == value):
            print("The square root is: %r" % guess)
            print("It took %r interation(s)" % icount)
            check = True
        else:
            guess = (guess + value/guess)/2
            icount += 1
                
else:
    print("A number was not entered, quiting")   

    
