from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from . models import Employees
from . serializers import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
import io


# Create your views here.
class EmployeeList(APIView):

    def get(self, request):
        all_employee = Employees.objects.all()
        serializer = EmployeeSerializer(all_employee, many=True)
        return JsonResponse(serializer.data, safe=False)
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type='application/json')
        # return Response(serializer.data)

    @csrf_exempt
    def post_request(request):
        if request.method == 'POST':
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serializer = EmployeeSerializer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Record Updated!'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
