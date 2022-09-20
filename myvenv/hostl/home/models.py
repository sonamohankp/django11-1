from distutils.command.upload import upload
from django.db import models

class Department(models.Model):
    depart_name=models.CharField(max_length=100, null=True, blank=True)
    depart_desps=models.TextField(null=True, blank=True)
    def __str__(self):
        return  self.depart_name
class doctors(models.Model):
    doc_name=models.CharField(max_length=100,null=True, blank=True)
    doc_spec=models.CharField(max_length=100,null=True, blank=True)
    depart_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')
    def __str__(self):
        return 'DR '+ self.doc_name+'-('+self.doc_spec+')'
         
class booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_phone=models.CharField(max_length=100)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
      