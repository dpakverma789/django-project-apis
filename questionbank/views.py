from django.http import HttpResponse
from django.http import JsonResponse
from . models import QuestionBank
from . serializers import QuestionBankSerializer


def question_bank(request):
    all_question = QuestionBank.objects.all()
    serializer = QuestionBankSerializer(all_question, many=True)
    return JsonResponse(serializer.data, safe=False)


def home(request):
    html_tag = """
                <h1>Welcome to the APIs</h1>
                <h5>Available urls for apis are</h5>
                <ol>
                    <li>
                        <a href="https://djangoapii.herokuapp.com/employee">
                            https://djangoapii.herokuapp.com/employee
                        </a>
                    </li>
                    <li>
                        <a href="https://djangoapii.herokuapp.com/cart/cart-items">
                            https://djangoapii.herokuapp.com/cart/cart-items
                        </a>
                    </li>
                    <li>
                        <a href="https://djangoapii.herokuapp.com/quiz">
                            https://djangoapii.herokuapp.com/quiz
                        </a>
                    </li>
                </ol>
    """
    return HttpResponse(html_tag)
