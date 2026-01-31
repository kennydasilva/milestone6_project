from api.models import Notification

class NotificationService:

    @staticmethod
    def create_notification(data):
        return Notification.objects.create(**data)
    

    @staticmethod
    def list_notifications(filters=None):
        qs=Notification.objects.all()
        if filters:
            qs=qs.filter(**filters)
        return qs
    
    @staticmethod
    def mark_as_sent(notification_id):
        notification=Notification.objects.get(id=notification_id)
        notification.is_sent=True
        notification.save()
        return notification