from my_functions import build_experiment, estimate_max_hr, build_person
import json 
from my_classes import Person, Experiment, Subject, Supervisor

#aufrufen der Inputs
"""hier müssen die Inputs neu gemacht werden 
damit sie über die Subclassen laufen
und dann kann man die sachen auch anders erstellen"""


experiment_name = input("Enter name of the Experiment: ")
date = input("when was the experiment taken?: ")

supervisor_first_name = input("Enter the First Name of the Supervisor: ")
supervisor_last_name = input("Enter the last Name of the Supervisor: ")
supervisor_age = int(input("Enter subject's age: "))
supervisor_sex = input("Enter subject's sex (male/female): ")

subject_first_name = input("Enter the First Name of the Subject: ")
subject_last_name = input("Enter the last Name of the Subject: ")
subject_age = int(input("Enter subject's age: "))
subject_sex = input("Enter subject's sex (male/female): ")

# first_name = input("Enter first name of The Person : ")
# last_name = input("Enter last name of the Person: ")
# sex = input("Enter sex (male/female): ")
# age = int(input("Enter age: "))

# Erstellen der Person und des Experiments 
# person = Person(first_name, last_name, age, sex)
supervisor = Supervisor(supervisor_first_name, supervisor_last_name,supervisor_age)
subject = Subject(subject_first_name, subject_last_name, subject_age, subject_sex)
experiment = Experiment(experiment_name, date, supervisor, subject)

# Mergen des Experiments
# total_experiment = {**person.__dict__, **experiment.__dict__}
filename = 'Data/Experiment_data.json'
experiment.save(filename)
print("Person information:")
# Speichern der kombinierten Daten in eine JSON-Datei

print(experiment.__dict__)
# print(total_experiment)

# with open('Data/Experiment_data.json', 'w') as datei:
#     json.dump(total_experiment, datei, indent=4)