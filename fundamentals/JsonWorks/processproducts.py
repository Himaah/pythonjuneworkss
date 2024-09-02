from json import load


f=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fundamentals\\JsonWorks\\products.json",encoding="UTF-8")


items=load(f)

# print(len(items))
item_titles=[i.get("title") for i in items]

# print(item_titles)

# jewelery_products=[i.get("title") for i in items if i.get("category")=="jewelery"]
# print(jewelery_products)


# for i in items:
#     # print(i.get("title"))
#     if i.get("category")=="jewelery":
#         print(i.get("title"))

products_price=[i.get("title") for i in items if i.get("price") >100]
# print(products_price)

# products available in range of 100 - 150
products_price_150=[i.get("title") for i in items if i.get("price") in range (100,151)]
# print(products_price_150)

products_pricee_150=[i.get("title") for i in items if i.get("price")>=100 and i.get("price")<=150]
# print(products_pricee_150)

products_priceid=[i.get("id") for i in items if i.get("price")>=100 and i.get("price")<=150]
# print(products_priceid)



# max reviews
def get_rating_count(dic):

    return dic.get("rating").get("count")

top_selling_products=max(items,key=get_rating_count)

print(top_selling_products.get("title"), top_selling_products.get("rating"))

# min reviews

def get_rating_count(dic):

    return dic.get("rating").get("count")

least_selling_products=min(items,key=get_rating_count)

print(least_selling_products.get("title"), least_selling_products.get("rating"))




