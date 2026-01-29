from django.db import models

class Notification(models.Model):
    title=models.CharField(max_length=255)
    message=models.TextField()
    email= models.EmailField()
    is_sent=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=['-created_at']
    
    def __str__(self):
        return self.title