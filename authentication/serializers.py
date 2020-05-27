from rest_framework import serializers
from django.contrib.auth import get_user_model

class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        password  = self.validated_data['password']
        password2  = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'Passwords must match'})

        user = get_user_model().objects.create_user(email=self.validated_data['email'],
                                        username=self.validated_data['username'],
                                        password=self.validated_data['password'],
                                        )
        return user