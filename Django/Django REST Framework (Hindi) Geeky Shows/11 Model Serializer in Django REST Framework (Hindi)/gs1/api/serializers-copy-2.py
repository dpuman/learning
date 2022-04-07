from rest_framework import serializers

from api.models import Student

# Validator


def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('name Should start with R')


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'
        # red_only_fields = ['name', 'roll']
        # extra_kwargs = {'name': {'read_only': True}}

    # object level

    # def validate(self, data):
    #     nm = data.get('name')
    #     ct = data.get('city')
    #     if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
    #         raise serializers.ValidationError('Rohits city Must be Ranchi')
    #     return data

    #   Field Level Validator

    # def validate_roll(self, value):
    #     if value >= 200:
    #         raise serializers.ValidationError('seat full')
    #     return value
