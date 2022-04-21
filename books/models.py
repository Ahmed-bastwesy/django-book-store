from django.db import models

# Create your models here.
class Author (models.Model):
        name=models.CharField(max_length=250)

        def __str__(self):
            return self.name

class Book(models.Model):
    name=models.CharField(max_length=250)
    publish_date=models.DateField(null=True)
    add_to_site=models.DateTimeField(auto_now_add=True)
    Author=models.ForeignKey(Author , on_delete=models.CASCADE)
    price=models.FloatField()
    appropriate=models.CharField(max_length=100, choices=[("child","under 8"),("between","8-15"),("adult","adults")],default="adult")
    image=models.FileField(default='default.jpg', upload_to='static/images')

    def __str__(self):
        return self.name

