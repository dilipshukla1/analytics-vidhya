from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

@csrf_exempt
def login_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid method'}, status=405)

    body = json.loads(request.body)
    user = authenticate(username=body.get('email'), password=body.get('password'))

    if not user:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)

    login(request, user)
    return JsonResponse({'message': 'Logged in'})


def public_info(request):
    return JsonResponse({'status': 'public-ok'})


@login_required
def user_profile(request):
    user = request.user
    return JsonResponse({'id': user.id, 'email': user.email})
