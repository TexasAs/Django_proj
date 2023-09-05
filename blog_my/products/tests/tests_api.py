from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product
from products.serilaizers import ProductSerializer


class ProductApiTestCase(APITestCase):
    def test_get(self):
        # создаем экземпляры классов согласно расшаренному списку полей сериалтзатора
        product_1 = Product.objects.create(name = "Some", description = "Tru", description_category = "th",
                                           receipt_date = "2023-09-04T14:34:11.593501Z")
        product_2 = Product.objects.create(name="Some 1", description="Tru 1", description_category="th",
                                           receipt_date="2023-09-04T14:34:11.593501Z")
        # указываем ссылку api запроса
        url = 'http://127.0.0.1:8000/api_products/get_all/'
        #url = reverse('book-list')
        print(url)
        # формируем ответ по ссылке url и обрабатывать его будет своего рода браузер client
        responce = self.client.get(url)
        # формируем данные по созданным экземплярам которые как мы думаем должны вернутся в ответ на запрос
        # в параметры экземпляра серилайзера продуктов передаем список экземпляров класса продукт, и так как это список в параметрах указываем many=True
        serializer_data = ProductSerializer([product_1, product_2], many=True).data
        # сравниваем ожидаемый и получаемый ответы
        self.assertEquals(serializer_data, responce.data)
        # также сравниваем и статус коды ответов
        self.assertEquals(status.HTTP_200_OK, responce.status_code)

        #print(responce)
        print(serializer_data)
        print(responce.data)

        #   для coverage набрать в терминале $ coverage run - -source = '.'. / manage.py test .
