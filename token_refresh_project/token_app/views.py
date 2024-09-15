from rest_framework.response import Response
from rest_framework.views import APIView
from .token_generator import generate_token
from .token_decoder import decode_token

class TokenRefreshView(APIView):
    def post(self, request):
        token = request.headers.get('Authorization')
        if not token:
            return Response({'error':'Unauthorized'},status=401)
        decoded_token = decode_token(token)
        if not decoded_token:
            return Response({'error':'Invalid token'}, status=401)
        user_id = decoded_token['user_id']
        new_token = generate_token(user_id)
        return Response({'token':new_token}, status=200)
