from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShowBox
from .serializers import ShowBoxSerializers
from django.http import JsonResponse


class ShowBoxView(APIView):

    # to retrieve all records or record based on id and name of product
    def get(self, request, id=None, show_name=None):
        if id:
            item = ShowBox.objects.get(id=id)
            serializer = ShowBoxSerializers(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        if show_name:
            item = ShowBox.objects.get(show_name=show_name)
            serializer = ShowBoxSerializers(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        # items = ShowBox.objects.all()
        # serializer = ShowBoxSerializers(items, many=True)
        # return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

# def get(request):
#     items = ShowBox.objects.all()
#     serializer = ShowBoxSerializers(items, many=True)
#     return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)