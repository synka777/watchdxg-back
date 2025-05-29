from rest_framework import serializers
from .models import XAccount, XUser


class XAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = XAccount
        fields = ['id', 'handle']


class XUserSerializer(serializers.ModelSerializer):
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
            'followers_count',
            'featured_url',
            'follower'
        ]