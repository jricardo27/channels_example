import datetime
from django.contrib.auth.models import User
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'
    date_format = '%Y-%m-%d %H:%M:%S.%f'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'server_time': datetime.datetime.now().strftime(
                self.date_format,
            ),
            'users': User.objects.all(),
        })

        return context
