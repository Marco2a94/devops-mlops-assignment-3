class Converter:
    def __init__(self):
        self.conversion_rates = {
            'EUR': 1.0,  # Base currency, Euro
            'USD': 1.18,  # US dollar conversion rate
            'GBP': 0.85,  # British pound conversion rate
            'CAD': 1.5,  # Canadian dollar conversion rate
            'JPY': 130.0,  # Japanese yen conversion rate
        }
        print("Converter object successfully initialized")

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.conversion_rates or to_currency not in self.conversion_rates:
            raise ValueError("Invalid currency code")
        
        # Convert amount to base currency (EUR)
        base_amount = amount / self.conversion_rates[from_currency]
        
        # Convert from base currency to target currency
        converted_amount = base_amount * self.conversion_rates[to_currency]
        
        return converted_amount