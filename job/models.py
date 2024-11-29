from django.db import models
from django.contrib.auth.models import User
import datetime
from tinymce.models import HTMLField
# Create your models here.

class studentuser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='studentuser')
    mobile=models.CharField(max_length=15,null=True)
    image=models.ImageField(null=True,upload_to='profile_pic')
    resume=models.FileField(null=True,upload_to='Profile_pic')
    gender=models.CharField(max_length=10,null=True)
    type=models.CharField(max_length=15,null=True)
    email=models.EmailField(max_length=100,null=True)

    def _str_(self):
        return self.user.username
    




class news(models.Model):
    news_title=models.TextField(max_length=100,blank=False)
    news_dec=HTMLField()


class userpost(models.Model):
    id=models.AutoField(primary_key=True)
    jobdiscription=models.TextField(blank=False)
    jobtitle=models.TextField(max_length=200,blank=False)
    userid=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    created=models.DateTimeField(auto_now_add=True,blank=True)
    update=models.DateTimeField(auto_now=True,blank=True)
    # companylogo=models.ImageField(blank=True,null=True)
    vacancies=models.TextField(blank=False)
    experience=models.TextField(blank=False)
    jobmode=models.TextField(blank=False)
    minsalary=models.TextField(blank=False)
    maxsalary=models.TextField(blank=False)
    applybefor=models.TextField(blank=False)
    qualification=models.TextField(blank=False)
    skill=models.TextField(blank=False)
    location=models.TextField(blank=False)
    
    # companyname=models.CharField(max_length=10,null=True)
    # industry=models.CharField(max_length=10,null=True)
    # address=models.CharField(max_length=1000,null=True)
    # landlinephone=models.CharField(max_length=15,null=True)
    # cellphone=models.CharField(max_length=15,null=True)
    # companywebsite=models.CharField(max_length=1000,null=True)
    # companydescription=models.CharField(max_length=1000,null=True)
    


    def __str__(self):
        return f"{str(self.jobtitle)}"
class clinteragister(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='clinteuser')
    email=models.EmailField(max_length=150,null=True)
    mobile=models.CharField(max_length=15,null=True)
    image=models.ImageField(null=True,upload_to='profile_pic_clinte')
    gender=models.CharField(max_length=10,null=True)
    type=models.CharField(max_length=15,null=True)
    companyname=models.CharField(max_length=10,null=True)
    industry=models.CharField(max_length=10,null=True)
    orgtype=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=1000,null=True)
    location=models.CharField(max_length=10,null=True)
    landlinephone=models.CharField(max_length=15,null=True)
    cellphone=models.CharField(max_length=15,null=True)
    companywebsite=models.CharField(max_length=1000,null=True)
    noofemployees=models.CharField(max_length=100,null=True)
    companydescription=models.CharField(max_length=1000,null=True)
    companylogo=models.FileField(null=True,upload_to='company_logo_clinte')

    def _str_(self):
        return f"{str(self.email)}"
class recruitment(models.Model):
    resume=models.FileField(null=True,upload_to='recruiter_resume')
    recruituser=models.ForeignKey(userpost, on_delete=models.CASCADE,related_name='recruter')

class userpostreplay(models.Model):
    id=models.AutoField(primary_key=True)
    post = models.ForeignKey(User, on_delete=models.CASCADE,related_name='jobreplay' )
    candidatename= models.CharField(max_length=100,null=True)
    jobtitle= models.CharField(max_length=100,null=True)
    created=models.DateTimeField(auto_now_add=True,blank=True)
    resume=models.FileField(null=True,upload_to='jobapply')
    email= models.CharField(max_length=100,null=True)
    contact= models.CharField(max_length=100,null=True)

    # def __str__(self):
    #     return f"{str(self.jobtitle,self.candidatename)}"
    
    
    def _sjr_(self):
        return f"{str(self.jobtitle,self.candidatename)}"

   