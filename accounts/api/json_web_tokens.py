from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import exceptions
import jwt

from accounts.models import User
from django.conf import settings

class JWTAuthentication(BaseAuthentication):
    """
    Safe JWT Authentication class
    """
    def authenticate(self, request):
        auth_header = get_authorization_header(request)
        actual_data = auth_header.decode('utf-8')

        auth_token = actual_data.split(" ") # Gives Bearer * The Token

        if (len(auth_token)) != 2:
            raise exceptions.AuthenticationFailed("Invalid token")

        token = auth_token[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            username = payload['username']
            user = User.objects.get(username = username)
            return (user, token)

        except jwt.ExpiredSignatureError:
                raise exceptions.AuthenticationFailed("Expired token")
        
        except jwt.DecodeError:
                raise exceptions.AuthenticationFailed("Invalid token")

        except User.DoesNotExist:
                raise exceptions.AuthenticationFailed("Invalid User")


