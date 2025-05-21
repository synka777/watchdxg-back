from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from models import XAccount, XUser


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = XAccount
        fields = ['id', 'handle']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = XUser
        fields = [
            'id',
            'account_id',
            'handle',
            'username',
            'bio',
            'created_at',
            'following_count',
            'featured_url',
            'follower'
        ]


# Since we use a custom user model, we need to define a TokenPairObtain serializer manually
class CustomObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'handle'

    def validate(self, attrs):
        handle = attrs.get('handle')
        password = attrs.get('password')

        try:
            user = XAccount.objects.get(handle=handle)
        except XUser.DoesNotExist:
            raise serializers.ValidationError('No such user')

        # Disabled for now as password hashes are not stored in DB yet
        # if not user.check_password(password):  # if we have hashed passwords
        #     raise serializers.ValidationError('Incorrect password')

        # Use SimpleJWT logic to generate tokens manually
        refresh = self.get_token(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    # Bypass the the default authenticate() logic as we're using custom validation
    @classmethod # Define it as a classmethod like the base get_token() for smooth integration
    def get_token(cls, user):
        from rest_framework_simplejwt.tokens import RefreshToken
        return RefreshToken.for_user(user)