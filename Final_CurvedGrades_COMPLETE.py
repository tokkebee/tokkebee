#program that curves grades and allows teacher to check grades of their students
#this program assumes the teacher will input at least two students

#values
classroom={}
highestGrade=0
highestIndex=[]
avg=0
curvedGrades=[]
curveAvg=0
curveCheck=False

#functions
def menu(): #done!
    print("\nFUNCTION MENU: \n\nAVERAGE: Normal average of class's grades\nCURVE: Curved average of class's grades\nHIGHEST: Prints highest grade\nSTUDENT: Print particular student's grade\nGRADEBOOK: Prints roster and grades\nMENU: Repeat Function Menu")

def average(): #done!
    avg=sum(classroom.values())/(len(classroom))
    print("The class's uncurved average is " + str(avg) + ".")

def curve():
    for x in range(len(classroom)):
        oldGrade=list(classroom.values())[x]
        diff=100-highestGrade
        curvedGrades.append(oldGrade + diff)
    curveAvg=sum(curvedGrades)/(len(classroom))
    print("All scores were raised by " + str(diff) + " points. The average is now " + str(curveAvg) + ".")
    
def highest(): #done!
    names=list(classroom.keys())
    print("The following student(s) have the highest uncurved grade, " + str(highestGrade) + "% , in the class: ")
    for x in range(len(highestIndex)):
        print(names[highestIndex[x]])

def student(): #done!
    student=input("Which student's grade would you like to view? ").title()
    while student not in classroom:
        student=input("This student is not in the gradebook. Please try again: ").title()
    if curveCheck==True:
        print(student + "'s uncurved grade is " + str(classroom.get(student)) + "% and curved is " + str(curvedGrades[list(classroom).index(student)]) + ".")
    else:
        print(student + "'s uncurved grade is " + str(classroom.get(student)) + "%.")

def gradebook(): #done!
    names=list(classroom.keys())
    grades=list((classroom.values()))
    print("\nGRADEBOOK:")
    if curveCheck==True:
        for x in range(len(names)):
            print(names[x]+": Uncurved = " + str(grades[x]) + ", Curved = " + str(curvedGrades[x]))
    else:
        for x in range(len(names)):
            print(names[x]+": Uncurved = " + str(grades[x]))

#beginning of program
user=input("Type the student's full name and grade, separated by a comma (name, ##), or 'END' to end adding: ").lower()

#student name/grade input loop
count=0
while not user=='end':
    count+=1
    temp=user.split(', ') #to the ta, i learned splitting in high school and i only looked up the syntax.
    temp[1]=float(temp[1])
    classroom[temp[0].title()]=temp[1]
    
    #highest score, storing value and indexes
    if temp[1]>=highestGrade:
        if temp[1]>highestGrade: #clears old highscores
            #print("clear check")
            highestIndex.clear()
        highestGrade=temp[1]
        highestIndex.append(count-1)
        
        
        
    user=input("Another student?: ")
   
print("Ok, end of adding.")

#option loop
menu() #

while not user=="no":
    #menu loop
    menuOptions=["average","curve","highest","student","gradebook","menu"]
    option=input("\nType a menu choice: ").lower()
    while not option in menuOptions:
        print("Option does not exist.")
        option=input("\nType a menu choice: ").lower()

    #running the options and repeat
#     match option:
#         case "average":
#             average()
#         case "curve" and curveCheck==False:
#             curve()
#         case "curve" and curveCheck==True:
#             user=input("You already curved! Choose a different option: ")
#         case "highest":
#             highest()
#         case "student":
#             student()
#         case "gradebook":
#             gradebook()
#         case "menu":
#             menu()
            
    if option=="average":
        average()
    elif option=="curve" and curveCheck==False:
        curve()
        curveCheck=True
    elif option=="curve" and curveCheck==True:
        print("You already curved!")
    elif option=="highest":
        highest()
    elif option=="student":
        student()
    elif option=="gradebook":
        gradebook()
    elif option=="menu":
        menu()
    
    user=input("Would you like to run another option? (YES or NO): ").lower()
    while user != "yes" and user != "no":
        user=input("(YES or NO): ").lower()

print("\nThis is the end of the Curved Grades program!")