from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import User,Product,Base_User

class Base_UserSerializer(serializers.ModelSerializer):
    create_product = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Base_User
        fields = [
            'username',
            'email',
            'is_staff',
            'phone',
            'password',
            'create_product'
        ]
    def get_create_product(self,obj):
        request = self.context.get('request')
        return reverse('product-create',request = request)


class UserSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =[
            'id',
            'name',
            'email',
            'interest',
            'number',
            'age'
        ]

class ProductSerializer(serializers.ModelSerializer):
    update_product = serializers.HyperlinkedIdentityField(view_name='product-update',lookup_field = 'pk')
    class Meta:
        model = Product
        fields = [
            'id',
            'product_name',
            'product_desc',
            'product_price',
            'product_quantity',
            'update_product'
        ]

    def get_update_product(self,object):
        return "need to add link"

class ProductDeleteSerializer(serializers.ModelSerializer):
    delete_product = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'product_name',
            'product_desc',
            'product_price',
            'product_quantity',
            'delete_product'
        ]

    def get_delete_product(self,obj):
        request = self.context.get('request')

        return reverse("product-delete",kwargs={'pk':obj.id},request=request)

