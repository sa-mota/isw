import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

from coordination.models import ClassroomDegree


def main():
    ClassroomDegree.objects.create(id=1)
    ClassroomDegree.objects.create(id=2)
    ClassroomDegree.objects.create(id=3)
    ClassroomDegree.objects.create(id=4)
    ClassroomDegree.objects.create(id=5)
    ClassroomDegree.objects.create(id=6)
    ClassroomDegree.objects.create(id=7)
    ClassroomDegree.objects.create(id=8)
    ClassroomDegree.objects.create(id=9)
    ClassroomDegree.objects.create(id=10)


if __name__ == '__main__':
    main()
