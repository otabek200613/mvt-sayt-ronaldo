from django.contrib.auth.models import User
from django.db import models




class Home(models.Model):
    page_title = models.CharField(max_length=200,verbose_name="Page Title")
    first_letter = models.CharField(max_length=1,verbose_name="First letter of name",default="",null=True,blank=True)
    last_part= models.CharField(max_length=10,verbose_name="Last part of name",default="",null=True,blank=True)
    name = models.CharField(max_length=200,verbose_name="Name")
    is_active = models.BooleanField(default=True,verbose_name="Active")
    def __str__(self):
        return self.name
class Home_job(models.Model):
    owner = models.ForeignKey(Home,on_delete=models.CASCADE)
    job = models.CharField(max_length=200,verbose_name="Job")
    def __str__(self):
        return self.job


class About(models.Model):
    photo = models.ImageField(verbose_name="Photo",upload_to='photos/')
    description = models.TextField(verbose_name="Description")
    full_name = models.CharField(max_length=200,verbose_name="Full name")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    address = models.CharField(max_length=200,verbose_name="Address")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=200,verbose_name="Phone Number")
    project_count = models.IntegerField(verbose_name="Project Count")
    cv_url = models.URLField(verbose_name="CV URL",null=True,blank=True)
    is_active = models.BooleanField(default=True,verbose_name="Is active ?")
    def __str__(self):
        return self.full_name


class Resume_education(models.Model):
    date = models.CharField(max_length=100, verbose_name="Date of Education eg. 2014-2015")
    degree = models.CharField(max_length=200, verbose_name="Degree of Education")
    university = models.CharField(max_length=200, verbose_name="University of Education")
    description = models.TextField(verbose_name="Description for education")
    is_active = models.BooleanField(default=True, verbose_name="Is active ?")

    def __str__(self):
        return self.degree

    class Meta:
        verbose_name_plural = "Resume Education"
        ordering = ['-id']

class Resume_experience(models.Model):
    date = models.CharField(verbose_name="Date of Experience eg. 2014-2015")
    job = models.CharField(max_length=200,verbose_name="Job")
    company = models.CharField(max_length=200,verbose_name="Company")
    description = models.TextField(verbose_name="Description for experience")
    is_active = models.BooleanField(default=True,verbose_name="Is active ?")

    def __str__(self):
        return self.job
class Resume_skill(models.Model):
    title = models.CharField(max_length=200,verbose_name="Name of skill")
    percentage = models.IntegerField(verbose_name="Percentage of skill")
    is_active = models.BooleanField(default=True,verbose_name="Is active ?")

    def __str__(self):
        return self.title
class Resume_skill2(models.Model):
    title = models.CharField(max_length=200,verbose_name="Name of skill")
    percentage = models.IntegerField(verbose_name="Percentage of skill")
    is_active = models.BooleanField(default=True,verbose_name="Is active ?")

    def __str__(self):
        return self.title

class Resume_awards(models.Model):
    date = models.CharField(verbose_name="Date of Award eg. 2014-2015")
    award = models.CharField(max_length=200,verbose_name="Job")
    company = models.CharField(max_length=200,verbose_name="Company")
    description = models.TextField(verbose_name="Description for Award")
    is_active = models.BooleanField(default=True,verbose_name="Is active ?")
    def __str__(self):
        return self.award



class Service(models.Model):
    photo = models.ImageField(verbose_name="Photo",upload_to='photos/',null=True,blank=True)
    title = models.CharField(max_length=200,verbose_name="Title of Service")
    description = models.TextField(verbose_name="Description for Service")
    is_active = models.BooleanField(default=True,verbose_name="Is active ?")
    def __str__(self):
        return self.title

class Project(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name="Photo",upload_to='photos/',null=True,blank=True)
    title = models.CharField(max_length=200,verbose_name="Title of Project")



class ProjectsList(models.Model):
    awards = models.IntegerField(verbose_name="Awards")
    complete_projects = models.IntegerField(verbose_name="Complete projects")
    happy_clients = models.IntegerField(verbose_name="Happy clients")
    cups_of_coffe = models.IntegerField(verbose_name="Cups of coffe")
    is_active = models.BooleanField(default=True,verbose_name="Is active ?")











class Contact_me(models.Model):
    adress = models.CharField(max_length=200,verbose_name="Adress")
    number = models.CharField(max_length=200,verbose_name="Number")
    email = models.EmailField(verbose_name="Email")
    website = models.URLField(verbose_name="Website")
    website_url = models.URLField(verbose_name="Website URL",null=True,blank=True)
    is_active = models.BooleanField(default=True,verbose_name="Is active ?")







class Contact(models.Model):
    name = models.CharField(max_length=200,verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200,verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    is_read = models.BooleanField(default=False,verbose_name="Is read?")
    updated_date = models.DateTimeField(auto_now=True,verbose_name="Updated time")
    def __str__(self):
        return self.name




class Blog(models.Model):

    photo = models.ImageField(verbose_name="Photo",upload_to='photos/',null=True,blank=True)
    title = models.CharField(max_length=200,verbose_name="Title")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Created at")
    body = models.TextField(verbose_name="Body")
    is_active = models.BooleanField(default=True,verbose_name="Is active ?")

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,verbose_name="Blog", related_name='comments')
    full_name = models.CharField(max_length=200,verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Created at")
    is_active = models.BooleanField(default=False,verbose_name="Is active?")
    def __str__(self):
        return self.full_name


class Footer(models.Model):
    twitter = models.URLField(verbose_name="Twitter")
    facebook = models.URLField(verbose_name="Facebook")
    instagram = models.URLField(verbose_name="Instagram")
    adress = models.CharField(max_length=200,verbose_name="Adress")
    phone_number = models.CharField(max_length=200,verbose_name="Phone number")
    email = models.EmailField(verbose_name="Email")
    is_active = models.BooleanField(default=True,verbose_name="Is active ?")

























