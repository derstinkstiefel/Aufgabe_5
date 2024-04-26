from my_functions import build_experiment, estimate_max_hr, build_person
import json 
from my_classes import Person, Experiment

#aufrufen der Inputs
"""hier müssen die Inputs neu gemacht werden 
damit sie über die Subclassen laufen
und dann kann man die sachen auch anders erstellen"""


experiment_name = input("Enter name of the Experiment: ")
date = input("when was the experiment taken?: ")
supervisor = input("Enter the name of the Supervisor: ")
subject = input("enter subjekts name: ")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
sex = input("Enter sex (male/female): ")
age = int(input("Enter age: "))

# Erstellen der Person und des Experiments 
person = Person(first_name, last_name, age, sex)
experiment = Experiment(experiment_name, date, supervisor, subject)
# Mergen des Experiments
total_experiment = {**person.__dict__, **experiment.__dict__}
print("Person information:")
print(total_experiment)

with open('Data/Experiment_data.json', 'w') as datei:
    json.dump(total_experiment, datei, indent=4)