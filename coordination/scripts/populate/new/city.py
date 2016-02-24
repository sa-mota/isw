# coding=utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

from coordination.models import City


def main():
    City.objects.create(name='Abasolo')
    City.objects.create(name='Guanajuato')
    City.objects.create(name='Irapuato')
    City.objects.create(name='Pénjamo')
    City.objects.create(name='Salamanca')

if __name__ == '__main__':
    main()