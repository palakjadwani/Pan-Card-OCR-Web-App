from django.db import models
from .views import ocr_core

class Image(models.Model):
    image = models.ImageField()
    image_type = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        is_new = True if not self.pk else False
        super().save(*args, **kwargs)
        if is_new:
            info = ImageInfo()
            ocr_core(self.image, info)

class ImageInfo(models.Model):
    image_id = models.IntegerField()
    name = models.CharField(max_length=20, null=True)
    fname = models.CharField(max_length=20, null=True)
    dob = models.CharField(max_length=20, null=True)
    pan = models.CharField(max_length=20, null=True)
    # sign = models.ImageField()
    # pic = models.ImageField()
