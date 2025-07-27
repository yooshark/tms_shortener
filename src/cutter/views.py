from django.http.request import HttpRequest
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
)
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from cutter.forms import URLForm
from cutter.models import Urls
from cutter.service import load_url, get_random_string


def index(request:HttpRequest) -> HttpResponse:
    return render(request, 'cutter/index.html')

def redirect_hash(request: HttpRequest, url_hash: str) -> HttpResponseRedirect | HttpResponse:
    if url_hash == "favicon.ico":
        return HttpResponse(status=204)
    return redirect(load_url(url_hash).original_url)

def shorten_post(request: HttpRequest) -> HttpResponse:
    form = URLForm(request.POST)
    if not form.is_valid():
        return render(request, 'cutter/index.html', {'invalid_url': request.POST['url']})
    shortened_url_hash = make_shorten(form.cleaned_data['url'])
    shortened_url = request.build_absolute_uri(reverse('redirect', args=[shortened_url_hash]))
    return render(request, 'cutter/link.html', {'shortened_url': shortened_url})


def make_shorten(url: str) -> str:
    random_hash = get_random_string()
    mapping = Urls(original_url=url, hash=random_hash, created_at=timezone.now())
    mapping.save()
    return random_hash

