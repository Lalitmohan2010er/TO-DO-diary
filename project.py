import time
import os
print("         please make your TO DO LIST.....       ")
print("                                                 to save your list type SAVE")
data={}
while True :
    xyz=input(":- ")
    data[len(data)+1]=xyz
    if(xyz=="save"or xyz=="SAVE"):
        print("file saved")
        time.sleep(5)
        os.system("cls")
        
        break   
print("your total to do is :--->",len(data)-1)
print("-"*20)
print(" ")
print("to see your to do list plaese type yes")

while True:
    showinglist=input("type here:- " )
    if showinglist=="yes":
        print("thanks,your to do list is here ")
        print("_"*20)
        print(data.items())
        print(" ")
        print("thanks for using")
        break
    else:
        print("please, check your words or spelling")

