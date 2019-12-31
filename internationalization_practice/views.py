from django.shortcuts import render
from django.conf import settings
from django import shortcuts
from django.http import HttpResponse
from django.utils.translation import ugettext as _

res = None

# Create your views here.


def test_get_str():
    global res
    res = _("hello world")


def say_hello(request):
    # t = Thread(target=test_get_str)
    # t.start()
    # t.join()
    return HttpResponse(_("hello world"))


def switch_language(request):
    # Language
    lang_code = request.GET.get('language')
    next = request.GET.get('next')
    response = shortcuts.redirect(next)
    # if lang_code and translation.check_for_language(lang_code):
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code,
                        expires=36000,
                        domain='127.0.0.1')
    return response


def test2_view(request):
    code = _("hello world")
    response_context = {'lang': request.LANGUAGE_CODE,
                        'code': code,
                        'next': request.get_full_path(),
                        'languages': [l[0] for l in settings.LANGUAGES]}
    resp = render(request, 'internationlization/switch_language.html',
                              context=response_context)
    return resp
