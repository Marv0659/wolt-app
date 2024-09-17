from bottle import request, response
import re
import sqlite3

############################################################
def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

##############################
def db():
    # db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/company.db")  
    db = sqlite3.connect("basepage.db")
    db.row_factory = dict_factory # sqlite3.Row
    return db


##############################
def disable_cache():
    response.add_header("Cache-Control", "no-cache, no-store, must-revalidate")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)  


##############################
EMAIL_REGEX = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"
def validate_user_email():
    error = "Email invalid"
    user_email = request.forms.get("user_email", "")
    user_email = user_email.strip()
    if not re.match(EMAIL_REGEX, user_email): raise Exception(error, 400)
    return user_email


##############################
USER_PASSWORD_MIN = 8
USER_PASSWORD_MAX = 50
USER_PASSWORD_REGEX = f"^.{{{USER_PASSWORD_MIN},{USER_PASSWORD_MAX}}}$"
def validate_user_password():
    error = f"Password {USER_PASSWORD_MIN} to {USER_PASSWORD_MAX} characters"
    user_password = request.forms.get("user_password", "").strip()
    if not re.match(USER_PASSWORD_REGEX, user_password): raise Exception(error, 400)
    return user_password

##############################

USER_NAME_MIN = 2
USER_NAME_MAX = 20
USER_NAME_REGEX = f"^.{{{USER_NAME_MIN},{USER_NAME_MAX}}}$"
def validate_user_name():
    error = f"Name {USER_NAME_MIN} to {USER_NAME_MAX} characters"
    user_name = request.forms.get("user_name", "").strip()
    if not re.match(USER_NAME_REGEX, user_name): raise Exception(error, 400)
    return user_name

##############################

USER_LAST_NAME_MIN = 2
USER_LAST_NAME_MAX = 20
USER_LAST_NAME_REGEX = f"^.{{{USER_LAST_NAME_MIN},{USER_LAST_NAME_MAX}}}$"
def validate_user_last_name():
    error = f"Last name {USER_LAST_NAME_MIN} to {USER_LAST_NAME_MAX} characters"
    user_last_name = request.forms.get("user_last_name", "").strip()
    if not re.match(USER_LAST_NAME_REGEX, user_last_name): raise Exception(error, 400)
    return user_last_name

##############################
