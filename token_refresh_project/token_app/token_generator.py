import jwt
from django.conf import settings
from datetime import datetime,timedelta

def generate_token(user_id):
    """
    Generates a new bearer token for the given user ID.

    Args:
        user_id(int): The ID of the user.

    Returns:
        str: The generated bearer token.

    Notes:
        The token is a JSON Web Token (JWT) that contains the user ID and expiration time.
        The token is signed with the project's secret key using the HS256 algorithm.
        The token is valid for 10 minutes after it's generated.

    """

    payload = {
        'user_id': user_id,
        'exp': datetime.now(datetime.timezone.utc) + timedelta(minutes=10)
    }

    token = jwt.encode(payload,settings.SECRET_KEY, algorithm='HS256')

    return token.decode('utf-8')
