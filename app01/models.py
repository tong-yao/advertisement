from django.db import models


class DataReport(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)        #日期
    Ad_name = models.CharField(max_length=255, blank=True, null=True)  #广告名称
    Distribution_channel = models.CharField(max_length=255, blank=True, null=True) #投放渠道
    Exposure = models.CharField(max_length=255, blank=True, null=True)   #曝光量
    Click_volume = models.CharField(max_length=255, blank=True, null=True)   #点击量
    Click_rate = models.CharField(max_length=255, blank=True, null=True)   #点击率
    price = models.DecimalField(max_digits=60, decimal_places=3, blank=True, null=True)   #单价
    Consumption = models.DecimalField( max_digits=60, decimal_places=3, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it en '_'.

    class Meta:
        managed = False
        db_table = 'data_report'




class UserTable(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    rbac = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_table'


