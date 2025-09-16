from celery import shared_task
import time


@shared_task(queue="addition")
def add(x, y):
    time.sleep(20)  # simulate delay
    print("Hello World...!!!")
    return x + y
