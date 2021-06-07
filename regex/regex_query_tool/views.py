from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import re

# Create your views here.
def regex(request):
    if request.method == "POST":
        text = request.POST['text']
        expression = request.POST['regex_text']
        matched = re.findall(expression, text)

        context = {"matched": matched, "text":text, "expression": expression}
        return render(request, "regex_query/index.html", context=context)

    return render(request, "regex_query/index.html")