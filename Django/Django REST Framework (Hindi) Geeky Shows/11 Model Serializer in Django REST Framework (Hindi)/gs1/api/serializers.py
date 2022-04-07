from rest_framework import serializers

from api.models import Student


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)

    # Validator

    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('name Should start with R')

    name = serializers.CharField(validators=[start_with_r])

    class Meta:
        model = Student
        fields = '__all__'
        # red_only_fields = ['name', 'roll']
        # extra_kwargs = {'name': {'read_only': True}}

    #   Field Level Validator

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('seat full')
        return value

    # object level

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'shatil' and ct.lower() != 'dhaka':
            raise serializers.ValidationError('Rohits city Must be Ranchi')
        return data
