from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.contrib.messages import constants as messages
from myapp.models import ThongTin, DeTai, HoiDong


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

    return HttpResponseRedirect('/')


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


def detai_sua(request):
    return render(request, 'detai/edit.html')


def detai_timkiem(request):
    return render(request, 'detai/search.html')

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
                        email=email, sdt=sdt, hoc_vi=hocvi, chuyen_nganh=chuyennganh)
    thongtin.save()

    return HttpResponseRedirect('/giangvien/them')


def giangvien_sua(request):
	thongtin = ThongTin.objects.get(user__id= 24)
	return render(request, 'giangvien/edit.html', {'data':thongtin})


def edit_gv(request):
	name = request.POST.get('name')
	msgv = request.POST.get('msgv')
	diachi = request.POST.get('diachi')
	email = request.POST.get('email')
	sdt = request.POST.get('sdt')
	hocvi = request.POST.get('hocvi')
	chuyennganh = request.POST.get('chuyennganh')

	user = User.objects.get(id = 24)
	user.username = name
	user.save()

	thongtin = ThongTin.objects.get(user__id=24)
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

def hoidong_them(request):
    return render(request, 'hoidong/add-new.html')


def hoidong_sua(request):
    return render(request, 'hoidong/edit.html')


def hoidong_timkiem(request):
    return render(request, 'hoidong/search.html')
