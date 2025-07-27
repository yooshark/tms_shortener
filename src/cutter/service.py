import random
import string

from django.conf import settings
from cutter.models import Urls


def get_random_string() -> str:
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(settings.HASH_LENGTH))


def load_url(url_hash: str) -> Urls:
    return Urls.objects.get(hash=url_hash)
