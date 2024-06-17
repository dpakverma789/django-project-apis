from rest_framework import serializers
from . models import QuestionBank


class QuestionBankSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    question = serializers.CharField(max_length=500)
    option_1 = serializers.CharField(max_length=200)
    option_2 = serializers.CharField(max_length=200)
    option_3 = serializers.CharField(max_length=200)
    option_4 = serializers.CharField(max_length=200)
    answer = serializers.CharField(max_length=200)
