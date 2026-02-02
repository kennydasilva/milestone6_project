from api.models import Notification

class NotificationService:

    @staticmethod
    def create_notification(data):

        try:

            return Notification.objects.create(**data)
        except e:
            raise Exception("Error: {e}")
        
    
    

    @staticmethod
    def list_notifications(filters=None):

        try:
            qs=Notification.objects.all()
            if filters:
                qs=qs.filter(**filters)
            return qs
        
        except e:
            raise Exception("Error: {e}")
    
    
    @staticmethod
    def mark_as_sent(notification_id):
        try:
            notification=Notification.objects.get(id=notification_id)
            notification.is_sent=True
            notification.save()
            return notification
        
        except objectDoesNotExist:
            return None
        


    @staticmethod
    def remove_notifications(notification_id):
        try:
            notification=Notification.objects.get(id=notification_id)
            notification.delete()
            return True

        except objectDoesNotExist:
            return False


    @staticmethod
    def update(notification_id, data):
        try:
            notification=Notification.objects.get(id=notification_id)

        except objectDoesNotExist:
            return None
        
        for field, value in data.items():
            setattr(Notification, field, value)

        notification.save()
        return notification
        