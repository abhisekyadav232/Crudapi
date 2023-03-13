from rest_framework import serializers
from . models import Student
class StudentSerializer(serializers.ModelSerializer):

    # validator
    # def start_with_r(value):
    #     if value[0].lower() != 'a':
    #         raise serializers.ValidationError('Name must be start with A')
    #     return(value)
    # name = serializers.CharField(validators = [start_with_r])
   
   
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
#field lavel validation 
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('seat full contact the management for the donation')
        return value

# object lavel validataion

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        
        if nm.lower()== 'sruti' and ct.lower() != 'noida':
            raise serializers.ValidationError('City must be Noida')
        return data


