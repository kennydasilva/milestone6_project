from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.services.notification_service import NotificationService
from api.serializers.notification_dto import (
    NotificationCreateDTO,
    NotifictionResponseDTO,
    NotificationUpdateDTO

)

from drf_yasg.utils import swagger_auto_schema


class NotificationListCreateController(APIView):

    @swagger_auto_schema(
        request_body=NotificationCreateDTO,
        responses={201: NotifictionResponseDTO}
    )
    def post(self, request, *args, **kwargs):
        dto = NotificationCreateDTO(data=request.data)
        dto.is_valid(raise_exception=True)

        notification = NotificationService.create_notification(dto.validated_data)
        serializer = NotifictionResponseDTO(notification)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: NotifictionResponseDTO(many=True)}
    )
    def get(self, request, *args, **kwargs):
        notifications = NotificationService.list_notifications()
        serializer = NotifictionResponseDTO(notifications, many=True)
        return Response(serializer.data)


class NotificationUpdateDeleteController(APIView):

    @swagger_auto_schema(
        request_body=NotificationUpdateDTO,
        responses={200: NotifictionResponseDTO}
    )
    def patch(self, request, id, *args, **kwargs):
        dto = NotificationUpdateDTO(data=request.data)
        dto.is_valid(raise_exception=True)

        notification = NotificationService.update(id, dto.validated_data)

        if not notification:
            return Response(
                {"detail": "Notification not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = NotifictionResponseDTO(notification)
        return Response(serializer.data)

    @swagger_auto_schema(responses={204: "No Content"})
    def delete(self, request, id, *args, **kwargs):
        deleted = NotificationService.remove_notifications(id)

        if not deleted:
            return Response(
                {"detail": "Notification not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(status=status.HTTP_204_NO_CONTENT)



class NotificationMarkAsSentController(APIView):

    @swagger_auto_schema(
        responses={200: NotifictionResponseDTO}
    )
    def patch(self, request, id, *args, **kwargs):
        notification = NotificationService.mark_as_sent(id)

        if not notification:
            return Response(
                {"detail": "Notification not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = NotifictionResponseDTO(notification)
        return Response(serializer.data)
