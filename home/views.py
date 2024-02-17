from django.shortcuts import render
from django.views.generic import TemplateView
from .models import DishCategory, Gallery
from .forms import ReservationForm


class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = DishCategory.objects.filter(is_visible=True)
        gallery = Gallery.objects.filter(is_visible=True)
        reservation_form = ReservationForm()

        context['categories'] = categories
        context['gallery'] = gallery
        context['reservation_form'] = reservation_form
        return context

    def post(self, request, *args, **kwargs):
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            return render(request, 'index.html', {'reservation_form': reservation_form})
        else:
            return render(request, 'index.html', {'reservation_form': reservation_form})


# def main_page(request):
#     categories = DishCategory.objects.filter(is_visible=True)
#     gallery = Gallery.objects.filter(is_visible=True)
#
#     context = {
#         'categories': categories,
#         'gallery': gallery,
#     }
#     return render(request, 'index.html', context=context)
