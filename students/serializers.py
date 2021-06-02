from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('pk', 'first_name', 'last_name', 'email', 'classroom')
        
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MPDBObtainTokenPairView(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MPDBObtainTokenPairView, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['sub'] = 'MpdbUser'
        return token