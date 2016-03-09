# coding=utf-8
import argparse

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

import cast
from coordination.scripts import model_interface, db_interface


def register_grades(
        career,
        file_type,
        quarter
):
    if file_type == cast.FileType.grades_summary:
        db_interface.register_grades_from_summary(career, quarter)
    else:
        raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))


def main(args):
    quarter = model_interface.get_quarter(args.period, args.year)

    register_grades(args.career, args.file_type, quarter)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Registra calificaciones a partir de un archivo.')
    parser.add_argument('file_type', help='Tipo de archivo', type=cast.cast_string_to_file_type)
    parser.add_argument('career', help='Código de la carrera', type=model_interface.get_career)
    parser.add_argument('period', help='Código del periodo', type=model_interface.get_period)
    parser.add_argument('year', help='Año', type=model_interface.get_year)

    arguments = parser.parse_args()
    main(arguments)