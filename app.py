import random
import string
from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def generate_random(count, upper, lower, numbers, symbols):
    if upper==False and lower==False and numbers==False and symbols==False:
        return ''
    else:
        all_characters = ""
        if lower:
            all_characters += string.ascii_lowercase
        if upper:
            all_characters += string.ascii_uppercase
        if numbers:
            all_characters += string.digits
        if symbols:
            all_characters += string.punctuation
        
    
        password = []
        if lower:
            password.append(random.choice(string.ascii_lowercase))
        if upper:
            password.append(random.choice(string.ascii_uppercase))
        if numbers:
            password.append(random.choice(string.digits))
        if symbols:
            password.append(random.choice(string.punctuation))
        
        # Fill the rest of the password length with random choices from all selected categories
        remaining_length = count - len(password)
        password.extend(random.choices(all_characters, k=remaining_length))
        
        # Shuffle the result to avoid predictable patterns
        random.shuffle(password)
        
        return ''.join(password)

@app.route('/',methods=['POST','GET'])
def get():
    if request.method=='POST':
        count=request.form.get('input-box')
        upper='upper-case' in request.form
        lower='lower-case' in request.form
        numbers='numbers' in request.form
        symbols='symbols' in request.form
        password=generate_random(int(count),upper,lower,numbers,symbols)
        return render_template("index.html",data=password)


if __name__=="__main__":
    app.run(debug=True)