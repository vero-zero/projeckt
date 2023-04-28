from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Gameuser
from django.utils import timezone
# Create your views here.
def main(request):
    if request.method == "POST":
        nickname = request.POST.get("user")
        if nickname != "":
            try:
                _id = Gameuser.objects.get(name=nickname)
            except:
                _id = None
            if _id is None:
                msg = "사용가능한 닉네임 입니다."
                u = Gameuser( name = nickname, c_date=timezone.now())
                u.save()
                return render(request, 'game/main.html', {'msg': msg})
            else:   
                error_msg = "중복된닉네임입니다."
                return render(request, 'game/main.html', {'error_msg': error_msg})
    return render(request, "game/main.html")

def gameing(request):
    return render(request, "gameing.html")
    
#def over(request):