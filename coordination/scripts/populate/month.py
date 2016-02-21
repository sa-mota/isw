import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

from coordination.models import Month


def main():
    Month.objects.create(name='Enero')
    Month.objects.create(name='Febrero')
    Month.objects.create(name='Marzo')
    Month.objects.create(name='Abril')
    Month.objects.create(name='Mayo')
    Month.objects.create(name='Junio')
    Month.objects.create(name='Julio')
    Month.objects.create(name='Agosto')
    Month.objects.create(name='Septiembre')
    Month.objects.create(name='Octubre')
    Month.objects.create(name='Noviembre')
    Month.objects.create(name='Diciembre')

if __name__ == '__main__':
    main()
