message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

name = "ada lovelace brace"
print(name.title())

message1 = "JJK"
message2 = "123"
print(message1 + " " + message2)

print("Languages:\nPython\nC\nJavaScript")

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[2].title())
print(bicycles[-1].title())

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
print(motorcycles[2].title())
motorcycles.append('jjk')
print(motorcycles[-1])
print(motorcycles)
motorcycles.insert(3, 'ducati')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
print("\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle.title(),"\n")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles,"\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']	#对列表元素排列顺序的修改是永久性的
cars.sort()
print(cars,"\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars,"\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']	# sorted() 对列表进行临时排序
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars,"\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']	#方法 reverse() 永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，为此只需对列表再次调用 reverse() 即可
print(cars)
cars.reverse()
print(cars,"\n",len(cars),"\n")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!","\n")

for value in range(1,5):
	print(value)

number = list(range(1,6))
print(number)

even_numbers = list(range(2,20,2))
print(even_numbers)
print("min=",min(even_numbers),"max=",max(even_numbers),"sum=",sum(even_numbers),"\n")

squares = [value**2 for value in range(1,11)]
print(squares)

for value1 in range(1,21):
	print(value1)
print(list(range(1,21))[4:6])
print(list(range(1,21))[:6])
print(list(range(1,21))[3:])
print(list(range(1,21))[-4:])
vga = list(range(1,21))
for num in vga[-6:]:
	print(num)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#num = list(range(1,10**6+1))
#print("min=",min(num),"max=",max(num),"sum=",sum(num),"\n")

dimensions = (200, 50)	#整个生命周期内都不变，可使用元组
print(dimensions[0])
print(dimensions[1])

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

age = 25
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")
