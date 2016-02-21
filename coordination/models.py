from django.core.urlresolvers import reverse
from django.db import models

app_label = 'sicpe'

class AcademicDegree(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'Academic degree'
        verbose_name_plural = 'Academic degrees'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class AcademicTitle(models.Model):
    academic_degree = models.ForeignKey(AcademicDegree)
    average_grade = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        null=True
    )
    comment = models.CharField(
        max_length=256,
        null=True
    )
    institution = models.ForeignKey('Institution')
    knowledge_area = models.ForeignKey('KnowledgeArea')
    professor = models.ForeignKey('Professor')
    speciality = models.ForeignKey(
        'Speciality',
        null=True
    )
    year = models.ForeignKey('Year')

    class Meta:
        app_label = app_label
        ordering = [
            'professor',
            'knowledge_area',
        ]
        unique_together = (
            ('knowledge_area', 'speciality', 'academic_degree', 'institution', 'professor',),
        )
        verbose_name = 'Academic title'
        verbose_name_plural = 'Academic titles'

    def __unicode__(self):
        return u'{:s} {:s}'.format(
            self.professor,
            self.academic_degree
        )


class Career(models.Model):
    code = models.CharField(
        max_length=4,
        unique=True
    )
    name = models.CharField(
        max_length=128,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'Career'
        verbose_name_plural = 'Careers'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class City(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class Classroom(models.Model):
    career = models.ForeignKey(Career)
    degree = models.ForeignKey('ClassroomDegree')
    identifier = models.ForeignKey('ClassroomIdentifier')
    quarter = models.ForeignKey('Quarter')
    student = models.ManyToManyField(
        'Student',
        through='StudentInClassroom'
    )
    tutor = models.ForeignKey('Professor')

    class Meta:
        app_label = app_label
        ordering = [
            'career',
            'quarter',
            'degree',
            'identifier',
        ]
        unique_together = (
            ('career', 'quarter', 'degree', 'identifier',),
        )
        verbose_name = 'Classroom'
        verbose_name_plural = 'Classrooms'

    def __unicode__(self):
        return u'{:s} {:s} {:s}{:s}'.format(
            self.career.code,
            self.quarter,
            self.degree,
            self.identifier
        )

    def get_absolute_url(self):
        return reverse(
            'classrooms-view',
            kwargs={'pk': self.id}
        )


class ClassroomDegree(models.Model):
    class Meta:
        app_label = app_label
        ordering = [
            'id',
        ]
        verbose_name = 'Degree'
        verbose_name_plural = 'Degrees'

    def __unicode__(self):
        return u'{:d}'.format(self.id)


class ClassroomIdentifier(models.Model):
    name = models.CharField(
        max_length=8,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'Classroom identifier'
        verbose_name_plural = 'Classrooms identifiers'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class ClassroomLeader(models.Model):
    classroom = models.OneToOneField(Classroom)
    leader = models.OneToOneField('Student')

    class Meta:
        app_label = app_label
        ordering = [
            'classroom',
        ]
        unique_together = (
            ('classroom', 'leader'),
        )
        verbose_name = 'Classroom leader'
        verbose_name_plural = 'Classrooms leaders'

    def __unicode__(self):
        return u'{:s} {:s}'.format(
            self.classroom,
            self.leader
        )


class CurricularAxis(models.Model):
    code = models.CharField(
        max_length=4,
        unique=True
    )
    name = models.CharField(
        max_length=64,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
            'code',
        ]
        verbose_name = 'Curricular axis'
        verbose_name_plural = 'Curricular axes'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class CurricularMap(models.Model):
    career = models.ForeignKey(Career)
    year = models.OneToOneField('Year')

    class Meta:
        app_label = app_label
        ordering = [
            'year',
            'career',
        ]
        unique_together = (
            ('year', 'career'),
        )
        verbose_name = 'Curricular map'
        verbose_name_plural = 'Curricular maps'

    def __unicode__(self):
        return u'{:s} {:s}'.format(
            self.year,
            self.career
        )


class Frequency(models.Model):
    name = models.CharField(
        max_length=16,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'Frequency'
        verbose_name_plural = 'Frequencies'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class Gender(models.Model):
    code = models.CharField(
        max_length=2,
        unique=True
    )
    name = models.CharField(
        max_length=16,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class Generation(models.Model):
    curricular_map = models.ForeignKey(CurricularMap)
    quarter = models.OneToOneField('Quarter')

    class Meta:
        app_label = app_label
        ordering = [
            'quarter',
        ]
        unique_together = (
            ('curricular_map', 'quarter'),
        )
        verbose_name = 'Generation'
        verbose_name_plural = 'Generations'

    def __unicode__(self):
        return u'{:s} {:s}'.format(
            self.quarter,
            self.curricular_map.career
        )


class Institution(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField(max_length=256)
    pnpc = models.BooleanField()
    state = models.ForeignKey('State')

    class Meta:
        app_label = app_label
        ordering = [
            'name',
            'state',
            'city',
        ]
        unique_together = (
            ('city', 'state', 'name'),
        )
        verbose_name = 'Institution'
        verbose_name_plural = 'Institutions'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class KnowledgeArea(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'Knowledge area'
        verbose_name_plural = 'Knowledge areas'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class Month(models.Model):
    name = models.CharField(
        max_length=16,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'Month'
        verbose_name_plural = 'Months'

    def __unicode__(self):
        return u'{:s}'.format(self.name)

    def __lt__(self, other):
        if self.id < other.id:
            return True
        else:
            return False

    def __gt__(self,other):
        return other < self


class Period(models.Model):
    code = models.CharField(
        max_length=2,
        unique=True
    )
    end = models.OneToOneField(
        Month,
        related_name='end',
        unique=True
    )
    start = models.OneToOneField(
        Month,
        related_name='start',
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'start',
        ]
        verbose_name = 'Period'
        verbose_name_plural = 'Periods'

    def __unicode__(self):
        return u'{:s} - {:s}'.format(
            self.start,
            self.end
        )

    def __lt__(self, other):
        if self.start < other.inicio:
            return True
        else:
            return False

    def __gt__(self,other):
        return other < self


class PreferenceLevel(models.Model):
    name = models.CharField(
        max_length=16,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'Preference level'
        verbose_name_plural = 'Preference levels'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class PreferredSubjectByProfessor(models.Model):
    preference_level = models.ForeignKey(PreferenceLevel)
    professor = models.ForeignKey('Professor')
    subject = models.ForeignKey('Subject')

    class Meta:
        app_label = app_label
        ordering = [
            'professor',
            'subject',
        ]
        unique_together = (
            ('professor', 'subject'),
        )
        verbose_name = 'Preferred subject by professor'
        verbose_name_plural = 'Preferred subjects by professor'

    def __unicode__(self):
        return u'{:s}'.format(self.professor)


class Professor(models.Model):
    active = models.BooleanField()
    city = models.ForeignKey(
        City,
        blank=True,
        null=True
    )
    cv = models.FilePathField(
        blank=True,
        null=True
    )
    email = models.EmailField()
    employee_number = models.IntegerField(primary_key=True)
    gender = models.ForeignKey(Gender)
    initials = models.CharField(max_length=8)
    name = models.CharField(max_length=64)
    phone = models.CharField(
        blank=True,
        max_length=15,
        null=True
    )
    state = models.ForeignKey(
        'State',
        blank=True,
        null=True
    )
    type = models.ForeignKey('ProfessorType')

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class ProfessorEvaluation(models.Model):
    academy = models.DecimalField(
        decimal_places=2,
        max_digits=4
    )
    activities_support = models.DecimalField(
        decimal_places=2,
        max_digits=4
    )
    administrative_aspects = models.DecimalField(
        decimal_places=2,
        max_digits=4
    )
    advisories = models.DecimalField(
        decimal_places=2,
        max_digits=4
    )
    assignment_management = models.DecimalField(
        decimal_places=2,
        max_digits=4
    )
    attendance_punctuality = models.DecimalField(
        decimal_places=2,
        max_digits=4
    )
    class_review = models.DecimalField(
        decimal_places=2,
        max_digits=4
    )
    continuous_education = models.DecimalField(
        decimal_places=2,
        max_digits=4
    )
    professor = models.ForeignKey(Professor)
    quarter = models.ForeignKey('Quarter')
    research = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        null=True
    )
    students_evaluation = models.DecimalField(
        decimal_places=2,
        max_digits=4
    )
    training = models.DecimalField(
        decimal_places=2,
        max_digits=4
    )
    tutoring = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        null=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'quarter',
            'professor',
        ]
        unique_together = (
            ('quarter', 'professor'),
        )
        verbose_name = 'Professor evaluation'
        verbose_name_plural = 'Professors evaluations'

    def __unicode__(self):
        return u'{:s} {:s}'.format(
            self.quarter,
            self.professor
        )


class ProfessorEvaluationWeight(models.Model):
    academy = models.FloatField(null=True)
    activities_support = models.FloatField(null=True)
    administrative_aspects = models.FloatField(null=True)
    advisories = models.FloatField(null=True)
    assignment_management = models.FloatField(null=True)
    attendance_punctuality = models.FloatField(null=True)
    class_review = models.FloatField(null=True)
    continuous_education = models.FloatField(null=True)
    professor_type = models.ForeignKey('ProfessorType')
    quarter = models.ForeignKey('Quarter')
    research = models.FloatField(null=True)
    students_evaluation = models.FloatField(null=True)
    training = models.FloatField(null=True)
    tutor = models.BooleanField()
    tutoring = models.FloatField(null=True)

    class Meta:
        app_label = app_label
        ordering = [
            'quarter',
        ]
        unique_together = (
            ('quarter', 'professor_type', 'tutor'),
        )
        verbose_name = 'Professor evaluation weight'
        verbose_name_plural = 'Professor evaluation weights'

    def __unicode__(self):
        return u'{:s}'.format(self.professor_type)


class ProfessorInactive(models.Model):
    comment = models.CharField(max_length=256)
    professor = models.OneToOneField(
        'Professor',
        primary_key=True
    )
    quarter = models.ForeignKey('Quarter')

    class Meta:
        app_label = app_label
        ordering = [
            'professor',
        ]
        verbose_name = 'Professor inactive'
        verbose_name_plural = 'Professors inactive'

    def __unicode__(self):
        return u'{:s}'.format(self.professor)


class ProfessorType(models.Model):
    code = models.CharField(
        max_length=4,
        unique=True
    )
    name = models.CharField(
        max_length=32,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'Professor type'
        verbose_name_plural = 'Professor types'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class Quarter(models.Model):
    period = models.ForeignKey(Period)
    year = models.ForeignKey('Year')

    class Meta:
        app_label = app_label
        ordering = [
            'year',
            'period',
        ]
        unique_together = (
            ('year', 'period'),
        )

    def __unicode__(self):
        return u'{:s} {:s}'.format(
            self.year,
            self.period
        )

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False

        print self.period, other.period
        if self.period < other.period:
            return True
        elif self.period > other.period:
            return False
        else:
            return False

    def __gt__(self, other):
        return other < self


class Scholarship(models.Model):
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=6
    )
    frequency = models.ForeignKey(Frequency)
    name = models.CharField(max_length=128)
    quarter = models.ForeignKey(Quarter)

    class Meta:
        app_label = app_label
        ordering = [
            'name',
            'quarter',
        ]
        unique_together = (
            ('quarter', 'name'),
        )
        verbose_name = 'Scholarship'
        verbose_name_plural = 'Scholarships'

    def __unicode__(self):
        return u'{:s} {:s}'.format(
            self.name,
            self.quarter
        )


class Speciality(models.Model):
    knowledge_area = models.ForeignKey(KnowledgeArea)
    name = models.CharField(max_length=32)

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        unique_together = (
            ('knowledge_area', 'name'),
        )
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class State(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'State'
        verbose_name_plural = 'States'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class Student(models.Model):
    gender = models.ForeignKey(Gender)
    generation = models.ForeignKey(Generation)
    leader = models.BooleanField()
    name = models.CharField(max_length=64)
    registration_number = models.IntegerField(primary_key=True)
    scholarship = models.ManyToManyField(
        Scholarship,
        blank=True
    )
    status = models.ForeignKey('StudentStatus')

    class Meta:
        app_label = app_label
        ordering = [
            'name'
        ]
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class StudentDefinitiveDeregistration(models.Model):
    comment = models.CharField(
        blank=True,
        max_length=256
    )
    quarter = models.ForeignKey('Quarter')
    reason = models.ForeignKey('StudentDeregistrationReason')
    student = models.OneToOneField(
        'Student',
        primary_key=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'student',
            'quarter',
        ]
        verbose_name = 'Student definitive deregistration'
        verbose_name_plural = 'Student definitive deregistrations'

    def __unicode__(self):
        return u'{:s} {:s}'.format(
            self.student,
            self.quarter
        )


class StudentDeregistrationReason(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'Student deregistration reason'
        verbose_name_plural = 'Student deregistration reasons'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class StudentGraduated(models.Model):
    quarter = models.ForeignKey('Quarter')
    student = models.OneToOneField(
        'Student',
        primary_key=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'quarter',
            'student',
        ]
        verbose_name = 'Student graduated'
        verbose_name_plural = 'Students graduated'

    def __unicode__(self):
        return u'{:s} {:s}'.format(
            self.quarter,
            self.student
        )


class StudentInClassroom(models.Model):
    classroom = models.ForeignKey(Classroom)
    student = models.ForeignKey(Student)

    class Meta:
        app_label = app_label
        ordering = [
            'classroom',
            'student',
        ]
        unique_together = (
            ('classroom', 'student'),
        )
        verbose_name = 'Student in classroom'
        verbose_name_plural = 'Students in classroom'

    def __unicode__(self):
        return u'{:s} {:s}'.format(
            self.classroom,
            self.student
        )


class StudentNotRegistered(models.Model):
    quarter = models.ForeignKey('Quarter')
    student = models.OneToOneField(
        'Student',
        primary_key=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'quarter',
            'student',
        ]
        verbose_name = 'Student not registered'
        verbose_name_plural = 'Students not registered'

    def __unicode__(self):
        return u'{:s} {:s}'.format(
            self.quarter,
            self.student
        )


class StudentInTaughtSubject(models.Model):
    final_grade = models.DecimalField(
        blank=True,
        decimal_places=2,
        max_digits=4,
        null=True
    )
    first_grade = models.DecimalField(
        blank=True,
        decimal_places=2,
        max_digits=4,
        null=True
    )
    opportunity = models.ForeignKey('SubjectOpportunity')
    regular_grade = models.DecimalField(
        blank=True,
        decimal_places=2,
        max_digits=4,
        null=True
    )
    second_grade = models.DecimalField(
        blank=True,
        decimal_places=2,
        max_digits=4,
        null=True
    )
    student = models.ForeignKey(Student)
    taught_subject = models.ForeignKey('TaughtSubject')
    taught_subject_status = models.ForeignKey(
        'TaughtSubjectStatus',
        blank=True,
        null=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'taught_subject',
            'student',
        ]
        unique_together = (
            ('taught_subject', 'student'),
        )
        verbose_name = 'Student in taught subject'
        verbose_name_plural = 'Students in taught subject'

    def __unicode__(self):
        return u'{:s} {:s}'.format(
            self.taught_subject,
            self.student
        )


class StudentStatus(models.Model):
    name = models.CharField(
        max_length=16,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'Student state'
        verbose_name_plural = 'Student statuses'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class StudentTemporalDeregistration(models.Model):
    comment = models.CharField(
        blank=True,
        max_length=256
    )
    quarter = models.ForeignKey(Quarter)
    reason = models.ForeignKey(StudentDeregistrationReason)
    student = models.OneToOneField(
        Student,
        primary_key=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'student',
            'quarter',
        ]
        verbose_name = 'Student temporal deregistration'
        verbose_name_plural = 'Students temporal deregistration'

    def __unicode__(self):
        return u'{:s} {:s}'.format(
            self.student,
            self.quarter
        )


class Subject(models.Model):
    classroom_practical_hours = models.IntegerField()
    classroom_theoretical_hours = models.IntegerField()
    code = models.CharField(max_length=8)
    credits = models.IntegerField()
    curricular_axis = models.ForeignKey(CurricularAxis)
    curricular_map = models.ForeignKey(CurricularMap)
    degree = models.ForeignKey(ClassroomDegree)
    name = models.CharField(max_length=64)
    practical_hours = models.IntegerField()
    prerequisite = models.ManyToManyField(
        'self',
        blank=True
    )
    theoretical_hours = models.IntegerField()

    class Meta:
        app_label = app_label
        ordering = [
            'degree',
            'name',
        ]
        unique_together = (
            ('code', 'curricular_map', 'curricular_axis'),
        )
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class SubjectOpportunity(models.Model):
    name = models.CharField(
        max_length=16,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'Subject opportunity'
        verbose_name_plural = 'Subject opportunities'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class TaughtSubject(models.Model):
    classroom = models.ForeignKey(Classroom)
    professor = models.ForeignKey(Professor)
    student = models.ManyToManyField(
        Student,
        through=StudentInTaughtSubject
    )
    subject = models.ForeignKey(Subject)

    class Meta:
        app_label = app_label
        ordering = [
            'classroom',
            'subject',
        ]
        unique_together = (
            ('subject', 'classroom'),
        )
        verbose_name = 'Taught subject'
        verbose_name_plural = 'Taught subjects'

    def __unicode__(self):
        return u'{:s} {:s}'.format(
            self.subject,
            self.group_identifier
        )


class TaughtSubjectStatus(models.Model):
    name = models.CharField(
        max_length=16,
        unique=True
    )

    class Meta:
        app_label = app_label
        ordering = [
            'name',
        ]
        verbose_name = 'Taught subject status'
        verbose_name_plural = 'Taught subject statuses'

    def __unicode__(self):
        return u'{:s}'.format(self.name)


class Year(models.Model):
    class Meta:
        app_label = app_label
        ordering = [
            'id',
        ]
        verbose_name = 'Year'
        verbose_name_plural = 'Years'

    def __unicode__(self):
        return u'{:d}'.format(self.id)

    def __lt__(self, other):
        if self.id < other.id:
            return True
        else:
            return False