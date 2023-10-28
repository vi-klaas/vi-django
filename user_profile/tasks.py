from celery import shared_task


@shared_task
def print_hello():
    print("Hello, world 3!")


@shared_task
def print_bye():
    print("Bye, world 3!")
