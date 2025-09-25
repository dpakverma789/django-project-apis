from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from .models import QuestionBank
from .serializers import QuestionBankSerializer


def question_bank(request):
    all_question = QuestionBank.objects.all()
    serializer = QuestionBankSerializer(all_question, many=True)
    return JsonResponse(serializer.data, safe=False)


def home(request: HttpRequest):
    base_domain = request.get_host()
    html_tag = f"""
                <h1>Welcome to the APIs</h1>
                <h5>Available urls for apis are</h5>
                <ol>
                    <li>
                        Employee Details API:
                        <a href="/employee" target="_blank">
                            {base_domain}/employee
                        </a>
                    </li>
                    <li>
                        Shopping Cart Details API: 
                        <a href="/cart/cart-items" target="_blank">
                            {base_domain}/cart/cart-items
                        </a>
                    </li>
                    <li>
                        Quiz Game Questions API: 
                        <a href="/quiz" target="_blank">
                            {base_domain}/quiz
                        </a>
                    </li>
                    <li> Show Box Theater APIs: 
                       <ul>
                             <li>
                                <a href="/show/shows" target="_blank">
                                    {base_domain}/show/shows
                                </a>
                            </li>
                            <li>
                                <a href="/show/theaters" target="_blank">
                                    {base_domain}/show/theaters
                                </a>
                            </li>
                            <li>
                                <a href="/show/booking" target="_blank">
                                    {base_domain}/show/booking
                                </a>
                            </li>
                       </ul>
                    </li>
                </ol>
    """
    return HttpResponse(html_tag)
