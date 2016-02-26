from django.contrib import admin

from models import *


class CareerAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
    )
admin.site.register(Career, CareerAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(City, CityAdmin)


class ClassroomAdmin(admin.ModelAdmin):
    list_display = (
        'career',
        'quarter',
        'degree',
        'identifier',
        'leader',
        'tutor',
    )
admin.site.register(Classroom, ClassroomAdmin)


class ClassroomDegreeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )
admin.site.register(ClassroomDegree, ClassroomDegreeAdmin)


class ClassroomIdentifierAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(ClassroomIdentifier, ClassroomIdentifierAdmin)


class CurricularAxisAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
    )
admin.site.register(CurricularAxis, CurricularAxisAdmin)


class CurricularMapAdmin(admin.ModelAdmin):
    list_display = (
        'career',
        'year',
    )
admin.site.register(CurricularMap, CurricularMapAdmin)


class GenderAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
    )
admin.site.register(Gender, GenderAdmin)


class MonthAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(Month, MonthAdmin)


class PeriodAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'start',
        'end',
    )
admin.site.register(Period, PeriodAdmin)


class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type',
        'email',
        'phone',
    )
admin.site.register(Professor, ProfessorAdmin)


class ProfessorTypeAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
    )
admin.site.register(ProfessorType, ProfessorTypeAdmin)


class QuarterAdmin(admin.ModelAdmin):
    list_display = (
        'period',
        'year',
    )
admin.site.register(Quarter, QuarterAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(State, StateAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'registration_number',
        'name',
        'status',
        'generation',
    )
admin.site.register(Student, StudentAdmin)


class StudentStatusAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(StudentStatus, StudentStatusAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'curricular_axis',
        'degree',
    )
admin.site.register(Subject, SubjectAdmin)


class TaughtSubjectAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'classroom',
        'professor',
    )
admin.site.register(TaughtSubject, TaughtSubjectAdmin)


class YearAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )
admin.site.register(Year, YearAdmin)