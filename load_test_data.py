'''заполнение тестовыми данными'''

import random
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from faker import Faker
from kpc.models import Teacher, Discipline, Auditorium, Group, Pair, LessonStatus, Lesson

fake = Faker()

# Создание учителей
for _ in range(5):
    user = User.objects.create(username=fake.user_name())
    teacher = Teacher.objects.create(user=user)

# Создание дисциплин
disciplines_names = ['Математика', 'Физика', 'Литература', 'История', 'Иностранный язык']
for name in disciplines_names:
    Discipline.objects.create(name=name)

# Создание аудиторий
for i in range(1, 6):
    Auditorium.objects.create(name=f'A{i}')

# Создание групп
for i in range(1, 11):
    Group.objects.create(name=f'Group-{i}')

# Создание пар
for i in range(1, 6):
    Pair.objects.create(number=i)

# Создание статусов занятия
LessonStatus.objects.create(name='Предложено')
LessonStatus.objects.create(name='Утверждено')

# Создание занятий
for _ in range(10):
    teacher = random.choice(Teacher.objects.all())
    discipline = random.choice(Discipline.objects.all())
    auditorium = random.choice(Auditorium.objects.all())
    group = random.choice(Group.objects.all())
    pair = random.choice(Pair.objects.all())
    status = random.choice(LessonStatus.objects.all())
    date = datetime.now() + timedelta(days=random.randint(1, 30))
    
    lesson = Lesson.objects.create(
        teacher=teacher,
        discipline=discipline,
        auditorium=auditorium,
        group=group,
        para=pair,
        lesson_status=status,
        date=date
    )

print("Данные заполнены успешно!")
