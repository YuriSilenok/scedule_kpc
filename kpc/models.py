'''Модели для приложения'''

from django.db.models import Model, ForeignKey, CASCADE, \
    CharField, IntegerField, DateField
from django.contrib.auth.models import User


class Teacher(Model):
    '''Преподаватель'''
    user = ForeignKey(User, on_delete=CASCADE)

class Discipline(Model):
    """Дисциплина"""
    name = CharField(max_length=100)

class Auditorium(Model):
    """Аудитория"""
    name = CharField(max_length=5)

class Group(Model):
    """Группа"""
    name = CharField(max_length=10)

class Pair(Model):
    """Пара"""
    number = IntegerField()


class LessonStatus(Model):
    """Статус занятия: Предложено, Утверждено
    Заполняется командой `python manage.py loaddata static_data`"""
    name = CharField(max_length=10)


class Lesson(Model):
    """Занятие"""
    discipline = ForeignKey(Discipline, on_delete=CASCADE)
    teacher = ForeignKey(Teacher, on_delete=CASCADE)
    auditorium = ForeignKey(Auditorium, on_delete=CASCADE)
    group = ForeignKey(Group, on_delete=CASCADE)
    para = ForeignKey(Pair, on_delete=CASCADE)
    lesson_status = ForeignKey(LessonStatus, on_delete=CASCADE)
    date = DateField()
