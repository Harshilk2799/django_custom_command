from django.core.management.base import BaseCommand
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError

# Custom Command with Argument
class Command(BaseCommand):
    help = "Create a normal user"

    def add_arguments(self, parser):
        parser.add_argument("username", type=str, help="The username for the user")
        parser.add_argument("email", type=str, help="The email for the user")
        parser.add_argument("password", type=str, help="The password for the user")

    def handle(self, *args, **kwargs):
        username = kwargs["username"]
        email = kwargs["email"]
        password = kwargs["password"]

        try:
            User.objects.create_user(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"User {username} created successfully"))
        
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f"Error: {e.error_dict}"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {str(e)}"))