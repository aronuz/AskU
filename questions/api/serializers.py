from django.db import models
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from questions.models import Answer, Question


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    created_at = serializers.StringRelatedField()
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_unswered = serializers.SerializerMethodField()

    class Meta:
        model = Question
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_answers_count(self, instance):
        return instance.answers.count()

    def get_user_has_unswered(self, instance):
        request = self.context.get("request")
        return instance.answers.filter(author=request.user).exists()
