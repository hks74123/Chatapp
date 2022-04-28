from django.apps import AppConfig


class ChatGroupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Chat_group'
    
    def ready(self):
        import Chat_group.signals