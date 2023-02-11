class fruitJuice:
    def __init__(self, pc, pf, pt,ps, price):
        self.productCode=pc
        self.productFlavour=pf
        self.packType=pt
        self.packSize=ps
        self.productPrice=price

    def FruitJuice(self):
        self.productCode=0
        self.productFlavour=""
        self.packType=""
        self.packSize=0
        self.productPrice=0

    def discount(self):
        self.productPrice=self.productPrice*(90/100)

    def display(self):
        print("product details")
        print(self.productCode)
        print(self.productFlavour)
        print(self.packType)
        print(self.packSize, "ml")
        print(self.productPrice)
        print("--------------------")

#main

p1=fruitJuice(102,"orange","tetra-pack",200, 50)
p1.discount()
p1.display()

p2=fruitJuice(103,"apple","tetra-pack",200, 50)
p2.discount()
p2.display()




