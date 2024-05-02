from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm
from .models import News, Category
from .models import PHOTOGRAPHY
def news_list_view(request):
    news_list_slide = News.pulished.all()
    latest_news_5 = News.pulished.all()[:5]
    iqtisodiy_news_one = News.pulished.filter(category__nomi='Iqtisodiyot')[0]
    iqtisodiy_news_4 = News.pulished.filter(category__nomi='Iqtisodiyot')[1:5]
    sport_news_one = News.pulished.filter(category__nomi='Sport')[0]
    sport_news_4 = News.pulished.filter(category__nomi='Sport')[1:5]
    texnologiya_news_one = News.pulished.filter(category__nomi='Texnologiya')[0]
    texnologiya_news_4 = News.pulished.filter(category__nomi='Texnologiya')[1:5]
    siyosiy_news_one = News.pulished.filter(category__nomi='Siyosat')[0]
    siyosiy_news_4 = News.pulished.filter(category__nomi='Siyosat')[1:5]
    rasmlar = PHOTOGRAPHY.objects.all()


    context = {
        'news_list': news_list_slide,
        'latest_news_5' : latest_news_5,
        'iqtisodiy_news_one' : iqtisodiy_news_one,
        'iqtisodiy_news_4' : iqtisodiy_news_4,
        'sport_news_one' : sport_news_one,
        'sport_news_4' : sport_news_4,
        'texnologiya_news_one' : texnologiya_news_one,
        'texnologiya_news_4' : texnologiya_news_4,
        'siyosiy_news_one' : siyosiy_news_one,
        'siyosiy_news_4' : siyosiy_news_4,
        'rasmlar' : rasmlar

    }

    return render(request,template_name='index.html', context=context)
def news_detail_view(request, slug):
    news_detail = News.pulished.get(slug = slug)
    yaqin_news = News.pulished.filter(category__nomi=news_detail.category)[:3]
    context = {
        'news_detail': news_detail,
        'yaqin_news': yaqin_news
    }
    return render(request,template_name='single_page.html', context=context)

def texno_news_view(request):
    news_list = News.pulished.filter(category__nomi = 'Texnologiya')

    context = {
        'news_list' : news_list
    }
    return render(request, template_name='texno.html', context=context)

def mahalliy_news_view(request):
    news_list = News.pulished.filter(category__nomi = 'Mahalliy')
    context = {
        'news_list' : news_list
    }
    return render(request, template_name='mahalliy.html', context=context)

def xorij_news_view(request):
    news_list = News.pulished.filter(category__nomi = 'Xorij')
    context = {
        'news_list' : news_list
    }
    return render(request, template_name='xorij.html', context=context)
def siyosat_news_view(request):
    news_list = News.pulished.filter(category__nomi = 'Siyosat')
    context = {
        'news_list' : news_list
    }
    return render(request, template_name='siyosat.html', context=context)
def iqtisodiyot_news_view(request):
    news_list = News.pulished.filter(category__nomi = 'Iqtisodiyot')
    context = {
        'news_list' : news_list
    }
    return render(request, template_name='iqtisodiyot.html', context=context)
def sport_news_view(request):
    news_list = News.pulished.filter(category__nomi = 'Sport')
    context = {
        'news_list' : news_list
    }
    return render(request, template_name='sport.html', context=context)
def contact_view(request):
    form = ContactForm(request.POST)
    if form.is_valid() and request.method == 'POST' :
        form.save()
        return HttpResponse("Xabaringiz muvoffaqiyatli yuborildi")
    context = {
        'form' : form
    }

    return render(request, template_name='contact.html' , context = context)

def about_us_view(request):
    context = {

    }
    return render(request, template_name='about.html', context=context)
