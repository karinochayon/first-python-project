employees_txt = open('Employees.txt', 'a')
read_employees = open("Employees.txt", "r+")
attendance_log_file = open("attendance.txt", 'a')
read_attendance = open("attendance.txt", 'r+')
import datetime


class Employee:

    def __init__(self):
        choice = int(input("welcome!\n if you want to add employees manually please press 1. \n if you want to add employess from file please press 2. \n if you want to delete employees manually please press 3. \n if you want to delete employess from file please press 4. \n if you want to mark attendance please press 5. \n if you want to generate attendance report please press 6. \n if you want to print a report for current month for all employees please press 7. \n if you want to print an attendance report for all employees who where late (after 09:30 AM) please press 8. \n your answer: "))

        if choice == 1:
            self.add_manually()
        elif choice == 2:
            self.add_from_file()
        elif choice == 3:
            self.delete_manually()
        elif choice == 4:
            self.delete_from_file()
        elif choice == 5:
            self.mark_attendance()
        elif choice == 6:
            self.generate_attendance_report()
        elif choice == 7:
            self.report_all_employees()
        elif choice == 8:
            self.report_late()
        else:
            print("Eroor! Please enter a valid number")


    def add_manually(self):

        while True:
            employee_id = input("Add an id number: ")

            for item in read_employees.readlines():
                item = item.split()
                if item[0] == employee_id:
                    print("Already exist in data base. Try again.")
                    self.add_manually()

            if employee_id.isdigit() == False or len(employee_id) != 9:
                print("Id is not valid. please try again.")
            else:
                break

        while True:
            employee_name = input("Add a name: ")
            if employee_name.isalpha() == False:
                print("invalid name")
            else:
                break

        while True:
            employee_phone = input("Add a phone number: ")
            if len(employee_phone) != 10 or employee_phone.isdigit == False:
                print("invalid Phone number")
            else:
                break

        while True:
            employee_age = input("Add an Age: ")
            if int(employee_age) > 120 or employee_age.isdigit() == False:
                print("invalid age")
            else:
                break

        employees_txt.write(str(employee_id)+" "+employee_name+" "+employee_phone+" "+employee_age+"\n")


    def add_from_file(self):

        path = input("please enter a file path: ")
        user_file = open(path, "r")

        list_of_existing = []
        list_from_read_employee = list(x.split() for x in read_employees.readlines())

        for index,line in enumerate(user_file.readlines()):
            line = line.split()
            count = 0

            for i in line:

                if i.isdigit() == True and len(i) == 9:
                    count = count + 1
                    id = i


                if i.isalpha() == True:
                    count = count + 1
                    name = i

                if len(i) == 10 and i.isdigit() == True and i[0:2] == "05":
                    count = count + 1
                    phone = i

                if len(i) <= 3 and i.isdigit() == True:
                    count = count + 1
                    age = i
            if id in list_of_existing:
                count = "duplicate"
            else:
                list_of_existing.append(id)

            for line in list_from_read_employee:
                if line != []:
                    if line[0] == id:
                        count = "duplicate"


            if count == 4:
                employees_txt.write("{} {} {} {} \n".format(id, name, phone, age))

            else:
                print("Eroor! in line {} one or more data is not supplied/invalid/already exist".format(index+1))

    def delete_manually(self):

        user_input_delete = input("Please enter the id number of the employee you want to delete: ").strip()
        if user_input_delete.isdigit() == True and len(user_input_delete) == 9:

            a_list = []

            for line in read_employees.readlines():
                a_list.append(line.split())

            for item in a_list:
                if user_input_delete in item:
                    a_list.remove(item)

            read_employees.truncate(0)


            for item in a_list:
                item = " ".join(item)
                read_employees.write("\n" + item.strip() + "\n")


        else:
            print("Eroor! invalid id, Try again")
            self.delete_manually()



    def delete_from_file(self, not_exist=None):

        path_to_delete = input("please enter a file path which contains date of employees to delete: ")
        user_file = open(path_to_delete, "r")

        for index, line in enumerate(user_file.readlines()):
            line = line.split()
            count = 0

            for i in line:

                if i.isdigit() == True and len(i) == 9:
                    count = count + 1
                    id = i

                if i.isalpha() == True:
                    count = count + 1

                if len(i) == 10 and i.isdigit() == True and i[0:2] == "05":
                    count = count + 1

                if len(i) <= 3 and i.isdigit() == True:
                    count = count + 1

            list_from_user_file = list(x.split() for x in user_file.readlines())
            for item in list_from_user_file:
                if item != []:
                    if item[0] == id:
                        not_exist == False

            if count == 4 and not_exist != False:

                a_list = []
                for line in read_employees.readlines():
                    a_list.append(line.split())

                for item in a_list:
                    if id in item:
                        a_list.remove(item)

                read_employees.truncate(0)

                for item in a_list:
                    item = " ".join(item)
                    read_employees.write("\n" + item.strip() + "\n")
            else:
                print("in line {} one or more data is invalid / not supplied / already exist".format(index+1))

    def mark_attendance(self):
        employee_enter_id = input("Please enter your id number to mark attendance: ")

        if employee_enter_id.isdigit() == True and len(employee_enter_id) == 9:
            count = 0
            for line in read_employees.readlines():
                if employee_enter_id in line:
                    count = count + 1

            if count == 1:
                attendance_log_file.write(employee_enter_id + "- mark attendance - " + str(datetime.datetime.now()) + "\n")
            else:
                print("Eroor! the id number you enter is not on the employee file")

        else:
            print("Eroor! the id number you enter is not valid")

    def generate_attendance_report(self):
        employee_to_generate = input("Please enter the id number of the employee you want to generate his attendance report: ")

        if employee_to_generate.isdigit() == True and len(employee_to_generate) == 9:
            print("for {} - this is all the entries of his attendance: \n".format(employee_to_generate))
            count = 0

            for line in read_employees.readlines():
                if employee_to_generate in line:
                    count = count + 1

            if count == 1:
                for line in read_attendance.readlines():
                    if employee_to_generate in line:
                        print(line)
            else:
                print("Eroor! the id number you enter is not on the employee file")

        else:
            print("Eroor! the id number you enter is not valid")

    def report_all_employees(self):
        count = 0
        x = datetime.datetime.now()
        month = x.strftime("%m")

        for line in read_attendance.readlines():
            x = line.split()[4]
            if month in x[5:7]:
                count = count + 1
                print(line)
            else:
                pass

        if count == 0:
            print("No attendance report for active employee in this current month")

    def report_late(self):
        count = 0
        for line in read_attendance.readlines():
            x = line.split()[5]
            if x.split() > ['09:30:00.000000']:
                count = count + 1
                print(line)
            else:
                pass

        if count == 0:
            print("No employees were late this month.")


run = Employee()
employees_txt.close()
read_employees.close()
attendance_log_file.close()