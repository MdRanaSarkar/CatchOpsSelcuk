<<<<<<< HEAD
from rest_framework import  serializers

from  AccountApp.models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=Account
        fields=['email','username','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self):
        account=Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password!=password2:
            raise serializers.ValidationError({'password':'password must match'})
        account.set_password(password)
        account.save()
        return account
=======
from AccountApp.models import Account
from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = '__all__'

class UserSerializerWithToken(UserSerializer):
	token = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Account
		fields = ['id', 'username', 'email','is_admin','is_active','is_staff', 'is_superuser','token']
		# exclude = ['refresh', 'access']
	
	def get_token(self, obj):
		token = RefreshToken.for_user(obj)
		return str(token.access_token)


class RegistrationSerializer(serializers.ModelSerializer):
	password2=serializers.CharField(style={'input_type':'password'},write_only=True)
	class Meta:
		model=Account
		fields=['email','username','password','password2']
		extra_kwargs={
			'password':{'write_only':True}
		}

	def save(self):
		account=Account(
			email=self.validated_data['email'],
			username=self.validated_data['username'],
		)
		password=self.validated_data['password']
		password2=self.validated_data['password2']

		if password!=password2:
			raise serializers.ValidationError({'password':'password must match'})
		account.set_password(password)
		account.save()
		return account
>>>>>>> 88043f25a323dcb3e130d0f3c017b947168ddef4
