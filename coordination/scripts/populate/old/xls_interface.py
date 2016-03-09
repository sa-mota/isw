# coding=utf-8
import os
from collections import namedtuple

import xlrd

import cast
from coordination.models import (
    Period,
    Year
)
from coordination.scripts import model_interface

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

    if file_type == cast.FileType.academic_load:
        data_dir = 'soporte/sac15po01-procedimientos-de-servicios-escolares/sac01rg24-carga-academica/'

        filename = '{:s}/{:s}{:s}-{:s}{:s}.xls'
        filename = filename.format(career.code, quarter.year, quarter.period.code, degree, identifier)
        filename = filename.lower()
    elif file_type == cast.FileType.grades_summary:
        data_dir = 'clave/sac01po02-evaluacion-del-aprendizaje/concentrado/'

        filename = '{:s}/{:s}{:s}.xls'
        filename = filename.format(career.code, quarter.year, quarter.period.code)
        filename = filename.lower()
    elif file_type == cast.FileType.professor_planning:
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

    if data_type == cast.DataType.academic_load:
        if file_type == cast.FileType.academic_load:
            if year == 2013:
                cells = cast.TaughtSubjectInAcademicLoadData(
                    degree=Point2D(4, 12),
                    identifier=Point2D(4, 12),
                    opportunity=Point2D(3, 12),
                    subject=Point2D(0, 12)
                )
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(year))
        else:
            raise Exception('¡Documento no soportado <{:s}>!¡'.format(year))
    elif data_type == cast.DataType.general:
        if file_type == cast.FileType.academic_load:
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
    elif data_type == cast.DataType.first_grade:
        if file_type == cast.FileType.grades_summary:
            if year == 2013:
                cells = cast.GradeData(
                    absence=Point2D(8, 3),
                    career=Point2D(4, 3),
                    degree=Point2D(6, 3),
                    final_grade=Point2D(-1, -1),
                    first_grade=Point2D(7, 3),
                    gender=Point2D(3, 3),
                    identifier=Point2D(6, 3),
                    professor=Point2D(11, 3),
                    registration_number=Point2D(1, 3),
                    regular_grade=Point2D(-1, -1),
                    second_grade=Point2D(-1, -1),
                    status=Point2D(-1, -1),
                    student=Point2D(2, 3),
                    subject=Point2D(5, 3)
                )
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(year))
        else:
            raise Exception('¡Documento no soportado <{:s}>!¡'.format(year))
    elif data_type == cast.DataType.final_grade:
        if file_type == cast.FileType.grades_summary:
            if year == 2013:
                cells = cast.GradeData(
                    absence=Point2D(9, 3),
                    career=Point2D(4, 3),
                    degree=Point2D(6, 3),
                    final_grade=Point2D(8, 3),
                    first_grade=Point2D(-1, -1),
                    gender=Point2D(3, 3),
                    identifier=Point2D(6, 3),
                    professor=Point2D(15, 3),
                    registration_number=Point2D(1, 3),
                    regular_grade=Point2D(-1, -1),
                    second_grade=Point2D(-1, -1),
                    status=Point2D(11, 3),
                    student=Point2D(2, 3),
                    subject=Point2D(5, 3)
                )
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(year))
        else:
            raise Exception('¡Documento no soportado <{:s}>!¡'.format(year))
    elif data_type == cast.DataType.students_list:
        if file_type == cast.FileType.academic_load:
            if year == 2013:
                cells = cast.StudentData(
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
    elif data_type == cast.DataType.taught_subjects:
        if file_type == cast.FileType.professor_planning:
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
    if data_type == cast.DataType.academic_load:
        if file_type == cast.FileType.academic_load:
            if quarter.year == Year.objects.get(id=2013):
                sheet_name = 'T' + str(int(index))
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(quarter.year))
        else:
            raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))
    elif data_type == cast.DataType.final_grade:
        if file_type == cast.FileType.grades_summary:
            if quarter.year == Year.objects.get(id=2013):
                if quarter.period == Period.objects.get(code='SD'):
                    sheet_name = 'FINAL'
                else:
                    raise Exception('¡Periodo no soportado <{:s}>!'.format(quarter.period))
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(quarter.year))
        else:
            raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))
    elif data_type == cast.DataType.first_grade:
        if file_type == cast.FileType.grades_summary:
            if quarter.year == Year.objects.get(id=2013):
                if quarter.period == Period.objects.get(code='SD'):
                    sheet_name = 'PARCIAL 1'
                else:
                    raise Exception('¡Periodo no soportado <{:s}>!'.format(quarter.period))
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(quarter.year))
        else:
            raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))
    elif data_type == cast.DataType.general:
        if file_type == cast.FileType.academic_load:
            if quarter.year == Year.objects.get(id=2013):
                sheet_name = 'Datos'
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(quarter.year))
        else:
            raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))
    elif data_type == cast.DataType.students_list:
        if file_type == cast.FileType.academic_load:
            if quarter.year == Year.objects.get(id=2013):
                sheet_name = 'LISTAS'
            else:
                raise Exception('¡Año no soportado <{:d}>!'.format(quarter.year))
        else:
            raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))
    elif data_type == cast.DataType.taught_subjects:
        if file_type == cast.FileType.professor_planning:
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
    if file_type == cast.FileType.academic_load:
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


def get_columns(cells):
    columns = []
    for name in cells._fields:
        columns.append(getattr(cells, name).x)

    return columns


def read_grades_data(
        career,
        data_type,
        file_type,
        quarter
):
    workbook = open_workbook(career, file_type, quarter)
    worksheet = get_worksheet(data_type, file_type, quarter, workbook)

    cells = get_headers_cells(data_type, file_type, quarter)

    rows = read_up_to_empty(worksheet, cells.registration_number.y + 1, get_columns(cells), cells.registration_number.x)

    career_index = 1
    rows = [row for row in rows if row[career_index].upper() == career.code]

    grades_data = cast.cast_rows_to_grades_data(rows)
    return grades_data


def read_rows(
        worksheet,
        cells,
        num_rows_to_read
):
    data = []
    first_cell = getattr(cells, cells._fields[0])

    row = first_cell.y + 1
    while row < first_cell.y + num_rows_to_read:
        if row >= worksheet.nrows:
            break

        if worksheet.cell_type(row, first_cell.x) not in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK):
            tmp = []
            for field in cells._fields:
                cell = getattr(cells, field)
                tmp.append(worksheet.cell(row, cell.x).value)

            data.append(tmp)

        row += 1

    return data


def read_student_academic_load_data(
        career,
        degree,
        file_type,
        identifier,
        student_data,
        quarter
):
    data_type = cast.DataType.academic_load
    workbook = open_workbook(career, file_type, quarter, degree, identifier)
    worksheet = get_worksheet(data_type, file_type, quarter, workbook, index=student_data['number'])

    cells = get_headers_cells(data_type, file_type, quarter)

    num_rows_to_read = 9
    rows = read_rows(worksheet, cells, num_rows_to_read)

    academic_load_data = cast.cast_rows_to_academic_load_data(rows)
    return academic_load_data


def read_students_data(
        career,
        degree,
        file_type,
        identifier,
        quarter
):
    data_type = cast.DataType.students_list

    workbook = open_workbook(career, file_type, quarter, degree, identifier)
    worksheet = get_worksheet(data_type, file_type, quarter, workbook)

    cells = get_headers_cells(data_type, file_type, quarter)
    rows = read_up_to_empty(worksheet, cells.registration_number.y + 1, get_columns(cells), cells.registration_number.x)

    students_data = []
    for row in rows:
        tmp = {}

        gender_code = process_gender_code(row[0], file_type, quarter)
        tmp['gender'] = model_interface.get_gender(gender_code)

        name = row[1]
        tmp['name'] = cast.cast_string_to_name(name)

        number = row[2]
        tmp['number'] = cast.cast_string_to_integer(number)

        registration_number = row[3]
        tmp['registration_number'] = cast.cast_string_to_integer(registration_number)

        student_status_code = cast.cast_string_to_student_status_name(row[4])
        tmp['status'] = model_interface.get_student_status(student_status_code)

        students_data.append(tmp)

    return students_data


def read_taught_subjects(
        career,
        file_type,
        quarter
):
    data_type = cast.DataType.taught_subjects

    workbook = open_workbook(career, file_type, quarter)
    worksheet = get_worksheet(data_type, file_type, quarter, workbook)

    cells = get_headers_cells(data_type, file_type, quarter)
    rows = read_up_to_empty(worksheet, cells.subject.y + 1, get_columns(cells), cells.subject.x)

    taught_subjects_data = []
    for row in rows:
        tmp = {}

        classroom_degree = cast.cast_string_to_classroom_degree(row[0])
        tmp['classroom_degree'] = model_interface.get_classroom_degree(classroom_degree)

        classroom_identifier = cast.cast_string_to_classroom_identifier(row[1])
        tmp['classroom_identifier'] = model_interface.get_classroom_identifier(classroom_identifier)

        professor_name = cast.cast_string_to_name(row[2])
        tmp['professor'] = model_interface.get_professor(name=professor_name)

        subject_name = cast.cast_string_to_name(row[3])
        tmp['subject'] = model_interface.get_subject(name=subject_name)

        taught_subjects_data.append(tmp)

    return taught_subjects_data


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
            if col < 0:
                tmp.append(None)
            else:
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
    data_type = cast.DataType.general

    workbook = open_workbook(career, file_type, quarter, degree, identifier)
    worksheet = get_worksheet(data_type, file_type, quarter, workbook)

    cells = get_headers_cells(data_type, file_type, quarter)

    if worksheet.cell_type(cells.tutor.y, cells.tutor.x) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK):
        raise Exception('¡Tutor inválido!')

    tutor_name = worksheet.cell(cells.tutor.y, cells.tutor.x).value
    return cast.cast_string_to_name(tutor_name)