class Patient:

    # constructor

    def __init__(self,name, diesease, medical_history):
        self.name = name
        self._disease = diesease
        self.__age = 0
        self.__medical_history = medical_history
        hospital_name = "City Hospital"
        
   

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative.")
        else:
            self.__age = value

    def get_record(self):
        print(f"Patient Name: {self.name}")
        print(f"Disease: {self._disease}")
        print(f"Age: {self.__age}")
        print(f"Medical History: {self.__medical_history}")

    def update_record(self, new_disease, new_medical_history):
        self._disease = new_disease
        self.__medical_history = new_medical_history
        print("Patient record updated successfully.")

    def patient_info(self):
        print(f"Patient Name: {self.name}")
        print(f"Disease: {self._disease}")
        print(f"Age: {self.__age}")
        print(f"Medical History: {self.__medical_history}")

    @classmethod
    def change_hospital_name(cls, new_name):
        cls.hospital_name = new_name
        print(f"Hospital name changed to: {cls.hospital_name}")

    @staticmethod
    def call_emergency():
        print("Calling  112emergency services...")

patient1 = Patient("tanzeel","flu", "no prior medical history")
patient1.age = 30
patient1.get_record()   
patient1.update_record("cold", "allergic to penicillin")
patient1.patient_info()
Patient.change_hospital_name("General Hospital")
Patient.call_emergency()
