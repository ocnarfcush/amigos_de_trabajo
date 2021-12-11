from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from .models import AddInfo, Chat, ChatMessage, Employer, EmployerComment,  Forum, ForumMessage, LegalForm
from .models import EmploymentOppurtunity, ImmigrationHelpdesk, LearnEnglish, SpanishBusiness
from .serializers import AddInfoSerializer, ForumSerializer, ChatSerializer, ChatMessageSerializer
from .serializers import ForumMessageSerializer, EmployerSerializer, EmployerCommentSerializer, LegalFormSerializer
from .serializers import EmploymentOppurtunitySerializer, ImmigrationHelpdeskSerializer, LearnEnglishSerializer, SpanishBusinessSerializer
from rest_framework import viewsets


def index(request):
    return HttpResponse('index')


class AddInfoViewSet(viewsets.ModelViewSet):
    queryset = AddInfo.objects.all()
    serializer_class = AddInfoSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer


class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class EmployerCommentViewSet(viewsets.ModelViewSet):
    queryset = EmployerComment.objects.all()
    serializer_class = EmployerCommentSerializer


class ForumViewSet(viewsets.ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer


class ForumMessageViewSet(viewsets.ModelViewSet):
    queryset = ForumMessage.objects.all()
    serializer_class = ForumMessageSerializer


class EmploymentOppurtunityViewSet(viewsets.ModelViewSet):
    queryset = EmploymentOppurtunity.objects.all()
    serializer_class = EmploymentOppurtunitySerializer


class ImmigrationHelpdeskViewSet(viewsets.ModelViewSet):
    queryset = ImmigrationHelpdesk.objects.all()
    serializer_class = ImmigrationHelpdeskSerializer


class LearnEnglishViewSet(viewsets.ModelViewSet):
    queryset = LearnEnglish.objects.all()
    serializer_class = LearnEnglishSerializer


class LegalFormViewSet(viewsets.ModelViewSet):
    queryset = LegalForm.objects.all()
    serializer_class = LegalFormSerializer


class SpanishBusinessViewSet(viewsets.ModelViewSet):
    queryset = SpanishBusiness.objects.all()
    serializer_class = SpanishBusinessSerializer


