from django.urls import path
from .views import *

urlpatterns = [
    path('', view_plg_intro, name="plg-intro"),
    path('info/', view_plg_info, name="plg-info"),
    path('qna/', view_plg_qna, name="plg-qna"),
    path('qna-last/', view_plg_qna_last, name="plg-qna-last"),
    path('choice/', view_plg_choice, name="plg-choice"),
    path('room/', view_plg_room, name="plg-room"),
    path('mentor-rooms/<int:pk>/', MentorRoomDetailView.as_view(), name='mentor-room-detail'),
    path('mentor-rooms/match/', MentorRoomMatchView.as_view(), name='mentor-room-match'),
    path('questions/<int:order>/', QuestionDetailView.as_view(), name='question-detail'),
    path('answer/', AnswerCreateUpdateView.as_view(), name='answer-edit'),
    path('mentoring/', mentoring, name='mentee-create'),
]
  