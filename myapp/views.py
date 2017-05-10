from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def sinhvien_them(request):
    return render(request, 'sinhvien/add-new.html')


def sinhvien_sua(request):
    return render(request, 'sinhvien/edit.html')


def sinhvien_timkiem(request):
    return render(request, 'sinhvien/search.html')


def detai_them(request):
    return render(request, 'detai/add-new.html')


def detai_sua(request):
    return render(request, 'detai/edit.html')


def detai_timkiem(request):
    return render(request, 'detai/search.html')


def giangvien_them(request):
    return render(request, 'giangvien/add-new.html')


def giangvien_sua(request):
    return render(request, 'giangvien/edit.html')


def giangvien_timkiem(request):
    return render(request, 'giangvien/search.html')


def hoidong_them(request):
    return render(request, 'hoidong/add-new.html')


def hoidong_sua(request):
    return render(request, 'hoidong/edit.html')


def hoidong_timkiem(request):
    return render(request, 'hoidong/search.html')
