from django.contrib import admin, messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = ("name", "email", "phone", "status", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("status", "created_at")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    actions = ["mark_as_replied"]

    fieldsets = (
        ("Customer Information", {
            "fields": ("name", "email", "phone")
        }),
        ("Original Message", {
            "fields": ("message",)
        }),
        ("Reply Section", {
            "fields": ("reply_message",)
        }),
        ("Status", {
            "fields": ("status",)
        }),
        ("Metadata", {
            "fields": ("created_at",)
        }),
    )

    # ✅ BULK ACTION
    def mark_as_replied(self, request, queryset):
        updated = queryset.update(status="replied")
        self.message_user(
            request,
            f"{updated} message(s) marked as Replied.",
            messages.SUCCESS
        )

    mark_as_replied.short_description = "Mark selected messages as Replied"

    # ✅ Auto-fill default template when opening admin form
    def get_changeform_initial_data(self, request):
        return {
            "reply_message": (
                "Hello,\n\n"
                "Thank you for contacting Autonecto Electrics.\n\n"
                "We have received your message and will assist you shortly.\n\n"
                "Best regards,\n"
                "Autonecto Electrics Team"
            )
        }

    # ✅ Send Reply Button Logic
    def response_change(self, request, obj):
        if "_send_custom_reply" in request.POST:

            default_message = (
                f"Hello {obj.name},\n\n"
                "Thank you for contacting Autonecto Electrics.\n\n"
                "We have received your message and will assist you shortly.\n\n"
                "Best regards,\n"
                "Autonecto Electrics Team"
            )

            # Use custom reply if provided, otherwise fallback
            message_to_send = obj.reply_message if obj.reply_message else default_message

            try:
                send_mail(
                    subject="Response from Autonecto Electrics",
                    message=message_to_send,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[obj.email],
                )

                # Save default message if empty before
                if not obj.reply_message:
                    obj.reply_message = default_message

                obj.status = "replied"
                obj.save()

                self.message_user(
                    request,
                    "Reply email sent successfully!",
                    messages.SUCCESS
                )

            except Exception as e:
                self.message_user(
                    request,
                    f"Email failed to send: {e}",
                    messages.ERROR
                )

            return HttpResponseRedirect(request.path)

        return super().response_change(request, obj)