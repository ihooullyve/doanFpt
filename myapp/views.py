from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.contrib.messages import constants as messages
from myapp.models import ThongTin, DeTai, HoiDong
import json
import datetime


def index(request):
    return render(request, 'home/index.html')

# sinh vien


def sinhvien_them(request):
    detai = DeTai.objects.all()
    return render(request, 'sinhvien/add-new.html', {'detai': detai})


def add_sv(request):
    ten = request.POST.get('name')
    lop = request.POST.get('lop')
    madt = request.POST.get('madt')
    mssv = request.POST.get('mssv')

    user = User(username=mssv, password='A123123Z')
    user.set_password('A123123Z')
    user.save()
    # lay ma de tai
    detai = DeTai.objects.get(msdt=madt)
    #  save thong tin
    thongtin = ThongTin(user=user, ma_so=mssv, ho_ten=ten,
                        lop=lop, ma_detai=detai, choice='sv')
    thongtin.save()

    return HttpResponseRedirect('/sinhvien/them')


def sinhvien_sua(request):
    thongtin = ThongTin.objects.get(user__id=18)
    detai = DeTai.objects.all()
    return render(request, 'sinhvien/edit.html', {'data': thongtin, 'detai': detai})


def edit_sv(request):
    ten = request.POST.get('name')
    lop = request.POST.get('lop')
    madt = request.POST.get('madt')
    mssv = request.POST.get('mssv')

    user = User.objects.get(id=18)
    user.username = mssv
    user.save()

    detai = DeTai.objects.get(msdt=madt)
    thongtin = ThongTin.objects.get(user__id=18)
    thongtin.lop = lop
    thongtin.ma_detai = detai
    thongtin.ho_ten = ten
    thongtin.save()
    print('save!!!!')

    return HttpResponseRedirect('/sinhvien/chinhsua')


def sinhvien_timkiem(request):
    return render(request, 'sinhvien/search.html')


def search_sv(request):
    print('========= search =============')
    keywork = request.GET.get('keywork')
    print(keywork)
    thongtin = ThongTin.objects.filter(ma_so__contains=keywork)
    print(thongtin)
    return render(request, 'sinhvien/result.html', {'data': thongtin})
    # return HttpResponse(thongtin)


def detai_them(request):
    return render(request, 'detai/add-new.html')


def add_dt(request):
    name = request.POST.get('name')
    madt = request.POST.get('madt')

    detai = DeTai(msdt=madt, tendt=name)
    detai.save()

    return HttpResponseRedirect('/detai/them')


def detai_sua(request):
    detai = DeTai.objects.get(id=4)
    return render(request, 'detai/edit.html', {'data': detai})


def edit_dt(request):
    name = request.POST.get('name')
    madt = request.POST.get('madt')

    detai = DeTai.objects.get(id=4)
    detai.tendt = name
    detai.msdt = madt
    detai.save()

    return HttpResponseRedirect('/detai/chinhsua')


def detai_timkiem(request):
    return render(request, 'detai/search.html')


def search_dt(request):
    print('========= search =============')
    keywork = request.GET.get('keywork')
    print(keywork)
    detai = DeTai.objects.filter(msdt__contains=keywork)
    print(detai)
    return render(request, 'detai/result.html', {'data': detai})

#  giang vien


def giangvien_them(request):
    return render(request, 'giangvien/add-new.html')


def add_gv(request):
    name = request.POST.get('name')
    msgv = request.POST.get('msgv')
    diachi = request.POST.get('diachi')
    email = request.POST.get('email')
    sdt = request.POST.get('sdt')
    hocvi = request.POST.get('hocvi')
    chuyennganh = request.POST.get('chuyennganh')

    user = User(username=msgv, password='A123123Z')
    user.set_password('A123123Z')
    user.save()

    thongtin = ThongTin(user=user, ma_so=msgv, ho_ten=name, dia_chi=diachi,
                        email=email, sdt=sdt, hoc_vi=hocvi, chuyen_nganh=chuyennganh, choice='gv')
    thongtin.save()

    return HttpResponseRedirect('/giangvien/them')


def giangvien_sua(request):
    thongtin = ThongTin.objects.get(user__id=6)
    return render(request, 'giangvien/edit.html', {'data': thongtin})


def edit_gv(request):
    name = request.POST.get('name')
    msgv = request.POST.get('msgv')
    diachi = request.POST.get('diachi')
    email = request.POST.get('email')
    sdt = request.POST.get('sdt')
    hocvi = request.POST.get('hocvi')
    chuyennganh = request.POST.get('chuyennganh')

    user = User.objects.get(id=6)
    user.username = name
    user.save()

    thongtin = ThongTin.objects.get(user__id=6)
    thongtin.ho_ten = name
    thongtin.ma_so = msgv
    thongtin.dia_chi = diachi
    thongtin.email = email
    thongtin.sdt = sdt
    thongtin.hocvi = hocvi
    thongtin.chuyennganh = chuyennganh
    thongtin.save()

    return HttpResponseRedirect('/giangvien/chinhsua')


def giangvien_timkiem(request):
    return render(request, 'giangvien/search.html')


def search_gv(request):
    print('========= search =============')
    keywork = request.GET.get('keywork')
    print(keywork)
    thongtin = ThongTin.objects.filter(ma_so__contains=keywork)
    print(thongtin)
    return render(request, 'giangvien/result.html', {'data': thongtin})

# hoi dong


def hoidong_them(request):
    thongtin = ThongTin.objects.filter(choice='gv')
    return render(request, 'hoidong/add-new.html', {'thongtin': thongtin})


def add_hd(request):

    mahd = request.POST.get('mahd')
    chutich = request.POST.get('chutich')
    thuky = request.POST.get('thuky')
    giangvien = request.POST.getlist('giangvien')
    diachi = request.POST.get('diachi')
    day = request.POST.get('day')
    month = request.POST.get('month')
    year = request.POST.get('year')

    chutich = ThongTin.objects.get(ma_so=chutich)
    thuky = ThongTin.objects.get(ma_so=thuky)
    s = str(year + '-' + month + '-' + day)
    ngaybv = datetime.datetime.strptime(s, "%Y-%m-%d").date()
    for i in giangvien:
        obj = ThongTin.objects.get(ma_so=i)
        hoidong = HoiDong(mahd=mahd, chutich=chutich, ngaybv=ngaybv, thuky=thuky, msgv=obj, diachibv=diachi)
        hoidong.save()
        print('save!..............')

    return HttpResponseRedirect('/hoidong/them')


def hoidong_sua(request):
    thongtin = ThongTin.objects.filter(choice='gv')
    obj = HoiDong.objects.get(mahd='HD0001')
    return render(request, 'hoidong/edit.html', {'data': obj, 'thongtin': thongtin})


def edit_hd(request):
    mahd = request.POST.get('mahd')
    chutich = request.POST.get('chutich')
    thuky = request.POST.get('thuky')
    giangvien = request.POST.getlist('giangvien')
    diachi = request.POST.get('diachi')
    day = request.POST.get('day')
    month = request.POST.get('month')
    year = request.POST.get('year')
    chutich = ThongTin.objects.get(ma_so=chutich)
    thuky = ThongTin.objects.get(ma_so=thuky)
    s = str(year + '-' + month + '-' + day)
    ngaybv = datetime.datetime.strptime(s, "%Y-%m-%d").date()
    for i in giangvien:
        obj = ThongTin.objects.get(ma_so=i)
        hoidong = HoiDong.objects.get(mahd='HD0001')
        hoidong.mahd = mahd
        hoidong.chutich = chutich
        hoidong.thuky = thuky
        hoidong.msgv = obj
        hoidong.diachibv = diachi
        hoidong.ngaybv = ngaybv
        hoidong.save()
        print('save!..............')
    return HttpResponseRedirect('/hoidong/chinhsua')


def hoidong_timkiem(request):
    return render(request, 'hoidong/search.html')


def search_hd(request):
	print('========= search aa =============')
	keywork = request.GET.get('keywork')
	print(keywork)
	data = HoiDong.objects.filter(mahd__contains=keywork)
	print(data[0].msgv.ho_ten)
	return render(request, 'hoidong/result.html', {'data': data})