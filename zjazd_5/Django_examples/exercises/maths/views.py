from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from maths.models import Math


# Create your views here.

@login_required()
def math_operations(request, operations, a, b):
    if request.user:
        Math.objects.create(operations, a, b)


def calculate(operations, a, b):
    result = None
    if operations == "add":
        result = float(a + b)
    elif operations == "sub":
        result = float(a - b)
    elif operations == "mul":
        result = float(a * b)
    elif operations == "div":
        result = float(a / b)

    return result


def math_operations(request, operations, a, b):
    Math.objects.create(operations=operations, a=a, b=b)
    return HttpResponse(calculate(operations, a, b))


def math_list(request):
    objects = Math.objects.all()
    return render(
        request=request,
        template_name="math_list.html",
        context={"maths": objects}
    )


def math_details(request, id):
    m = Math.objects.get(pk=id)

    return render(
        request=request,
        template_name="math_details",
        context={"math": m,
                 'wynik': calculate(m.operations, m.a, m.b)
                 }

    )
