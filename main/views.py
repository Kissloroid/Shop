from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Kissloroid'
        context['content'] = 'Магазин мебели'

        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Kissloroid-about'
        context['content'] = 'О нас'
        context['text_on_page'] = 'Всяка ересь'
        return context


# def index(request):
#     context = {
#         'title': 'Kissloroid',
#         'content': 'Главная страница - HOME',
#     }
#
#     return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': "Текст о том почему этот магазин такой классный и какой хороший товар"

    }

    return render(request, 'main/about.html', context)
