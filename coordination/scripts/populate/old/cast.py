# coding=utf-8
from collections import namedtuple
from enum import Enum
from unicodedata import (
    category,
    normalize
)


########################################################################################################################
# Enumerations
########################################################################################################################
class DataType(Enum):
    academic_load = 1
    final_grade = 2
    first_grade = 3
    general = 4
    professor_planning = 5
    regular_grade = 6
    second_grade = 7
    students_list = 8
    taught_subjects = 9


class FileType(Enum):
    academic_load = 1
    grades_summary = 2
    professor_planning = 3


########################################################################################################################
# Data containers
########################################################################################################################
GradeData = namedtuple(
    'GradeData',
    ['absence',
     'career',
     'degree',
     'final_grade',
     'first_grade',
     'gender',
     'identifier',
     'professor',
     'registration_number',
     'regular_grade',
     'second_grade',
     'status',
     'student',
     'subject']
)

TaughtSubjectInAcademicLoadData = namedtuple(
    'TaughtSubjectInAcademicLoadData',
    ['degree', 'identifier', 'opportunity', 'subject']
)

StudentData = namedtuple(
    'StudentData',
    ['gender', 'name', 'number', 'registration_number', 'status']
)


########################################################################################################################
# Methods
########################################################################################################################
def cast_rows_to_academic_load_data(rows):
    academic_load_data = []
    for entry in rows:
        taught_subject_in_academic_load_data = TaughtSubjectInAcademicLoadData(
            degree=cast_string_to_classroom_degree(entry[0]),
            identifier=cast_string_to_classroom_identifier(entry[1]),
            opportunity=cast_string_to_subject_opportunity(entry[2]),
            subject=cast_string_to_name(entry[3])
        )

        academic_load_data.append(taught_subject_in_academic_load_data)

    return academic_load_data


def cast_rows_to_grades_data(
        rows
):
    grades_data = []
    for entry in rows:
        grade_data = GradeData(
            absence=cast_string_to_integer(entry[0]),
            career=cast_string_to_name(entry[1]),
            degree=cast_string_to_classroom_degree(entry[2]),
            final_grade=cast_string_to_float(entry[3]),
            first_grade=cast_string_to_float(entry[4]),
            gender=cast_string_to_gender(entry[5]),
            identifier=cast_string_to_classroom_identifier(entry[6]),
            professor=cast_string_to_name(entry[7]),
            registration_number=cast_string_to_integer(entry[8]),
            regular_grade=cast_string_to_float(entry[9]),
            second_grade=cast_string_to_float(entry[10]),
            status=cast_string_to_subject_status(entry[11]),
            student=cast_string_to_name(entry[12]),
            subject=cast_string_to_name(entry[13])

        )

        grades_data.append(grade_data)

    return grades_data


def cast_string_to_classroom_degree(string):
    string = strip_accents(string)

    classroom_degree = ''.join(character for character in string if character.isdigit())
    try:
        classroom_degree = int(classroom_degree)
    except:
        raise Exception('Cadena de grado de grupo no soportada <{:s}>'.format(string))

    return classroom_degree


def cast_string_to_classroom_identifier(string):
    string = strip_accents(string)

    if 'ISW' in string:
        if 'A' in string:
            classroom_identifier = 'A'
        elif 'B' in string:
            classroom_identifier = 'B'
        else:
            raise Exception('Cadena de identificador de grupo no soportada <{:s}>'.format(string))
    elif 'MIX' in string:
        if 'MIXTO' in string:
            string = string.replace('MIXTO', 'MIX')

        classroom_identifier = ''.join(character for character in string if not character.isdigit())
    elif 'UNI' in string:
        if 'UNICO' in string:
            string = string.replace('UNICO', 'UNI')

        classroom_identifier = ''.join(character for character in string if not character.isdigit())
    elif 'A' in string:
        classroom_identifier = 'A'
    elif 'B' in string:
        classroom_identifier = 'B'
    else:
        raise Exception('Cadena de identificador de grupo no soportada <{:s}>'.format(string))

    return classroom_identifier


def cast_string_to_file_type(string):
    if string == 'academic_load':
        file_type = FileType.academic_load
    elif string == 'grades_summary':
        file_type = FileType.grades_summary
    elif string == 'professor_planning':
        file_type = FileType.professor_planning
    else:
        raise Exception('¡Documento no soportado <{:s}>!')

    return file_type


def cast_string_to_float(string):
    if string is None:
        return None

    try:
        number = float(string)
    except:
        raise

    return number


def cast_string_to_gender(string):
    try:
        string_upper = string.upper()
        if string_upper == 'F':
            gender = 'F'
        elif string_upper == 'M' or string_upper == 'H':
            gender = 'M'
        else:
            raise Exception('¡Género no soportado <{:s}>!'.format(string))
    except AttributeError:
        code = cast_string_to_integer(string)

        if code == 0:
            gender = 'F'
        else:
            gender = 'M'
    except:
        raise

    return gender


def cast_string_to_integer(string):
    try:
        number = int(string)
    except:
        raise

    return number


def cast_string_to_name(string):
    name = strip_accents(string)
    name = name.title()

    return name


def cast_string_to_student_status_name(string):
    if string == 'REGULAR.':
        student_status_name = 'Regular'
    elif string == 'IRREGULAR.':
        student_status_name = 'Irregular'
    elif string == 'CONDICIONADO.':
        student_status_name = 'Condicionado'
    else:
        raise Exception('Cadena de estado de estudiante no soportada <{:s}>'.format(string))

    return student_status_name


def cast_string_to_subject_opportunity(string):
    if 'Reg.' == string:
        subject_opportunity = 'Regular'
    elif 'Rec.' == string:
        subject_opportunity = 'Recurse'
    elif 'Con.' == string:
        subject_opportunity = 'Condicionado'
    elif 'Baj.' == string:
        subject_opportunity = 'Baja'
    else:
        raise Exception('Cadena de oportunidad de asignatura no soportada <{:s}>'.format(string))

    return subject_opportunity


def cast_string_to_subject_status(string):
    if string is None:
        return None

    if 'REG' == string:
        subject_status = 'Regular'
    elif 'ORD' == string:
        subject_status = 'Ordinaria'
    else:
        raise Exception('Cadena de estado de asignatura no soportada <{:s}>'.format(string))

    return subject_status


def strip_accents(string):
    string = ''.join(character for character in normalize('NFKD', string) if category(character) != 'Mn')

    return string