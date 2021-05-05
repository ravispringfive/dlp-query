from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import logging

from dlpquery.models import Booking
from dlpquery.models import TestcustomobjectC
from dlpquery.serializers import BookingSerializer
from dlpquery.serializers import TestcustomobjectCSerializer
from rest_framework.decorators import api_view


logger = logging.getLogger(__name__)

@api_view(['GET', 'POST', 'DELETE'])
def dlpquery_booking(request):
    if request.method == 'GET':
        booking = Booking.objects.all()

        firstname = request.GET.get('firstname', None)
        if firstname is not None:
            booking = booking.filter(firstname__icontains=firstname)

        booking_serializer = BookingSerializer(booking, many=True)
        return JsonResponse(booking_serializer.data, safe=False)

    elif request.method == 'POST':
        booking_post_data = JSONParser().parse(request)
        booking_serializer = BookingSerializer(data=booking_post_data)
        if booking_serializer.is_valid():
            booking_serializer.save()
            return JsonResponse(booking_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(booking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Booking.objects.all().delete()
        return JsonResponse({'message': '{} booking were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def dlpquery_custom_object(request):
    if request.method == 'GET':
        custom_object = TestcustomobjectC.objects.all()

        firstname = request.GET.get('name', None)
        if firstname is not None:
            custom_object = custom_object.filter(name__icontains=firstname)

        custom_object_serializer = TestcustomobjectCSerializer(custom_object, many=True)
        return JsonResponse(custom_object_serializer.data, safe=False)

    elif request.method == 'POST':
        custom_object_post_data = JSONParser().parse(request)
        custom_object_serializer = TestcustomobjectCSerializer(data=custom_object_post_data)
        if custom_object_serializer.is_valid():
            custom_object_serializer.save()
            return JsonResponse(custom_object_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(custom_object_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = TestcustomobjectC.objects.all().delete()
        return JsonResponse({'message': '{} booking were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


def all_booking_data():
    booking = Booking.objects.all()
    booking_serializer = BookingSerializer(booking, many=True)
    for ordered_dict in booking_serializer.data:
        print(dict(ordered_dict))


def all_custom_object_data():
    custom_object = TestcustomobjectC.objects.all()
    custom_object_serializer = TestcustomobjectCSerializer(custom_object, many=True)
    for ordered_dict in custom_object_serializer.data:
        print(dict(ordered_dict))
