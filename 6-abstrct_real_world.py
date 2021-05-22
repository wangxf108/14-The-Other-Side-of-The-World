# 面向对象
latitude = float("40.09")
longitude = float("-3.47")

# 前面的latitude的值乘以后面的负整数   __mul__()
antipode_latitude = latitude.__mul__(int("-1")) 

# 前面的值，加上后面的float. __add_
antipode_longitude1 = longitude.__add__(float("180"))

# 前面的值，减去后面的值
antipode_longitude2 = longitude.__sub__(float("180"))

print(antipode_latitude)
print(antipode_longitude1)
print(antipode_longitude2)