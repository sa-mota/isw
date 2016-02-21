# coding=utf-8
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


def get_classroom_degree(id):
    try:
        degree = ClassroomDegree.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Exception('Grado no encontrado <{:d}>.'.format(id))

    return degree


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


def get_professor_type(code):
    try:
        professor_type = ProfessorType.objects.get(code=code)
    except ObjectDoesNotExist:
        raise Exception('Tipo de profesor no encontrado <{:s}>.'.format(code))

    return professor_type


def get_state(name):
    try:
        state = State.objects.get(name=name)
    except ObjectDoesNotExist:
        raise Exception('Estado no encontrado <{:s}>.'.format(name))

    return state


def get_year(id):
    try:
        year = Year.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Exception('Año no encontrado <{:d}>.'.format(id))

    return year