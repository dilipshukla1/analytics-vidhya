from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)

    import json
    data = json.loads(request.body)
    user = authenticate(
        request,
        username=data.get("email"),
        password=data.get("password"),
    )

    if user is None:
        return JsonResponse({"error": "Invalid credentials"}, status=401)

    login(request, user)
    return JsonResponse({"message": "Logged in"})


def profile_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Not logged in"}, status=401)

    return JsonResponse({
        "email": request.user.email,
        "id": request.user.id
    })

