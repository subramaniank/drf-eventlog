from rest_framework import authentication, exceptions


class TestAppAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        raise exceptions.AuthenticationFailed('No such user')
