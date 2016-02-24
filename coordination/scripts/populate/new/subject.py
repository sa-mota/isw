# coding=utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

import django

from coordination.models import Subject
import coordination.scripts.populate.old.model_interface as model_interface


def main():
    career = model_interface.get_career(code='ISW')
    year = model_interface.get_year(id=2013)
    curricular_map = model_interface.get_curricular_map(
        career=career,
        year=year
    )

    spine = model_interface.get_curricular_axis(code='CV')
    speciality = model_interface.get_curricular_axis(code='ES')
    optional = model_interface.get_curricular_axis(code='OP')
    transversal = model_interface.get_curricular_axis(code='TR')

    ####################################################################################################################
    # first
    ####################################################################################################################
    degree = model_interface.get_classroom_degree(1)
    Subject.objects.create(
        classroom_practical_hours=1,
        classroom_theoretical_hours=4,
        code='INGI',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Inglés I',
        practical_hours=2,
        theoretical_hours=4
    )
    Subject.objects.create(
        classroom_practical_hours=1,
        classroom_theoretical_hours=2,
        code='VAS',
        credits=3,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Valores del ser',
        practical_hours=1,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=4,
        classroom_theoretical_hours=2,
        code='CDI',
        credits=8,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Cálculo diferencial e integral',
        practical_hours=6,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=3,
        code='MAD',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Matemáticas discretas',
        practical_hours=3,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='ELM',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Electricidad y magnetismo',
        practical_hours=3,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=3,
        code='IAP',
        credits=7,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Introducción a la programación',
        practical_hours=3,
        theoretical_hours=4
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='ADM',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Administración',
        practical_hours=3,
        theoretical_hours=3
    )

    ####################################################################################################################
    # second
    ####################################################################################################################
    degree = model_interface.get_classroom_degree(2)
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='INGII',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Inglés II',
        practical_hours=5,
        theoretical_hours=5
    )
    Subject.objects.create(
        classroom_practical_hours=1,
        classroom_theoretical_hours=2,
        code='INE',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Inteligencia emocional',
        practical_hours=1,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='CAV',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Cálculo vectorial',
        practical_hours=5,
        theoretical_hours=5
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='ALL',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Álgebra lineal',
        practical_hours=5,
        theoretical_hours=5
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='SID',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Sistemas digitales',
        practical_hours=3,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=3,
            classroom_theoretical_hours=2,
            code='POO',
            credits=7,
            curricular_map=curricular_map,
            curricular_axis=spine,
            degree=degree,
            name='Programación orientada a objetos',
            practical_hours=4,
            theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=4,
        classroom_theoretical_hours=1,
        code='ESD',
        credits=7,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Estructuras de datos',
        practical_hours=6,
        theoretical_hours=2
    )

    ####################################################################################################################
    # third
    ####################################################################################################################
    degree = model_interface.get_classroom_degree(3)
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=3,
        code='INGIII',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Inglés III',
        practical_hours=3,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=1,
        classroom_theoretical_hours=2,
        code='DEI',
        credits=3,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Desarrollo interpersonal',
        practical_hours=1,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=3,
        code='ECD',
        credits=8,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Ecuaciones diferenciales',
        practical_hours=4,
        theoretical_hours=4
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=3,
        code='PRE',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Probabilidad y estadística',
        practical_hours=5,
        theoretical_hours=6
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='ARC',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Arquitectura de computadoras',
        practical_hours=4,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=1,
        code='POE',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Programación orientada a eventos',
        practical_hours=5,
        theoretical_hours=1
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='BAD',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Bases de datos',
        practical_hours=4,
        theoretical_hours=2
    )

    ####################################################################################################################
    # fourth
    ####################################################################################################################
    degree = model_interface.get_classroom_degree(4)
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=3,
        code='INGIV',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Inglés IV',
        practical_hours=3,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=1,
        classroom_theoretical_hours=2,
        code='HAP',
        credits=3,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Habilidades del pensamiento',
        practical_hours=1,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='MEN',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Métodos numéricos',
        practical_hours=3,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='PRW',
        credits=7,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Programación web',
        practical_hours=4,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=1,
        code='BDD',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Bases de datos distribuidas',
        practical_hours=4,
        theoretical_hours=1
    )
    Subject.objects.create(
        classroom_practical_hours=1,
        classroom_theoretical_hours=4,
        code='INS',
        credits=7,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Ingeniería de software',
        practical_hours=2,
        theoretical_hours=5
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=3,
        code='FUR',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Fundamentos de redes',
        practical_hours=3,
        theoretical_hours=3
    )

    ####################################################################################################################
    # fifth
    ####################################################################################################################
    degree = model_interface.get_classroom_degree(5)
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=3,
        code='INGV',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Inglés V',
        practical_hours=3,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=1,
        classroom_theoretical_hours=2,
        code='HAO',
        credits=3,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Habilidades organizacionales',
        practical_hours=1,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='PRO',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Programación concurrente',
        practical_hours=3,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=1,
        code='EDA',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Estructuras de datos avanzadas',
        practical_hours=5,
        theoretical_hours=1
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='ANS',
        credits=7,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Análisis de sistemas',
        practical_hours=4,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='RED',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Redes',
        practical_hours=4,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='SIO',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Sistemas operativos',
        practical_hours=3,
        theoretical_hours=3
    )

    ####################################################################################################################
    # sixth
    ####################################################################################################################
    degree = model_interface.get_classroom_degree(6)
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=3,
        code='INGVI',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Inglés VI',
        practical_hours=3,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=1,
        classroom_theoretical_hours=2,
        code='ETP',
        credits=3,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Ética profesional',
        practical_hours=1,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='DSC',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Desarrollo de sistemas cliente/servidor',
        practical_hours=4,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='DIS',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Diseño de sistemas',
        practical_hours=4,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='SAI',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Seguridad informática',
        practical_hours=3,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='LEA',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Lenguajes y autómatas',
        practical_hours=4,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=0,
        classroom_theoretical_hours=0,code='ESOFI',
        credits=8,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Estancia I',
        practical_hours=8,
        theoretical_hours=0
    )

    ####################################################################################################################
    # seventh
    ####################################################################################################################
    degree = model_interface.get_classroom_degree(7)
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=3,
        code='INGVII',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Inglés VII',
        practical_hours=3,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='MAS',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Mantenimiento de sistemas',
        practical_hours=3,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='CAS',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Calidad de software',
        practical_hours=3,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='COI',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Compiladores e intérpretes',
        practical_hours=4,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='INE',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Ingeniería económica',
        practical_hours=3,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='VIA',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=optional,
        degree=degree,
        name='Visión artificial',
        practical_hours=3,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=0,
        classroom_theoretical_hours=0,
        code='ESOFII',
        credits=8,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Estancia II',
        practical_hours=8,
        theoretical_hours=0
    )

    ####################################################################################################################
    # eighth
    ####################################################################################################################
    degree = model_interface.get_classroom_degree(8)
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=3,
        code='INGVIII',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Inglés VIII',
        practical_hours=3,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='DAM',
        credits=7,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Desarrollo de aplicaciones móviles',
        practical_hours=4,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='REI',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Reingeniería',
        practical_hours=3,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=3,
        code='PPS',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Planeación de proyectos de software',
        practical_hours=3,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='INA',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Inteligencia artificial',
        practical_hours=3,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='GRM',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Graficación y multimedia',
        practical_hours=4,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='REV',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=optional,
        degree=degree,
        name='Realidad virtual',
        practical_hours=3,
        theoretical_hours=2
    )

    ####################################################################################################################
    # ninth
    ####################################################################################################################
    degree = model_interface.get_classroom_degree(9)
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=3,
        code='INGIX',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Inglés IX',
        practical_hours=3,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='SII',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Sistemas de información',
        practical_hours=3,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=3,
        code='APS',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=spine,
        degree=degree,
        name='Administración de proyectos de software',
        practical_hours=3,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='DSI',
        credits=6,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Desarrollo de sistemas inteligentes',
        practical_hours=4,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=1,
        classroom_theoretical_hours=3,
        code='ADT',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Administración de TIC',
        practical_hours=2,
        theoretical_hours=3
    )
    Subject.objects.create(
        classroom_practical_hours=2,
        classroom_theoretical_hours=2,
        code='DAM',
        credits=5,
        curricular_map=curricular_map,
        curricular_axis=optional,
        degree=degree,
        name='Desarrollo de aplicaciones móviles avanzadas',
        practical_hours=3,
        theoretical_hours=2
    )
    Subject.objects.create(
        classroom_practical_hours=3,
        classroom_theoretical_hours=2,
        code='AOS',
        credits=7,
        curricular_map=curricular_map,
        curricular_axis=speciality,
        degree=degree,
        name='Arquitecturas orientadas a servicios',
        practical_hours=4,
        theoretical_hours=3
    )

    ####################################################################################################################
    # tenth
    ####################################################################################################################
    degree = model_interface.get_classroom_degree(10)
    Subject.objects.create(
        classroom_practical_hours=0,
        classroom_theoretical_hours=0,
        code='ESOFIII',
        credits=40,
        curricular_map=curricular_map,
        curricular_axis=transversal,
        degree=degree,
        name='Estadía',
        practical_hours=40,
        theoretical_hours=0
    )


if __name__ == '__main__':
    django.setup()
    main()