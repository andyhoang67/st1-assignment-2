class Patient:
    def __init__(self, patient_id, name):
        self.__patient_id = patient_id
        self.__name = name

    def set_patient_id(self, patient_id):
        if patient_id != "":
            self.__patient_id = patient_id

    def set_name(self, name):
        if name != "":
            self.__name = name

    def get_patient_id(self):
        return self.__patient_id

    def get_name(self):
        return self.__name