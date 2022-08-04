from rest_framework import serializers
from .models import drink

class drinkserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=drink
        fields=['id','name','description']
