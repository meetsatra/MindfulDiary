from django.db import models
from django.contrib.auth.models import User

# Journal Entry Model
class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    entry_text = models.TextField()
    # mood, weather
    def __str__(self) -> str:
        return self.entry_text

# Feedback Model
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Chatbot Conversation Model (for chat history)
class ChatbotConversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Extend User Profile (if needed)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional user profile fields, e.g., profile picture, bio, etc.

# Google OAuth Token Storage (for social authentication)
class SocialToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.CharField(max_length=255)
    token = models.TextField()
    # You may need to store additional data like token expiration date

    class Meta:
        unique_together = ('user', 'provider')

# Add any other models you need for your project, such as chatbot responses, user preferences, etc.
