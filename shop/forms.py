from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Newsletter

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Електронна пошта")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'newsletter-input',
                'placeholder': 'Ваш email для новин',
                'required': True
            })
        }

class CustomPasswordResetForm(PasswordResetForm):
    new_username = forms.CharField(
        label="ЛОГІН, ПІД ЯКИМ ХОЧЕТЕ ЗАЙТИ",
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Наприклад: B',
            'style': 'width: 100%; padding: 12px; background: #110e0c; border: 1px solid #333; color: #fff;'
        })
    )

    def save(self, **kwargs):
        requested_username = self.cleaned_data.get('new_username')

        extra_email_context = kwargs.get('extra_email_context', {})
        extra_email_context.update({'requested_username': requested_username})
        kwargs['extra_email_context'] = extra_email_context

        super().save(**kwargs)


class CustomSetPasswordForm(SetPasswordForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user