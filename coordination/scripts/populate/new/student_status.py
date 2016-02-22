import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

from coordination.models import StudentStatus


def main():
    StudentStatus.objects.create(name='Baja temporal')
    StudentStatus.objects.create(name='Baja definitiva')
    StudentStatus.objects.create(name='Condicionado')
    StudentStatus.objects.create(name='Egresado')
    StudentStatus.objects.create(name='Irregular')
    StudentStatus.objects.create(name='No inscrito')
    StudentStatus.objects.create(name='Regular')

if __name__ == '__main__':
    main()