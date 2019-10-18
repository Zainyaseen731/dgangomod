from django.urls import path
#from .views import list_view
from .views import register
urlpatterns = [
   # path('admin/', admin.site.urls),
    #path('',list_view,name='list_view'),
    path('',register,name='register')
]
