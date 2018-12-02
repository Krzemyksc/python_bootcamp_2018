from django.shortcuts import render

# Create your views here.
def fake_view(request):
    return render(request=request, template_name="products_list.html", content=None)