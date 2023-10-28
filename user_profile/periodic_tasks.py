import time

from celery import shared_task


@shared_task
def print_hello_periodic():
    print("hello again!")
    return time.time()
