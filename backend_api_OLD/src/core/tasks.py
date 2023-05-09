from celery import shared_task


@shared_task
def loop_task() -> bool:
    print(f"task={'ping_celery_redis'.upper()} is done")
    return True
