from rest_framework import serializers
from .models import ShowBox


class ShowBoxSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShowBox
        fields = '__all__'