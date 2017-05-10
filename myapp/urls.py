from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # sinh vien
    url(r'^sinhvien/them$', views.sinhvien_them, name="sinhvien_them"),
    url(r'^sinhvien/add_sv$', views.add_sv, name="add_sv"),
    url(r'^sinhvien/chinhsua$', views.sinhvien_sua, name="sinhvien_sua"),
    url(r'^sinhvien/edit_sv$', views.edit_sv, name="edit_sv"),
    url(r'^sinhvien/timkiem$', views.sinhvien_timkiem, name="sinhvien_timkiem"),
    url(r'^sinhvien/search_sv$', views.search_sv, name="search_sv"),
    # detai
    url(r'^detai/them$', views.detai_them, name="detai_them"),
    url(r'^detai/chinhsua$', views.detai_sua, name="detai_sua"),
    url(r'^detai/timkiem$', views.detai_timkiem, name="detai_timkiem"),
    # giang vien
    url(r'^giangvien/them$', views.giangvien_them, name="giangvien_them"),
    url(r'^giangvien/add_gv$', views.add_gv, name="add_gv"),
    url(r'^giangvien/chinhsua$', views.giangvien_sua, name="giangvien_sua"),
    url(r'^giangvien/edit_gv$', views.edit_gv, name="edit_gv"),
    url(r'^giangvien/timkiem$', views.giangvien_timkiem, name="giangvien_timkiem"),
    url(r'^giangvien/search_gv$', views.search_gv, name="search_gv"),
    # hoi dong
    url(r'^hoidong/them$', views.hoidong_them, name="hoidong_them"),
    url(r'^hoidong/chinhsua$', views.hoidong_sua, name="hoidong_sua"),
    url(r'^hoidong/timkiem$', views.hoidong_timkiem, name="hoidong_timkiem"),
]
