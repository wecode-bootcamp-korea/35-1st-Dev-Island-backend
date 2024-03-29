import json

import bcrypt
import jwt
from django.http            import JsonResponse
from django.views           import View
from django.conf            import settings

from users.models     import User

def signin_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
            user = User.objects.get(id=payload['id'])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message':'INVALID_TOKEN'}, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status=400)

        return func(self, request, *args, **kwargs)

    return wrapper