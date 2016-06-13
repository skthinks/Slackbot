
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from db_utils import *


@csrf_exempt
def posting(request):
    r = request.POST
    user_id = r.get('user_id')
    user_name = r.get('user_name')
    text = r.get('text')
    insert_user_db(user_id, user_name)
    update_offence_db(user_id, text)
    return HttpResponse(str(request))
