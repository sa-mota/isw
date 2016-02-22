import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

from coordination.models import Year


def main():
    Year.objects.create(id=2007)
    Year.objects.create(id=2008)
    Year.objects.create(id=2009)
    Year.objects.create(id=2010)
    Year.objects.create(id=2011)
    Year.objects.create(id=2012)
    Year.objects.create(id=2013)
    Year.objects.create(id=2014)
    Year.objects.create(id=2015)
    Year.objects.create(id=2016)

if __name__ == '__main__':
    main()
