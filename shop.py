class Shop:
    shop_name = 'Basis'
    address = 'chrompet'
    products = { 'shirts' : [10,350], 'mobiles': [5, 20000], 'laptops': [0, 85000]}

    def __init__(self, name, phone_no, address):
        self.name = name
        self.phone_no = phone_no
        self.address = address
        self.cart = {}

    @staticmethod
    def line():
        print('*********************************')


    @classmethod
    def display_products(cls):
        cls.line()
        print('Products available in the shop are:',end='\n\n')
        print('Product name','Qty','\tPrice',sep='\t')
        print('------------','---','\t-----',sep='\t')

        for product in cls.products:
            print(product, cls.products[product][0], cls.products[product][1],sep='\t\t')
        print()
        cls.line()


    def customer_details(self):
        self.line()
        print('Customer Details:')

        print()
        print('Name:',self.name)
        print('Phone No:',self.phone_no)
        print('Address:',self.address)

        print()

        if self.cart == {}:
            print('Your cart is empty.')
        else:
            print('Product name','Qty','\tSubtotal',sep='\t')
            print('------------','---','\t--------',sep='\t')

            total = 0

            for product in self.cart:
                subtotal = self.cart[product]*Shop.products[product][1]
                total += subtotal
                
                print(product, self.cart[product], subtotal,sep='\t\t')
            self.line()
            print('Total:',total)
        self.line()

    
    def add_product(self):
        self.line()
        print('ADD A PRODUCT')
        print()

        product = input('Enter a product:') #shirts

        if product in Shop.products:
            print()
            qty = int(input('Enter the Qty:'))
            if Shop.products[product][0] >= qty:
                if product in self.cart:
                    self.cart[product] += qty
                else:
                    self.cart[product] = qty
                Shop.products[product][0] -= qty
                print('Product added successfully')

            else:
                print(f'Out of Stock!! only {Shop.products[product][0]} left!')

        else:
            self.line()
            print('The product is not available in the shop.')

        self.line()

    def remove_product(self):
        self.line()
        if self.cart == {}:
            print('Your cart is empty, So cannot remove the products')
        else:
            product = input('Enter a product:')
            if product in self.cart:
                qty = int(input('Enter the qty:'))
                if self.cart[product] >= qty:
                    self.cart[product] -= qty
                    Shop.products[product][0] += qty
                    if self.cart[product] == 0:
                        self.cart.pop(product)
                    print('product removed successfully')

                else:
                    print(f'Cannot remove, since you added only {self.cart[product]} products.')

            else:
                print('This product is not available in the cart.')

        self.line()


    
    def main(self):
        self.line()
        print('Welcome to the Shop!!!')
        self.line()

        while True:
            print('Enter 1 to display all the products available in the shop.')
            print('Enter 2 to display your details.')
            print('Enter 3 to add a product.')
            print('Enter 4 to remove the product.')
            print('Enter 5 to exit.')
            print()

            option = int(input('Enter your option:'))

            if option == 1:
                self.display_products()

            elif option == 2:
                self.customer_details()

            elif option == 3:
                self.add_product()

            elif option == 4:
                self.remove_product()

            elif option == 5:
                self.line()
                print('Thank you for visiting!!!')
                self.line()
                return

            else:
                self.line()
                print('Invalid option')
                self.line()

        
        



c1 = Shop('bharani',9876543212, 'chennai')
c1.main()

c2 = Shop('bharani',9876543212, 'chennai')
c2.main()


