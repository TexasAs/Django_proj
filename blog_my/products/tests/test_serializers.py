from django.test import TestCase

from products.models import Product
from products.serilaizers import ProductSerializer


class ProductSerializerTestCase(TestCase):

    def test_ser(self):

        product_1 = Product.objects.create(name = "Some", description = "Tru", description_category = "th",
                                           receipt_date = "2023-09-05T17:20:45.536006Z")
        product_2 = Product.objects.create(name="Some 1", description="Tru 1", description_category="th",
                                           receipt_date="None")

        serializer_data1 = ProductSerializer(product_1).data
        serializer_data2 = ProductSerializer(product_2).data

        expected_data = [
            {
                'name': product_1.name,
                'description': product_1.description,
                'description_category': 'th',
                'receipt_date': '2023-09-04T14:34:11.593501Z'
            },
            {
                'name': 'Some 1',
                'description': 'Tru 1',
                'description_category': 'th',
                'receipt_date': '2023-09-04T14:34:11.593501Z'
            }
        ]


        print(serializer_data1)
        print(expected_data)

        self.assertEquals(str(expected_data[0])[:-29], str(serializer_data1)[:-29])
        self.assertEquals(str(expected_data[1])[:-29], str(serializer_data2)[:-29])