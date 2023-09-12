from rest_framework import routers
from .views import QuestionViewSet, ChoiceViewSet,AnswerListCreateAPIView, AnswerRetrieveUpdateDestroyAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include



router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Your API Title",
      default_version='v1',
      description="Your API Description",
   ),
   public=True,
   permission_classes=(),
)

urlpatterns = [

   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('answers/', AnswerListCreateAPIView.as_view(), name='answer-list-create'),
   path('answers/<int:pk>/', AnswerRetrieveUpdateDestroyAPIView.as_view(), name='answer-retrieve-update-delete'),


] + router.urls