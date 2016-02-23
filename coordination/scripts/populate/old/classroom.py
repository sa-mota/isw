# coding=utf-8
import argparse

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

import cast
import db_interface
import model_interface
import xls_interface


def create_group(
        career,
        current_quarter,
        degree,
        file_type,
        generation,
        identifier
):
    if file_type == cast.FileType.academic_load:
        db_interface.create_group_from_academic_load(career, degree, generation, identifier, current_quarter)
    else:
        raise Exception('¡Documento no soportado <{:s}>!'.format(file_type))


def main(args):
    current_quarter = model_interface.get_quarter(args.current_period, args.current_year)

    curricular_map = model_interface.get_curricular_map(args.career, args.generation_year)
    generation_quarter = model_interface.get_quarter(args.generation_period, args.generation_year)
    generation = model_interface.get_generation(curricular_map, generation_quarter)

    create_group(args.career, current_quarter, args.degree, args.file_type, generation, args.identifier)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Registra un grupo a partir de un archivo.')
    parser.add_argument('file_type', help='Tipo de archivo', type=xls_interface.cast_string_to_file_type)
    parser.add_argument('career', help='Código de la carrera', type=model_interface.get_career)
    parser.add_argument('degree', help='Grado del grupo', type=model_interface.get_classroom_degree)
    parser.add_argument('identifier', help='Identificador del grupo', type=model_interface.get_classroom_identifier)
    parser.add_argument('generation_period', help='Código del periodo de la generación', type=model_interface.get_period)
    parser.add_argument('generation_year', help='Año de la generación', type=model_interface.get_year)
    parser.add_argument('current_period', help='Código del periodo actual', type=model_interface.get_period)
    parser.add_argument('current_year', help='Año actual', type=model_interface.get_year)

    arguments = parser.parse_args()
    main(arguments)