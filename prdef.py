print ('')
print ("задание 1")
def print_hello ():
    print("Привет мир!")
print_hello ()
print_hello ()

print ('')
print ("задание 2")
def greet(name):
    print(f"Привет, {name}!")

greet("Анна")
greet("Олег")

print ('')
print ("задание 3")
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

print ('')
print ("задание 4")
def greet(name="Гость"):
    print(f"Привет, {name}!")

greet("Анна")
greet()

print ('')
print ("задание 5")
def subtract(a, b):
    return a - b

print(subtract(10, 3))
print(subtract(a=10, b=3))
print(subtract(b=3, a=10))

print ('')
print ("задание 6")
def introduce(name, city="Москва"):
    return f"Меня зовут {name}, я из города {city}"

print(introduce("Анна"))
print(introduce("Олег", "Казань"))

print ('')
print ("задание 7")
def multiply(*args):
    result = 1
    for number in args:
        result *= number
    return result

print(multiply(2, 3, 4))
print(multiply(5, 6))
print(multiply())

print ('')
print ("задание 8")
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Анна", age=18, city="Москва")

print ('') 
print ("задание 9")
def order(product, *extras, quantity=1):
    result = f"Товар: {product}, количество: {quantity}"
    if extras:
        result += f", дополнения: {', '.join(extras)}"
    return result

print(order("Пицца"))
print(order("Пицца", "Сыр", "Соус", quantity=2))

print ('')
print ("задание 10")
def profile(name, age=18, **kwargs):
    result = [f"Имя: {name}", f"Возраст: {age}"]

    for key, value in kwargs.items():
        result.append(f"{key} — {value}")

    return result

print(profile("Анна"))
print(profile("Олег", 20, city="Москва", job="Программист"))