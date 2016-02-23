# coding=utf-8
from cast import *
from coordination.models import (
    Year
)

import model_interface

import os
import xlrd


########################################################################################################################
# Named tuples
########################################################################################################################
Point2D = namedtuple('Point2D', ['x', 'y'])


########################################################################################################################
# Methods
########################################################################################################################
def get_file_path(
        career,
        file_type,
        quarter,
        degree=None,
        identifier=None
):
    sgc_directory = os.getcwd() + '/coordination/sgc/'

    if file_type == FileType.academic_load:
        data_dir = 'soporte/sac15po01-procedimientos-de-servicios-escolares/sac01rg24-carga-academica/'

        filename = '{:s}/{:s}{:s}-{:s}{:s}.xls'
        filename = filename.format(career.code, quarter.year, quarter.period.code, degree, identifier)
        filename = filename.lower()
    elif file_type == FileType.professor_planning:
        data_dir = 'clave/sac01po01-gestion-de-la-asignatura/sac01rg01-planeacion-cautrimestral-de-personal-docente/'

        filename = '{:s}/{:s}{:s}.xls'
        filename = filename.format(career.code, quarter.year, quarter.period.code)
        filename = filename.lower()
    else:
        raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))

    file_path = sgc_directory + data_dir + filename
    return file_path


def get_headers_cells(
        data_type,
        file_type,
        quarter
):
    year = quarter.year.id

    if data_type == DataType.academic_load:
        if file_type == FileType.academic_load:
            if year == 2013:
                cells = TaughtSubjectInAcademicLoadData(
                    degree=Point2D(4, 12),
                    identifier=Point2D(4, 12),
                    opportunity=Point2D(3, 12),
                    subject=Point2D(0, 12)
                )
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(year))
        else:
            raise Exception('¡Documento no soportado <{:s}>!¡'.format(year))
    elif data_type == DataType.general:
        if file_type == FileType.academic_load:
            labels = ['tutor']

            Indices = namedtuple('Indices', labels)
            indices = Indices(0)

            Cells = namedtuple('Cells', labels)
            if year == 2013:
                cells = Cells(tutor=Point2D(2, 16))
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(year))

            columns = [
                cells.tutor.x,
            ]
        else:
            raise Exception('¡Documento no soportado <{:s}>!'.format(year))
    elif data_type == DataType.students_list:
        if file_type == FileType.academic_load:
            if year == 2013:
                cells = StudentData(
                    gender=Point2D(3, 7),
                    name=Point2D(2, 7),
                    number=Point2D(0, 7),
                    registration_number=Point2D(1, 7),
                    status=Point2D(5, 7)
                )
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(year))
        else:
            raise Exception('¡Documento no soportado <{:s}>!'.format(year))
    elif data_type == DataType.taught_subjects:
        if file_type == FileType.professor_planning:
            labels = [
                'degree',
                'identifier',
                'professor',
                'subject'
            ]

            Indices = namedtuple('Indices', labels)
            indices = Indices(0, 1, 2, 3)

            Cells = namedtuple('Cells', labels)
            if year == 2013:
                cells = Cells(
                    degree=Point2D(1, 0),
                    identifier=Point2D(1, 0),
                    professor=Point2D(2, 0),
                    subject=Point2D(0, 0)
                )
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(year))

            columns = [
                cells.degree.x,
                cells.identifier.x,
                cells.professor.x,
                cells.subject.x
            ]
        else:
            raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))
    else:
        raise Exception('¡Dato no soportado <{:s}>!'.format(data_type))

    return cells


def get_sheet_name(
        data_type,
        file_type,
        quarter,
        index=None
):
    if data_type == DataType.academic_load:
        if file_type == FileType.academic_load:
            if quarter.year == Year.objects.get(id=2013):
                sheet_name = 'T' + str(int(index))
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(quarter.year))
        else:
            raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))
    elif data_type == DataType.general:
        if file_type == FileType.academic_load:
            if quarter.year == Year.objects.get(id=2013):
                sheet_name = 'Datos'
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(quarter.year))
        else:
            raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))
    elif data_type == DataType.students_list:
        if file_type == FileType.academic_load:
            if quarter.year == Year.objects.get(id=2013):
                sheet_name = 'LISTAS'
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(quarter.year))
        else:
            raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))
    elif data_type == DataType.taught_subject:
        if file_type == FileType.professor_planning:
            if quarter.year == Year.objects.get(id=2013):
                sheet_name = 'Lista'
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(quarter.year))
        else:
            raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))
    else:
        raise Exception('¡Dato no soportado <{:s}>!'.format(data_type))

    return sheet_name


def get_worksheet(
        data_type,
        file_type,
        quarter,
        workbook,
        index=None
):
    sheet_name = get_sheet_name(data_type, file_type, quarter, index)
    try:
        worksheet = workbook.sheet_by_name(sheet_name)
    except:
        raise

    return worksheet


def open_workbook(
        career,
        file_type,
        quarter,
        degree=None,
        identifier=None
):
    file_path = get_file_path(career, file_type, quarter, degree, identifier)
    try:
        workbook = xlrd.open_workbook(file_path)
    except:
        raise

    return workbook


def process_gender_code(
        code,
        file_type,
        quarter
):
    if file_type == FileType.academic_load:
        if quarter.year == Year.objects.get(id=2013):
            code_upper = code.upper()
            if code_upper == 'F':
                gender_code = 'F'
            elif code_upper == 'M':
                gender_code = 'M'
            else:
                raise Exception('¡Código no soportado <{:s}>!'.format(code))
        else:
            raise Exception('¡Año no soportado <{:d}>!'.format(quarter.year))
    else:
        raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))

    return gender_code


def read_students_data(
        career,
        degree,
        file_type,
        identifier,
        quarter
):
    data_type = 'students'

    workbook = open_workbook(career, file_type, quarter, degree, identifier)
    worksheet = get_worksheet(data_type, file_type, quarter, workbook)

    headers_cells = get_headers_cells(data_type, file_type, quarter)

    rows = read_up_to_empty(
        worksheet,
        headers_cells['cells'].registration_number.y + 1,
        headers_cells['columns'],
        headers_cells['indices'].registration_number
    )

    students_data = []
    for row in rows:
        tmp = {}

        gender_code = process_gender_code(row[headers_cells['indices'].gender], file_type, quarter)
        tmp['gender'] = model_interface.get_gender(gender_code)

        name = row[headers_cells['indices'].name]
        tmp['name'] = cast_string_to_name(name)

        registration_number = row[headers_cells['indices'].registration_number]
        tmp['registration_number'] = cast_string_to_registration_number(registration_number)

        student_status_code = cast_string_to_student_status_name(
            row[headers_cells['indices'].status],
            file_type,
            quarter
        )
        tmp['status'] = model_interface.get_student_status(student_status_code)

        students_data.append(tmp)

    return students_data


def read_up_to_empty(
        worksheet,
        row_start,
        cols,
        master_col
):
    data = []

    row = row_start
    while True:
        if row >= worksheet.nrows:
            break

        if worksheet.cell_type(row, cols[master_col]) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK):
            break

        tmp = []
        for col in cols:
            tmp.append(worksheet.cell(row, col).value)

        data.append(tmp)
        row += 1

    return data


def read_tutor_name(
        career,
        degree,
        file_type,
        identifier,
        quarter
):
    data_type = 'general'
    file_path = get_file_path(career, degree, file_type, identifier, quarter)

    try:
        workbook = xlrd.open_workbook(file_path)
    except Exception as e:
        raise Exception(e.message)

    sheet_name = get_sheet_name(data_type, file_type, quarter)
    worksheet = workbook.sheet_by_name(sheet_name)

    headers_cells = get_headers_cells(data_type, file_type, quarter)

    if worksheet.cell_type(headers_cells['cells'].tutor.y, headers_cells['cells'].tutor.x) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK):
        raise Exception('¡Tutor inválido!')

    tutor_name = worksheet.cell(headers_cells['cells'].tutor.y, headers_cells['cells'].tutor.x).value
    return cast_string_to_name(tutor_name)