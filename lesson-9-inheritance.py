# inheritance
# error handling
# dates

class Employee:
    def __init__(self, name, id_number, date_of_birth, gender):
        self.name = name
        self.id_number = id_number
        self.date_of_birth = date_of_birth
        self.gender = gender

    def print_details(self):
        print(f"Name: {self.name} \nID: {self.id_number} \nDate_of_birth: {self.date_of_birth} \nGender: {self.gender}")


class PermanentEmployee(Employee):  # this is inheritance
    def __init__(self, name, id_number, date_of_birth, gender, salary, job_number):
        # self.name = name
        # self.id_number = id_number
        # self.date_of_birth = date_of_birth
        # self.gender = gender
        super().__init__(name, id_number, date_of_birth, gender)  # instead of re-writing the first class, you can use this
        self.salary = salary
        self.job_number = job_number  # added details
    def print_salary(self):
        print(f"Salary is Ksh {self.salary}")

    def print_job_number(self):
        print(f"Job number: {self.job_number}")


class TemporaryEmployee(Employee):
    def __init__(self, name, id_number, date_of_birth, gender, hourly_pay, temp_job_number, begin_date, end_date):
        super().__init__(name, id_number, date_of_birth, gender)
        self.hourly_pay = hourly_pay
        self.temp_job_number = temp_job_number
        self.begin_date = begin_date
        self.end_date = end_date

    def print_hourly_pay(self):
        print(f"Hourly pay: Ksh{self.hourly_pay}")

    def print_temp_job_number(self):
        print(f"Temp job number: {self.temp_job_number}")

    def print_begin_date(self):
        print(f"Begin date: {self.end_date}")

    def print_end_date(self):
        print(f"End date: {self.end_date}")




permanent1 = PermanentEmployee("Jerry Maina", 3976635, "1997-02-25", "M", "663,770", "345-764-897")

permanent1.print_details()
permanent1.print_salary()

temporary1 = TemporaryEmployee("Jackie Mwaniki", 3678298, "1990-06-07", "Female", "1,500", "tem-564-564", "2024-09-10", "2024-11-10")

temporary1.print_details()
temporary1.print_hourly_pay()
# temporary1.temp_job_number()
temporary1.print_begin_date()
temporary1.print_end_date()

