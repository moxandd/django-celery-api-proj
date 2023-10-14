from django.shortcuts import render
from django.http import HttpResponse
from .models import Newsletter
from .tasks import send_start
from datetime import datetime, timedelta, timezone

def test_view(request, newsletter_id):

    now = datetime.now(timezone.utc)

    newsletter = Newsletter.objects.get(id=newsletter_id)
    newsletter_start = newsletter.send_start - now
    time_before_execution = int(newsletter_start.total_seconds())

    time = time_before_execution

    if time >= 0:
        send_start.apply_async(args=(newsletter_id,), countdown=time)
        if time > 0:
            return HttpResponse("Task has been added in query...")
    else:
        newsletter_end =  newsletter.send_end - now
        time_before_end = int(newsletter_end.total_seconds())
        if time_before_end >= 0:
            send_start.apply_async(args=(newsletter_id,), countdown=0)
            return HttpResponse("Newsletter is working...")
        else:
            return HttpResponse("The newsletter is expired... It's not gonna be executed")
        