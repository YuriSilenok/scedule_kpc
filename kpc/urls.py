'''привязка url и методов'''

from django.urls import path
from . import views

urlpatterns = [
    path('schedule/', views.schedule_view, name='schedule_view'),
    path('api/schedule/group/<int:group_id>/', views.LessonListByGroup.as_view(), name='lesson-list-by-group'),
]
