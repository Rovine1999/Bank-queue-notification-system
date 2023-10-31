from rest_framework.authentication import TokenAuthentication


#Auth class to handle token authentication for APIs
class BearerTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'


AUTH_CLASS = BearerTokenAuthentication
