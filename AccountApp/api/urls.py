<<<<<<< HEAD
from  django.urls import path
from AccountApp.api.views import registration_view
from rest_framework.authtoken.views import obtain_auth_token

app_name='AccountApp_api'
urlpatterns = [
path('register/',registration_view,name='registration'),
path('login/', obtain_auth_token,name='login')
]
=======
from AccountApp.api import views
from django.urls import path

app_name='AccountApp_api'

urlpatterns = [
	
	path('register/',views.registration_view,name='registration'),

	path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
>>>>>>> 88043f25a323dcb3e130d0f3c017b947168ddef4
