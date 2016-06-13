from datetime import date, timedelta

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from db_utils import *
from models import User


@csrf_exempt
def posting(request):
    r = request.POST
    user_id = r.get('user_id')
    user_name = r.get('user_name')
    text = r.get('text')
    user, created = User.objects.get_or_create(user_id=user_id,
        user_name=user_name)
    user.save()
    update_offence_db(user_id, text)
    return HttpResponse()


def get_search_param(req):
    req = str(req)
    req = req.replace('>', "").replace("'", "").replace('>', "")
    req = req.split('/')
    return req[len(req) - 1]


def leaderboard(request):
    user_list = OffenceLog.objects.values('user').distinct()
    data_span = get_search_param(request)
    end_date = date.today()
    what_to = end_date.weekday()
    if data_span == "monthly":
        startdate = end_date.replace(day=1)
    else:
        startdate = end_date - timedelta(days=what_to)
    leaderboard = []
    for user in user_list:
        leader = {}
        name_obj = User.objects.get(user_id=user['user'])
        leader['name'] = name_obj.user_name
        leader['on_leave'] = len(OffenceLog.objects.all().filter(user=user['user'],
            offence_type="on_leave", timestamp__range=[startdate, end_date]))
        leader['arrive_late'] = len(OffenceLog.objects.all().filter(user=user['user'],
            offence_type="come_late", timestamp__range=[startdate, end_date]))
        leader['leave_early'] = len(OffenceLog.objects.all().filter(user=user['user'],
            offence_type="leaving_early", timestamp__range=[startdate, end_date]))
        leaderboard.append(leader)
    return JsonResponse(leaderboard, safe=False)
