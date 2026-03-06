from django.urls import path
from .views import BookingListView, BookingCreateView, BookingThankYouView

app_name = "bookings"

urlpatterns = [
    path('', BookingCreateView.as_view(), name='booking_form'),   # ← Book Now page
    path('list/', BookingListView.as_view(), name='booking_list'), # Admin only
    path('thank-you/', BookingThankYouView.as_view(), name='booking_thankyou'),
]
