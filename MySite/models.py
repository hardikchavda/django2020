from django.db import models

# Create your models here.
city_data = [
    ('rkt','Rajkot'),
    ('amd','Ahmedabad'),
    ('sur','Surat'),
    ]

class Stud_info(models.Model):
    s_name = models.CharField(max_length=264,unique=True, verbose_name="Name")
    s_age = models.IntegerField(default=18,null=False,verbose_name="Age")
    s_city = models.CharField(default="Rajkot",choices=city_data,max_length=50,verbose_name="City")
    s_address=models.CharField(max_length=500,verbose_name="Address")
    s_phone = models.CharField(max_length=12, blank=True,null=True,verbose_name="Phone Number")

    def __str__(self):
        return self.s_name

    class Meta:
        verbose_name = "Student Information"
        verbose_name_plural = "Student's Information"

class Stud_marks(models.Model):
    s_info  = models.ForeignKey("Stud_info") 
    s_marks1 = models.IntegerField(null=False,verbose_name="Django",default=0)
    s_marks2 = models.IntegerField(null=False,verbose_name="Ionic",default=0)
    s_marks3 = models.IntegerField(null=False,verbose_name="Hadoop",default=0)
    s_total = models.IntegerField(null=False,verbose_name="Total",default=0)
    s_per = models.FloatField(null=False,verbose_name="Percentage",default=0)    

    def __str__(self):
        return "Marks Table"

    class Meta:
         verbose_name = "Student Result"
         verbose_name_plural = "Student's Result"    
