from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Category, Course, Lesson
from membership.models import Pricing


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
        # queryset= Category.objects.all()
    )
    pricing_tiers = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
        # queryset= Pricing.objects.all()
    )
    lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        model  = Course
        fields = "__all__"
        lookup_field = 'slug'
