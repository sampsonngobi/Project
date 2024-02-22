import csv
from student_manager import add_student, update_student, load_student_data, write_to_file, remove_student, get_student, compute_cost
from pytest import approx
import pytest

ID_INDEX = 0
NAME_INDEX = 1
CLASSES_INDEX = 2
COST_INDEX = 3

student_data = load_student_data("student_info.csv")

def test_add_student():

    for student in student_data:

        assert len(student) == 4

        assert isinstance(student[ID_INDEX], str) 



def  test_compute_cost():

     compute_cost()
     
     cost_per_month = ''
     for student in student_data:
        if student[ID_INDEX] == 2345:
            expected_result = student[CLASSES_INDEX] * student[COST_INDEX] * 4
            assert cost_per_month == expected_result

        if student[ID_INDEX] == 1:
            expected_result = student[CLASSES_INDEX] * student[COST_INDEX] * 4
            assert isinstance (student[CLASSES_INDEX] , str)
        

            


   

    






    







pytest.main(["-v", "--tb=line", "-rN", __file__])