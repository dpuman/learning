from rest_framework import serializers

from api.models import Student

# Validator


def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('name Should start with R')


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    # object level

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('Rohits city Must be Ranchi')
        return data

    #   Field Level Validator

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('seat full')
        return value

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.roll = validate_data.get('roll', instance.roll)
        instance.city = validate_data.get('city', instance.city)
        instance.save()
        return instance
