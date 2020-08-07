from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('motto/',views.motto,name="Motto"),
    path('profile/',views.profile,name="profile"),
]