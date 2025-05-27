import json

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Student




def t(request):
    return render(request, "sysfortest/testdeepseek.html")

def first(request):
    if request.method == "POST":
        print(request.POST)
        password = request.POST["password"]
        username = request.POST["username"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect(test)
        else:
            return redirect(registration)
            # user = User.objects.create_user(login1, password=password, email=email)
            # user.save()
            # user = authenticate(request, username=login1, password=password, email=email)
            # request.user = user
            #
            # login(request, user)
            # return redirect(test)

    else:
        return render(request, "sysfortest/first.html")


def leaderboard(request):
    leaders = Student.objects.order_by("best_time")
    print(leaders.first().user.username)
    if len(leaders)>100:
        leaders = leaders[0:100]
    return render(request,"sysfortest/leaderboard.html",context={"leaders":leaders})

def test(request):
    return render(request, "sysfortest/second.html")
def primer_ex(request):
    if request.method == "POST":
        data = request.body
        data = data.decode("utf-8")
        data = json.loads(data)
        print(data["score"])
        buf = {}
        stdent = Student.objects.filter(user=request.user).first()
        print(stdent.user.username)
        print(stdent.results)

        print(stdent.results)
        stdent.results['primer'].append([data["score"],data["time"]])
        if stdent.best_time > data["time"] and data["score"]==10:
            stdent.best_time = data["time"]
        stdent.save()


        #
        # with open("sysfortest/results.json","r") as jsonf:
        #     buf = json.loads(jsonf.read())
        #     try:
        #         buf[request.user.username]["primer"].append([data["score"],data["time"]])
        #     except:
        #         buf[request.user.username] = {"primer":[],"slova":[]}
        #         buf[request.user.username]["primer"].append([data["score"],data["time"]])

        print(stdent.results)
        # with open("sysfortest/results.json", "w") as jsonff:
        #     json.dump(buf, jsonff)
    return render(request, "sysfortest/primer_test.html")

def profile(request):
    return render(request ,"sysfortest/profile.html",context={"name":request.user.username})
def words_test(request):
    if request.method == "POST":
        print("POST ON WOOORDS")
        data = request.body
        data = data.decode("utf-8")
        data = json.loads(data)
        print(data["score"])
        buf = {}
        stdent = Student.objects.filter(user=request.user).first()
        stdent.results['slova'].append(data["score"])
        stdent.save()
        return JsonResponse({"result": data["score"]})

        # with open("sysfortest/results.json","r") as jsonf:
        #     buf = json.loads(jsonf.read())
        #     try:
        #         buf[request.user.username]["slova"].append(data["score"])
        #     except:
        #         buf[request.user.username] = {"primer":[],"slova":[]}
        #         buf[request.user.username]["slova"].append(data["score"])
        #
        #     print(buf)
        # with open("sysfortest/results.json", "w") as jsonff:
        #     json.dump(buf, jsonff)
    else:
        return render(request, "sysfortest/words_test.html")


def registration(request):
    if request.method == "POST":
        print("PSOR reg \n")
        logi1n = request.POST["login"]
        password1 = request.POST["password"]
        email = request.POST["email"]
        user = User.objects.create_user(logi1n,email,password1)
        user.save()

        user = authenticate(request,username=logi1n,password=password1)
        st = Student()
        st.user = user
        st.avg_time = "0"
        st.test_passed = 0
        st.save()
        login(request, user)
        return redirect(test)
    else:
        return render(request, "sysfortest/reg.html")

def api(request, number=0):
    if request.method == "POST":
        data = request.body
        data = data.decode("utf-8")
        data = json.loads(data)
        my_field = data["post_data"]
        name = data["post_name"]
        print(type(my_field))
        return JsonResponse({"massage": f"data received,Hi {name}, your score is {my_field}"},safe=False)
    if request.method == "GET":
        if request.user.is_authenticated:
            buf = {}
            #with open("/home/IDenI/Memory-development-site/sysfortest/words.json") as jsonf:
            with open("sysfortest/words.json") as jsonf:
                buf = json.loads(jsonf.read())
            return JsonResponse(buf)


    else:
        return JsonResponse({"error": "Bad request"}, status=400)

def results_sender(request):
    try:
        stdent = Student.objects.filter(user=request.user).first()
        return  JsonResponse({"results":stdent.results})
    except:
        redirect(first)
