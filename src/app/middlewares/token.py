from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from app.utils.jwt import decode_jwt
from dotenv import load_dotenv
import os
load_dotenv()


def get_token_from_header(token: HTTPBearer = Depends(HTTPBearer())):
    return token.credentials


def verify_admin_token(token: str = Depends(get_token_from_header)):
    try:
        uid = decode_jwt(token, os.environ.get("admin_jwt_secret"))
        return uid
    except:
        raise HTTPException(
            status_code=401, detail="Invalid Token Verification")
