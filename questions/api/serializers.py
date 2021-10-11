from django.db import models
from rest_framework import serializers
from questions.models import Answer, Question


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    created_at = serializers.StringRelatedField()
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_unswered = serializers.SerializerMethodField()

    class Meta:
        model = Question
        exclude = ["id", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_answers_count(self, instance):
        return instance.answers.count()

    def get_user_has_unswered(self, instance):
        request = self.context.get("request")
        return instance.answers.filter(author=request.user).exists()


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    created_at = serializers.StringRelatedField()
    likes_count = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()
    question_slug = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        exclude = ["question", "voters", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_liked(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()

    def get_question_slug(self, instance):
        return instance.question.slug
