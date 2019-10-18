from django.contrib import admin
from .models import Post
#admin.site.register(Post)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields=[
        'title',
        'user_name',
        'slug',
        'email',
        'phone',
        'publish', 
        'publish_date',
        'updated','timestemp','age'
        
    ]
    readonly_fields=['updated','timestemp','age']

    def age(self,obj,*args,**kwargs):
        return str(obj.age())
    class Meta:
        model=Post

admin.site.register(Post,PostAdmin)