from django.contrib.auth.views import LoginView
from django.views.generic import FormView

from accounts.forms import RegistrationForm


class UserRegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        return {
            'page_title': 'Register',
        } | super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# расширение представления из приложения auth
# class UserLoginView(LoginView):
#     template_name = 'accounts/login.html'

