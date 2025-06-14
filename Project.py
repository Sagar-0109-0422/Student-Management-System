import json
import os

filename="project2.json"

def Insert():
    print("---------------------------------------------")
    sid=input("Enter Student ID: ")
    name=input("Enter Student Name: ")
    grades=int(input("Enter the grades in Subject: "))
    print("---------------------------------------------")
    entry={
        "ID":sid,
        "Name":name,
        "Grade":grades}
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    found=False
    for datum in data:
        if datum["ID"]==sid:
            print("Error as Same Id are inserted")
            found=True
            break
    if not found:
            # Append new entry
            data.append(entry)

            # Write updated list to file
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            print("-------------------------------------------------")
            print("Data written successfully to Project2.json!")
            print("-------------------------------------------------")
            
            
    
    
def Update():
    print("---------------------------------------------")
    print("---------------------------------------------")
    print("Enter your choice to update")
    print("1. Student ID")
    print("2. Student Name")
    print("3. Student Grades")
    print("---------------------------------------------")
    print("---------------------------------------------")
    
    ch=int(input("Enter your choice: "))
    print("---------------------------------------------")
    print("---------------------------------------------")
    if ch==1:
        name=input("Enter the name of Student")
        sid=input("Enter new Student ID")
        print("---------------------------------------------")
        print("---------------------------------------------")
        with open(filename,"r") as file:
            datam=json.load(file)
        
        for datum in datam:
            if datum["Name"]==name:
                datum["ID"]=sid
        

        # Write updated list to file
        with open(filename, "w") as file:
            json.dump(datam, file, indent=4)
        print("Updated Successfully") 
        print("---------------------------------------------")
        print("---------------------------------------------")
    elif ch==2:
        print("---------------------------------------------")
        print("---------------------------------------------")
        name=input("Enter the new name of Student")
        sid=input("Enter Student ID")
        print("---------------------------------------------")
        print("---------------------------------------------")
        with open(filename,"r") as file:
            datam=json.load(file)
        
        for datum in datam:
            if datum["ID"]==sid:
                datum["Name"]=name
        # Write updated list to file
        with open(filename, "w") as file:
            json.dump(datam, file, indent=4)
        print("Updated Successfully")
        print("---------------------------------------------")
        print("---------------------------------------------")
    elif ch==3:
        print("---------------------------------------------")
        print("---------------------------------------------")
        grade=input("Enter the new grade of Student")
        sid=input("Enter Student ID")
        print("---------------------------------------------")
        print("---------------------------------------------")
        with open(filename,"r") as file:
            datam=json.load(file)
        
        for datum in datam:
            if datum["ID"]==sid:
                datum["Grade"]=grade
                
        

        # Write updated list to file
        with open(filename, "w") as file:
            json.dump(datam, file, indent=4)
        print("Updated Successfully")
        print("---------------------------------------------")
        print("---------------------------------------------")
    else:
        print("---------------------------------------------")
        print("---------------------------------------------")
        print("Please Enter the valid Option")
        print("---------------------------------------------")
        print("---------------------------------------------")
        

def Delete():
    print("---------------------------------------------")
    print("---------------------------------------------")
    print("Enter your choice to delete record of student")
    print("1. Student ID")
    print("2. Student Name")
    print("---------------------------------------------")
    print("---------------------------------------------")
    ch=int(input("Enter your choice: "))
    print("---------------------------------------------")
    print("---------------------------------------------")
    with open(filename,"r") as file:
        datam=json.load(file)
    if ch==1:
        sid=input("Enter the Id of the student")
        print("---------------------------------------------")
        print("---------------------------------------------")
        datam = [student for student in datam if student["ID"] != sid]
        with open(filename, "w") as file:
            json.dump(datam, file, indent=4)
        print("Record Deleted Successfully")
        print("---------------------------------------------")
        print("---------------------------------------------")
    elif ch==2:
        
        name=input("Enter the Name of the student")
        print("---------------------------------------------")
        print("---------------------------------------------")
        datam = [student for student in datam if student["Name"] != name]
        with open(filename, "w") as file:
            json.dump(datam, file, indent=4)
        print("Record Deleted Successfully")
        print("---------------------------------------------")
        print("---------------------------------------------")


def Display():
    with open(filename,"r") as file:
        data=json.load(file)
    for datum in data:
        print("---------------------------------------------")
        print("---------------------------------------------")
        print("Id:",datum.get("ID"),"\t\tName: ",datum.get("Name"),"\t\tGrade:",datum.get("Grade"))
        print("---------------------------------------------")
        print("---------------------------------------------")

def Analyze():
    with open(filename,"r") as file:
        data=json.load(file)
    print("---------------------------------------------")
    print("---------------------------------------------")
    for datum in data:
        if datum["Grade"]>40:
            print("Id:",datum.get("ID"),"\t\tName: ",datum.get("Name"),"\t\tGrade:",datum.get("Grade"),"Pass")
        else:
            print("Id:",datum.get("ID"),"\t\tName: ",datum.get("Name"),"\t\tGrade:",datum.get("Grade"),"Fail")    
    print("---------------------------------------------")
    print("---------------------------------------------")       
            
def Calculate():
    with open(filename,"r") as file:
        data=json.load(file)
    n=0
    Sum=0
    for datum in data:
        Sum+=datum["Grade"]
        n+=1
    Average=Sum/n
    print("---------------------------------------------")
    print("---------------------------------------------")
    print("The average of the Students Grade is ",Average)
    print("---------------------------------------------")
    print("---------------------------------------------")


def main():
    while True:
        print("---------------------------------------------")
        print("\t\tStudent Management System")
        print("---------------------------------------------")
        print("---------------------------------------------")

        print("Enter your choice: ")
        print("1. Adding the Students Records")
        print("2. Updating the Students Records")
        print("3. Deleting the Students Records")
        print("4. Display Reports")
        print("5. Analyze Reports")
        print("6. Calculate Average")
        print("---------------------------------------------")
        print("---------------------------------------------")


        choice=int(input("Enter your clear choice from above lists: "))
        print("---------------------------------------------")
        match choice:
            case 1:
                Insert()
            case 2:
                Update()
            case 3:
                Delete()
            case 4:
                Display()
            case 5:
                Analyze()
            case 6:
                Calculate()
            case _:
                print("Error on choice")
        ch=input("Do you wat to continue: Y or N")
        if ch=="Y":
            continue
        else:
            break
        
    
main()