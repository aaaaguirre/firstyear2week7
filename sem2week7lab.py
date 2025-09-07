import time

staff_list = [[100, "Jones", "Jack", "01-10-2000", 5, 60000, 0],
              [200, "Smith", "Mary", "01-07-2000", 6, 70000, 0],
              [300, "Bennett", "Patrick", "01-11-2001", 6, 70000, 0],
              [400, "Lewis", "Ann", "01-12-2011", 4, 40000, 0]]

# Function Menu
def print_menu():
    print("\t*" * 50)
    print("\t*                  HR Department                 *")
    print("\t*" * 50)
    print("\t* 1) Add Employee                                *")
    print("\t* 2) Search Employees                            *")
    print("\t* 3) List Employees                              *")
    print("\t* 4) Set Bonus                                   *")
    print("\t* 5) Exit                                        *")
    print("\t*" * 50)


# Function Grade
def valid_grade(grade):
    return grade in range(1, 9)

#  Option 1: Add Employee
def add_employee():
    print("Enter details for new employee:")
    staff_id = int(input("Staff ID: "))
    first_name = input("First name: ")
    surname = input("Surname: ")
    date_of_commencement = input("Date of commencement of employment (dd-mm-yyyy-): ")
    while True:
        grade = int(input("Grade (1-8): "))
        if valid_grade(grade):
            break
        else:
            print("Invalid grade. Please enter a grade between 1 and 8.")
    salary = float(input("Salary: "))
    bonus = 0
    staff_list.append([staff_id, surname, first_name, date_of_commencement, grade, salary, bonus])

# Option 2: Search Employee
def search_emp(staff_id):
    found = False
    for employee in staff_list:
        if employee[0] == staff_id:
            found = True
            print("Employee details:")
            print("Staff ID:", employee[0])
            print("First name:", employee[2])
            print("Surname:", employee[1])
            print("Date of commencement of employment:", employee[3])
            print("Grade:", employee[4])
            print("Salary:", employee[5])
            print("Bonus:", employee[6])
            break
    if not found:
        print("Employee not found.")

# Option 3: List Employees
def emp_display():
    print("Employee List:")
    for employee in staff_list:
        print(employee)
    print("Total employees:", len(staff_list))

# Option 4: Set Bonus
def calc_bonus():
    current_year = int(time.strftime("%Y"))
    for employee in staff_list:
        start_year = int(employee[3].split("-")[2])
        years_worked = current_year - start_year
        bonus = years_worked * 0.01 * employee[5]
        employee[6] = bonus


#  Main Code
def main():
    while True:
        print_menu()
        option = input("Please enter option:")

        if option == "1":
            add_employee()
        elif option == "2":
            staff_id = int(input("Enter staff id to search:"))
            search_emp(staff_id)
        elif option == "3":
            emp_display()
        elif option == "4":
            calc_bonus()
            print("Bonus set successfully.")
        elif option == "5":
            print("Exiting the HR System.")
            break
        else:
            print("Invalid option entered. Please enter a valid option.")


if __name__ == "__main__":
    main()