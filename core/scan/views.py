from django.shortcuts import render, HttpResponse
from .forms import ScanForm
from django.views import View
from django.views.generic.edit import FormView, CreateView
from .models import Scan

# Create your views here.


# def scan_view(request):
#     return render(request, 'scan/index.html')


# class ScanView(View):
#     form_class = ScanForm
#     initial = {"key": "value"}
#     template_name = "scan/index.html"
    
#     def get(self, request, *args, **kwargs):
#         # Create an instance of the form if needed
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {"form": form})
    

class ScanView(CreateView):
    template_name = "scan/index.html"
    form_class = ScanForm
    success_url = "/done/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # You can process the form data here if needed.
        print(form.cleaned_data)  # Use cleaned_data to access form data
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # If the form is invalid, print the errors for debugging
        print(form.errors)
        return super().form_invalid(form)
    
def done_view(request):
    return HttpResponse("عملیات با موفقیت انجام شد")