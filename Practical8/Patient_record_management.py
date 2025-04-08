"""
pseudocode:
defsequence name, age, last_admission_date, and medical_history
    define a constructor to initialize the attributes
    define a method to print the patient's information
"""

# Patient record management system
class Patients ():
    #include name, age, the last admission date, and the str to describe the patient's medical history
    def __init__(self, name, age, last_admission_date, medical_history):
        self.name = name
        self.age = age
        self.last_visit_date = last_admission_date
        self.history = medical_history
        self.patients = []
        # append the patient to the list
        self.patients.append(self)


    # add a method to print the patient's information
    def print_patients(self):
        #print the patient's information

        print(f"Name: {self.name}, Age: {self.age}, Last Admission Date: {self.last_visit_date}, Medical History: {self.history}")
        
    

# example
patient1 = Patients("John Doe", 30, "2025-04-08", "No known allergies")
patient2 = Patients("Jane Smith", 25, "2025-04-09", "Allergic to penicillin")
patient3 = Patients("Tom", 40, "2025-04-10", "No known allergies")
patient1.print_patients()
patient2.print_patients()

