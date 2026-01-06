import os
from datetime import datetime, timedelta
from typing import Optional

from jose import jwt
from passlib.context import CryptContext

# =========================
# JWT CONFIG
# =========================

SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_THIS_IN_PROD")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
)

# =========================
# PASSWORD HASHING
# =========================
"""
WHY bcrypt_sha256?

- bcrypt alone has a HARD 72-byte password limit
- bcrypt_sha256 hashes first with SHA-256, THEN bcrypt
- Prevents crashes + security bugs
- Recommended by Passlib for modern systems
"""

pwd_context = CryptContext(
    schemes=["bcrypt_sha256"],
    deprecated="auto"
)

# =========================
# PASSWORD HELPERS
# =========================

def hash_password(password: str) -> str:
    """
    Hash a password securely.
    Safe for long passwords.
    """
    if not password:
        raise ValueError("Password cannot be empty")
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against its hash.
    """
    if not plain_password or not hashed_password:
        return False
    return pwd_context.verify(plain_password, hashed_password)

# =========================
# JWT TOKEN HELPERS
# =========================

def create_access_token(
    data: dict,
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    Create a signed JWT access token.
    """
    to_encode = data.copy()

    expire = datetime.utcnow() + (
        expires_delta
        if expires_delta
        else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    to_encode.update({
        "exp": expire,
        "iat": datetime.utcnow(),
        "type": "access"
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

