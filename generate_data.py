import pandas as pd

products=[
("Noise Cancelling Wireless Headphones","electronics","Premium wireless headphones with active noise cancellation and long battery life.",129),
("Budget Bluetooth Earbuds","electronics","Affordable compact Bluetooth earbuds for daily travel and calls.",39),
("Travel Backpack","bags","Lightweight laptop travel backpack with water resistant material and multiple pockets.",59),
("Running Shoes","fashion","Comfortable lightweight running shoes with breathable mesh for daily workouts.",79),
("Smart Watch","electronics","Fitness smartwatch with heart rate tracking GPS and notifications.",149),
("Laptop Stand","electronics","Adjustable ergonomic aluminum laptop stand for office and home use.",45),
("Mechanical Keyboard","electronics","Compact mechanical keyboard for programming gaming and office work.",89),
("USB C Hub","electronics","Multiport USB C hub with HDMI USB and card reader for laptops.",49),
("Yoga Mat","fitness","Non-slip exercise yoga mat with comfortable cushioning.",29),
("Coffee Maker","home","Automatic coffee maker for home and office with programmable brewing.",99),
]
rows=[]
uid=[1,2,3,4,5]
for i,(name,cat,desc,price) in enumerate(products,1):
    rows.append({"product_id":i,"product_name":name,"description":desc,"category":cat,"price":price,"user_id":uid[i%len(uid)]})
pd.DataFrame(rows).to_csv("products.csv",index=False)
print("Created products.csv")
