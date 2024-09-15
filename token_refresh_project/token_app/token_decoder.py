import jwt
from django.conf import settings

def decode_token(token):
    """
      Decodes a bearer token and returns the payload if valid, otherwise returns None.

    Args:
        token (str): The bearer token to be decoded.

    Returns:
        dict or None: The decoded payload if the token is valid, otherwise None.
    
    """
    try:
        """
        Attempt to decode the token using the SECRET_KEY from Django settings.
        The algorithms parameter is set to ['HS256'] to specify the HMAC SHA-256 algorithm.
        """
        payload = jwt.decode(token,settings.SECRET_KEY, algorithms = ['HS256'])
        """
        If the token is valid, return the decoded payload.
        """
        return payload
    
    except jwt.ExpiredSignatureError:
        """
        catch the ExpiredSignatureError exception, which is raised when the token has expired.
        Return None to indicate that the token is invalid.
        """
        return None
    
    except jwt.InvalidTokenError:
        """
        Catch the InvalidTokenError exception, which is raised when the token is invalid or Malformed(any information that cannot be read or correctly processed)
        Return None to indicate that the token is invalid.
        """
        return None
    
    