from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_predictions.models import Prediction

@api_view(['POST'])
def add_prediction(request):
    loan_id = request.data.get('loan_id')
    predict = request.data.get('predict')

    prediction = Prediction(loan_id=loan_id, predict=predict)
    prediction.save()
    
    return Response("Prediction added successfully")




def home(request):
    
    return HttpResponse('Информация по запросам по адресу /info')

   
def info(request):
    
    return HttpResponse(""" 
<p>
    Для отправки по API POST запроса с предсказанием модели по ипотечному кредитованию,
</p>
<p>
    полученного из Airflow, данные нужно подать в виде .json на URL 'http://localhost:8000/api/airflow/'
</p>
<p>
    Пример запроса:
    response = requests.post(URL, data=from_airflow.json, headers={'Content-Type': 'application/json'})
</p>

<p>  
    ___________________________________________________________________________________________________
</p>

<p>  
    Админка доступна по адресу /admin
</p>
""")
