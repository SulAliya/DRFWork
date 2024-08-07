from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_list = [
            {'last_name':'Petrov', 'first_name': 'Ivan'},
            {'last_name': 'Ivanov', 'first_name': 'Petr'},
            {'last_name': 'Semenov', 'first_name': 'Alex'},

        ]

        users_for_create = []
        for user_item in user_list:
            users_for_create.append(
                User(**user_item)
            )

        User.objects.bulk_create(users_for_create)