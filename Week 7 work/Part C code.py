class Practitioner:
    def __init__(self, practitioner_id, name, specialty):
        self.__practitioner_id = practitioner_id
        self.__name = name
        self.__specialty = specialty

    def set_practitioner_id(self, practitioner_id):
        if practitioner_id != "":
            self.__practitioner_id = practitioner_id

    def set_name(self, name):
        if name != "":
            self.__name = name

    def set_specialty(self, specialty):
        if specialty != "":
            self.__specialty = specialty

    def get_practitioner_id(self):
        return self.__practitioner_id

    def get_name(self):
        return self.__name

    def get_specialty(self):
        return self.__specialty
    
    