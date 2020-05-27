from rest_framework import serializers
from .models import Poll

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

class PollCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__' # доступны все поля

class PollUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        exclude = ('start_date',) # доступны для изменения все поля кроме start_date
