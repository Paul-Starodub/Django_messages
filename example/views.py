from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        print(request.POST["email"])
        print(request.POST["password"])

        if request.POST["password"] == "password":
            messages.error(request, "Your password isn't complex enough")
            return redirect("example:index")

        messages.info(request, "This is the info message!")
        messages.error(request, "ERROR! ERROR!")
        messages.success(request, "You registered succesfully")
        messages.warning(request, "Be careful!")

        return redirect("example:show_messages")

    return render(request, "example/index.html")


def show_messages(request: HttpRequest) -> HttpResponse:
    return render(request, "example/show_messages.html")
