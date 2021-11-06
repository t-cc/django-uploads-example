from django.db import models


def username(instance, file):
    string_username = str(instance).split()[0]
    return f"profiles/{string_username}/{file}"


class FileUploadModel(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(
        default="profiles/profile.jpg",
        upload_to=username,
        blank=True
    )

    def __unicode__(self):
        return self.name
