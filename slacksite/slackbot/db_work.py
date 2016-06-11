from models import User, OffenceLog


def check_present(userid):
    if User.objects.filter(user_id=userid).exists():
        return True
    return False


def create_user_entry(userid, username):
    new_user = User(user_name=username, user_id=userid)
    new_user.save()


def insert_user_db(req):
    username = req.get('user_name')
    userid = req.get('user_id')
    if check_present(userid):
        return
    create_user_entry(userid, username)


def update_offence_db(user_id, message):
    message = message.lower()
    offence = ""
    if "leaving" in message:
        offence = "leaving_early"
    elif "reaching" in message or "in by" in message or "be in" in message:
        offence = "come_late"
    elif "leave" in message:
        offence = "on_leave"
    else:
        offence = "N/A"
    if offence == "N/A":
        return
    user = User.objects.get(user_id=user_id)
    new_entry = OffenceLog(user=user, offence_type=offence)
    new_entry.save()


def process_request(req):
    userid = req.get('user_id')
    message = req.get('text')
    message = message.lower()
    update_offence_db(userid, message)


def get_users_db():
    user_list = User.objects.all()
    for user in user_list:
        print user.user_name


def get_offence_db():
    user_list = OffenceLog.objects.all()
    for slacker in user_list:
        print slacker.user_id, "\t",
        print slacker.timestamp, "\t",
        print slacker.offence_type
