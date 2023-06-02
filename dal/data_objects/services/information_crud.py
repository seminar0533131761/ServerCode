from builtins import super

from dal.data_objects.services.basemodel import BaseModel
from dal.models.information import Information
import pandas as pd
import os.path


class InformationCrud(BaseModel):
    def __init__(self):
        super().__init__()
        self.information = {}
        self.informations = []
        self.my_path = os.path.abspath(os.path.dirname(__file__))
        self.path = os.path.join(self.my_path, "../../../api/csvs/information.csv")
        self.df = pd.read_csv(self.path)

    def get(self, id):
        int_id = int(id)
        row = self.df.loc[self.df['id'] == int_id]
        st = row.to_string(header=False, index=False)
        lst = st.split(".")
        self.information = Information(lst[0], lst[1], lst[2], lst[3], lst[4])
        return self.information

    def add_students_information(self, nw_students):
        try:
            students_information = []
            for index, row in nw_students.iterrows():
                information = Information(row["id"], row["educator_recommendation"], row["pricipal_recommendation"],
                                          row["til_analysis"], row["occupational_counseling"])
                students_information.append(information)
            for row in students_information:
                new_student_information = {"id": int(row.id), "educator_recommendation": row.educator_recommendation,
                                           "pricipal_recommendation": row.pricipal_recommendation,
                                           "til_analysis": row.til_analysis,
                                           "occupational_counseling": row.occupational}
                self.df = self.df._append(new_student_information, ignore_index=True)
            self.df.to_csv(self.path, index=False)
            return True
        except Exception as err:
            return False
