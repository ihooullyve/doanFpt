from django.contrib import admin
from .models import DeTai, HoiDong, ThongTin


class DeTaiAdmin(admin.ModelAdmin):
    list_display = ['msdt', 'tendt']


class HoiDongAdmin(admin.ModelAdmin):
    list_display = ['mahd', 'chutich', 'thuky', 'msgv', 'ngaybv', 'diachibv']


class ThongTinAdmin(admin.ModelAdmin):
    list_display = ['user', 'ma_so', 'ho_ten', 'lop', 'dia_chi',
                    'email', 'sdt', 'hoc_vi', 'chuyen_nganh', 'ma_detai', 'ngaysinh', 'choice']


admin.site.register(DeTai, DeTaiAdmin)
admin.site.register(HoiDong, HoiDongAdmin)
admin.site.register(ThongTin, ThongTinAdmin)
