from coordination.models import (
    Classroom,
    Student,
    StudentInClassroom,
)
from xls_interface import (
    FileType,
    read_tutor_name,
    read_students_data,
)

import coordination.scripts.populate.old.model_interface as model_interface


def create_classroom(
        career,
        degree,
        file_type,
        identifier,
        quarter
):
    tutor_name = read_tutor_name(career, degree, file_type, identifier, quarter)
    professor = model_interface.get_professor(tutor_name)

    try:
        classroom = Classroom.objects.create(
            career=career,
            degree=degree,
            identifier=identifier,
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

    file_type = FileType.academic_load

    if degree == model_interface.get_classroom_degree(1):
        students = create_students(career, degree, file_type, generation, identifier, quarter)
    else:
        students = find_students(file_type, quarter)

    classroom = create_classroom(career, degree, file_type, identifier, quarter)
    register_students_in_classroom(classroom, students)


def create_students(
        career,
        degree,
        file_type,
        generation,
        identifier,
        quarter
):
    students_data = read_students_data(career, degree, file_type, identifier, quarter)

    students = []
    try:
        for entry in students_data:

            student = Student.objects.create(
                gender=entry['gender'],
                generation=generation,
                leader=False,
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
    students_data = read_students_data(career, degree, file_type, identifier, quarter)

    students = []
    try:
        for entry in students_data:
            student = Student.objects.get(registration_number=entry['registration_number'])

        students.append(student)
    except:
        raise

    return students


def register_students_in_classroom(
        students,
        classroom
):
    try:
        for student in students:
            StudentInClassroom.objects.create(classroom, student)
    except:
        raise