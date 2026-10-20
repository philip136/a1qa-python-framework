from dataclasses import dataclass


@dataclass(frozen=True)
class RegistrationCreds:
    email_name: str
    email_domain: str
    password: str
    domain_extension: str
