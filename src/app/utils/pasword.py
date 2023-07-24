from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str):
    """Verify plain text password with hashed password

    Args:
        plain_password (str): plain text password
        hashed_password (str): hashed password

    Returns:
        bool: true, if password match else false
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    """Return hashed password from plain text password

    Args:
        password (str): plain text password

    Returns:
        str: hashed [asswprd]
    """
    return pwd_context.hash(password)
