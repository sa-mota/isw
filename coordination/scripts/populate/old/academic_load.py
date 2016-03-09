# coding=utf-8
import argparse

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

import cast
import db_interface
import model_interface


def register_academic_loads(
        classroom,
        file_type,
):
    if file_type == cast.FileType.academic_load:
        db_interface.register_academic_loads_from_file(classroom)
    else:
        raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))


def main(args):
    quarter = model_interface.get_quarter(args.period, args.year)
    classroom = model_interface.get_classroom(args.career, args.degree, args.identifier, quarter)

    register_academic_loads(classroom, args.file_type)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Registra asignaturas impartidas a partir de un archivo.')
    parser.add_argument('file_type', help='Tipo de archivo', type=cast.cast_string_to_file_type)
    parser.add_argument('career', help='Código de la carrera', type=model_interface.get_career)
    parser.add_argument('degree', help='Grado del grupo', type=model_interface.get_classroom_degree)
    parser.add_argument('identifier', help='Identificador del grupo', type=model_interface.get_classroom_identifier)
    parser.add_argument('period', help='Código del periodo', type=model_interface.get_period)
    parser.add_argument('year', help='Año', type=model_interface.get_year)

    arguments = parser.parse_args()
    main(arguments)