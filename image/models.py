from django.db import models
from PIL import Image


class ImageSave(models.Model):
    """
    При заполнении модели имеется возможноть личной оптимизации изображения,
    также имеется значение по умолчанию
    """
    height = models.PositiveIntegerField(default=800, blank=True)
    width = models.PositiveIntegerField(default=400, blank=True)
    image = models.ImageField(upload_to='files', max_length=100)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > self.height or img.width > self.width:
            output_size = (self.height, self.width)
            img.thumbnail(output_size)
            img.save(self.image.path)
