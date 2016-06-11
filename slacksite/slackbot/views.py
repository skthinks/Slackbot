
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from models import User, Leaderboards


def check_present(user_id):
    user_id_list = User.objects.values_list('user_id', flat=True)
    if user_id in user_id_list:
        return True
    return False


def check_present_stats(user_id):
    user_id_list = Leaderboards.objects.values_list('user_id', flat=True)
    if user_id in user_id_list:
        return True
    return False


def insert_user_db(req):
    username = req.get('user_name')
    userid = req.get('user_id')
    if check_present(userid):
        return
    new_user = User(
        user_name = username, 
        user_id = userid
    )
    new_user.save()


def insert_stats_db(req):
    userid = req.get('user_id')
    message = req.get('text')
    if not check_present_stats(userid):
        new_entry = Leaderboards(
            user_id = userid, 
            leave_early = 0,  
            arrive_late = 0,
            on_leave = 0
        )
        new_entry.save()
    # get_stats_db()
    print message


def get_users_db():
    user_list = User.objects.all()
    for user in user_list:
        print user.user_name

# def get_stats


@csrf_exempt
def posting(request):
    print "Logging Activity..."
    r = request.POST
    insert_user_db(r)
    insert_stats_db(r)
    # get_users_db()
    return HttpResponse(str(request))
