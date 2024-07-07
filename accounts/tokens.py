from rest_framework_simplejwt.tokens import RefreshToken

class CustomRefreshToken(RefreshToken):
    @classmethod
    def for_user(cls, user):
        token = super().for_user(user)
        token["email"] = user.email  # Add the email to the token payload
        token["firstName"] = user.firstName  # Add the firstname to the token payload
        token["lastName"] = user.lastName  # Add the lastname to the token payload
        token["phone"] = user.phone  # Add the phone to the token payload
        return token


def get_tokens_for_user(user):
    refresh = CustomRefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }