from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


from .models import MyUser

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirm", widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username',)

    def clean_passwords(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("password don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeform(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = MyUser
        fields = ('username',)

class UserAdmin(BaseUserAdmin):
    form = UserChangeform
    add_form = UserCreationForm

    list_display = ('id', 'username','is_level_1', "is_level_2", 'is_level_3', 'first_name', 'last_name')
    list_filter = ('is_level_3', "is_level_2")

    fieldsets = (
        (None, {'fields':('username', 'password')}),
        ('Personal info', {"fields":('first_name', 'last_name')}),
        ('Permissions', {'fields':("is_staff", "is_active","is_superuser", "is_level_1", "is_level_2","is_level_3")})
    )
    search_fields = ["username"]
    filter_horizontal = ()
    

admin.site.register(MyUser, UserAdmin)





