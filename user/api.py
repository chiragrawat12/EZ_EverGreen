from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, PurchaseSerializer, ProductSerializer, LoginSerializer,Getting_Started_SectionSerializer,Getting_Started_Affiliate_LinkSerializer,Model_Content_Affiliate_LinkSerializer,Model_Content_SectionSerializer,Customize_Content_SectionSerializer,Customize_Content_Affiliate_LinkSerializer,Publish_SectionSerializer,Publish_Affiliate_LinkSerializer,Resources_Affiliate_LinkSerializer,Resources_SectionSerializer
from django.http import HttpResponse
from .models import Purchase, Product, Login,Getting_Started_Section,Getting_Started_Affiliate_Link,Model_Content_Affiliate_Link,Model_Content_Section,Customize_Content_Section,Customize_Content_Affiliate_Link,Publish_Affiliate_Link,Publish_Section,Resources_Section,Resources_Affiliate_Link
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)

    
class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('email',)
    # def get(self, request):
    #     user = User.objects.all()
    #     serializer = UserSerializer(user, many=True)
    #     return Response(serializer.data)
# class UserListView(generics.ListAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     filter_backends = (DjangoFilterBackend,)
#     filter_fields = ('email',)

# class PurchaseList(APIView):
#     def get(self, request,purby):
#         try:
#             purchases = Purchase.objects.get(purchased_by=purby)
#         except Purchase.DoesNotExist:
#             return Response("User with id: {} is not found in database.".format(purby),
#                             status=status.HTTP_404_NOT_FOUND)
#         serializer = PurchaseSerializer(purchases, many=True)
#         return Response(serializer.data)

class PurchaseListView(generics.ListAPIView):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('purchased_by',)


class ProductList(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


class LoginList(APIView):
    def get(self, request, user_id):
        try:
            login = Login.objects.get(user=user_id)
        except Login.DoesNotExist:
            return Response("User with id: {} is not found in database.".format(user_id),
                            status=status.HTTP_404_NOT_FOUND)
        serializer = LoginSerializer(login)
        return Response(serializer.data)

    def put(self, request, user_id):
        try:
            login = Login.objects.get(user=user_id)
        except Login.DoesNotExist:
            return Response("User with id: {} is not found in database.".format(user_id),
                            status=status.HTTP_404_NOT_FOUND)

        serializer = LoginSerializer(login, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Getting_Started_SectionList(APIView):
    def get(self,request):
        section = Getting_Started_Section.objects.all()
        serializer = Getting_Started_SectionSerializer(section,many=True)
        return Response(serializer.data)


class Getting_Started_Affiliate_LinkListView(generics.ListAPIView):
    serializer_class = Getting_Started_Affiliate_LinkSerializer
    queryset = Getting_Started_Affiliate_Link.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('Section_Name__Section',)

class Model_Content_SectionList(APIView):
    def get(self,request):
        section = Model_Content_Section.objects.all()
        serializer = Model_Content_SectionSerializer(section,many=True)
        return Response(serializer.data)


class Model_Content_Affiliate_LinkListView(generics.ListAPIView):
    serializer_class = Model_Content_Affiliate_LinkSerializer
    queryset = Model_Content_Affiliate_Link.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('Section_Name__Section',)

class Customize_Content_SectionList(APIView):
    def get(self,request):
        section = Customize_Content_Section.objects.all()
        serializer = Customize_Content_SectionSerializer(section,many=True)
        return Response(serializer.data)


class Customize_Content_Affiliate_LinkListView(generics.ListAPIView):
    serializer_class = Customize_Content_Affiliate_LinkSerializer
    queryset = Customize_Content_Affiliate_Link.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('Section_Name__Section',)

class Publish_SectionList(APIView):
    def get(self,request):
        section = Publish_Section.objects.all()
        serializer = Publish_SectionSerializer(section,many=True)
        return Response(serializer.data)


class Publish_Affiliate_LinkListView(generics.ListAPIView):
    serializer_class = Publish_Affiliate_LinkSerializer
    queryset = Publish_Affiliate_Link.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('Section_Name__Section',)

class Resources_SectionList(APIView):
    def get(self,request):
        section = Resources_Section.objects.all()
        serializer = Resources_SectionSerializer(section,many=True)
        return Response(serializer.data)


class Resources_Affiliate_LinkListView(generics.ListAPIView):
    serializer_class = Resources_Affiliate_LinkSerializer
    queryset = Resources_Affiliate_Link.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('Section_Name__Section',)