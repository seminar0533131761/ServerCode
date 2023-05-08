from dal.data_objects.services.icrud import ICRUD
from dal.data_objects.services.student_crud import StudentCrud
from dal.models.students_desires import StudentsDesires


class StudentsDesiresCrud(ICRUD):
    def __init__(self):
        super().__init__()
        self.preferences = self.my_data_base["preferences"]
        self.obj_students_desires = []
        self.my_preferences = {}


    def delete_async(self, id):
        pass

    def update_async(self, id):
        pass

    def get_async(self, _id):
        # tmp_preferences = self.preferences.find_one({"_id": _id})
        # self.my_preferences = StudentsDesires(tmp_preferences["_id"], tmp_preferences["preference1"],tmp_preferences["preference2"],tmp_preferences["recommendation1"],tmp_preferences["recommendation2"],tmp_preferences["final_answer"])
        self.my_preferences = StudentsDesires("214088999", "math","history","to accept","not to accept","math")
        return self.my_preferences

    def get_all_async(self):
        pass
    def create_async(self, obj):
        pass
    def get_final_answer_by_class_name(self,class_name):
        student=StudentCrud()
        student_desires=StudentsDesiresCrud()
        student_desires_lst=[]
        new_students=student.get_student_by_class_name(class_name)
        for student in new_students:
            student_desires_lst.append(student_desires.get_async(student.id))
        print(list(student_desires_lst))
        return student_desires_lst
    def get_students_by_final_answer(self,training_name):
        self.obj_students_desires.extend([StudentsDesires("214088999", "math", "history", "to accept", "not to accept", "math"),
                                          StudentsDesires("214088999", "math", "history", "to accept", "not to accept","history"),
                                          StudentsDesires("214088999", "math", "history", "to accept", "not to accept", "math")])
        specified_training = [i for i in self.obj_students_desires if i.training_name == training_name]
        print(list(specified_training[0].training_name))
        return specified_training
