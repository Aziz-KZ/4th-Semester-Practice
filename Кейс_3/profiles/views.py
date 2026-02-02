from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile

def home(request):
    greeting = None
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            if name.strip():
                profile = Profile(name=name)
                profile.save()
                greeting = f"Привет, {name}!"
            else:
                greeting = "Имя не может быть пустым."
    else:
        form = ProfileForm()
    return render(request, "home.html", {"form": form, "greeting": greeting})

