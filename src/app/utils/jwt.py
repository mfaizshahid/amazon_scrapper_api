from jwt import encode, decode
import os
from dotenv import load_dotenv
load_dotenv()


def encode_jwt(uid: str, jwt_secret: str):
    """Function to return JWT encoded string based on user id

    Args:
        uid (str): user id
        jwt_secret (str): jwt secret

    Returns:
        (str): returns JWT encoded string
    """
    return encode({"uid": uid}, jwt_secret,  algorithm="HS256")


def decode_jwt(jwt_str: str, jwt_secret: str):
    """Function to return user id from encoded jwt

    Args:
        jwt_str (str): JWT string
        jwt_secret (str): jwt secret

    Returns:
        (str): user id
    """
    data = decode(jwt_str, jwt_secret,  algorithms=["HS256"])
    return data.get("uid")
