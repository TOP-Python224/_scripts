from django.views.generic import FormView

from accounts.forms import RegistrationForm


class RegistrationView(FormView):
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

