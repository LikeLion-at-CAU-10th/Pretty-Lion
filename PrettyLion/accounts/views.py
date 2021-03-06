from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import get_user_model

User = get_user_model()

def do_duplicate_check(request):
    print('아이디 중복 체크')
    user_id = request.GET.get('user_id')
    try:
        # 중복 검사 실패
        _id = User.objects.get(user_id=user_id)
    except:
        # 중복 검사 성공
        _id = None
    if _id is None:
        duplicate = "pass"
    else:
        duplicate = "fail"
    context = {'duplicate': duplicate}


# Create your views here.
def signup(request):
    if request.method == 'POST' or request.method == "FILES":
            if request.POST['password'] == request.POST['password_check']:
                if request.POST.get("mento_selection") == "mento":
                    is_mento = True
                else:
                    is_mento = False

                try:
                    user = User.objects.create_user(
                    username =request.POST["username"],
                    password =request.POST['password'],
                    nickname =request.POST['nickname'],
                    bio=request.POST['bio'],
                profile_photo =request.FILES.get('profile_photo'),
                is_staff  =is_mento)
                
                    auth.login(request, user)
                    return redirect('index')
                except IntegrityError:
                    return render(request, 'signup.html', {'id_unique_error' : "아이디가 이미 존재합니다."})
                
            else:
                return render(request, "signup.html", {'password_error'
                                                       : "비밀번호를 잘 못 입력하셨습니다!"})
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        userid = request.POST.get("username")
        pw = request.POST.get("password")
        user = auth.authenticate(request, username=userid, password=pw)
        print(userid, pw)
        if user is not None:
            print("user존재")
            auth.login(request, user)
            return redirect('index')
        else:
            print("user 없음")
            return render(request, 'login.html')
    else:
        
        return render(request, 'login.html')
        


def logout(request):
    auth.logout(request)
    return redirect('index')

