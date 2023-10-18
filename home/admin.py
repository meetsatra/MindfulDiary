from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(JournalEntry)
admin.site.register(Feedback)
admin.site.register(ChatbotConversation)
admin.site.register(UserProfile)
admin.site.register(SocialToken)
