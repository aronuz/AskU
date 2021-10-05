from django.urls.conf import include
from rest_framework import urlpatterns
from django.urls import include, path

from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from questions.api import views as qv

router = DefaultRouter()
router.register(r"questions", qv.QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("questions/<slug:slug>/answer/",
         qv.AnswerCreateView.as_view(), name="answer-create")
]
