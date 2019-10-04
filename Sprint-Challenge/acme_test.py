import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_steal_and_explode(self):
        """Test that stealability and explode and working properly."""
        steal_list = ['Not so stealable...', 'Kinda stealable.', 'Very stealable!']
        explode_list = ['Fizzle', '...boom!', 'BABOOM!!']

        prod = Product('Test Product', price=15, weight=30, fl=0.8)
        self.assertIn(prod.stealability(), steal_list)
        self.assertIn(prod.explode(), explode_list)


class AcmeReportTests(unittest.TestCase):
    """Test case for acme_report"""

    def test_default_num_products(self):
        """Test default number of products"""
        testProds = generate_products()
        self.assertEqual(len(testProds), 30)

    def test_legal_names(self):
        """Test legality of generated product names"""
        testProds = generate_products()
        for x in testProds:
            split_name = x.name.split()
            self.assertIn(split_name[0], ADJECTIVES)
            self.assertIn(split_name[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
