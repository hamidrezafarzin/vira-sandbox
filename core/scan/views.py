from django.shortcuts import render, HttpResponse, HttpResponseRedirect
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
    

# class ScanView(CreateView):
#     template_name = "scan/index.html"
#     form_class = ScanForm
#     success_url = "/done/"

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # You can process the form data here if needed.
#         print(form.cleaned_data)  # Use cleaned_data to access form data
#         return super().form_valid(form)
    
#     def form_invalid(self, form):
#         # If the form is invalid, print the errors for debugging
#         # print(form.errors)
#         print("data:", form.cleaned_data)
#         return super().form_invalid(form)


def scan_view(request):
    if request.method == "POST":
        # data = request.POST.dict()
        form = ScanForm(request.POST, request.FILES)
        # uploaded_file = request.FILES
        # print("uploaded_file", uploaded_file)
        # print("data", data)

        # path = default_storage.save('tmp/somename.png', ContentFile(uploaded_file.read()))
        # tmp_file = os.path.join(settings.STATIC_ROOT, path)
        # captured_image_data = request.POST.get('photo')
        # print("captured_image_data", captured_image_data)
        # print(data)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        else:
            print(form.errors)

        # print(form)
        return HttpResponse('{"detail": "ok"}')
        # return HttpResponseRedirect("/done/")
    form = ScanForm()
    return render(request, "scan/index.html", {"form": form})
