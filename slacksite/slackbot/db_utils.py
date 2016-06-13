from models import User, OffenceLog


def update_offence_db(user_id, message):
    message = message.lower()
    offence = ""
    if "leaving" in message:
        offence = "leaving_early"
    elif ("reaching" in message or
          "in by" in message or
          "be in" in message):
        offence = "come_late"
    elif "leave" in message:
        offence = "on_leave"
    else:
        return
    user = User.objects.get(user_id=user_id)
    new_entry = OffenceLog(user=user, offence_type=offence)
    new_entry.save()
