from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# 나머지 모델 정의는 동일하게 유지합니다.
class Help(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    email = models.TextField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

