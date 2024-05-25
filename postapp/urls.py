from  django.urls import  path
from .views import  *
urlpatterns=[
    path("",home,name='home'),
    path("projects",projects,name='projects'),
    path('about',about,name='about'),
    path('con',contact,name='con'),
    # path('send-email/', send_email_to_users, name='send_email_to_user')
    path('contact/', contact_view, name='con')
]