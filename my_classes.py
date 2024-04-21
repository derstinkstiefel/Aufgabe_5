import json

class Person:
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.estimate_max_hr = self.estimate_max_hr()

    def estimate_max_hr(self):
        """
        See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
        """
        if self.sex == "male":
            return int(223 - 0.9 * self.age)
        elif self.sex == "female":
            return int(226 - 1.0 * self.age)
        else:
            return None  # Handle unknown sex

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file, indent=4)


class Experiment:
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file, indent=4)

