import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

import django

from coordination.models import CurricularMap
import coordination.scripts.model_interface as model_interface


def main():
    CurricularMap.objects.create(
        year=model_interface.get_year(id=2013),
        career=model_interface.get_career(code='ISW')
    )

if __name__ == '__main__':
    django.setup()
    main()