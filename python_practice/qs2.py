class CarServiceStation:
    # A dictionary of service codes to service names and prices
    servicePrices = {
        'BS01': {'name': 'Basic Servicing', 'hatchback': 2000, 'sedan': 4000, 'suv': 5000},
        'EF01': {'name': 'Engine Fixing', 'hatchback': 5000, 'sedan': 8000, 'suv': 10000},
        'CF01': {'name': 'Clutch Fixing', 'hatchback': 2000, 'sedan': 4000, 'suv': 6000},
        'BF01': {'name': 'Brake Fixing', 'hatchback': 1000, 'sedan': 1500, 'suv': 2500},
        'GF01': {'name': 'Gear Fixing', 'hatchback': 3000, 'sedan': 6000, 'suv': 8000},
    }

    def generateBill(self, type, serviceCodes):
        total = 0
        services = ''

        # Iterate through the service codes
        for code in serviceCodes:
            # Get the service name and price for the specified car type
            service = self.servicePrices.get(code)
            price = service[type]

            # Add the price to the total and append the service name to the services string
            total += price
            services += f"{service['name']} - ₹ {price}\n"

        # Check if the total bill is more than ₹10000 and add a complimentary cleaning if it is
        if total > 10000:
            services += 'Complimentary Cleaning\n'

        # Return the bill with the total amount and list of services
        return f"Type of Car - {type}\n{services}Total Bill - ₹ {total}"


station = CarServiceStation()

# Example usage:
print(station.generateBill('hatchback', ['BS01', 'EF01']))
