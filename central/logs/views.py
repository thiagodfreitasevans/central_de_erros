# Django
from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Rest
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Project
from .models import Log
from .serializers import LogSerializer
from .permissions import IsOwner
from .filters import LogFilterSet
# Create your views here.
class ListLogsViewset(generics.ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [IsOwner, IsAuthenticated,]
    filterset_class = LogFilterSet

    def post(self, request, format=None):
        context = {
            "request": self.request,
        }
        log = LogSerializer(data=request.data, context=context)
        if log.is_valid():
            log.save()
            return Response(log.data, status=status.HTTP_201_CREATED)
        return Response(log.errors, status=status.HTTP_400_BAD_REQUEST)
class LogViewset(APIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [IsOwner, IsAuthenticated]
    def get(self, request, pk, format=None):
        queryset = get_object_or_404(Log.objects.all(), pk=pk)
        serializer = LogSerializer(queryset)
        return Response(serializer.data)    
    def patch(self, request, pk):
        log = get_object_or_404(Log.objects.all(), pk=pk)
        serializer = LogSerializer(log, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        log = get_object_or_404(Log.objects.all(), pk=pk)
        log.delete()
        return Response({"Requested log was deleted.".format(pk)},status=204)


