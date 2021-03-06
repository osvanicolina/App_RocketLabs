from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class UnlockAccountTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + user.password + six.text_type(timestamp) +
            six.text_type(user.profile.is_blocked)
        )

unlock_account_token = UnlockAccountTokenGenerator()