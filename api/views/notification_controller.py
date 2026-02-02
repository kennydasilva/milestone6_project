from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from api.services.notification_service import NotificationService
from api.serializers.notification_dto import(
    NotificationCreateDTO,
    NotifictionResponseDTO,
    NotificationUpdateDTO
)
from drf_yasg.utils import swagger_auto_schema


class NoticationlistCreateController(APIView):
    
    @swagger_auto_schema(
            request_body=NotificationCreateDTO,
            responses={201: NotifictionResponseDTO}
    )
    def post(self, request):
        dto=NotificationCreateDTO(data=request.data)
        dto.is_valid(raise_exception=True)

        notification=NotificationService.create_notification(dto.validated_data)
        response =NotifictionResponseDTO(notification)

        return Response(response.data, status=status.HTTP_201_CREATED)
    

    @swagger_auto_schema(
            request_body=NotificationCreateDTO,
            responses={201: NotifictionResponseDTO}
    )
    def get(self, request):
        notifications=NotificationService.list_notifications()
        serializer=NotifictionResponseDTO(notifications, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(responses={204: "No Content"})  
    def delete(self, request, id):
        notifiction=NotificationService.remove_notifications(id)
        serializer=NotifictionResponseDTO(notifiction)
        return Response(serializer.data)
    
    @swagger_auto_schema(
            request_body=NotificationUpdateDTO,
            responses={200: NotifictionResponseDTO}
    ) 
    def patch(self, request, id):
        dto=NotificationUpdateDTO(data=request.data)
        dto.is_valid(raise_exception=True)

        notification=NotificationService.update(id, dto.validated_data)

        if not notification:
            return Response(
                {"detail": "Notification not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        Response=NotifictionResponseDTO(notification)
        return Response(Response.data)
    
    


class NotificationMarkAsSentController(APIView):


    @swagger_auto_schema(
            
            responses={200: NotifictionResponseDTO}
    ) 
    def patch(self, request, id):
        notifiction=NotificationService.mark_as_sent(id)
        serializer=NotifictionResponseDTO(notifiction)
        return Response(serializer.data)