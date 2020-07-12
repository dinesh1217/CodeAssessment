from django.urls import path, include
from .views import QuestionView, ChoiceView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('question', QuestionView)
router.register('choice', ChoiceView)


urlpatterns = router.urls
