"""Представления"""

from django.shortcuts import render
from rest_framework import generics
from .serializers import LessonSerializer
from .models import Lesson, Group, Teacher, Auditorium


def schedule_view(request):
    # Get all lessons initially
    lessons = Lesson.objects.all()

    # Retrieve distinct groups, teachers, and auditoriums for dropdown options
    groups = Group.objects.all()
    teachers = Teacher.objects.select_related('user').all()
    auditoriums = Auditorium.objects.all()

    # Filter lessons based on selected options in dropdown menus
    group_filter = request.GET.get('group_filter')
    if group_filter:
        lessons = lessons.filter(group_id=group_filter)

    teacher_filter = request.GET.get('teacher_filter')
    if teacher_filter:
        lessons = lessons.filter(teacher_id=teacher_filter)

    auditorium_filter = request.GET.get('auditorium_filter')
    if auditorium_filter:
        lessons = lessons.filter(auditorium_id=auditorium_filter)

    # Pass filtered lessons along with dropdown options to the template
    context = {
        'lessons': lessons,
        'groups': groups,
        'teachers': teachers,
        'auditoriums': auditoriums,
    }

    return render(request, 'schedule.html', context)


class LessonListByGroup(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        return Lesson.objects.filter(group_id=group_id)
