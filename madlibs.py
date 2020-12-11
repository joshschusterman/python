# Simple madlibs program, just for fun with concatenation.

location = input("Country or city: ")
surface1 = input("Surface: ")
surface2 = input("Another surface: ")
surface3 = input("Another surface: ")
place1 = input("Place: ")
place2 = input("Another place: ")
place3 = input("Another place: ")
place4 = input("Another place: ")
geo1 = input("Geographic feature: ")
geo2 = input("Another geographic feature: ")

churchill = f"We shall go on to the end, we shall fight in \
{location}, we shall fight on the {surface1} and the {surface2}, we shall fight \
with growing confidence and growing strength in the {place1}, we shall \
defend our {geo1}, whatever the cost may be, we shall fight on the {geo2}, \
we shall fight on the {surface3}, we shall fight in the {place2} and in \
the {place3}, we shall fight in the {place4}; we shall never surrender!"

print("\n")
print(churchill)
print("\n")