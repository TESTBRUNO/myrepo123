from django.shortcuts import render
from myapp.models import books
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect


def index(request):
    user = User.objects.filter(username = request.session.get("user_name",False))
    if request.method == "POST":
      data = request.POST
      new = books(name = data["field1"], author = data["field2"], count =   data["field3"])
      new.save()

    res = books.objects.all()
    #res = books.objects.filter(id=2)
    return render(request, 'index.html', {"test":res, "username":user})




def card(request, id):
  if request.session.get("is_auth",False)==True:
    book = books.objects.filter(id = id)
    return render(request,"card.html", {"id":book})
  else:
    return redirect(auth)



def auth(request):
  if request.method == "POST":
    data = request.POST
    user = authenticate(username=data["login"], password=data["psw"])
    if user:
      request.session["is_auth"] = True
      request.session["user_name"] = user.username
      
      #return HttpResponse(f"Привет,{user.username} {request.session.get#('is_auth', False)} user.id ")
      return render(request, 'auth.html',{"username":user})
      
    else:
      return HttpResponse(f"Сбой #авторизации")
  else: 
    return render(request, 'auth.html')



def reg(request):
  if request.method == "POST":
     data = request.POST
     user = User.objects.create_user(data["login"],"",data["psw"])
     user.save()

  return render(request,'auth.html')


#from django.contrib.auth.models import User

#from django.contrib.auth import authenticate