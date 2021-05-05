from rest_framework import serializers
from dlpquery.models import TestcustomobjectC
from dlpquery.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id',
                  'firstname',
                  'lastname',
                  'age',
                  'gender',
                  'booking_date',
                  'amount',
                  'email',
                  'agepax2_c',
                  'agencynumber_c',
                  'arrivaldate_c',
                  'bkharrivaldate_c')


class TestcustomobjectCSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestcustomobjectC
        fields = ('id',
                  'createddate',
                  'isdeleted',
                  'name',
                  'systemmodstamp',
                  'address_c',
                  'sfid',
                  'field_hc_lastop',
                  'field_hc_err',
                  'extid_c',
                  'last_name_c',
                  'external_id_c')
