from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from user.models import Product, Purchase
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        purchases = Purchase.objects.filter(
            purchased_by=request.user.id)
        purchased_product = []
        for purchase in purchases:
            purchased_product.append(purchase.product)
        products = Product.objects.all()
        context = {'products': products,
                   'purchased_product': purchased_product}
    else:
        products = Product.objects.all()
        context = {'products':products}
    return render(request, "home.html", context)


def contact(request):
    if request.method == 'POST':
        feedback = request.POST['feedback']
        if request.user.is_authenticated:
            email = request.user.email
            if request.user.first_name != "":
                name = request.user.first_name + " " + request.user.last_name
            else:
                name = request.user.username
            context = {'name': name, 'email': email}
        else:
            name = request.POST['name']
            email = request.POST['email']
            context = {}

        mail_subject = 'Feedback From {}'.format(name)
        message = render_to_string('feedback_email.html', {
            'name': name,
            'email': email,
            'feedback': feedback
        })

        text_content = strip_tags(message)

        email = EmailMultiAlternatives(
            mail_subject,
            text_content,
            settings.EMAIL_HOST_USER,
            ['chiragrawat12@gmail.com', ]
        )
        email.attach_alternative(message, "text/html")
        email.send(fail_silently=False)

        messages.info(request, "Thankyou for your Feedback.")
        return redirect('contact')
    else:
        if request.user.is_authenticated:
            email = request.user.email
            if request.user.first_name != "":
                name = request.user.first_name + " " + request.user.last_name
            else:
                name = request.user.username
            context = {'name': name, 'email': email}
            return render(request, "contact_us.html", context)
        else:
            context = {}
            return render(request, "contact_us.html", context)


def product(request, pname, id):
    try:
        product = Product.objects.get(product_name=pname, id=id)
    except Product.DoesNotExist:
        raise Http404("Product Does not exists!")
    if request.user.is_authenticated:
        try:
            purchases = Purchase.objects.get(
                purchased_by=request.user.id, product=id)
            context = {'id': id, 'pname': pname,
                       'purchases': purchases, 'product': product}
        except Purchase.DoesNotExist:
            context = {'id': id, 'pname': pname,
                       'product': product}
    else:
        context = {'id': id, 'pname': pname,
                   'product': product}
    return render(request, 'product.html', context)


@login_required(login_url='login')
def download(request, pname, id):
    try:
        product = Product.objects.get(product_name=pname, id=id)
    except Product.DoesNotExist:
        raise Http404("Page does not exists!")
    try:
        purchases = Purchase.objects.get(
            purchased_by=request.user.id, product=id)
    except Purchase.DoesNotExist:
        raise Http404("Page does not exists!")

    if purchases.product != product:
        raise Http404("Page does not exists!")
    else:
        return redirect(product.product_download.url)



