# class product():
#     count=0

#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         product.count+=1


#     def product_info(self):
#         print(f"the price {self.name} is RS {self.price}.")

#     @classmethod
#     def total_quantity(cls):
#         print(f"total no of product in store = {cls.count}")
    
#     @staticmethod
#     def cal_discount(price,discount):
#         print(f"discount price = {price-(price*discount/100)}")

# p1=product("phone",10_000)
# p2=product("laptop",10_0000)
# p3=product("earpods",20_000)

# p1.product_info()        
# product.total_quantity()
# p1.cal_discount(p1.price,12)



#####Q

# class bankaccount():
#     def __init__(self,acc_no,owner_name,balance):
#         self.acc_no = acc_no
#         self.owner_name = owner_name
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance += amount
#         print( "Deposited  :",amount)
    
#     def withraw(self,amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("widhraw amt :",amount)
#         else:
#             print("insuffecient balance")

#     def check_balance(self):
#         print("current balance",self.balance)
        
# acc=bankaccount(100985,"kunal",100_000)

# acc.deposit(1000)
# acc.check_balance()
# acc.withraw(20000)


####q


# class book():

#     def __init__(self,title,author):
#         self.title = title
#         self.author= author
#         self.reviews = []

#     def add_reviews(self,review):
#         self.reviews.append(review)
#         print("review added !")

#     def count_reviews(self):
#         print("total reviews :",len(self.reviews))

#     def  display_reviews(self):
#         print("all reviews :")
#         for r in self.reviews:
#             print("->",r)

# b_1=book("py","kunal")

# b_1.add_reviews("very helpful !")

# b_1.display_reviews()
  

#####Q



# class student():
#     def __init__(self,name,roll_no,marks):
#         self._name=name
#         self._roll_no = roll_no
#         self._marks = marks
    
#     def get_name(self):
#         return self._name
#     def get_roll_no(self):
#         return self._roll_no
#     def get_marks(self):
#         return self._marks
    
#     def set_name(self,name):
#         if name != "":
#             self._name=name
#         else:
#             print("name cannot be empty!")

#     def set_roll_no(self,roll_no):
#         if 1<=roll_no<=100:
#             self._roll_no=roll_no
#         else:
#             print("roll no must be b/w 1 to 100")
    
#     def set_marks(self,marks):
#         if marks>=0:
#             self._marks=marks
#         else:
#             print("marks cannor be negtive!")


# s=student("kunal",23,90)
# print(s.get_name())
# s.set_marks(1)
# s.set_roll_no(10)
# print(s.get_roll_no())


#####q

# class shape:
#     def area(self):
#      return 0 
    
# class circle(shape):
#       def __init__(self,radius):
#        self.radius=radius

#       def area(self):
#        return 3.14*self.radius*self.radius      
# class rectangle(shape):
#       def __init__(self,length,breath):
#          self.length = length
#          self.breath = breath
#       def area(self):
#          return self.length*self.breath
# class triangel(shape):
#       def __init__(self,base,height):
#          self.base=base
#          self.height=height
#       def area(self):
#          return 0.5*self.base*self.height
      
# c=circle(5)
# print("circle area ",c.area())

# r=rectangle(3,5)
# print("rectangle area",r.area())

# t=triangel(30,6)
# print("triange area",t.area())
         
         
      
#####Q



# class vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

# class car(vehicle):
#     def __init__(self, brand, model,seats):
#         super().__init__(brand, model)
#         self.seats= seats

# class bike(vehicle):
#     def __init__(self, brand, model,engine_cc):
#         super().__init__(brand, model)
#         self.engine_cc= engine_cc

# c= car("mahindra","rox",5)
# b=bike("BMW","rx100",250)

# print(c.brand,c.model,c.seats)
# print(b.model,b.brand,b.engine_cc)


######Q


# class person:

#     def __init__(self,name="",age=None,address=""):
#         self.name = name
#         self.age = age
#         self.address = address
    

# p1 = person("kunal")
# p2 = person("aditya",23)
# p3 = person("yash",20,"delhi")

# print(p1.name,p1.age,p1.address)
# print(p2.name,p2.age,p2.address)
# print(p3.name,p3.age,p3.address)
        
         

        



        