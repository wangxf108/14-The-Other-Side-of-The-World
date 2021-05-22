# 在程序中想插入地图的函数，但是python不自带，所以载入folium，使用其中的map object type
# 另外自己想需要一个variable，但不清楚使用什么，可以google，看别人用什么。

from folium import Map

latitude = float("40.09")
longitude = float("-3.47")

antipode_latitude = latitude.__mul__(int("-1")) 

# __lt__小于但不等于； __le__小于等于。
# 通过输入dir(float)找到float, 然后输入 help(float.__le__) 找到对应函数

if longitude.__lt__(float("0")):
    antipode_longitude = longitude.__add__(float("180"))

elif longitude.__eq__(float("0")):
    antipode_longitude = float("180")

elif longitude.__gt__(float("180")):
    antipode_longitude = str("Invalid Longitude")

else:
    antipode_longitude = longitude.__sub__(float("180"))

# python中的list object is used to store multiple objects.(any kinks)
location = list((antipode_latitude, antipode_longitude))
mymap = Map(location)
mymap.save(str("antipode.html"))

print(antipode_latitude)
print(antipode_longitude)
print(mymap)
 