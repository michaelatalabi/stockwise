from django.shortcuts import render

from django.http import JsonResponse
from .services.stock_service import get_stock_data

def stock_data(request, symbol):
    try:
        data = get_stock_data(symbol)
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
