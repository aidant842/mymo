from .models import Test


def create_test_instance():
    Test.objects.create(name="from cron")
