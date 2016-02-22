import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

from coordination.models import ProfessorType


def main():
    ProfessorType.objects.create(
        code='ADM',
        name='Administrativo'
    )
    ProfessorType.objects.create(
        code='PA',
        name='Profesor de asignatura'
    )
    ProfessorType.objects.create(
        code='PTC',
        name='Profesor de tiempo completo'
    )

if __name__ == '__main__':
    main()