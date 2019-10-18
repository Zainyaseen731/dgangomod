from django.db import models
from django.db.models.signals import post_save,pre_save
from .validator import valid_email
from django.utils.text import slugify
from django.utils.timesince import timesince
from datetime import timedelta,datetime,date 
#import datetime
#from django.utils import timezone

PUBLISH_CHOICES=( 
    ('draft','Draft'),
    ('public','Public'),
    ('private','Private'),
    ('publish','Publish')
)
class Post(models.Model):
    id=models.BigAutoField(primary_key=True)
    
    title=models.CharField(max_length=240,default="hay")
    user_name=models.CharField(max_length=30,default="zain")
    email=models.CharField(max_length=40,default="zain@gmail.com")
    slug=models.SlugField(null=True,blank=True)
    phone=models.IntegerField(null=True)
    context=models.TextField(null=True,blank=True)
    publish=models.CharField(max_length=120,choices=PUBLISH_CHOICES,default='draft')
    view_count=models.IntegerField(default=0)
    publish_date=models.DateField(auto_now=False,auto_now_add=False)
    auther_email=models.CharField(max_length=240,validators=[valid_email],null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    timestemp=models.DateTimeField(auto_now_add=True)

    #def save(self,*args,**kwargs):
       # if not self.slug:
         #  self.slug=slugify(self.title)
        #super(Post,self).save(*args,**kwargs)

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
    

    def __unicode__(self):
        return (self.user_name)

    def __str__(self):
        return (self.user_name)

    def age(self):
        if self.publish=='publish':
            now=datetime.now()
            publish_time=datetime.combine(
                         self.publish_date,
                         datetime.now().min.time()
                     )
            try:
                difference=now-publish_time
            except:
                return "Unknown"
            if difference <=timedelta(minutes=1):
                return "Just now"
            return '{time} ago'.format(time=timesince(publish_time).split(",")[0])
        return "Not published"



def pre_save_receiver(sender,instance,*args,**kwargs):
    print("before save")
    if not instance.slug:
        instance.slug=slugify(instance.title)
pre_save.connect(pre_save_receiver,sender=Post)

def post_save_receiver(sender,instance,created,*args,**kwargs):
    print("after save")
    if not instance.slug:
        instance.slug=slugify(instance.title)
        instance.save()
post_save.connect(post_save_receiver,sender=Post)