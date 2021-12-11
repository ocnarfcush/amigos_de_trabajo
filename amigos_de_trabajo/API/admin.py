from django.contrib import admin
from .models import AddInfo, Forum, ForumMessage, Chat, ChatMessage, LegalForm, Employer, EmployerComment
from .models import EmploymentOppurtunity, ImmigrationHelpdesk, LearnEnglish, SpanishBusiness

admin.site.register(AddInfo)
admin.site.register(LegalForm)
admin.site.register(EmploymentOppurtunity)
admin.site.register(ImmigrationHelpdesk)
admin.site.register(LearnEnglish)
admin.site.register(SpanishBusiness)

class ForumMessageInline(admin.TabularInline):
    model = ForumMessage
    extra = 0


class ChatMessageInline(admin.TabularInline):
    model = ChatMessage
    extra = 0


class EmployerCommentInline(admin.TabularInline):
    model = EmployerComment
    extra = 0


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('area', 'title', 'creation_time')
    inlines = [ForumMessageInline,]


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('area',)
    inlines = [ChatMessageInline,]


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('area','name', 'rating')
    inlines = [EmployerCommentInline,]