from django.urls import path
from api.views.notification_controller import (
    NotificationListCreateController,
    NotificationUpdateDeleteController,
    NotificationMarkAsSentController
)

urlpatterns = [
    path('notifications/', NotificationListCreateController.as_view()),
    path('notifications/<int:id>/', NotificationUpdateDeleteController.as_view()),
    path('notifications/<int:id>/send/', NotificationMarkAsSentController.as_view()),
]
