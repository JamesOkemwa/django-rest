from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    body = request.body # byte string of JSON data
    data = {}

    try:
        data = json.loads(body) # string of JSON data -> Python Dictionary
    except:
        pass

    print(data)
    print(request.GET) # url query params
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    data["params"] = dict(request.GET)
    return JsonResponse(data)
