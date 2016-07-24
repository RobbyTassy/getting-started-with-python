class Employee:
    # common class base for all employees
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print ("Total employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

    # this is going to create the first object of our Employee class

emp1 = Employee ('Greg', 50000)
emp2 = Employee ('Chris', 70000)
emp3 = Employee ('Rob', 100000)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp1.displayCount()
