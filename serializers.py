from rest_framework import serializers
from .models import fraud


class fraud_serializer(serializers.ModelSerializer):
	class Meta:
		model = fraud
		fields = '__all__'

