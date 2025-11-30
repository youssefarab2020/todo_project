from django.db import models as m

# Create your models here.
class Task(m.Model):
    title=m.CharField(max_length=200)
    complete=m.BooleanField(default=False)
    created=m.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title