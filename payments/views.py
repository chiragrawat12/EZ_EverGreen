from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from user.models import Product, Purchase
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import stripe
from decouple import config
import json

stripe.api_key = config('STRIPE_API_KEY')


@login_required(login_url='login')
def payment_stripe(request, pname, id):
    try:
        product = Product.objects.get(product_name=pname, id=id)
    except Product.DoesNotExist:
        raise Http404("Page Does not exists!")
    try:
        purchases = Purchase.objects.get(
            purchased_by=request.user.id, product=product.id)
        pay = True
    except Purchase.DoesNotExist:
        pay = False

    if pay:
        raise Http404("Page not found!")

    if request.method == 'POST':
        try:
            state = request.POST['State']
        except:
            state = ''
        customer = stripe.Customer.create(
            email=request.user.email,
            name=request.POST['name'],
            address={
                'line1': request.POST['line1'],
                'postal_code': request.POST['postal_code'],
                'city': request.POST['city'],
                'state': state,
                'country': request.POST['country'],
            },
            source=request.POST['stripeToken']
        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=product.price*100,
            currency='usd',
            description=product.product_name
        )
        purchased = Purchase(purchased_by=request.user, product=product)
        purchased.save()

        mail_subject = 'Thankyou for purchasing our Product: {}'.format(
            product.product_name)
        message = render_to_string(
            'payment_success_email.html', {'product': product, 'through': 'Stripe'})

        text_content = strip_tags(message)

        email = EmailMultiAlternatives(
            mail_subject,
            text_content,
            settings.EMAIL_HOST_USER,
            [request.user.email, ]
        )
        email.attach_alternative(message, "text/html")
        email.send(fail_silently=False)
        return redirect('success', product.product_name, product.id, product.price, 'Stripe')
    else:
        context = {'product': product, }
        return render(request, 'payment_stripe.html', context)


@login_required(login_url='login')
def successMsg(request, pname, id, amt, through):
    try:
        product = Product.objects.get(product_name=pname, id=id, price=amt)
    except Product.DoesNotExist:
        raise Http404("Page does not exists!")
    try:
        purchases = Purchase.objects.get(
            purchased_by=request.user.id, product=id)
    except Purchase.DoesNotExist:
        raise Http404("Page does not exists!")
    if purchases.product != product:
        raise Http404("Page does not exists!")
    return render(request, 'success.html', {'amount': amt, 'product': product, 'through': through})


@login_required(login_url='login')
def payment_paypal(request, pname, id):
    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            product = Product.objects.get(
                product_name=body['pname'], id=body['id'], price=body['amount'])
        except Product.DoesNotExist:
            raise Http404("Page does not exists!")
        try:
            purchases = Purchase.objects.get(
                purchased_by=request.user.id, product=body['id'])
            pay = True
        except Purchase.DoesNotExist:
            pay = False
        if pay:
            raise Http404("Page does not exists!")
        purchased = Purchase(purchased_by=request.user, product=product)
        purchased.save()
        mail_subject = 'Thankyou for purchasing our Product: {}'.format(
            product.product_name)
        message = render_to_string(
            'payment_success_email.html', {'product': product, 'through': 'Paypal'})

        text_content = strip_tags(message)

        email = EmailMultiAlternatives(
            mail_subject,
            text_content,
            settings.EMAIL_HOST_USER,
            [request.user.email, ]
        )
        email.attach_alternative(message, "text/html")
        email.send(fail_silently=False)
    else:
        try:
            product = Product.objects.get(product_name=pname, id=id)
        except Product.DoesNotExist:
            raise Http404("Page Does not exists!")
        try:
            purchases = Purchase.objects.get(
                purchased_by=request.user.id, product=product.id)
            pay = True
        except Purchase.DoesNotExist:
            pay = False
        if pay:
            raise Http404("Page not found!")
        context = {'product': product, }
        return render(request, 'payment_paypal.html', context)


@login_required(login_url='login')
def payment(request, pname, id):
    try:
        product = Product.objects.get(product_name=pname, id=id)
    except Product.DoesNotExist:
        raise Http404("Page Does not exists!")
    try:
        purchases = Purchase.objects.get(
            purchased_by=request.user.id, product=product.id)
        pay = True
    except Purchase.DoesNotExist:
        pay = False
    if pay:
        raise Http404("Page not found!")
    context = {'pname': pname, 'id': id}
    return render(request, 'payment_choice.html', context)
