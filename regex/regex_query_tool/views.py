from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import RegexForm
import re


def regex(request):

    form = RegexForm()

    if request.method == "POST":

        form = RegexForm(request.POST)

        if form.is_valid():
            text        = form.cleaned_data.get('text')
            expression  = form.cleaned_data.get('regex_text')
            
            try:
                matched = re.findall(expression, text)

            except:
                error   = "Expression not valid"
                context = {"form":form, "error": error}
                return render(request, "regex_query/index.html", context=context)

            else:
                context = {"matched": matched, "form":form}
                return render(request, "regex_query/index.html", context=context)


    return render(request, "regex_query/index.html", context={"form": form})