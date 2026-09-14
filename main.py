from pyscript import display, document

#part 1

fullname = 'Jan Immanuel Diaz Cabading' #stringggggg
age = 15 #int
h3ight = 164.745 #float
countries_vc_it_jp = ['Vatican City', 'Italy', 'Japan'] #list
student_type = False #boolean
student_profile = { #dictionary 
    'color': 'Maroon',
    'car_brand': 'BMW',
    'shoe_size': 9.5,
    'best_friends': 'Jacob Minguillo, Andre Pagud, Raphael Buan, Parminder Bhullar, Paul Afable'
}
fav_fruits = {'Banana', 'Melon', 'Watermelon', 'Grape', 'Sweet Mango'} #set
DOTW = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') #tuple

display(f"Full Name: {fullname}", target="output")
display(f"Age: {age}", target="output")
display(f"Height: {h3ight} cm", target="output")
display(f"Countries to Visit: {','.join(countries_vc_it_jp)}", target="output")
display(f"Is New Student: {student_type}", target="output")

# for student profile (used ai to organize them)

display(f"Color: {student_profile['color']}", target="output")
display(f"Car Brand: {student_profile['car_brand']}", target="output")
display(f"Shoe Size: {student_profile['shoe_size']}", target="output")
display(f"Best Friends: {student_profile['best_friends']}", target="output")

# end
display(f"Favorite Fruits: {', '.join(fav_fruits)}", target="output")
display(f"Days of the Week: {', '.join(DOTW)}", target="output")

# end of part 1
# start of part 2

def add_numbers():
num1 = float(document.querySelector("#num1").value)
num2 = float(document.querySelector("#num2").value)
result = num1 + num2
document.querySelector("#result").innerText = result

def subtract_numbers():
num1 = float(document.querySelector("#num1").value)
num2 = float(document.querySelector("#num2").value)
result = num1 - num2
document.querySelector("#result").innerText = result

        
        def multiply_numbers():
            num1 = float(document.querySelector("#num1").value)
            num2 = float(document.querySelector("#num2").value)
            result = num1 * num2
            document.querySelector("#result").innerText = result


        def divide_numbers():
            num1 = float(document.querySelector("#num1").value)
            num2 = float(document.querySelector("#num2").value)

if num2 == 0:
                document.querySelector("#result").innerText = "Cannot divide by zero"
                return

result = num1 / num2
document.querySelector("#result").innerText = result

# end of part 2
