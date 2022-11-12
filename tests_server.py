from unittest import TestCase
from server import app

class FetchRewardsTests(TestCase):
    """App tests."""

    def setUp(self):
        """Gets called before every test."""

        # Get the Flast test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):
        """Test homepage page."""

        result = self.client.get("/")
        self.assertIn(b"Hello", result.data)
        self.assertEqual(result.status_code, 200)

    def test_add_transactions(self):
        """Test page add transactions."""

        result = self.client.post("/add-transactions", 
                                data={"Payer": "doggy", "Points": "123"})
        self.assertIn(b"This route allows to add payer", result.data)

    def test_spend_points(self):
        """Test page spend points."""

        result = self.client.post("/spend-points", 
                                data={"Points-spend": 123})
        self.assertIn(b"How much would you like to fetch?", result.data)

    def test_show_balance(self):
        """Test page show balance."""

        result = self.client.get("/show-balance")

        self.assertIn(b"payer", result.data)

    


if __name__ == "__main__":
    import unittest

    unittest.main()