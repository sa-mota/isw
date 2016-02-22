import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

from coordination.models import ClassroomIdentifier


def main():
    ClassroomIdentifier.objects.create(name='A')
    ClassroomIdentifier.objects.create(name='B')


if __name__ == '__main__':
    main()