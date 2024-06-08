#1
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
x = sample_dict.keys()
print(x)

#2
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75,
    'chemistry': 89,
    'GK': 50
    
}
y = sample_dict.values()
print(sum(y))

#3
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
minimum = min(sample_dict, key=sample_dict.get)
print(minimum)

#4
sample_dict = {
    "name": "Khalid",
    "age": 23,
    "salary": 1000,
    "city": "Baku"
}
sample_dict.pop("name")
sample_dict.pop("salary")
print(sample_dict)

#5
sample_dict = {
    "name": "Khalid",
    "age": 23,
    "salary": 1000,
    "city": "Baku"}
sample_dict.pop("age")
sample_dict.pop("city")
print(sample_dict)

#6
number = 0
sum_of_number = 0
while number < 10:
    num = int(input("Enter 10 integer:"))
    sum_of_number += num
    number += 1
print(number/sum_of_number)    
        
#7
number = 24
result = ''''''
count = 0
while count <= 10:
    result += f"{number}*{count}={number*count}\n"
    count+= 1
    print(result)

#8 - açıqcası dediyiniz kimi etməyin yolunu tapa bilmədim. Gbt-dəən də soruşdum oda pramoy cavab verdi
number = int(input("Enter a number to calculate its factorial: "))
result = 1
if number < 0:
    print("Invalid input.")
elif number == 0 or number == 1:
    result = 1    
else:
     for i in range(1, number + 1):
        result *= i
print(f"The factorial of {number} is {result}")

#9
number = input("Enter a number to calculate its digits: ")
sum_of_digits = 0
for digit in number:
     sum_of_digits += int(digit)
print(f"The sum of the digits of {number} is {sum_of_digits}")



#10
user_input = input("Enter a string: ")
character_count = len(user_input)
print(f"The number of characters in the string is: {character_count}")