import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

from coordination.models import Period
import coordination.scripts.populate.old.model_interface as model_interface


def main():
    Period.objects.create(
        code='EA',
        start=model_interface.get_month(name='Enero'),
        end=model_interface.get_month(name='Abril')
    )
    Period.objects.create(
        code='MA',
        start=model_interface.get_month(name='Mayo'),
        end=model_interface.get_month(name='Agosto')
    )
    Period.objects.create(
        code='SD',
        start=model_interface.get_month(name='Septiembre'),
        end=model_interface.get_month(name='Diciembre')
    )

if __name__ == '__main__':
    main()