from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.utils.timezone import tzinfo
import datetime

def storage_information_view(request):
  not_left_visitors = Visit.objects.filter(leaved_at__isnull=True)
  non_closed_visits = []
  for visitor in not_left_visitors:
    time_in = localtime() - visitor.entered_at
    time_format = time_in.total_seconds()/60
    is_strange = True if time_format > 60 else False
    non_closed_visits.append(
      {  
      'who_entered': visitor.passcard,
      'entered_at': visitor.entered_at,
      'duration': time_in,
      'is_strange': is_strange
    }
    )
    context = {
        'non_closed_visits': non_closed_visits
    }
  return render(request, 'storage_information.html', context)
