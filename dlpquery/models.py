from django.db import models


class TestcustomobjectC(models.Model):
    createddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    systemmodstamp = models.DateTimeField(blank=True, null=True)
    address_c = models.CharField(db_column='address__c', max_length=255, blank=True,
                                 null=True)  # Field renamed because it contained more than one '_' in a row.
    sfid = models.CharField(unique=True, max_length=18, db_collation='ucs_basic', blank=True, null=True)
    field_hc_lastop = models.CharField(db_column='_hc_lastop', max_length=32, blank=True,
                                   null=True)  # Field renamed because it started with '_'.
    field_hc_err = models.TextField(db_column='_hc_err', blank=True,
                                null=True)  # Field renamed because it started with '_'.
    extid_c = models.CharField(db_column='extid__c', unique=True, max_length=25, blank=True,
                           null=True)  # Field renamed because it contained more than one '_' in a row.
    last_name_c = models.CharField(db_column='last_name__c', max_length=255, blank=True,
                           null=True)  # Field renamed because it contained more than one '_' in a row.
    external_id_c = models.FloatField(db_column='external_id__c', unique=True, blank=True,
                              null=True)  # Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'salesforce\".\"testcustomobject__c'


class Booking(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    booking_date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    email = models.CharField(max_length=35, blank=True, null=True)
    agepax2_c = models.TextField(db_column='AgePAX2__c', blank=True, null=True)
    agencynumber_c = models.CharField(db_column='agencynumber__c', max_length=80, blank=True, null=True)
    arrivaldate_c = models.CharField(db_column='arrivaldate__c', max_length=80, blank=True, null=True)
    bkharrivaldate_c = models.CharField(db_column='bkharrivaldate__c', max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'public\".\"booking'
