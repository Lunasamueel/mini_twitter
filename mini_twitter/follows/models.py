from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Follow(models.Model):
    following = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name="follower", on_delete=models.CASCADE)
    created_id = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('following', 'follower')

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
    


    