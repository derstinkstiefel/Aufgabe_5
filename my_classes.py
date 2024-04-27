import json

class Person:
    def __init__(self, first_name, last_name, age, sex ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def save(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.__dict__, f)

    def estimate_max_hr(age_years : int , sex : str) -> int:
        """
        See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
        """
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age_years
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age_years
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
    
#subklassen für die mainclass Person erstellen
class Supervisor(Person):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)

class Subject(Person):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)


class Experiment:
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def save(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.__dict__, f)


