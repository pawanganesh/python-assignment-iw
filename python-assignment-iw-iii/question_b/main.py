# Create a console application for an IT Academy with the
# following features:
# a) The academy program should have a fixed course of study.
# b) If a new student is interested in the academy program the student can
# inquiry about the course of study.
# c) Student Registration with Rs. 20000 (deposit). Students are allowed to
# pay in two installments with Rs. 10000 each.
# d) Display all the student’s information from the academy with their payments
# and remaining payments.
# e) Update the student information if needed.
# f) Delete the student information if he/she left the program.
# g) Return the deposit amount (Rs. 20000) to the students after the
# successful completion of the course and check the balance.
# Remember it should be a full feature CONSOLE APP. You can store
# the course of study and the student’s detail in your preferred file
# format (.csv, .txt, etc).
# Ignore the permissions for now. Anyone who runs the script is allowed to
# access all the features. Develop the app with OOP Approach.

import csv
import shutil
from tempfile import NamedTemporaryFile

def user_display():
    print("------------------------------------------")
    print("Welcome to IT Academy")
    print('1. Course of Study')
    print('2. New Student Registration')
    print('3. Student\'s Detail')
    print('4. Update Student Deposit')
    print('5. Delete Student Information')
    print('6. Return Amount')
    print('Press 0 key to exit')
    print("------------------------------------------")


user_display()
choice = int(input("Please enter your choice: "))

while choice != 0:
    def course_inquiry():
        with open('course_of_study.txt', 'r') as fp:
            course_detail = fp.read()
        print(course_detail)

    def new_student_registration(amount_return=False):
        print("Please provide us your following personal details:")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        contact_number = input("Enter your contact number: ")
        print("Please provide us your following educational details:")
        college_name = input("Enter your college name: ")
        faculty = input("Enter your faculty: ")
        print("Fee Details:\nStudent Registration with Rs. 20000 (deposit).\nStudents are allowed to pay in two "
              "installments with Rs. 10000 each.")
        while True:
            try:
                deposit_amount = int(input("Enter amount for registration: "))
                if deposit_amount == 10000 or deposit_amount == 20000:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("You should enter amount in number form and amount should be 10000 or 20000")

        remaining_amount = 20000 - deposit_amount

        lst = [name, email, contact_number, college_name, faculty, deposit_amount, remaining_amount, amount_return]

        with open('student_details.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            # writer.writerow(['name', 'email', 'contact_number', 'college_name', 'faculty', 'deposit_amount', 'remaining_amount', 'amount_return'])
            writer.writerow(lst)



    def student_detail():
        with open('student_details.csv', 'r') as file:
            reader = csv.reader(file)
            for col in reader:
                print(col)


    def update_deposit():
        name = input("Enter student name to deposit amount: ")
        filename = 'student_details.csv'
        temp_file = NamedTemporaryFile(delete=False, mode='w')
        total_deposit = 20000

        with open(filename, "r") as file, temp_file:
            reader = csv.DictReader(file)
            fieldnames = ['name', 'email', 'contact_number', 'college_name', 'faculty', 'deposit_amount',
                          'remaining_amount', 'amount_return']
            writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                if name is not None:
                    if str(row['name']) == str(name):
                        while True:
                            try:
                                print("Your remaining amount to deposit is Rs.", row['remaining_amount'])
                                initial_deposit_amount = int(row['deposit_amount'])
                                if int(row['remaining_amount']) == 0:
                                    print("Congratulations! You have already deposited Rs. 20000")
                                    break
                                elif initial_deposit_amount == 10000:
                                    second_installment = int(input("Enter amount to deposit: "))
                                    if second_installment == 10000:
                                        initial_deposit_amount += second_installment
                                        row['deposit_amount'] = initial_deposit_amount
                                        row['remaining_amount'] = total_deposit - initial_deposit_amount
                                        print("Your remaining amount to deposit is Rs.", row['remaining_amount'])
                                        print("Thank you for depositing full amount")
                                        break
                                    else:
                                        raise ValueError
                            except ValueError:
                                print("Please enter amount in number form and second installment should be Rs. 10000")
                        # print(row)
                writer.writerow(row)
            shutil.move(temp_file.name, filename)
            return True
        return False


    def delete_info():
        data = []
        student = input("Please enter a student's name to be deleted: ")
        with open('student_details.csv', 'r') as rfile:
            reader = csv.reader(rfile)
            for row in reader:
                data.append(row)
                for field in row:
                    if field == student:
                        data.remove(row)
                        print("You have deleted", student, "from the student's list")


        with open('student_details.csv', 'w') as wfile:
            writer = csv.writer(wfile)
            writer.writerows(data)

    def return_amount():
        name = input("Enter student name to return amount: ")

        filename = 'student_details.csv'
        temp_file = NamedTemporaryFile(delete=False, mode='w')

        with open(filename, "r") as file, temp_file:
            reader = csv.DictReader(file)
            fieldnames = ['name', 'email', 'contact_number', 'college_name', 'faculty', 'deposit_amount',
                          'remaining_amount', 'amount_return']
            writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                if name is not None:
                    if str(row['name']) == str(name):
                        while True:
                            if int(row['deposit_amount']) != 20000:
                                print(
                                    "You must complete this course and should have deposited Rs. 20000 to get amount return back")
                                break
                            else:
                                confirm = input("Have you completed the course? [y/n]: ")
                                if confirm == 'y' or confirm == 'Y':
                                    row['amount_return'] = 'True'
                                    print("Congratulations! you have successfully completed course and got you money back.")
                                    break
                                else:
                                    print("Please enter [y or Y] to confirm: ")
                writer.writerow(row)
            shutil.move(temp_file.name, filename)
            return True
        # return False

    switcher = {
        1: course_inquiry,
        2: new_student_registration,
        3: student_detail,
        4: update_deposit,
        5: delete_info,
        6: return_amount,
    }
    switcher.get(choice)()
    user_display()
    choice = int(input("Please enter your choice: "))
