import pytest
import lab3


def test_p1():
    shopping_list = ['flour', 'baking powder', 'baking soda', 'buttermilk', 'butter', 'brown sugar', 'chocolate chips']
    shopping_list_orig = shopping_list.copy()
    assert lab3.p1(shopping_list) == shopping_list_orig[:4] + shopping_list_orig[5:], 'output is different from original list minus butter'
    assert shopping_list == shopping_list_orig, 'input list was mutated'


def test_p2():
    shopping_list = ['flour', 'baking powder', 'baking soda', 'buttermilk', 'butter', 'brown sugar', 'chocolate chips']
    shopping_list_orig = shopping_list.copy()
    assert lab3.p2(shopping_list) == shopping_list_orig[:4] + shopping_list_orig[5:], 'output is different from original list minus butter'
    assert shopping_list != shopping_list_orig, 'input list was not mutated'


def test_p3():
    students = [
        ('April', 9078273),
        ('Greg', 3016445),
        ('Carter', 4598974),
        ('Ben', 5089601),
        ('Toni', 6838897),
        ('John', 7834461),
        ('Courtney', 6663484)
    ]
    students_orig = students.copy()
    assert lab3.p3(students, '89') == students_orig[0:2] + students_orig[5:]
    assert lab3.p3(students, '01') == students_orig[0:1] + students_orig[2:3] + students_orig[4:]
    assert lab3.p3(students, '0') == students_orig[2:3] + students_orig[4:]

def test_bonus_question():
    students = [
        ('April', 9078273),
        ('Greg', 3016445),
        ('Carter', 4598974),
        ('Ben', 5089601),
        ('Toni', 6838897),
        ('John', 7834461),
        ('Courtney', 6663484)
    ]
    assert lab3.bonus_question(students, '89') == [('April', 9078273), ('Greg', 3016445), ('Carter', 45974), ('Ben', 50601), ('Toni', 68387), ('John', 7834461), ('Courtney', 6663484)]
    assert lab3.bonus_question(students, '0') == [('April', 978273), ('Greg', 316445), ('Carter', 4598974), ('Ben', 58961), ('Toni', 6838897), ('John', 7834461), ('Courtney', 6663484)]
