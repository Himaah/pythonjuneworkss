mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]

#print all mobile names and brands.

mobile_names= [mob.get("title") for mob in mobiles]
# print(mobile_names)

brands={mob.get("brand") for mob in mobiles}
# print(brands)


# print samsung mobile users

samsung_users=[mob.get("title") for mob in mobiles if mob.get("brand")=="samsung"]
# print(samsung_users)

# print all mkbile names ranging from 23k to 40k

mobille_names=[mob.get("title") for mob in mobiles if mob.get("price") in range (23000,40001)]
# print(mobille_names)


# print costly mobile

max_price=0
for mob in mobiles:
    if mob.get("price") > max_price:
        max_price=mob.get("price")
max_price_mob=[mob.get("title") for mob in mobiles if (mob.get("price"))==max_price]
# print(max_price_mob)


def get_price(mob):
    return mob.get("price")

costly_mobile=max(mobiles,key=get_price)
# print(costly_mobile)

costly_mobilee=max(mobiles, key= lambda mob:mob.get("price"))
# print(costly_mobilee)

cheapest_mobile=min(mobiles,key=get_price)
print(cheapest_mobile)

total_cost= sum([mob.get("price") for mob in mobiles])
print(total_cost)