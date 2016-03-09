# coding=utf-8
import django
django.setup()
from django.core.exceptions import ObjectDoesNotExist

from coordination.models import *


def get_career(code):
    try:
        career = Career.objects.get(code=code)
    except ObjectDoesNotExist:
        raise Exception('Carrera no encontrada <{:s}>.'.format(code))

    return career


def get_city(name):
    try:
        city = City.objects.get(name=name)
    except ObjectDoesNotExist:
        raise Exception('Ciudad no encontrada <{:s}>.'.format(name))

    return city


def get_classroom(
        career,
        degree,
        identifier,
        quarter
):
    try:
        classroom = Classroom.objects.get(career=career, degree=degree, identifier=identifier, quarter=quarter)
    except ObjectDoesNotExist:
        raise Exception('Grupo no encontrado <{:s}, {:s}, {:s}, {:s}>.'.format(career, degree, identifier, quarter))

    return classroom


def get_classroom_degree(id):
    try:
        classroom_degree = ClassroomDegree.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Exception('Grado de grupo no encontrado <{:d}>.'.format(id))

    return classroom_degree


def get_classroom_identifier(name):
    try:
        classroom_identifier = ClassroomIdentifier.objects.get(name=name)
    except ObjectDoesNotExist:
        raise Exception('Identificador de grupo no encontrado <{:s}>.'.format(name))

    return classroom_identifier


def get_curricular_axis(code):
    try:
        curricular_axis = CurricularAxis.objects.get(code=code)
    except ObjectDoesNotExist:
        raise Exception('Eje curricular no encontrado <{:s}>.'.format(code))

    return curricular_axis


def get_curricular_map(
        career,
        year
):
    try:
        curricular_map = CurricularMap.objects.get(
            year=year,
            career=career
        )
    except ObjectDoesNotExist:
        raise Exception('Mapa curricular no encontrado <{:s}, {:d}>.'.format(career, year))

    return curricular_map


def get_gender(code):
    try:
        gender = Gender.objects.get(code=code)
    except ObjectDoesNotExist:
        raise Exception('Género no encontrado <{:s}>.'.format(code))

    return gender


def get_generation(curricular_map, quarter):
    try:
        generation = Generation.objects.get(curricular_map=curricular_map, quarter=quarter)
    except ObjectDoesNotExist:
        raise Exception('Generación no encontrada <{:s}, {:s}>.'.format(curricular_map, quarter))

    return generation


def get_month(name):
    try:
        month = Month.objects.get(name=name)
    except ObjectDoesNotExist:
        raise Exception('Mes no encontrado <{:s}>.'.format(name))

    return month


def get_period(code):
    try:
        period = Period.objects.get(code=code)
    except ObjectDoesNotExist:
        raise Exception('Periodo no encontrado <{:s}>.'.format(code))

    return period


def get_professor(name):
    try:
        professor = Professor.objects.get(name=name)
    except ObjectDoesNotExist:
        raise Exception('Profesor no encontrado <{:s}>.'.format(name))

    return professor


def get_professor_type(code):
    try:
        professor_type = ProfessorType.objects.get(code=code)
    except ObjectDoesNotExist:
        raise Exception('Tipo de profesor no encontrado <{:s}>.'.format(code))

    return professor_type


def get_quarter(period, year):
    try:
        quarter = Quarter.objects.get(period=period, year=year)
    except ObjectDoesNotExist:
        raise Exception('Cuatrimestre no encontrado <{:s}, {:s}>.'.format(period, year))

    return quarter


def get_state(name):
    try:
        state = State.objects.get(name=name)
    except ObjectDoesNotExist:
        raise Exception('Estado no encontrado <{:s}>.'.format(name))

    return state


def get_student(registration_number):
    try:
        student = Student.objects.get(registration_number=registration_number)
    except ObjectDoesNotExist:
        raise Exception('Estudiante no encontrado <{:d}>.'.format(registration_number))

    return student


def get_student_in_taught_subject(student, taught_subject):
    try:
        student_in_taught_subject = StudentInTaughtSubject.objects.get(student=student, taught_subject=taught_subject)
    except ObjectDoesNotExist:
        raise Exception('Estudiante en asignatura impartida no encontrado <{:s}, {:s}>.'.format(student, taught_subject))

    return student_in_taught_subject


def get_student_status(name):
    try:
        student_status = StudentStatus.objects.get(name=name)
    except ObjectDoesNotExist:
        raise Exception('Estado de estudiante no encontrado <{:s}>.'.format(name))

    return student_status


def get_subject(name):
    try:
        subject = Subject.objects.get(name=name)
    except ObjectDoesNotExist:
        raise Exception('Asignatura no encontrada <{:s}>.'.format(name))

    return subject


def get_subject_opportunity(name):
    try:
        subject_opportunity = SubjectOpportunity.objects.get(name=name)
    except ObjectDoesNotExist:
        raise Exception('Oportunidad de asignatura no encontrada <{:s}>.'.format(name))

    return subject_opportunity


def get_taught_subject(classroom, subject):
    try:
        taught_subject = TaughtSubject.objects.get(classroom=classroom, subject=subject)
    except ObjectDoesNotExist:
        raise Exception('Asignatura impartida no encontrada <{:s}, {:s}>.'.format(classroom, subject))

    return taught_subject


def get_taught_status(name):
    try:
        taught_subject_status = TaughtSubjectStatus.objects.get(name=name)
    except ObjectDoesNotExist:
        raise Exception('Estado de asignatura impartida no encontrado <{:s}>.'.format(name))

    return taught_subject_status


def get_year(id):
    try:
        year = Year.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Exception('Año no encontrado <{:d}>.'.format(id))

    return year