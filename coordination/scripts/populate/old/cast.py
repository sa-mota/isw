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
    general = 2
    professor_planning = 3
    students_list = 4
    taught_subjects = 5


class FileType(Enum):
    academic_load = 1
    professor_planning = 2


########################################################################################################################
# Data containers
########################################################################################################################
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
def cast_string_to_file_type(string):
    if string == 'academic_load':
        file_type = FileType.academic_load
    elif string == 'professor_planning':
        file_type = FileType.professor_planning
    else:
        raise Exception('¡Documento no soportado <{:s}>!')

    return file_type


def cast_string_to_registration_number(string):
    try:
        registration_number = int(string)
    except:
        raise

    return registration_number


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


def strip_accents(string):
    string = ''.join(character for character in normalize('NFKD', string) if category(character) != 'Mn')

    return string