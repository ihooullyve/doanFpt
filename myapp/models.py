from django.db import models
from datetime import datetime


class GiangVien(models.Model):
    msgv = models.CharField(max_length=255)
    tengv = models.CharField(max_length=255)
    diachigv = models.CharField(max_length=255)
    email = models.EmailField(max_length=70, blank=True)
    sdt = models.IntegerField(default=0)
    hocvi = models.CharField(max_length=255)
    chuyennganh = models.CharField(max_length=255)

    def __str__(self):
        return u'%s' % self.msgv


class DeTai(models.Model):
    msdt = models.CharField(max_length=255)
    tendt = models.CharField(max_length=255)
    tengv = models.ForeignKey(GiangVien, null=True)

    def __str__(self):
        return u'%s' % self.msdt


class SinhVien(models.Model):
    mssv = models.CharField(max_length=255)
    tensv = models.CharField(max_length=255)
    lop = models.CharField(max_length=255)
    msdt = models.ForeignKey(DeTai, null=True)
    ngaysinh = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return u'%s' % self.mssv


class HoiDong(models.Model):
    mahd = models.CharField(max_length=255)
    chutich = models.ForeignKey(
        GiangVien, related_name='gv_chutich', null=True)
    thuky = models.ForeignKey(GiangVien, related_name='gv_thuky', null=True)
    msgv = models.ForeignKey(GiangVien, related_name='gv_msgv', null=True)
    ngaybv = models.DateTimeField(default=datetime.now(), blank=True)
    diachibv = models.CharField(max_length=255)

    def __str__(self):
    	return u'%s' % self.mahd
