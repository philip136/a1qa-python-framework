import os
from dotenv import load_dotenv

# Load .env file automatically
load_dotenv()


class EnvProvider:
    @staticmethod
    def _require_env(name: str) -> str:
        value = os.environ.get(name)
        if not value:
            raise EnvironmentError(f'Missing required environment variable: "{name}". Check your .env file.')
        return value

    @staticmethod
    def basic_auth_user() -> str:
        return EnvProvider._require_env("BASIC_AUTH_USER")

    @staticmethod
    def basic_auth_password() -> str:
        return EnvProvider._require_env("BASIC_AUTH_PASSWORD")

    @staticmethod
    def test_user() -> str:
        return EnvProvider._require_env("TEST_USER")

    @staticmethod
    def test_password() -> str:
        return EnvProvider._require_env("TEST_PASSWORD")
