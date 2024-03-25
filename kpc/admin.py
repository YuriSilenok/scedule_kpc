'''Админка'''

from django.contrib import admin
from .models import Teacher, Discipline, Auditorium, Group, Pair, \
    LessonStatus, Lesson

admin.site.register([Teacher, Discipline, Auditorium, Group, Pair, LessonStatus, Lesson])
