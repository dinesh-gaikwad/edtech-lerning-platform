from django.db import models
from django.contrib.auth.models import User
from academy.models import Course

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_id = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.user.email} - {self.course.title}"