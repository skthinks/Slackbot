from django.shortcuts import render

# Create your views here.
import psycopg2
import urlparse

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from models import User

def check_present(user_id):
    user_id_list = User.objects.values_list('user_id', flat=True)
    if user_id in user_id_list:
        return True
    return False


def insert_user_db(req):
    username = req.get('user_name')
    userid = req.get('user_id')
    ans = check_present(userid)
    if check_present(userid):
        return
    new_user = User(user_name = username, user_id = userid)
    new_user.save()
    user_list = User.objects.all()
    for user in user_list:
        print user.user_name

# def get_users_db():



@csrf_exempt
def posting(request):
    print "Logging Activity..."
    r = request.POST
    insert_user_db(r)
    # get_users_db
    return HttpResponse(str(request))
