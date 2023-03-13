from rest_framework import serializers
from .models import Student

#validators
def start_with_r(value):
    if value[0].lower()!='s':
        raise serializers.ValidationError('Name Should be start with S')

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20,validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=20) 
    def create(self, validated_data):
        return Student.objects.create(**validated_data) 
    
    def update(sef, instance, validated_data):
        instance.id = validated_data.get('id',instance.id)
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
# field lavel validation
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('seat full please contact to the management for donation')
        return value