# coding=utf-8
import argparse

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

import cast
from coordination.scripts import model_interface, db_interface


def create_taught_subjects(
        career,
        quarter,
        file_type,
):
    if file_type == cast.FileType.professor_planning:
        db_interface.create_taught_subjects_from_professor_planning(career, quarter)
    else:
        raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))


def main(args):
    quarter = model_interface.get_quarter(args.period, args.year)

    create_taught_subjects(args.career, quarter, args.file_type)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Registra asignaturas impartidas a partir de un archivo.')
    parser.add_argument('file_type', help='Tipo de archivo', type=cast.cast_string_to_file_type)
    parser.add_argument('career', help='Código de la carrera', type=model_interface.get_career)
    parser.add_argument('period', help='Código del periodo', type=model_interface.get_period)
    parser.add_argument('year', help='Año', type=model_interface.get_year)

    arguments = parser.parse_args()
    main(arguments)