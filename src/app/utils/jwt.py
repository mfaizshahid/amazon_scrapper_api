from jwt import encode, decode
import os
from dotenv import load_dotenv
load_dotenv()


def encode_jwt(uid: str):
    """Function to return JWT encoded string based on user id

    Args:
        uid (str): user id

    Returns:
        (str): returns JWT encoded string
    """
    return encode({"uid": uid}, os.environ.get("jwt_secret"),  algorithm="HS256")


def decode_jwt(jwt_str: str):
    """Function to return user id from encoded jwt

    Args:
        jwt_str (str): JWT string

    Returns:
        (str): user id
    """
    data = decode(jwt_str, os.environ.get(
        "jwt_secret"),  algorithms=["HS256"])
    return data.get("uid")
