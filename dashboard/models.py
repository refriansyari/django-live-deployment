from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()

# Create your models here.
class forfile(models.Model):
    file_name = models.CharField(max_length=200)
    file_link = models.FileField(upload_to='file_list/')
    created = models.DateTimeField(editable=False, null=True)
    modified = models.DateTimeField(null=True)
    user = models.ForeignKey(
        get_user_model(), related_name='users',
        on_delete=models.CASCADE, null=True
    )

    def save (self, *args, **kwargs ):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(forfile, self).save(*args, **kwargs)


    def __str__(self):
        return self.file_name
    
    def delete(self, *args, **kwargs):
        self.file_link.delete()
        super().delete(*args, **kwargs)

