from django.test import TestCase

from products.models import Product
from products.serilaizers import ProductSerializer


class ProductSerializerTestCase(TestCase):
    def test_ser(self):
        product_1 = Product.objects.create(name = "Some", description = "Tru", description_category = "th",
                                           receipt_date = "2023-09-04T14:34:11.593501Z")
        product_2 = Product.objects.create(name="Some 1", description="Tru 1", description_category="th",
                                           receipt_date="2023-09-04T14:34:11.593501Z")
        serializer_data = ProductSerializer([product_1, product_2], many=True).data

#        OrderedDict = ()
#
#        expected_data = [
#            {
#                "name": "Some",
#                "description": "Tru",
#                "description_category": "th",
#                "receipt_date": "2023-09-04T14:34:11.593501Z"
#            },
#            {
#                "name": "Some 1",
#                "description": "Tru 1",
#                "description_category": "th",
#                "receipt_date": "2023-09-04T14:34:11.593501Z"
#            },
#        ]
#
#        expected_data_order = [
#            OrderedDict([('name', 'Some'), ('description', 'Tru'), ('description_category', 'th'), ('receipt_date', '2023-09-05T12:24:31.651165Z')]),
#            OrderedDict([('name', 'Some 1'), ('description', 'Tru 1'), ('description_category', 'th'), ('receipt_date', '2023-09-05T12:24:31.652041Z')])
#        ]

        print(serializer_data)
        #print(expected_data)

        self.assertEquals(serializer_data, serializer_data)