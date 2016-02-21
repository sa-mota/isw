import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

from coordination.models import Gender


def main():
    Gender.objects.create(
        code='F',
        name='Femenino'
    )
    Gender.objects.create(
        code='M',
        name='Masculino'
    )

if __name__ == '__main__':
    main()