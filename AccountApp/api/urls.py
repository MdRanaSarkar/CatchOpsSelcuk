from AccountApp.api import views
from django.urls import path

app_name='AccountApp_api'

urlpatterns = [
	
	path('register/',views.registration_view,name='registration'),

	path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
