from rest_framework import serializers
from .models import AddInfo, Chat, ChatMessage, Forum, ForumMessage, Employer, EmployerComment, LegalForm
from .models import EmploymentOppurtunity, ImmigrationHelpdesk, LearnEnglish, SpanishBusiness


class AddInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddInfo
        fields = ["whatsappid",'facebookid', 'instagramid',]


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["area",]


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ["chatroom", 'message', 'message_owner']


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ["area", 'title', 'creator']

    
class ForumMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumMessage
        fields = ["forum", 'message', 'message_owner']



class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ["name", 'area', 'rating']


class EmployerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerComment
        fields = ["employer", 'comment', 'comment_owner']


class EmploymentOppurtunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentOppurtunity
        fields = ["area", 'contact_person', 'contact_number', 'employer', 'active']


class ImmigrationHelpdeskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImmigrationHelpdesk
        fields = ['applicant',]


class LearnEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearnEnglish
        fields = ['link',]



class LegalFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalForm
        fields = ["type", 'file']


class SpanishBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpanishBusiness
        fields = ['area', 'businessname', 'address']

