SHOPPING_LIST = ['flour', 'baking powder', 'butter', 'brown sugar', 'chocolate chips']
STUDENTS = [
    ('April', 9078273),
    ('Greg', 3016445),
    ('Carter', 4598974),
    ('Ben', 5089601),
    ('Toni', 6838897),
    ('John', 7834461),
    ('Courtney', 6663484)
]

def p1(ingredients):
    """
    Given a list of ingredients, if the list contains 'butter', this function returns a new instance of the
    list where 'butter' has been removed from the list. This function does NOT mutate the input list. 

    :param list ingredients: List of ingredients (as strings)
    :return: A new list containing ingredients with 'butter' removed
    :rtype: list
    """

    return 


def p2(ingredients):
    """
    Given a list of ingredients, if the list contains 'butter', this function removes 'butter' from the list
    by mutating the list in place, then returns the mutated list.

    :param list ingredients: List of ingredients (as strings)
    :return: A new list containing ingredients with 'butter' removed
    :rtype: list
    """

    return 


def p3(student_list, remove_when_id_contains):
    """
    Given a list of tuples containing students first names and their student ID numbers,
    returns a new list with all students except those whose ID number contains 
    the sequential digits in remove_when_id_contains. Does not mutate student_list.

    :param list student_list: A list of tuples of (student_name, student_ID)
    :param string remove_when_id_contains: A string of digits. When the student_ID
      contains these digits, the student is not included in the returned list
    :return: A new list without students whose student IDs contain the sequential digits in
      remove_when_id_contains
    :rtype: list
    """

    return 


def bonus_question(student_list, digits_to_remove):
    """
    Given a list of tuples containing students first names and their student ID numbers,
    lists, returns a new list with all students, where the student ID numbers have been
    modified to remove occurrences of the sequence of digits in  digits_to_remove. 

    :param list student_list: A list of tuples of (student_name, student_ID)
    :param string digits_to_remove: A string of digits. When the student_ID
      contains these digits, the student ID is modified to remove them.
    :return: A new list of students with modified student IDs. s
    :rtype: list
    """

    return 

#The lines below will run some automatic tests to tell you if your functions are awesome or if they're 
#a hot mess of junk :p
if __name__ == '__main__':
    print('Starting value of SHOPPING_LIST: ', SHOPPING_LIST)
    
    print('\np1(SHOPPING_LIST): ', p1(SHOPPING_LIST))
    print('Value of SHOPPING_LIST after p1: ', SHOPPING_LIST)

    print('\np2(SHOPPING_LIST): ', p2(SHOPPING_LIST))
    print('Value of SHOPPING_LKIST after p2: ', SHOPPING_LIST)
    
    print('\np3(STUDENTS, \'89\'')
    print(p3(STUDENTS, '89'))

    print('\nbonus_question(STUDENTS, \'89\'')
    print(bonus_question(STUDENTS, '89'))
