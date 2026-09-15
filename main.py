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
    'shoe_size': 8.5,
    'best_friends': 'Jacob Minguillo, Andre Pagud, Raphael Buan, Parminder Bhullar, Paul Afable'
}
fav_fruits = {'Banana', 'Melon', 'Watermelon', 'Grape', 'Sweet Mango'} #set
DOTW = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') #tuple

display(f"My full name is, {fullname}", target="output")
display(f"My age is, {age}", target="output")
display(f"My height is, {h3ight} cm", target="output")
display(f"I wanna travel to, {','.join(countries_vc_it_jp)}", target="output")
display(f"Am I a new student? {student_type}", target="output")

# for student profile (used ai to organize them)

display(f"My fav color: {student_profile['color']}", target="output")
display(f"My fav car brand: {student_profile['car_brand']}", target="output")
display(f"My shoe size: {student_profile['shoe_size']}", target="output")
display(f"My best friends are: {student_profile['best_friends']}", target="output")

# end
display(f"I love these fruits: {', '.join(fav_fruits)}", target="output")
display(f"Days of the Week: {', '.join(DOTW)}", target="output")

# end of part 1

# start of part 2

def add(i):
    n1 = float(document.getElementById("n1").value)
    n2 = float(document.getElementById("n2").value)
    document.getElementById("result").innerText = n1 + n2

def subtract(i):
    n1 = float(document.getElementById("n1").value)
    n2 = float(document.getElementById("n2").value)
    document.getElementById("result").innerText = n1 - n2

def multiply(i):
    n1 = float(document.getElementById("n1").value)
    n2 = float(document.getElementById("n2").value)
    document.getElementById("result").innerText = n1 * n2

def divide(i):
    n1 = float(document.getElementById("n1").value)
    n2 = float(document.getElementById("n2").value)
    document.getElementById("result").innerText = n1 / n2