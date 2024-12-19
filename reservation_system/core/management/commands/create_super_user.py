from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'Create a superuser with the specified username, email, and password.'

    def add_arguments(self, parser):
        parser.add_argument('-u', '--username', type=str, help='Username of the superuser')
        parser.add_argument('-p', '--password', type=str, help='Password of the superuser')
        parser.add_argument('-e', '--email', type=str, help='Email address of the superuser')

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        email = options['email']

        User = get_user_model()
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))
