from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HomeView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        dct = {"msg" : "jwt authentication created successfully.."}
        return Response(dct)
