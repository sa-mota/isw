# coding=utf-8
import django
django.setup()

import cast
from coordination.models import (
    Classroom,
    Period,
    Professor,
    Student,
    StudentInTaughtSubject,
    TaughtSubject,
    Year,
)
import xls_interface

import coordination.scripts.populate.old.model_interface as model_interface


def create_classroom(
        career,
        degree,
        file_type,
        identifier,
        quarter,
        leader=None
):
    tutor_name = xls_interface.read_tutor_name(career, degree, file_type, identifier, quarter)
    professor = model_interface.get_professor(tutor_name)

    try:
        classroom = Classroom.objects.create(
            career=career,
            degree=degree,
            identifier=identifier,
            leader=leader,
            quarter=quarter,
            tutor=professor
        )
    except:
        raise

    return classroom


def create_group_from_academic_load(
        career,
        degree,
        generation,
        identifier,
        quarter
):

    file_type = cast.FileType.academic_load

    if degree == model_interface.get_classroom_degree(1):
        students = create_students(career, degree, file_type, generation, identifier, quarter)
    else:
        students = find_students(file_type, quarter)

    classroom = create_classroom(career, degree, file_type, identifier, quarter, None)
    register_students_in_classroom(classroom, students)


def create_taught_subjects_from_professor_planning(
        career,
        quarter
):
    file_type = cast.FileType.professor_planning
    taught_subjects_data = xls_interface.read_taught_subjects(career=career, file_type=file_type, quarter=quarter)

    for professor in Professor.objects.all():
        professor.active = False
        professor.save()

    taught_subjects = []
    try:
        for entry in taught_subjects_data:
            professor = entry['professor']
            professor.active = True

            classroom = model_interface.get_classroom(
                career=career,
                degree=entry['classroom_degree'],
                identifier=entry['classroom_identifier'],
                quarter=quarter
            )

            taught_subject = TaughtSubject.objects.create(
                classroom=classroom,
                professor=professor,
                subject=entry['subject']
            )

            taught_subjects.append(taught_subject)
    except:
        raise

    return taught_subjects


def create_students(
        career,
        degree,
        file_type,
        generation,
        identifier,
        quarter
):
    students_data = xls_interface.read_students_data(career, degree, file_type, identifier, quarter)

    students = []
    try:
        for entry in students_data:
            student = Student.objects.create(
                gender=entry['gender'],
                generation=generation,
                name=entry['name'],
                registration_number=entry['registration_number'],
                status=entry['status']
            )

            students.append(student)
    except:
        raise

    return students


def find_students(
        career,
        degree,
        file_type,
        identifier,
        quarter
):
    students_data = xls_interface.read_students_data(career, degree, file_type, identifier, quarter)

    students = []
    try:
        for entry in students_data:
            student = Student.objects.get(registration_number=entry['registration_number'])

        students.append(student)
    except:
        raise

    return students


def register_students_in_classroom(
        classroom,
        students
):
    try:
        for student in students:
            # classroom.student.create(registration_number=student.registration_number)
            classroom.student.add(student)
    except:
        raise


def register_academic_loads_from_file(classroom):
    file_type = cast.FileType.academic_load

    students_data = xls_interface.read_students_data(
        classroom.career,
        classroom.degree,
        file_type,
        classroom.identifier,
        classroom.quarter
    )

    for student in classroom.student.all():
        student_data = search_student_in_students_data(students_data, student)
        academic_load_data = xls_interface.read_student_academic_load_data(
            classroom.career,
            classroom.degree,
            file_type,
            classroom.identifier,
            student_data,
            classroom.quarter
        )

        for entry in academic_load_data:
            degree = model_interface.get_classroom_degree(entry.degree)
            identifier = model_interface.get_classroom_identifier(entry.identifier)

            current_classroom = model_interface.get_classroom(
                career=classroom.career,
                degree=degree,
                identifier=identifier,
                quarter=classroom.quarter
            )

            subject = model_interface.get_subject(entry.subject)
            taught_subject = TaughtSubject.objects.get(
                classroom=current_classroom,
                subject=subject
            )

            opportunity = model_interface.get_subject_opportunity(entry.opportunity)
            StudentInTaughtSubject.objects.create(
                opportunity=opportunity,
                student=student,
                taught_subject=taught_subject
            )


def register_grades_from_grades_data(
        career,
        data_type,
        grades_data,
        quarter
):
    for entry in grades_data:
        degree = model_interface.get_classroom_degree(entry.degree)
        identifier = model_interface.get_classroom_identifier(entry.identifier)
        classroom = model_interface.get_classroom(career, degree, identifier, quarter)
        student = model_interface.get_student(entry.registration_number)
        subject = model_interface.get_subject(entry.subject)
        taught_subject = model_interface.get_taught_subject(classroom, subject)
        student_in_taught_subject = model_interface.get_student_in_taught_subject(student, taught_subject)

        if data_type == cast.DataType.first_grade:
            student_in_taught_subject.first_grade = entry.first_grade
        elif data_type == cast.DataType.second_grade:
            student_in_taught_subject.second_grade = entry.second_grade
        elif data_type == cast.DataType.regular_grade:
            student_in_taught_subject.regular_grade = entry.regular_grade
        elif data_type == cast.DataType.final_grade:
            status = model_interface.get_taught_status(entry.status)

            student_in_taught_subject.taught_subject_status = status
            student_in_taught_subject.final_grade = entry.final_grade
        else:
            raise Exception('¡Dato no soportado <{:s}>!'.format(data_type))

        student_in_taught_subject.save()


def register_grades_from_summary(
        career,
        quarter
):
    file_type = cast.FileType.grades_summary

    data_type = cast.DataType.first_grade
    grades_data = xls_interface.read_grades_data(career, data_type, file_type, quarter)
    register_grades_from_grades_data(career, data_type, grades_data, quarter)

    if quarter.year != Year.objects.get(id=2013):
        if quarter.period != Period.objects.get(code='SD'):
            data_type = cast.DataType.second_grade
            grades_data = xls_interface.read_grades_data(career, data_type, file_type, quarter)
            register_grades_from_grades_data(career, data_type, grades_data, quarter)

            data_type = cast.DataType.regular_grade
            grades_data = xls_interface.read_grades_data(career, data_type, file_type, quarter)
            register_grades_from_grades_data(career, data_type, grades_data, quarter)

    data_type = cast.DataType.final_grade
    grades_data = xls_interface.read_grades_data(career, data_type, file_type, quarter)
    register_grades_from_grades_data(career, data_type, grades_data, quarter)


def search_student_in_students_data(
        students_data,
        student
):
    student_data = None
    for entry in students_data:
        if entry['name'] == student.name:
            student_data = entry
            break

    if student_data is None:
        raise Exception('¡Estudiante no encontrado <{:s}>!'.format(student))

    return student_data