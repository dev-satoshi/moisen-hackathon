from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "pages/index.html"


class MedicineListView(TemplateView):
    template_name = "pages/medicine/list.html"


class MedicineRegisterView(TemplateView):
    template_name = "pages/medicine/register.html"


class MedicineDetailView(TemplateView):
    template_name = "pages/medicine/detail.html"


class MedicineSearchView(TemplateView):
    template_name = "pages/medicine/search.html"
