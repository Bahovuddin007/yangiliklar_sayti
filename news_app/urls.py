from django.urls import path
from .views import news_list_view, news_detail_view, contact_view, about_us_view, texno_news_view, mahalliy_news_view, \
    xorij_news_view, siyosat_news_view, iqtisodiyot_news_view, sport_news_view

urlpatterns = [
    path('', news_list_view, name = 'home_page'),
    path('texnologiya/', texno_news_view, name = 'texno_news'),
    path('mahalliy/', mahalliy_news_view, name = 'mahalliy_news'),
    path('xorij/', xorij_news_view, name = 'xorij_news'),
    path('siyosat/', siyosat_news_view, name = 'siyosat_news'),
    path('iqtisodiyot/', iqtisodiyot_news_view, name = 'iqtisodiyot_news'),
    path('sport/', sport_news_view, name = 'sport_news'),
    path('<str:slug>', news_detail_view, name = 'detail_page'),
    path('contact-us/', contact_view, name = 'contact_page'),
    path('about/', about_us_view, name = 'about_us_page'),
]
