import asyncio
import time

import aiohttp
import requests
from django.db.models import Q
from django.http import JsonResponse

from app.models import Item


def hard(request):
    count = Item.objects.filter(Q(value__gt=500) & Q(name__icontains="a")).count()
    return JsonResponse({"count": count})


async def ahard(request):
    count = await Item.objects.filter(
        Q(value__gt=500) & Q(name__icontains="a")
    ).acount()
    return JsonResponse({"count": count})


def easy(request):
    count = Item.objects.filter(value__gt=500).count()
    return JsonResponse({"count": count})


async def aeasy(request):
    count = await Item.objects.filter(value__gt=500).acount()
    return JsonResponse({"count": count})


def sync_with_api(request):
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        external_data = response.json()
        return JsonResponse({"status": "success"})
    return JsonResponse({"error": "Failed to fetch API data"}, status=500)


async def async_with_api(request):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://jsonplaceholder.typicode.com/posts"
        ) as response:
            if response.status == 200:
                external_data = await response.json()
                return JsonResponse({"status": "success"})
            return JsonResponse({"error": "Failed to fetch API data"}, status=500)


def sync_sleep(request):
    time.sleep(1)
    return JsonResponse({"status": "success"})


async def async_sleep(request):
    await asyncio.sleep(1)
    return JsonResponse({"status": "success"})
