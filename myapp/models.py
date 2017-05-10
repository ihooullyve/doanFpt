from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class DeTai(models.Model):
	msdt = models.CharField(max_length=255)
	tendt = models.CharField(max_length=255)

	def __str__(self):
		return u'%s' % self.msdt


class ThongTin(models.Model):
	LIST_CHOICES = (
		('sv', "Sinh Vien"),
		('gv', "Giang Vien"),
	)

	user = models.ForeignKey(User, related_name='user_thongtin', null=True)
	ma_so = models.CharField(max_length=255, null=True)
	ho_ten = models.CharField(max_length=255, null=True)
	lop = models.CharField(max_length=255, null=True)
	dia_chi = models.CharField(max_length=255, null=True)
	email = models.EmailField(max_length=70, blank=True, null=True)
	sdt = models.IntegerField(default=0)
	hoc_vi = models.CharField(max_length=255, null=True)
	chuyen_nganh = models.CharField(max_length=255, null=True)
	ma_detai = models.ForeignKey(DeTai, null=True)
	ngaysinh = models.DateField(blank=True, null=True)
	choice = models.CharField(choices=LIST_CHOICES, max_length=45)


	def __str__(self):
		return u'%s' % self.user


class HoiDong(models.Model):
    mahd = models.CharField(max_length=255)
    chutich = models.ForeignKey(
        ThongTin, related_name='gv_chutich', null=True)
    thuky = models.ForeignKey(ThongTin, related_name='gv_thuky', null=True)
    msgv = models.ForeignKey(ThongTin, related_name='gv_msgv', null=True)
    ngaybv = models.DateField(blank=True, null=True)
    diachibv = models.CharField(max_length=255)

    def __str__(self):
        return u'%s' % self.mahd
