import os
import mymodul

myfamily=mymodul.myfamily

def func1(key,value):
    try:
        for y, x in myfamily.items():
            if myfamily[y][key]==value:
                print(myfamily[y]["fname"],myfamily[y]["lname"],myfamily[y]["phone"])
        x=input("press Enter for another search")
        os.system('clear')
    except:
        print("key or value not correct, please try again")
        

i=0

while i<10:
    
    key= input("Type in which key you would like to find or press 0 to exit: ")
    if key=="0" or key=="exit" or key=="out":
        break
    value= input("Enter a " + key + " for search: ")

    if key== "last name" or key == "family":
        key="lname"
    if key== "first name" or key == "name":
        key="fname"
    
    
    func1(key,value)
