import jwt
import time

from lib2to3.pgen2.tokenize import TokenError
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from .methods import to_dict, to_str
from posts.models import User
from .serializers import logger
from yatube_api.settings import BLACK_LIST_ACCESS, SECRET_KEY

class MyTokenRefreshSerializer(TokenRefreshSerializer):
    pass



class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        # предусмотреть получение актуального токена
        rd = request.data
        refresh = rd.get('refresh')
        user_by_refresh = OutstandingToken.objects.get(token=refresh).user
        if 'access' in rd:
            access = rd['access']
            payload = jwt.decode(jwt=access, key=SECRET_KEY, algorithms=['HS256'])

            logger.debug(payload)
            user_by_access = User.objects.get(pk=payload['user_id'])
            jti = payload['jti']
            exp = payload['exp']
            if user_by_refresh == user_by_access:
                logger.debug('USER WAS IDENTIFIED')
                str = f'{exp}:{jti}\n'
                opened_file = open('access_blacklist.txt', 'a')
                opened_file.write(str)
                logger.debug('TOKEN WAS BLACKLISTED')
                opened_file.close()

        to_read = open('access_blacklist.txt', 'r')
        new_dict=to_dict(to_read.read())
        to_read.close()
        
        now = int(time.time())

        keys = []
        
        for key in new_dict:
            if int(key) > now:
                logger.debug(f'TOKEN {new_dict[key]} STILL CAN BE USED')
            else:
                logger.debug(f'TOKEN {new_dict[key]} WILL BE DESTROYED')
                keys.append(key)
        
        for key in keys:
            del new_dict[key]
        
        to_write = open('access_blacklist.txt', 'w')
        to_write.write(to_str(new_dict))
        to_write.close()

            

        # получить информацию о токене: Exp и user    

        # занести полученный токен в чёрный список
        serializer = self.get_serializer(data=request.data)
        logger.debug(request.__dict__)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)