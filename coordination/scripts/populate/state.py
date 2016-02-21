import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

from coordination.models import State


def main():
    State.objects.create(name='Guanajuato')

if __name__ == '__main__':
    main()