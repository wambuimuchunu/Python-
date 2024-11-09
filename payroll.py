
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id  
        self.name = name      

    
    def calculate_payroll(self):
        raise NotImplementedError("Subclasses must implement this method")



class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name)  
        self.weekly_salary = weekly_salary  

    
    def calculate_payroll(self):
        return self.weekly_salary



class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)  
        self.hours_worked = hours_worked  
        self.hourly_rate = hourly_rate    

    
    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate



class CommissionEmployee(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary, commission):
        super().__init__(emp_id, name, weekly_salary)  
        self.commission = commission  

    
    def calculate_payroll(self):
        return self.weekly_salary + self.commission


# Example usage:
if __name__ == "__main__":
   
    salary_employee = SalaryEmployee(emp_id=1, name="Mary Magdaline", weekly_salary=1000)
    hourly_employee = HourlyEmployee(emp_id=2, name="Judus iscariote", hours_worked=40, hourly_rate=15)
    commission_employee = CommissionEmployee(emp_id=3, name="Simon Peter", weekly_salary=800, commission=200)

    
    employees = [salary_employee, hourly_employee, commission_employee]
    for employee in employees:
        print(f"Payroll for {employee.name} (ID: {employee.emp_id}): ksh{employee.calculate_payroll()}")
