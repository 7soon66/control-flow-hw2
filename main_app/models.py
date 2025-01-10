from django.db import models
from django.urls import reverse
# Create your models here.


MEALS=(
    ('B',"Breakfast"),
    ('L','Lunch'),
    ('D','Dinner')
)

#if you want to access meals MEALS[0][0]

class Donkey(models.Model):
    name=models.CharField(max_length=100)
    breed=models.CharField(max_length=100)
    describtion = models.TextField(max_length=250)
    age = models.IntegerField()
    # image = models.CharField(default=None, blank=True, null=True, max_length=2000)

    image=models.ImageField(upload_to='main_app/static/upload/',default="")


    def get_absolute_url(self):
        return reverse("detail", kwargs={"donkey_id": self.id})
    
    def __str__(self):
        return self.name

class Feeding(models.Model):
    date=models.DateField()
    meal =models.CharField(max_length=1,choices=MEALS,default=MEALS[0][0])
    donkey=models.ForeignKey(Donkey, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.donkey.name} {self.get_meal_display()} on {self.date}"