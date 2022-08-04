from abc import ABC, abstractmethod


class Credentials(ABC):
    @abstractmethod
    def get_credentials(self, user_id: str) -> str:
        pass


class AWSSignature(Credentials):
    def get_credentials(self, user_id: str) -> str:
        return "saf322-f32342-r32f2-f3223sa-f323"


class BearerToken(Credentials):
    def get_credentials(self, user_id: str) -> str:
        return "5/efwt43g5y44y3434y3y43y43y3y35y55"


class UsernameAndPasswordCredentials(Credentials):
    def get_credentials(self, user_id: str) -> str:
        return "admin:admin1"


class AuthenticationHandler(ABC):
    @abstractmethod
    def authenticate(self, credentials: Credentials):
        pass

    @abstractmethod
    def supports(self, cls):
        pass


class AWSAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials: Credentials):
        if self.supports(credentials):
            return self.authenticate_in_aws(credentials)
        return None

    def supports(self, cls):
        return isinstance(cls, AWSSignature)

    @staticmethod
    def authenticate_in_aws(credentials):
        return True if credentials.get_credentials("1") else False


class BearerTokenAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials: Credentials):
        if self.supports(credentials):
            return self.is_token_valid(credentials)
        return None

    def supports(self, cls):
        return isinstance(cls, BearerToken)

    @staticmethod
    def is_token_valid(credentials):
        return True if credentials.get_credentials("1") else False


class UsernameAndPasswordAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials: Credentials):
        if self.supports(credentials):
            return self.is_password_valid(credentials)
        return None

    def supports(self, cls):
        return isinstance(cls, UsernameAndPasswordCredentials)

    @staticmethod
    def is_password_valid(credentials):
        return True if credentials.get_credentials("1") else False


class ChainAuthenticationElement:
    def __init__(self, authentication_handler: AuthenticationHandler, next=None):
        self._authentication_handler = authentication_handler
        self._next = next

    def authenticate(self, credentials: Credentials):
        if self._authentication_handler.authenticate(credentials):
            print(f"Authentication using handler {credentials.__class__.__name__}")
            return True
        return self._next and self._next.authenticate(credentials)


if __name__ == "__main__":
    authentication_handler_uap = UsernameAndPasswordAuthenticationHandler()
    authentication_handler_bearer = BearerTokenAuthenticationHandler()
    authentication_handler_aws = AWSAuthenticationHandler()

    last_element = ChainAuthenticationElement(authentication_handler_aws)
    middle_element = ChainAuthenticationElement(
        authentication_handler_bearer, last_element
    )
    first_element = ChainAuthenticationElement(
        authentication_handler_uap, middle_element
    )

    first_element.authenticate(AWSSignature())
    first_element.authenticate(UsernameAndPasswordCredentials())
    first_element.authenticate(BearerToken())
