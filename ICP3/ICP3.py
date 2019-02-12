class Employee(object):
    num_employees = 0
    total_salary = 0

    def __init__(self, n, f, s, d):
        self.name = n
        self.family = f
        self.salary = s
        self.department = d
        Employee.num_employees = Employee.num_employees + 1
        Employee.total_salary = Employee.total_salary + s

    def getNumEmployees(self):
        return self.num_employees

    def getEmployee(self):
        print("Name: ", self.name, " Family: ", self.family, " Salary: ", self.salary, " Department: ", self.department)

    def averageSalary(self):
        if(Employee.num_employees>0):
            average_salary = Employee.total_salary/Employee.num_employees
            return average_salary

class Fulltime_Employee(Employee):
    def __init__(self, n, f, s, d, ft):
        Employee.__init__(self, n, f, s, d)
        self.ft = ft

    def getEmployee(self):
        print("Is Full Time: ")
        Employee.getEmployee(self)


employee1 = Employee("bob", "none", 10, "Science")
employee2 = Employee("francis", "wife and 2 kids", 20, "Math")
employee3 = Fulltime_Employee("maggie", "1 kid", 15, "Research", True)

print("Total Employees: ", employee1.getNumEmployees())

employee1.getEmployee()
employee2.getEmployee()
employee3.getEmployee()

print("\nAverage Salary: $", employee1.averageSalary())

