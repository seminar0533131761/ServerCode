class Student:
    def __init__(self, id, first_name, last_name, phone, class_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.class_name = class_name

    def __str__(self):
        return f'The creature type is {self.first_name}'
