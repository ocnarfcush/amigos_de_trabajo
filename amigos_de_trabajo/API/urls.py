from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('addinfo', views.AddInfoViewSet, basename='add_info')
router.register('chat', views.ChatViewSet, basename='chat')
router.register('chatmessage', views.ChatMessageViewSet, basename='chat_message')
router.register('employer', views.EmployerViewSet, basename='employer')
router.register('employercomment', views.EmployerCommentViewSet, basename='employer_comment')
router.register('employmentoppurtunity', views.EmploymentOppurtunityViewSet, basename='employment')
router.register('Forum', views.ForumViewSet, basename="forums")
router.register('forummessage', views.ForumMessageViewSet, basename='forum_message')
router.register('immigrationhelp', views.ImmigrationHelpdeskViewSet, basename='immigration_help')
router.register('legalforms', views.LegalFormViewSet, basename='legal_forms')
router.register('learnenglish', views.LearnEnglishViewSet, basename='learn_english')
router.register('spanishfriendlybusinesses', views.SpanishBusinessViewSet, basename='spanish_businesses')


urlpatterns = [
    path('home/', views.index, name='home'),
    path("", include(router.urls)),
]