import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isw.settings')

import django

from coordination.models import Professor
import coordination.scripts.populate.old.model_interface as model_interface


def main():
    irapuato = model_interface.get_city(name='Irapuato')
    penjamo = model_interface.get_city(name='Penjamo')

    female = model_interface.get_gender(code='F')
    male = model_interface.get_gender(code='M')

    administrative = model_interface.get_professor_type(code='ADM')
    pa = model_interface.get_professor_type(code='PA')
    ptc = model_interface.get_professor_type(code='PTC')

    guanajuato = model_interface.get_state(name='Guanajuato')
    
    Professor.objects.create(active=0,
                             email='ahernandez@uppenjamo.edu.mx',
                             employee_number=1000,
                             gender=female,
                             initials='AHA',
                             name='Hernandez Avila Alejandra',
                             type=pa)
    Professor.objects.create(active=0,
                             email='adriana.montoya@uppenjamo.edu.mx',
                             employee_number=1065,
                             gender=female,
                             initials='AMA',
                             name='Montoya Ayala Adriana',
                             type=pa)
    Professor.objects.create(active=0,
                             email='bmartinezr@uppenjamo.edu.mx',
                             employee_number=1055,
                             gender=male,
                             initials='BMR',
                             name='Martinez Ramirez Benjamin',
                             type=pa)
    Professor.objects.create(active=0,
                             email='cvaldez@uppenjamo.edu.mx',
                             employee_number=1003,
                             gender=male,
                             initials='CAVH',
                             name='Valdez Herrera Carlos Alberto',
                             type=pa)
    Professor.objects.create(active=1,
                             city=irapuato,
                             email='carlos.uribe@uppenjamo.edu.mx',
                             employee_number=1064,
                             state=guanajuato,
                             gender=male,
                             initials='CMU',
                             name='Martinez Uribe Carlos',
                             type=pa)
    Professor.objects.create(active=0,
                             email='ckamper@uppenjamo.edu.mx',
                             employee_number=1004,
                             gender=female,
                             initials='CK',
                             name='Kamper Christine',
                             type=pa)
    Professor.objects.create(active=0,
                             email='earriaga@uppenjamo.edu.mx',
                             employee_number=1074,
                             gender=male,
                             initials='EAAH',
                             name='Arriaga Hurtado Erick Angel',
                             type=pa)
    Professor.objects.create(active=0,
                             email='eperez@uppenjamo.edu.mx',
                             employee_number=1073,
                             gender=male,
                             initials='EJPO',
                             name='Perez Onate Edgar De Jesus',
                             type=pa)
    Professor.objects.create(active=0,
                             email='fgutierrez@uppenjamo.edu.mx',
                             employee_number=1010,
                             gender=male,
                             initials='FJGM',
                             name='Gutierrez Melesio Francisco Javier',
                             type=pa)
    Professor.objects.create(active=0,
                             email='gcendejas@uppenjamo.edu.mx',
                             employee_number=1066,
                             gender=female,
                             initials='GAC',
                             name='Anaya Cendejas Giezi',
                             type=pa)
    Professor.objects.create(active=1,
                             city=penjamo,
                             email='gmedrano@uppenjamo.edu.mx',
                             employee_number=1130,
                             gender=male,
                             initials='GMA',
                             name='Medrano Arredondo Gilberto ',
                             state=guanajuato,
                             type=pa)
    Professor.objects.create(active=1,
                             city=penjamo,
                             email='gsantoyo@uppenjamo.edu.mx',
                             employee_number=1012,
                             state=guanajuato,
                             gender=female,
                             initials='GST',
                             name='Santoyo Tafoya Graciela',
                             type=pa)
    Professor.objects.create(active=1,
                             city=penjamo,
                             email='gcastro@uppenjamo.edu.mx',
                             employee_number=1093,
                             gender=male,
                             initials='GCM',
                             name='Castro Murillo Guilebaldo',
                             state=guanajuato,
                             type=pa)
    Professor.objects.create(active=0,
                             email='ptejeda@uppenjamo.edu.mx',
                             employee_number=1013,
                             gender=male,
                             initials='GPTA',
                             name='Tejeda Adame Gustavo Paul',
                             type=pa)
    Professor.objects.create(active=0,
                             city=penjamo,
                             email='ilichjasso@uppenjamo.edu.mx',
                             employee_number=58,
                             gender=male,
                             initials='IAJM',
                             name='Jasso Martinez Ilich Abdelcadir',
                             state=guanajuato,
                             type=ptc)
    Professor.objects.create(active=0,
                             email='jecortez@uppenjamo.edu.mx',
                             employee_number=1016,
                             gender=female,
                             initials='JCC',
                             name='Cortes Castaneda Jennifer',
                             type=pa)
    Professor.objects.create(active=0,
                             email='lcamacho@uppenjamo.edu.mx',
                             employee_number=1043,
                             gender=male,
                             initials='JLSC',
                             name='Soto Camacho Jesus Leonardo',
                             type=pa)
    Professor.objects.create(active=0,
                             email='jurbina@uppenjamo.edu.mx',
                             employee_number=1080,
                             gender=male,
                             initials='JUG',
                             name='Urbina Guerrero Jesus',
                             type=administrative)
    Professor.objects.create(active=0,
                             email='fbello@uppenjamo.edu.mx',
                             employee_number=28,
                             gender=male,
                             initials='JFBA',
                             name='Bello Avila Jose Francisco',
                             type=pa)
    Professor.objects.create(active=0,
                             city=irapuato,
                             email='jaltamirano@uppenjamo.edu.mx',
                             employee_number=1095,
                             gender=male,
                             initials='JLAH',
                             name='Altamirano Hernandez Jose Luis',
                             state=guanajuato,
                             type=pa)
    Professor.objects.create(active=0,
                             city=penjamo,
                             email='jlvargas@uppenjamo.edu.mx',
                             employee_number=1134,
                             gender=male,
                             initials='JLVR',
                             name='Vargas Rodriguez Jose Luis',
                             state=guanajuato,
                             type=pa)
    Professor.objects.create(active=0,
                             email='jsoto@uppenjamo.edu.mx',
                             employee_number=1017,
                             gender=male,
                             initials='JSC',
                             name='Soto Cerda Jorge',
                             type=pa)
    Professor.objects.create(active=0,
                             email='pamartinez@uppenjamo.edu.mx',
                             employee_number=1028,
                             gender=male,
                             initials='JPMS',
                             name='Martinez Sierra Juan Pablo',
                             type=pa)
    Professor.objects.create(active=0,
                             email='lgonzalez@uppenjamo.edu.mx',
                             employee_number=1082,
                             gender=male,
                             initials='LFGH',
                             name='Gonzalez Herrero Laider Fernando',
                             type=pa)
    Professor.objects.create(active=0,
                             email='lgarcia@uppenjamo.edu.mx',
                             employee_number=1035,
                             gender=female,
                             initials='LDGS',
                             name='Garcia Solorio Leidy Diana',
                             type=pa)
    Professor.objects.create(active=1,
                             city=penjamo,
                             email='lmorozco@uppenjamo.edu.mx',
                             employee_number=1122,
                             gender=male,
                             initials='LMOG',
                             name='Orozco Guerrero Luis Miguel',
                             state=guanajuato,
                             type=pa)
    Professor.objects.create(active=1,
                             city=irapuato,
                             email='lmburgara@uppenjamo.edu.mx',
                             employee_number=1092,
                             gender=male,
                             initials='LMBL',
                             name='Burgara Lopez Luis Moises',
                             state=guanajuato,
                             type=pa)
    Professor.objects.create(active=0,
                             city=penjamo,
                             email='memontoya@uppenjamo.edu.mx',
                             employee_number=1020,
                             gender=female,
                             initials='MEMA',
                             name='Montoya Ayala Maria Elena',
                             state=guanajuato,
                             type=pa)
    Professor.objects.create(active=0,
                             email='mogarcia@uppenjamo.edu.mx',
                             employee_number=1022,
                             gender=male,
                             initials='MOGG',
                             name='Garcia Gonzalez Mario Oleg',
                             type=pa)
    Professor.objects.create(active=0,
                             email='notorres@uppenjamo.edu.mx',
                             employee_number=1026,
                             gender=female,
                             initials='NTF',
                             name='Torres Figueroa Norma',
                             type=pa)
    Professor.objects.create(active=1,
                             email='pcervantes@uppenjamo.edu.mx',
                             employee_number=1029,
                             gender=male,
                             initials='PACM',
                             name='Cervantes Martinez Pedro Antonio',
                             type=pa)
    Professor.objects.create(active=0,
                             email='rnegrete@uppenjamo.edu.mx',
                             employee_number=1030,
                             gender=male,
                             initials='RNS',
                             name='Negrete Soto Reynaldo',
                             type=pa)
    Professor.objects.create(active=1,
                             city=irapuato,
                             email='samota@uppenjamo.edu.mx',
                             employee_number=1104,
                             gender=male,
                             initials='SAMG',
                             name='Mota Gutierrez Sergio Alejandro',
                             phone='4641146191',
                             state=guanajuato,
                             type=ptc)
    Professor.objects.create(active=0,
                             email='sdelgado@uppenjamo.edu.mx',
                             employee_number=1077,
                             gender=male,
                             initials='SDZ',
                             name='Delgado Zavala Sergio',
                             type=pa)
    Professor.objects.create(active=0,
                             email='uamezcua@uppenjamo.edu.mx',
                             employee_number=1033,
                             gender=male,
                             initials='UAG',
                             name='Amezcua Garcia Ulises',
                             type=pa)

if __name__ == '__main__':
    django.setup()

    main()