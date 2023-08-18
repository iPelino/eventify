from rest_framework import serializers

from events.models import Category, Event


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Event
        fields = ['id', 'name', 'venue', 'start_date', 'end_date', 'category']
        extra_kwargs = {
            'id': {'read_only': True},
        }
