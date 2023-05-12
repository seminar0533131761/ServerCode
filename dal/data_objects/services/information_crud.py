from dal.data_objects.services.basemodel import BaseModel
from dal.models.information import Information
import pandas as pd
import os.path

class InformationCrud(BaseModel):
    def __init__(self):
        # super(InformationCrud,self).__init__()
        # # self.students_information = self.my_db["information"]
        # self.student_information = {}
        super().__init__()
        self.information = {}
        self.informations = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../../api/csvs/information.csv")
        self.df = pd.read_csv(path)

    def create_async(self, obj):
        pass

    def delete_async(self, id):
        pass

    def update_async(self, id):
        pass

    async def get_all_async(self):
        pass

    def get_async(self, id):
        # id,educator_recommendation,pricipal_recommendation,til_analysis,occupational_counseling
        # tmp_student_information = self.students_information.find_one({"_id": _id})
        # self.student_information = Information(tmp_student_information["_id"], tmp_student_information["educator_recommendation"],
        #                                        tmp_student_information["pricipal_recommendation"], tmp_student_information["til_analysis"],
        #                                        tmp_student_information["occupational_counseling"])

                # return self.student_information
        int_id = int(id)
        row = self.df.loc[self.df['id'] == int_id]
        st = row.to_string(header=False, index=False)
        lst = st.split(".")
        self.information = Information(lst[0], lst[1], lst[2], lst[3], lst[4])
        return self.information
