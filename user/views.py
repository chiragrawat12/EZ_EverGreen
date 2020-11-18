from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings

def handler404(request,exception):
    return render(request,'404.html',status=404)
def handler500(request,exception=None):
    return render(request,'500.html',status=500)
def handler400(request,exception=None):
    return render(request,'400.html',status=400)
def handler403(request,exception=None):
    return render(request,'403.html',status=403)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.getlist('remember')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if remember_me == ["yes"]:
                request.session.set_expiry(0)
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password.')
            return redirect('login')
    else:
        context = {}
        return render(request, 'login.html', context)


def logout(request):
    if not request.user.is_authenticated:
        return redirect('login')
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Akmauri account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            receiver = form.data.get('email')
            text_content = strip_tags(message)

            email = EmailMultiAlternatives(
                mail_subject,
                text_content,
                settings.EMAIL_HOST_USER,
                [receiver, ]
            )
            email.attach_alternative(message, "text/html")
            email.send(fail_silently=False)

            user_email = receiver.split('@')
            user_email[0] = user_email[0][0:2] + '*' * \
                (len(user_email[0])-2) + user_email[0][-2:]
            user_email = '@'.join(user_email)
            messages.success(
                request, "Activation Link has been sent to your Email: {}".format(user_email))
            return redirect('login')
            # return HttpResponse('Please confirm your email address to complete the registration')

    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, "register.html", context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
