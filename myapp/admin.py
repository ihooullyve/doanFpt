from django.contrib import admin
from .models import GiangVien, DeTai, SinhVien, HoiDong


class GiangVienAdmin(admin.ModelAdmin):
    list_display = ['msgv', 'tengv', 'diachigv',
                    'email', 'sdt', 'hocvi', 'chuyennganh']


class DeTaiAdmin(admin.ModelAdmin):
    list_display = ['msdt', 'tendt', 'tengv']


class SinhVienAdmin(admin.ModelAdmin):
    list_display = ['mssv', 'tensv', 'lop', 'msdt', 'ngaysinh']


class HoiDongAdmin(admin.ModelAdmin):
    list_display = ['mahd', 'chutich', 'thuky', 'msgv', 'ngaybv', 'diachibv']


admin.site.register(GiangVien, GiangVienAdmin)
admin.site.register(DeTai, DeTaiAdmin)
admin.site.register(SinhVien, SinhVienAdmin)
admin.site.register(HoiDong, HoiDongAdmin)
