from dal.data_objects.services.icrud import ICRUD
from dal.models.students_desires import StudentsDesires


class StudentsDesiresCrud(ICRUD):
    def __init__(self):
        super().__init__()
        self.preferences = self.my_data_base["preferences"]
        self.my_preferences = {}


    def delete_async(self, id):
        pass

    def update_async(self, id):
        pass

    def get_async(self, _id):
        # tmp_preferences = self.preferences.find_one({"_id": _id})
        # self.my_preferences = StudentsDesires(tmp_preferences["_id"], tmp_preferences["preference1"],tmp_preferences["preference2"],tmp_preferences["recommendation1"],tmp_preferences["recommendation2"],tmp_preferences["final_answer"])
        self.my_preferences = StudentsDesires("214088999", "math","history","good","good","math")
        return self.my_preferences

    def get_all_async(self):
        pass
    def create_async(self, obj):
        pass
