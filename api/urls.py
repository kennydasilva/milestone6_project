from django.urls import path
from api.views.notification_controller import (
    NoticationlistCreateController,
    NotificationMarkAsSentController
)

urlpatterns=[
    path('notifications/', NoticationlistCreateController.as_view()),
    path('notifications/<int:pk>/send/', NotificationMarkAsSentController.as_view()),

]