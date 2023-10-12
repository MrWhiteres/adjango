from os import getenv
from secrets import token_urlsafe
from dotenv import load_dotenv

load_dotenv()

DEBUG: bool | int = getenv('DEBUG', True)
SECRET_KEY: str = getenv('SECRET_KEY', token_urlsafe(70))
SENTRY_DSN: str = getenv('SENTRY_DSN', None)
