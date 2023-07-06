from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from users.models import User


class Command(BaseCommand):
    help = "Cria vários usuários não instrutores"

    def handle(self, *args, **kwargs):
        for i in range(10):
            random_name = get_random_string(6)
            random_email = f"{random_name}@mail.com"
            User.objects.create_user(
                username=random_name,
                name=random_name,
                email=random_email,
                password="123456",
                is_instructor=False,
            )
