from django.urls import path  
from .import views 


urlpatterns = [
    path('test/',views.test),
    path('',views.index,name="index"),
    path('service/',views.service,name="service"),
    path('guard/',views.guard,name="guard")
]



