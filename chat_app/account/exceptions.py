from rest_framework.exceptions import APIException

class UnsignedUser(APIException):
    status_code = 400
    default_detail = "user not logged in."
    default_code = "unsigned_user"