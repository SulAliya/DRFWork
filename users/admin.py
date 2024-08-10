from django.contrib import admin

from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name',)
    search_fields = ('email', 'first_name', 'last_name',)
    list_filter = ('id', 'email',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'amount', 'pay_method']
