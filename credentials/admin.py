from django.contrib import admin
from .models import Register,Districts,Branch,AccountType,FromTable,CheckboxOptions,LoggedUser


admin.site.register(Register)
admin.site.register(Districts)
admin.site.register(Branch)
admin.site.register(AccountType)
admin.site.register(FromTable)
admin.site.register(CheckboxOptions)
admin.site.register(LoggedUser)

