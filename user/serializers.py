from rest_framework import serializers
from .models import User, Purchase, Product, Login,Getting_Started_Section,Getting_Started_Affiliate_Link,Model_Content_Section,Model_Content_Affiliate_Link,Customize_Content_Affiliate_Link,Customize_Content_Section,Publish_Affiliate_Link,Publish_Section,Resources_Affiliate_Link,Resources_Section

class LoginSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    # user = serializers.IntegerField(required=False)

    class Meta:
        model = Login
        # fields = ['id', 'emai', 'password']
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        # fields = "__all__"


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['purchased_by', 'product']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ['id', 'product_name', 'product_link']
        fields = "__all__"

class Getting_Started_SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Getting_Started_Section
        fields = '__all__'

class Getting_Started_Affiliate_LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Getting_Started_Affiliate_Link
        fields = '__all__'

class Model_Content_SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model_Content_Section
        fields = '__all__'

class Model_Content_Affiliate_LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model_Content_Affiliate_Link
        fields = '__all__'

class Customize_Content_SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customize_Content_Section
        fields = '__all__'

class Customize_Content_Affiliate_LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customize_Content_Affiliate_Link
        fields = '__all__'

class Publish_SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish_Section
        fields = '__all__'

class Publish_Affiliate_LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish_Affiliate_Link
        fields = '__all__'

class Resources_SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources_Section
        fields = '__all__'

class Resources_Affiliate_LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources_Affiliate_Link
        fields = '__all__'