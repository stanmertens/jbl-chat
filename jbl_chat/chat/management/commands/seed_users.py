from argparse import ArgumentParser
from typing import Any

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = "Seed the database with random users"

    def add_arguments(self, parser: ArgumentParser) -> None:
        default = 10
        parser.add_argument(
            "--count",
            type=int,
            default=default,
            help=f"Number of users to create (default: {default})",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        User = get_user_model()
        faker = Faker()
        count = options["count"]

        for _ in range(count):
            username = faker.unique.first_name()
            password = faker.unique.password(
                length=10, special_chars=False, digits=False
            )
            image_url = f"https://api.dicebear.com/6.x/personas/svg?seed={username}"
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                    username=username,
                    password=password,
                    image_url=image_url,
                )
                msg = f"User created with username {username} and password {password}"
                self.stdout.write(self.style.SUCCESS(msg))
