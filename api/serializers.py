from rest_framework import serializers

from events.models import Category, Event


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Event
        fields = ['id', 'name', 'venue', 'start_date', 'end_date', 'category']
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.get(name=category_data['name'])
        event = Event.objects.create(category=category, **validated_data)
        return event
