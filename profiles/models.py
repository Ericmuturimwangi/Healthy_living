from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from djrichtextfield.models import RichTextField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Profile(models.Model):
    user = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, max_length=255)  # Add this field
    image = ProcessedImageField(
        processors=[ResizeToFill(300, 300)],
        format="WEBP",
        options={"quality": 75},
        upload_to="profiles/",
        blank=False,
    )
    bio = RichTextField(max_length=2500, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)  # Generate slug from username
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user.username)
