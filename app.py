from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def fizzBuzz():
    fizzbuzz_list = []
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            fizzbuzz_list.append('FizzBuzz')
        elif number % 3 == 0:
            fizzbuzz_list.append('Fizz')
        elif number % 5 == 0:
            fizzbuzz_list.append('Buzz')
        else:
            fizzbuzz_list.append(number)

   
    return render_template('fizzbuzz.html', fizzbuzz_list=fizzbuzz_list)
    

