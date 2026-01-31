from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.services.notification_service import NotificationService
from api.serializers.notification_dto import(
    NotificationCreateDTO,
    NotifictionResponseDTO
)


class NoticationlistCreateController(APIView):

    def get(self, request):
        notifications=NotificationService.list_notifications()
        serializer=NotifictionResponseDTO(notifications, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        dto=NotificationCreateDTO(data=request.data)
        dto.is_valid(raise_exception=True)

        notification=NotificationService.create_notification(dto.validated_data)
        response =NotifictionResponseDTO(notification)

        return Response(response.data, status=status.HTTP_201_CREATED)