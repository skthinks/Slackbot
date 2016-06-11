
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from db_work import *


@csrf_exempt
def posting(request):
    r = request.POST
    insert_user_db(r)
    process_request(r)
    return HttpResponse(str(request))
