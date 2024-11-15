from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EVTool.accounts'

    def ready(self):
        import EVTool.accounts.signals
