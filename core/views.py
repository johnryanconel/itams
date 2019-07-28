from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Asset


def home(request):
    context = {
        'assets': Asset.objects.all()
    }
    return render(request, 'core/home.html', context)


class AssetListView(ListView):
    model = Asset
    template_name = 'core/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'assets'
    ordering = ['-date_added']
    paginate_by = 10


class UserAssetListView(ListView):
    model = Asset
    template_name = 'core/user_assets.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'assets'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Asset.objects.filter(added_by=user).order_by('-date_added')


class AssetDetailView(DetailView):
    model = Asset


class AssetCreateView(LoginRequiredMixin, CreateView):
    model = Asset
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)


class AssetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Asset
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        asset = self.get_object()
        if self.request.user == asset.added_by:
            return True
        return False


class AssetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Asset
    success_url = '/'

    def test_func(self):
        asset = self.get_object()
        if self.request.user == asset.added_by:
            return True
        return False


def about(request):
    return render(request, 'core/about.html', {'title': 'About'})