from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, email, timestamp):
        print(user.pk)
        print("EMAIL" + str(email))
        print("TIMESTAMP", str(timestamp))
        return (
                text_type(user.pk) + text_type(timestamp) +
                text_type(email)
        )


account_activation_token = AccountActivationTokenGenerator()
