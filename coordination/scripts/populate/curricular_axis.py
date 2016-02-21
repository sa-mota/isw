import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

from coordination.models import CurricularAxis


def main():
    CurricularAxis.objects.create(
        code='CV',
        name='Columna vertebral'
    )
    CurricularAxis.objects.create(
        code='ES',
        name='Especialidad'
    )
    CurricularAxis.objects.create(
        code='OP',
        name='Optativa'
    )
    CurricularAxis.objects.create(
        code='TR',
        name='Transversal'
    )

if __name__ == '__main__':
    main()
