import os
import json
from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, sex, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.birthdate = birthdate

    def estimate_max_hr(self):
        age_years = self.calculate_age()
        if self.sex == "male":
            return int(223 - 0.9 * age_years)
        elif self.sex == "female":
            return int(226 - 1.0 * age_years)
        else:
            return None  # Handle unknown sex

    def calculate_age(self):
        today = datetime.today()
        birthdate = datetime.strptime(self.birthdate, '%Y-%m-%d')
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    def save(self, filename):
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file, indent=4)


class Subject(Person):
    def __init__(self, first_name, last_name, sex, birthdate, experiment_name):
        super().__init__(first_name, last_name, sex, birthdate)
        self.experiment_name = experiment_name


class Supervisor(Person):
    def __init__(self, first_name, last_name, sex, birthdate, department):
        super().__init__(first_name, last_name, sex, birthdate)
        self.department = department


# Beispiel für die Verwendung:
subject = Subject("John", "Doe", "male", "1990-05-15", "Experiment A")
supervisor = Supervisor("Dr.", "Smith", "female", "1980-03-10", "Biology")

print("Subject information:")
print(subject.__dict__)
print("Estimated max heart rate for subject:", subject.estimate_max_hr())

print("Supervisor information:")
print(supervisor.__dict__)
print("Estimated max heart rate for supervisor:", supervisor.estimate_max_hr())

# Daten speichern
subject.save('Data/Subject_data.json')
supervisor.save('Data/Supervisor_data.json')
