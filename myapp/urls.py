from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # sinh vien
    url(r'^sinhvien/them$', views.sinhvien_them, name="sinhvien_them"),
    url(r'^sinhvien/chinhsua$', views.sinhvien_sua, name="sinhvien_sua"),
    url(r'^sinhvien/timkiem$', views.sinhvien_timkiem, name="sinhvien_timkiem"),
    # detai
    url(r'^detai/them$', views.detai_them, name="detai_them"),
    url(r'^detai/chinhsua$', views.detai_sua, name="detai_sua"),
    url(r'^detai/timkiem$', views.detai_timkiem, name="detai_timkiem"),
    # giang vien
    url(r'^giangvien/them$', views.giangvien_them, name="giangvien_them"),
    url(r'^giangvien/chinhsua$', views.giangvien_sua, name="giangvien_sua"),
    url(r'^giangvien/timkiem$', views.giangvien_timkiem, name="giangvien_timkiem"),
    # hoi dong
    url(r'^hoidong/them$', views.hoidong_them, name="hoidong_them"),
    url(r'^hoidong/chinhsua$', views.hoidong_sua, name="hoidong_sua"),
    url(r'^hoidong/timkiem$', views.hoidong_timkiem, name="hoidong_timkiem"),
]
