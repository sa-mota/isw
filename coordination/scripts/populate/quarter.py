import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

import django

from coordination.models import Quarter
import coordination.scripts.model_interface as model_interface


def main():
    Quarter.objects.create(
        period=model_interface.get_period(code='SD'),
        year=model_interface.get_year(id=2013)
    )

    Quarter.objects.create(
        period=model_interface.get_period(code='EA'),
        year=model_interface.get_year(id=2014)
    )
    Quarter.objects.create(
        period=model_interface.get_period(code='MA'),
        year=model_interface.get_year(id=2014)
    )
    Quarter.objects.create(
        period=model_interface.get_period(code='SD'),
        year=model_interface.get_year(id=2014)
    )

    Quarter.objects.create(
        period=model_interface.get_period(code='EA'),
        year=model_interface.get_year(id=2015)
    )
    Quarter.objects.create(
        period=model_interface.get_period(code='MA'),
        year=model_interface.get_year(id=2015)
    )
    Quarter.objects.create(
        period=model_interface.get_period(code='SD'),
        year=model_interface.get_year(id=2015)
    )

    Quarter.objects.create(
        period=model_interface.get_period(code='EA'),
        year=model_interface.get_year(id=2016)
    )

if __name__ == '__main__':
    django.setup()

    main()
