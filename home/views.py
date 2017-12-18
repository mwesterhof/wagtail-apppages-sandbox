from django.views.generic import TemplateView


class AppTestView(TemplateView):
    template_name = 'home/app_test.html'


class ParamTestView(TemplateView):
    template_name = 'home/param_test.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['test'] = self.kwargs['test']
        return ctx


class SubTestView(TemplateView):
    template_name = 'home/sub_test.html'
