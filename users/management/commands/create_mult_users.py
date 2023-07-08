from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from users.models import User


class Command(BaseCommand):
    help = "Cria vários usuários não instrutores"

    def handle(self, *args, **kwargs):
        for i in range(10):
            random_name = get_random_string(6)
            randon_names = get_random_string(7)
            random_email = f"{random_name}@mail.com"
            User.objects.create_user(
                username=random_name,
                first_name=randon_names,
                last_name=randon_names,
                email=random_email,
                password="12346",
                is_instructor=False,
            )
