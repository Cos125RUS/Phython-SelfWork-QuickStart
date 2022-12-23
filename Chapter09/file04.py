class ProgStaff:
    companyName = 'ProgrammingLab'

    def __init__(self, pSalary):
        self.salary = pSalary
    
    def printInfo(self):
        print("Company name is", ProgStaff.companyName)
        print("Salary is", self.salary)

peter = ProgStaff(2500)
john = ProgStaff(2500)

print(peter.companyName)
print(john.companyName)
ProgStaff.companyName = 'ProgrammingSchool'
print(peter.companyName)
print(john.companyName)

print(peter.salary)
peter.salary = 2700
print(peter.salary)
print(john.salary)

peter.printInfo()
john.printInfo()
ProgStaff.printInfo(peter)
ProgStaff.printInfo(john)
