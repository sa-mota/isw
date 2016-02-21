# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDegree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Academic degree',
                'verbose_name_plural': 'Academic degrees',
            },
        ),
        migrations.CreateModel(
            name='AcademicTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('average_grade', models.DecimalField(null=True, max_digits=4, decimal_places=2)),
                ('comment', models.CharField(max_length=256, null=True)),
                ('academic_degree', models.ForeignKey(to='coordination.AcademicDegree')),
            ],
            options={
                'ordering': ['professor', 'knowledge_area'],
                'verbose_name': 'Academic title',
                'verbose_name_plural': 'Academic titles',
            },
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=4)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Career',
                'verbose_name_plural': 'Careers',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('career', models.ForeignKey(to='coordination.Career')),
            ],
            options={
                'ordering': ['career', 'quarter', 'degree', 'identifier'],
                'verbose_name': 'Classroom',
                'verbose_name_plural': 'Classrooms',
            },
        ),
        migrations.CreateModel(
            name='ClassroomDegree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Degree',
                'verbose_name_plural': 'Degrees',
            },
        ),
        migrations.CreateModel(
            name='ClassroomIdentifier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=8)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Classroom identifier',
                'verbose_name_plural': 'Classrooms identifiers',
            },
        ),
        migrations.CreateModel(
            name='ClassroomLeader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('classroom', models.OneToOneField(to='coordination.Classroom')),
            ],
            options={
                'ordering': ['classroom'],
                'verbose_name': 'Classroom leader',
                'verbose_name_plural': 'Classrooms leaders',
            },
        ),
        migrations.CreateModel(
            name='CurricularAxis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=4)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
                'ordering': ['name', 'code'],
                'verbose_name': 'Curricular axis',
                'verbose_name_plural': 'Curricular axes',
            },
        ),
        migrations.CreateModel(
            name='CurricularMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('career', models.ForeignKey(to='coordination.Career')),
            ],
            options={
                'ordering': ['year', 'career'],
                'verbose_name': 'Curricular map',
                'verbose_name_plural': 'Curricular maps',
            },
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=16)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Frequency',
                'verbose_name_plural': 'Frequencies',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=2)),
                ('name', models.CharField(unique=True, max_length=16)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
            },
        ),
        migrations.CreateModel(
            name='Generation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('curricular_map', models.ForeignKey(to='coordination.CurricularMap')),
            ],
            options={
                'ordering': ['quarter'],
                'verbose_name': 'Generation',
                'verbose_name_plural': 'Generations',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('pnpc', models.BooleanField()),
                ('city', models.ForeignKey(to='coordination.City')),
            ],
            options={
                'ordering': ['name', 'state', 'city'],
                'verbose_name': 'Institution',
                'verbose_name_plural': 'Institutions',
            },
        ),
        migrations.CreateModel(
            name='KnowledgeArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Knowledge area',
                'verbose_name_plural': 'Knowledge areas',
            },
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=16)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Month',
                'verbose_name_plural': 'Months',
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=2)),
                ('end', models.OneToOneField(related_name='end', to='coordination.Month')),
                ('start', models.OneToOneField(related_name='start', to='coordination.Month')),
            ],
            options={
                'ordering': ['start'],
                'verbose_name': 'Period',
                'verbose_name_plural': 'Periods',
            },
        ),
        migrations.CreateModel(
            name='PreferenceLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=16)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Preference level',
                'verbose_name_plural': 'Preference levels',
            },
        ),
        migrations.CreateModel(
            name='PreferredSubjectByProfessor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preference_level', models.ForeignKey(to='coordination.PreferenceLevel')),
            ],
            options={
                'ordering': ['professor', 'subject'],
                'verbose_name': 'Preferred subject by professor',
                'verbose_name_plural': 'Preferred subjects by professor',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('active', models.BooleanField()),
                ('cv', models.FilePathField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('employee_number', models.IntegerField(serialize=False, primary_key=True)),
                ('initials', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professors',
            },
        ),
        migrations.CreateModel(
            name='ProfessorEvaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academy', models.DecimalField(max_digits=4, decimal_places=2)),
                ('activities_support', models.DecimalField(max_digits=4, decimal_places=2)),
                ('administrative_aspects', models.DecimalField(max_digits=4, decimal_places=2)),
                ('advisories', models.DecimalField(max_digits=4, decimal_places=2)),
                ('assignment_management', models.DecimalField(max_digits=4, decimal_places=2)),
                ('attendance_punctuality', models.DecimalField(max_digits=4, decimal_places=2)),
                ('class_review', models.DecimalField(max_digits=4, decimal_places=2)),
                ('continuous_education', models.DecimalField(max_digits=4, decimal_places=2)),
                ('research', models.DecimalField(null=True, max_digits=4, decimal_places=2)),
                ('students_evaluation', models.DecimalField(max_digits=4, decimal_places=2)),
                ('training', models.DecimalField(max_digits=4, decimal_places=2)),
                ('tutoring', models.DecimalField(null=True, max_digits=4, decimal_places=2)),
            ],
            options={
                'ordering': ['quarter', 'professor'],
                'verbose_name': 'Professor evaluation',
                'verbose_name_plural': 'Professors evaluations',
            },
        ),
        migrations.CreateModel(
            name='ProfessorEvaluationWeight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academy', models.FloatField(null=True)),
                ('activities_support', models.FloatField(null=True)),
                ('administrative_aspects', models.FloatField(null=True)),
                ('advisories', models.FloatField(null=True)),
                ('assignment_management', models.FloatField(null=True)),
                ('attendance_punctuality', models.FloatField(null=True)),
                ('class_review', models.FloatField(null=True)),
                ('continuous_education', models.FloatField(null=True)),
                ('research', models.FloatField(null=True)),
                ('students_evaluation', models.FloatField(null=True)),
                ('training', models.FloatField(null=True)),
                ('tutor', models.BooleanField()),
                ('tutoring', models.FloatField(null=True)),
            ],
            options={
                'ordering': ['quarter'],
                'verbose_name': 'Professor evaluation weight',
                'verbose_name_plural': 'Professor evaluation weights',
            },
        ),
        migrations.CreateModel(
            name='ProfessorType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=4)),
                ('name', models.CharField(unique=True, max_length=32)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Professor type',
                'verbose_name_plural': 'Professor types',
            },
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period', models.ForeignKey(to='coordination.Period')),
            ],
            options={
                'ordering': ['year', 'period'],
            },
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('name', models.CharField(max_length=128)),
                ('frequency', models.ForeignKey(to='coordination.Frequency')),
                ('quarter', models.ForeignKey(to='coordination.Quarter')),
            ],
            options={
                'ordering': ['name', 'quarter'],
                'verbose_name': 'Scholarship',
                'verbose_name_plural': 'Scholarships',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('knowledge_area', models.ForeignKey(to='coordination.KnowledgeArea')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Speciality',
                'verbose_name_plural': 'Specialities',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('leader', models.BooleanField()),
                ('name', models.CharField(max_length=64)),
                ('registration_number', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='StudentDeregistrationReason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Student deregistration reason',
                'verbose_name_plural': 'Student deregistration reasons',
            },
        ),
        migrations.CreateModel(
            name='StudentInClassroom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('classroom', models.ForeignKey(to='coordination.Classroom')),
            ],
            options={
                'ordering': ['classroom', 'student'],
                'verbose_name': 'Student in classroom',
                'verbose_name_plural': 'Students in classroom',
            },
        ),
        migrations.CreateModel(
            name='StudentInTaughtSubject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('final_grade', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('first_grade', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('regular_grade', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('second_grade', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
            ],
            options={
                'ordering': ['taught_subject', 'student'],
                'verbose_name': 'Student in taught subject',
                'verbose_name_plural': 'Students in taught subject',
            },
        ),
        migrations.CreateModel(
            name='StudentStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=16)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Student state',
                'verbose_name_plural': 'Student statuses',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('classroom_practical_hours', models.IntegerField()),
                ('classroom_theoretical_hours', models.IntegerField()),
                ('code', models.CharField(max_length=8)),
                ('credits', models.IntegerField()),
                ('name', models.CharField(max_length=64)),
                ('practical_hours', models.IntegerField()),
                ('theoretical_hours', models.IntegerField()),
                ('curricular_axis', models.ForeignKey(to='coordination.CurricularAxis')),
                ('curricular_map', models.ForeignKey(to='coordination.CurricularMap')),
                ('degree', models.ForeignKey(to='coordination.ClassroomDegree')),
                ('prerequisite', models.ManyToManyField(related_name='prerequisite_rel_+', to='coordination.Subject', blank=True)),
            ],
            options={
                'ordering': ['degree', 'name'],
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='SubjectOpportunity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=16)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Subject opportunity',
                'verbose_name_plural': 'Subject opportunities',
            },
        ),
        migrations.CreateModel(
            name='TaughtSubject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('classroom', models.ForeignKey(to='coordination.Classroom')),
            ],
            options={
                'ordering': ['classroom', 'subject'],
                'verbose_name': 'Taught subject',
                'verbose_name_plural': 'Taught subjects',
            },
        ),
        migrations.CreateModel(
            name='TaughtSubjectStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=16)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Taught subject status',
                'verbose_name_plural': 'Taught subject statuses',
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Year',
                'verbose_name_plural': 'Years',
            },
        ),
        migrations.CreateModel(
            name='ProfessorInactive',
            fields=[
                ('comment', models.CharField(max_length=256)),
                ('professor', models.OneToOneField(primary_key=True, serialize=False, to='coordination.Professor')),
            ],
            options={
                'ordering': ['professor'],
                'verbose_name': 'Professor inactive',
                'verbose_name_plural': 'Professors inactive',
            },
        ),
        migrations.CreateModel(
            name='StudentDefinitiveDeregistration',
            fields=[
                ('comment', models.CharField(max_length=256, blank=True)),
                ('student', models.OneToOneField(primary_key=True, serialize=False, to='coordination.Student')),
            ],
            options={
                'ordering': ['student', 'quarter'],
                'verbose_name': 'Student definitive deregistration',
                'verbose_name_plural': 'Student definitive deregistrations',
            },
        ),
        migrations.CreateModel(
            name='StudentGraduated',
            fields=[
                ('student', models.OneToOneField(primary_key=True, serialize=False, to='coordination.Student')),
            ],
            options={
                'ordering': ['quarter', 'student'],
                'verbose_name': 'Student graduated',
                'verbose_name_plural': 'Students graduated',
            },
        ),
        migrations.CreateModel(
            name='StudentNotRegistered',
            fields=[
                ('student', models.OneToOneField(primary_key=True, serialize=False, to='coordination.Student')),
            ],
            options={
                'ordering': ['quarter', 'student'],
                'verbose_name': 'Student not registered',
                'verbose_name_plural': 'Students not registered',
            },
        ),
        migrations.CreateModel(
            name='StudentTemporalDeregistration',
            fields=[
                ('comment', models.CharField(max_length=256, blank=True)),
                ('student', models.OneToOneField(primary_key=True, serialize=False, to='coordination.Student')),
            ],
            options={
                'ordering': ['student', 'quarter'],
                'verbose_name': 'Student temporal deregistration',
                'verbose_name_plural': 'Students temporal deregistration',
            },
        ),
        migrations.AddField(
            model_name='taughtsubject',
            name='professor',
            field=models.ForeignKey(to='coordination.Professor'),
        ),
        migrations.AddField(
            model_name='taughtsubject',
            name='student',
            field=models.ManyToManyField(to='coordination.Student', through='coordination.StudentInTaughtSubject'),
        ),
        migrations.AddField(
            model_name='taughtsubject',
            name='subject',
            field=models.ForeignKey(to='coordination.Subject'),
        ),
        migrations.AddField(
            model_name='studentintaughtsubject',
            name='opportunity',
            field=models.ForeignKey(to='coordination.SubjectOpportunity'),
        ),
        migrations.AddField(
            model_name='studentintaughtsubject',
            name='student',
            field=models.ForeignKey(to='coordination.Student'),
        ),
        migrations.AddField(
            model_name='studentintaughtsubject',
            name='taught_subject',
            field=models.ForeignKey(to='coordination.TaughtSubject'),
        ),
        migrations.AddField(
            model_name='studentintaughtsubject',
            name='taught_subject_status',
            field=models.ForeignKey(blank=True, to='coordination.TaughtSubjectStatus', null=True),
        ),
        migrations.AddField(
            model_name='studentinclassroom',
            name='student',
            field=models.ForeignKey(to='coordination.Student'),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.ForeignKey(to='coordination.Gender'),
        ),
        migrations.AddField(
            model_name='student',
            name='generation',
            field=models.ForeignKey(to='coordination.Generation'),
        ),
        migrations.AddField(
            model_name='student',
            name='scholarship',
            field=models.ManyToManyField(to='coordination.Scholarship', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.ForeignKey(to='coordination.StudentStatus'),
        ),
        migrations.AddField(
            model_name='quarter',
            name='year',
            field=models.ForeignKey(to='coordination.Year'),
        ),
        migrations.AddField(
            model_name='professorevaluationweight',
            name='professor_type',
            field=models.ForeignKey(to='coordination.ProfessorType'),
        ),
        migrations.AddField(
            model_name='professorevaluationweight',
            name='quarter',
            field=models.ForeignKey(to='coordination.Quarter'),
        ),
        migrations.AddField(
            model_name='professorevaluation',
            name='professor',
            field=models.ForeignKey(to='coordination.Professor'),
        ),
        migrations.AddField(
            model_name='professorevaluation',
            name='quarter',
            field=models.ForeignKey(to='coordination.Quarter'),
        ),
        migrations.AddField(
            model_name='professor',
            name='city',
            field=models.ForeignKey(blank=True, to='coordination.City', null=True),
        ),
        migrations.AddField(
            model_name='professor',
            name='gender',
            field=models.ForeignKey(to='coordination.Gender'),
        ),
        migrations.AddField(
            model_name='professor',
            name='state',
            field=models.ForeignKey(blank=True, to='coordination.State', null=True),
        ),
        migrations.AddField(
            model_name='professor',
            name='type',
            field=models.ForeignKey(to='coordination.ProfessorType'),
        ),
        migrations.AddField(
            model_name='preferredsubjectbyprofessor',
            name='professor',
            field=models.ForeignKey(to='coordination.Professor'),
        ),
        migrations.AddField(
            model_name='preferredsubjectbyprofessor',
            name='subject',
            field=models.ForeignKey(to='coordination.Subject'),
        ),
        migrations.AddField(
            model_name='institution',
            name='state',
            field=models.ForeignKey(to='coordination.State'),
        ),
        migrations.AddField(
            model_name='generation',
            name='quarter',
            field=models.OneToOneField(to='coordination.Quarter'),
        ),
        migrations.AddField(
            model_name='curricularmap',
            name='year',
            field=models.OneToOneField(to='coordination.Year'),
        ),
        migrations.AddField(
            model_name='classroomleader',
            name='leader',
            field=models.OneToOneField(to='coordination.Student'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='degree',
            field=models.ForeignKey(to='coordination.ClassroomDegree'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='identifier',
            field=models.ForeignKey(to='coordination.ClassroomIdentifier'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='quarter',
            field=models.ForeignKey(to='coordination.Quarter'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='student',
            field=models.ManyToManyField(to='coordination.Student', through='coordination.StudentInClassroom'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='tutor',
            field=models.ForeignKey(to='coordination.Professor'),
        ),
        migrations.AddField(
            model_name='academictitle',
            name='institution',
            field=models.ForeignKey(to='coordination.Institution'),
        ),
        migrations.AddField(
            model_name='academictitle',
            name='knowledge_area',
            field=models.ForeignKey(to='coordination.KnowledgeArea'),
        ),
        migrations.AddField(
            model_name='academictitle',
            name='professor',
            field=models.ForeignKey(to='coordination.Professor'),
        ),
        migrations.AddField(
            model_name='academictitle',
            name='speciality',
            field=models.ForeignKey(to='coordination.Speciality', null=True),
        ),
        migrations.AddField(
            model_name='academictitle',
            name='year',
            field=models.ForeignKey(to='coordination.Year'),
        ),
        migrations.AlterUniqueTogether(
            name='taughtsubject',
            unique_together=set([('subject', 'classroom')]),
        ),
        migrations.AlterUniqueTogether(
            name='subject',
            unique_together=set([('code', 'curricular_map', 'curricular_axis')]),
        ),
        migrations.AddField(
            model_name='studenttemporalderegistration',
            name='quarter',
            field=models.ForeignKey(to='coordination.Quarter'),
        ),
        migrations.AddField(
            model_name='studenttemporalderegistration',
            name='reason',
            field=models.ForeignKey(to='coordination.StudentDeregistrationReason'),
        ),
        migrations.AddField(
            model_name='studentnotregistered',
            name='quarter',
            field=models.ForeignKey(to='coordination.Quarter'),
        ),
        migrations.AlterUniqueTogether(
            name='studentintaughtsubject',
            unique_together=set([('taught_subject', 'student')]),
        ),
        migrations.AlterUniqueTogether(
            name='studentinclassroom',
            unique_together=set([('classroom', 'student')]),
        ),
        migrations.AddField(
            model_name='studentgraduated',
            name='quarter',
            field=models.ForeignKey(to='coordination.Quarter'),
        ),
        migrations.AddField(
            model_name='studentdefinitivederegistration',
            name='quarter',
            field=models.ForeignKey(to='coordination.Quarter'),
        ),
        migrations.AddField(
            model_name='studentdefinitivederegistration',
            name='reason',
            field=models.ForeignKey(to='coordination.StudentDeregistrationReason'),
        ),
        migrations.AlterUniqueTogether(
            name='speciality',
            unique_together=set([('knowledge_area', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='scholarship',
            unique_together=set([('quarter', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='quarter',
            unique_together=set([('year', 'period')]),
        ),
        migrations.AddField(
            model_name='professorinactive',
            name='quarter',
            field=models.ForeignKey(to='coordination.Quarter'),
        ),
        migrations.AlterUniqueTogether(
            name='professorevaluationweight',
            unique_together=set([('quarter', 'professor_type', 'tutor')]),
        ),
        migrations.AlterUniqueTogether(
            name='professorevaluation',
            unique_together=set([('quarter', 'professor')]),
        ),
        migrations.AlterUniqueTogether(
            name='preferredsubjectbyprofessor',
            unique_together=set([('professor', 'subject')]),
        ),
        migrations.AlterUniqueTogether(
            name='institution',
            unique_together=set([('city', 'state', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='generation',
            unique_together=set([('curricular_map', 'quarter')]),
        ),
        migrations.AlterUniqueTogether(
            name='curricularmap',
            unique_together=set([('year', 'career')]),
        ),
        migrations.AlterUniqueTogether(
            name='classroomleader',
            unique_together=set([('classroom', 'leader')]),
        ),
        migrations.AlterUniqueTogether(
            name='classroom',
            unique_together=set([('career', 'quarter', 'degree', 'identifier')]),
        ),
        migrations.AlterUniqueTogether(
            name='academictitle',
            unique_together=set([('knowledge_area', 'speciality', 'academic_degree', 'institution', 'professor')]),
        ),
    ]
