from django.shortcuts import render
from .models import Announcement
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


class PostList(ListView):
    model = Announcement
    template_name = "blog/bejegyzes_list.html"
    queryset = Announcement.get_published().order_by("-updated_at")
    paginate_by = 9


class PostDetail(DetailView):
    model = Announcement
    template_name = "blog/bejegyzes_detail.html"

    def get_context_data(self, **kwargs):

        context = super(PostDetail, self).get_context_data(**kwargs)
        context["domain_name"] = (
            "https://"
            if self.request.is_secure()
            else "http://" + self.request.get_host()
        )

        return context
