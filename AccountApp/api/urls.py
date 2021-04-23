from  django.urls import path
from AccountApp.api.views import registration_view
from rest_framework.authtoken.views import obtain_auth_token

app_name='AccountApp_api'
urlpatterns = [
path('register/',registration_view,name='registration'),
path('login/', obtain_auth_token,name='login')
]