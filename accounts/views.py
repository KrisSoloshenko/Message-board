from django.shortcuts import render, redirect

from .models import Code


def confirm_user(request):
    random_code = request.POST['random_code']
    code = Code.objects.filter(code=random_code)
    if code.exists():
        obj = Code.objects.get(code=random_code)
        obj.user.is_active=True
        obj.user.is_staff=True
        obj.code = 0
        obj.save()
        obj.user.save()
    else:
        return render(request, 'invalid_code.html')
    return redirect('account_login')
