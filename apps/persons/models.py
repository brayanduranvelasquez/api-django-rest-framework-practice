from django.db import models

class PersonModel(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.IntegerField()
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, default="Male")
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name