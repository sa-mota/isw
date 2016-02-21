# coding=utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

from coordination.models import Career


def main():
    # Career.objects.create(
    #     code='IAG',
    #     name='Ingeniería Agroindustrial'
    # )
    # Career.objects.create(
    #     code='IBT',
    #     name='Ingeniería en Biotecnología'
    # )
    # Career.objects.create(
    #     code='IND',
    #     name='Ingeniería Industrial'
    # )
    Career.objects.create(
        code='ISW',
        name='Ingeniería en Software'
    )
    # Career.objects.create(
    #     code='LAG',
    #     name='Licenciatura en Administración y Gestión de Pequeñas y Medianas Empresas'
    # )

if __name__ == '__main__':
    main()
