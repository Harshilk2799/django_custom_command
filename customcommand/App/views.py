from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.management import call_command
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, "index.html")

@csrf_exempt
def print_message(request):
    if request.method == "POST":
        try:
            call_command("print_message")
            messages.success(request, "Success! Check Terminal")
        except Exception as e:
            print(e)
        return redirect("/")
    else:
        return redirect("/")