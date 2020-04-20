from werkzeug.security import safe_str_cmp #safe string compare
from models.user import UserModel

#when user send user name and pwd
#what happens when received
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

#when user is already logged in (jwt token) in header in request

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
