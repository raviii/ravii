from django.views.generic import TemplateView
from django.template import TemplateDoesNotExist

class StaticView(TemplateView):
    def get(self, request, page, *args, **kwargs):
        self.template_name = page
        response = super(StaticView, self).get(request, *args, **kwargs)
        try:
            return response.render()
        except TemplateDoesNotExist:
            raise Http404()
