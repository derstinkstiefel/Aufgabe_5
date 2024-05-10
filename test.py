from my_classes import Person, Experiment

# Test data
test_person = Person("John", "Doe", "male", 30)
test_experiment = Experiment("Test Experiment", "2024-04-21", "Dr. Smith", "Test Subject")

# Save test data
test_person.save('Data/Test_Person_data.json')
test_experiment.save('Data/Test_Experiment_data.json')

print("Test Person information:")
print(test_person.__dict__)
print("Test Experiment information:")
print(test_experiment.__dict__)