import os
from datetime import date, timedelta

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from db_utils import *
from models import User


TOKEN = os.environ['WEBHOOK_TOKEN']


@csrf_exempt
def handle_slack_post(request):
    r = request.POST
    data_span = request.GET
    if data_span:
        return JsonResponse({}, status=405, safe=False)
    req_token = r.get('token')
    if req_token != TOKEN:
        return JsonResponse({}, status=403, safe=False)
    user_id = r.get('user_id')
    user_name = r.get('user_name')
    text = r.get('text')
    if not user_id or not user_name:
        return JsonResponse({}, status=400, safe=False)
    user, created = User.objects.get_or_create(user_id=user_id,
                                               user_name=user_name)
    user.save()
    update_offence_db(user_id, text)
    return JsonResponse({})


def leaderboard(request):
    data_span = request.GET.get('q', None)
    if not data_span:
        return JsonResponse({}, status=400, safe=False)
    user_list = OffenceLog.objects.values('user').distinct()
    end_date = date.today()
    what_to = end_date.weekday()
    if data_span == "monthly":
        startdate = end_date.replace(day=1)
    elif data_span == 'weekly':
        startdate = end_date - timedelta(days=what_to)
    else:
        return JsonResponse({}, status=400, safe=False)
    leaderboard = []
    for user in user_list:
        leader = {}
        name_obj = User.objects.get(user_id=user['user'])
        name_obj.save()
        leader['name'] = name_obj.user_name
        leader['on_leave'] = (OffenceLog.objects.filter(
            user=user['user'], offence_type="on_leave",
            timestamp__range=[startdate, end_date])).count()
        leader['arrive_late'] = (OffenceLog.objects.filter(
            user=user['user'], offence_type="come_late",
            timestamp__range=[startdate, end_date])).count()
        leader['leave_early'] = (OffenceLog.objects.filter(
            user=user['user'], offence_type="leaving_early",
            timestamp__range=[startdate, end_date])).count()
        leaderboard.append(leader)
    return JsonResponse(leaderboard, status=200, safe=False)
