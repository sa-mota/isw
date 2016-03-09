"""isw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

import coordination.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^isw/$', TemplateView.as_view(template_name='isw.html'), name='isw'),

    url(r'^isw/calls/logo/$', TemplateView.as_view(template_name='isw/calls/logo.html'), name='isw-calls-logo'),
    url(r'^isw/calls/2016/development-contest-ea/$', TemplateView.as_view(template_name='isw/calls/2016/development-contest-ea.html'), name='isw-calls-2016-development-contest-ea'),

    url(r'^sicpe/delete/career/(?P<pk>\d+)/$', coordination.views.DeleteCareerView.as_view(), name='careers-delete'),
    url(r'^sicpe/delete/classroom/(?P<pk>\d+)/$', coordination.views.DeleteClassroomView.as_view(), name='classrooms-delete'),
    url(r'^sicpe/delete/generation/(?P<pk>\d+)/$', coordination.views.DeleteGenerationView.as_view(), name='generations-delete'),
    url(r'^sicpe/delete/professor/(?P<pk>\d+)/$', coordination.views.DeleteProfessorView.as_view(), name='professors-delete'),
    url(r'^sicpe/delete/student/(?P<pk>\d+)/$', coordination.views.DeleteStudentView.as_view(), name='students-delete'),
    url(r'^sicpe/delete/student-in-taught-subject/(?P<pk>\d+)/$', coordination.views.DeleteStudentInTaughtSubjectView.as_view(), name='student-in-taught-subjects-delete'),

    url(r'^sicpe/detail/career/(?P<pk>\d+)/$', coordination.views.CareerView.as_view(), name='careers-view',),
    url(r'^sicpe/detail/classroom/(?P<pk>\d+)/$', coordination.views.ClassroomView.as_view(), name='classrooms-view',),
    url(r'^sicpe/detail/generation/(?P<pk>\d+)/$', coordination.views.GenerationView.as_view(), name='generations-view',),
    url(r'^sicpe/detail/professor/(?P<pk>\d+)/$', coordination.views.ProfessorView.as_view(), name='professors-view',),
    url(r'^sicpe/detail/student/(?P<pk>\d+)/$', coordination.views.StudentView.as_view(), name='students-view',),
    url(r'^sicpe/detail/student-in-taught-subject/(?P<pk>\d+)/$', coordination.views.StudentInTaughtSubjectView.as_view(), name='student-in-taught-subjects-view',),

    url(r'^sicpe/new/career/$', coordination.views.CreateCareerView.as_view(), name='careers-new',),
    url(r'^sicpe/new/classroom/$', coordination.views.CreateClassroomView.as_view(), name='classrooms-new',),
    url(r'^sicpe/new/generation/$', coordination.views.CreateGenerationView.as_view(), name='generations-new',),
    url(r'^sicpe/new/professor/$', coordination.views.CreateProfessorView.as_view(), name='professors-new',),
    url(r'^sicpe/new/student/$', coordination.views.CreateStudentView.as_view(), name='students-new',),
    url(r'^sicpe/new/student-in-taught-subject/$', coordination.views.CreateStudentInTaughtSubjectView.as_view(), name='student-in-taught-subjects-new',),

    url(r'^sicpe/list/career/$', coordination.views.ListCareerView.as_view(), name='careers-list',),
    url(r'^sicpe/list/classroom/$', coordination.views.ListClassroomView.as_view(), name='classrooms-list',),
    url(r'^sicpe/list/generation/$', coordination.views.ListGenerationView.as_view(), name='generations-list',),
    url(r'^sicpe/list/professor/$', coordination.views.ListProfessorView.as_view(), name='professors-list',),
    url(r'^sicpe/list/student/$', coordination.views.ListStudentView.as_view(), name='students-list',),
    url(r'^sicpe/list/student-in-taught-subject/$', coordination.views.ListStudentInTaughtSubjectView.as_view(), name='student-in-taught-subjects-list',),

    url(r'^sicpe/edit/career/(?P<pk>\d+)/$', coordination.views.UpdateCareerView.as_view(), name='careers-edit',),
    url(r'^sicpe/edit/classroom/(?P<pk>\d+)/$', coordination.views.UpdateClassroomView.as_view(), name='classrooms-edit',),
    url(r'^sicpe/edit/generation/(?P<pk>\d+)/$', coordination.views.UpdateGenerationView.as_view(), name='generations-edit',),
    url(r'^sicpe/edit/professor/(?P<pk>\d+)/$', coordination.views.UpdateProfessorView.as_view(), name='professors-edit',),
    url(r'^sicpe/edit/student/(?P<pk>\d+)/$', coordination.views.UpdateStudentView.as_view(), name='students-edit',),
    url(r'^sicpe/edit/student-in-taught-subject/(?P<pk>\d+)/$', coordination.views.UpdateStudentInTaughtSubjectView.as_view(), name='student-in-taught-subjects-edit',),
]
