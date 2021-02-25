from celery import shared_task
from celery_progress.backend import ProgressRecorder
import time


@shared_task(bind=True)
def process_up_load(self, form):
    progress_recorder = ProgressRecorder(self)
    print('Upload: Task started')

    # Upload file/ save form
    form.save()


@shared_task(bind=True)
def my_task(self, seconds):
    progress_recorder = ProgressRecorder(self)
    result = 0
    for i in range(seconds):
        time.sleep(1)
        result += i
        progress_recorder.set_progress(i + 1, seconds)
    return result



