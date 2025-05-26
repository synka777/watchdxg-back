from .serializers import XUserSerializer, XAccountSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import XUser, XAccount


class XUserListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = XUserSerializer

    def get_queryset(self):
        queryset = XUser.objects.all() # Define queryset IN get_queryset()
        account_id = self.request.query_params.get('account_id')
        if account_id:
            queryset = queryset.filter(account_id=account_id)
        return queryset


class XAccountRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = XAccountSerializer
    queryset = XAccount.objects.all()
    lookup_field = 'handle'