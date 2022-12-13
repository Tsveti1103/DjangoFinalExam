from django.apps import AppConfig



class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dog_walks.accounts'

    def ready(self):
        import dog_walks.accounts.signals
