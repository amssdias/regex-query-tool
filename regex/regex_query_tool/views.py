from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def regex(request):
    if request.method == "POST":
        print(request.POST['text'])
        print(request.POST['regex_text'])

        return HttpResponseRedirect(reverse("regex"))

    return render(request, "regex_query/index.html")