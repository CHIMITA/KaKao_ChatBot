from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def keyboard(request): # 카카오톡에 버튼 정보 보냄
    return JsonResponse({
        'type':'buttons',
        'buttons':['오늘!','내일!']
    })

def answer(request): # 각 버튼 응답 내용
    json_str = ((request.body).decode('utf-8'))
    json_data = json.loads(json_str)
    dataContent = json_data['content']

    if dataContent == '오늘!':
        today = "오늘 급식"

        return JsonResponse({
            'message': {
                'text':today
            },
            'keyboard': {
                'type':'buttons',
                'buttons':['오늘!','내일!']
            }
        })
    elif dataContent == '내일!':
        tomorrow = "내일 급식"

        return JsonResponse({
            'message': {
                'text':tomorrow
            },
            'keyboard': {
                'type':'buttons',
                'buttons':['오늘!','내일!']
            }
        })