from dal.data_objects.services.icrud import ICRUD
from dal.models.information import Information


class InformationCrud(ICRUD):
    def __init__(self):
        super().__init__()
        self.students_information = self.my_data_base["information"]
        self.student_information = {}

    def create_async(self, obj):
        pass

    def delete_async(self, id):
        pass

    def update_async(self, id):
        pass

    async def get_all_async(self):
        pass

    def get_async(self, _id):
        # id,educator_recommendation,pricipal_recommendation,til_analysis,occupational_counseling
        # tmp_student_information = self.students_information.find_one({"_id": _id})
        # self.student_information = Information(tmp_student_information["_id"], tmp_student_information["educator_recommendation"],
        #                                        tmp_student_information["pricipal_recommendation"], tmp_student_information["til_analysis"],
        #                                        tmp_student_information["occupational_counseling"])

        self.student_information = Information("214088999", "great student has nothing what to improve", "she does not really like history",
                                               "the til is basically good but show more variably ability","did not go to occupational counseling")
        return self.student_information

