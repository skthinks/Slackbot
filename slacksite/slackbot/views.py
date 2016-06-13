from datetime import date, timedelta

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from db_utils import *
from models import User
import webpage_utils


@csrf_exempt
def posting(request):
    r = request.POST
    user_id = r.get('user_id')
    user_name = r.get('user_name')
    text = r.get('text')
    new_user, created = User.objects.get_or_create(user_id=user_id, 
        user_name=user_name)
    new_user.save()
    update_offence_db(user_id, text)
    return HttpResponse(str(request))


def get_search_param(req):
    req = str(req)
    req = req.replace('>', "").replace("'", "").replace('>', "")
    req = req.split('/')
    return req[len(req) - 1]


def leaderboard(request):
    user_list = OffenceLog.objects.values('user').distinct()
    data_span = get_search_param(request)
    enddate = date.today()
    what_to = enddate.weekday()
    if data_span == "monthly":
        startdate = enddate.replace(day=1)
    else:
        startdate = enddate - timedelta(days=what_to)
    leader = ""
    for user in user_list:
        name_obj = User.objects.get(user_id=user['user'])
        on_leave = OffenceLog.objects.all().filter(user=user['user'],
            offence_type="on_leave", timestamp__range=[startdate, enddate])
        arrive_late = OffenceLog.objects.all().filter(user=user['user'], offence_type="come_late")
        leave_early = OffenceLog.objects.all().filter(user=user['user'], offence_type="leaving_early")
        leader += ('<tr style="color:blue;">' +
            "<td>" + name_obj.user_name + "</td> " +
            "<td>" + str(len(leave_early)) + "</td>" +
            "<td>" + str(len(arrive_late)) + "</td>" +
            "<td>" + str(len(on_leave)) + "</td>>" +
            "</tr>"
        )
    return_page = "%s%s%s" % (webpage_utils.PAGE_HEADER, leader, webpage_utils.PAGE_FOOTER)
    return HttpResponse(return_page)
