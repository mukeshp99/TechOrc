from django.db import models

class BearerToken(models.Model):
    token = models.CharField(max_length=255)
    user_id = models.IntegerField()
    issued_at = models.DateTimeField(auto_now_add=True)

    