class Employee:
    NoEmpCount=0  #denotes the number of Employees initializing to Zero
    def __init__(self, NamEmp, EmpFamily, EmpSalary, EmpDepartment): #constructor
        self.NamEmp = NamEmp
        self.EmpFamily = EmpFamily
        self.EmpSalary = EmpSalary
        self.EmpDepartment = EmpDepartment
        Employee.NoEmpCount += 1
    def avgsalary(self, *Empsalaries):#taking the entire salaries as single input
        tot_sal = sum(Empsalaries)
        return tot_sal / len(Empsalaries) #using average formula totalsum/totalcount


class FulltimeEmployee(Employee):#inheriting the properties of Employee Class (Parent Class) 
    pass

#Creating Instances of Three Employees and assigning values
emp1 = Employee("Karan", "Rajput", 1550, "Developer")
emp2 = Employee("Shilpa", "Kesineni", 1430, "Audit")
emp3 = Employee("Ramya", "Thakur", 1900, "Tester")
# Member Function call for Employee Class
avgsalary = emp1.avgsalary(emp1.EmpSalary, emp2.EmpSalary, emp3.EmpSalary)

print("Average salary for the Data given as per employees:", avgsalary)

# Creating instances of FulltimeEmployee class
fullemp1 = FulltimeEmployee("Siri", "Sunny", 8699, "Manager")
fullemp2 = FulltimeEmployee("Meghana", "Tinku", 4500, "Sales")

# Calling member functions of FulltimeEmployee class that is nothing but the inherited Employee Class
avgsalary = fullemp1.avgsalary(fullemp1.EmpSalary, fullemp2.EmpSalary)
print("Average salary of full-time employees:", avgsalary)
print("Total Employee Count",Employee.NoEmpCount)
