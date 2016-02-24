import cast
from coordination.models import (
    Classroom,
    Student,
    StudentInClassroom,
)
import xls_interface

import coordination.scripts.populate.old.model_interface as model_interface


def create_classroom(
        career,
        degree,
        file_type,
        identifier,
        leader,
        quarter
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

    classroom = create_classroom(career, degree, file_type, identifier, students[0], quarter)
    register_students_in_classroom(classroom, students)


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
            StudentInClassroom.objects.create(classroom=classroom, student=student)
    except:
        raise