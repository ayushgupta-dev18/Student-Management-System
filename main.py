class Student:

    def __init__(self,name,roll_no,student_class,address):
        self.name = name
        self.roll_no = roll_no
        self.student_class = student_class
        self.address = address


students = []

while True:

    print("========Student Management System=========")
    print("1. Add Student  ")
    print("2. View Student ")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student ")
    print("6. Exit")

    choice = input("Enter Your Choice : ")
    print("\n")

# add student

    if choice == "1":

        name = input("Enter Student Name => ")
        roll_no = input("Enter Roll No => ")
        student_class = int(input("Enter Student Class => "))
        address = input("Enter Student Address => ")

        found = False
        
        for student in students:
            if student.roll_no == roll_no:
                found = True
                break

        if found:
            print("❌Roll No already exists ")
        else:        
            student = Student(name,roll_no,student_class,address)
            students.append(student)
            print("✅Student Added Successfuly  ")

#view student

    elif choice == "2":

        if len(students) == 0:
            print("No Student Exists")
        else:
            for student in students:
                print("========STUDENT DETAILS=========")
                print(f"Name : {student.name}")
                print(f"Roll No : {student.roll_no}")
                print(f"Class : {student.student_class}")
                print(f"Address : {student.address}")

#  search student
    elif choice == "3":
        roll_no = input("Enter the Student Roll  No : ")
 
        for student in students:
            if student.roll_no == roll_no:
            
                print("Student Found")
                print(f"Name : {student.name}")
                print(f"Roll No : {student.roll_no}")
                print(f"Class : {student.student_class}")
                print(f"Address : {student.address}")
                break
            
        else:
            print("No Student Found")
    
#  Update Student 
    elif choice == "4":
        roll_no = input("Enter Roll No : ")

        for student in students :
            if student.roll_no == roll_no:

                student.name = input ("Enter new Name : ")
                student.student_class = input("Enter new Class : ")
                student.address = input("Enter new Address : ")
                
                print("Student Updated Successfully ")

                break
        else: 
            print("No Student Found")

# Delete student
    elif choice == "5":
        roll_no = input("Enter Roll No : ")

        for student in students:
            if student.roll_no == roll_no:

                students.remove(student)
                print("Student Deleted Successfully ")
                break

        else:
            print("No Student found")



    elif choice == "6":
        break
    
    else: 
        print("Invalid Choice ,Try again !")                