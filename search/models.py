from django.db import models

from django.db.models import Q

class data(models.Model):
    chapter = models.CharField(max_length=50, default="")
    chapter_name = models.CharField(max_length=250, default="")
    section = models.CharField(max_length=10, default="")
    section_name = models.CharField(max_length=350, default="")
    description = models.TextField(default="")

    class Meta:
      verbose_name_plural = "IPC Sections"

    def __str__(self):
        return self.chapter
        return self.chapter_name
        return self.section
        return self.section_name
        return self.description