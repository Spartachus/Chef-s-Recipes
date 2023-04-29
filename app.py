from flask import Flask,render_template,request,url_for
import requests
from dotenv import load_dotenv
import os
from email.message import EmailMessage
import ssl
import smtplib


def configure():
  load_dotenv()

app = Flask(__name__)

Email = []

@app.route("/", methods=['POST','GET'])
def hello_world():
    configure()
    if request.method == 'POST':
      Api_Key = os.getenv("api_key")
      email_pass = os.getenv("email_password")
      if request.form['submit_button'] == 'search_button':
        try:
            food = request.form['contact']
            id_food = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?apiKey={Api_Key}&query={food}&number=1")
            food_id_json = id_food.json()
            food_id = food_id_json["results"][0]["id"]
            food_title = food_id_json["results"][0]["title"]
            hvjc = requests.get(f"https://api.spoonacular.com/recipes/{food_id}/summary?apiKey={Api_Key}")
            ghnv = hvjc.json()
            content = ghnv["summary"]
            return render_template("recipes.html",content = content,food = food)
        except:
          return render_template("failed.html")
      elif request.form['submit_button'] == 'random_button':
        id_food = requests.get(f"https://api.spoonacular.com/food/jokes/random?apiKey={Api_Key}&number=1")
        food_id_json = id_food.json()
        sdf = food_id_json["text"]

        hvjc = requests.get(f"https://api.spoonacular.com/food/trivia/random?apiKey={Api_Key}")
        ghnv = hvjc.json()
        sum = ghnv["text"]

        return render_template("random.html",content = sdf,food_title = sum)

      elif request.form['submit_button'] == 'subscribe_button':
        try:
            food = request.form['flow']
            email_sender = "chef.recipes.io@gmail.com"
            email_reciever = food
            Email.append(email_reciever)
            passcode = email_pass
            print(Email)

            subject = "Thanks for subscribing"
            body = """
            Here'a a joke:  'Why can't a bicycle stand on its own? It's two-tired.'
            """
            em = EmailMessage()
            em["From"] = email_sender
            em["To"] = email_reciever
            em["Subject"] = subject
            em.set_content(body)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
                smtp.login(email_sender, passcode)
                smtp.sendmail(email_sender, email_reciever, em.as_string())
            return render_template('success.html')
        except:
          return render_template('success.html')
    return render_template('index.html')


@app.route("/pasta", methods=['POST','GET'])
def pasta():
    configure()
    if request.method == 'POST':
      Api_Key = os.getenv("api_key")
      email_pass = os.getenv("email_password")
      if request.form['submit_button'] == 'search_button':
        try:
            food = request.form['contact']
            id_food = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?apiKey={Api_Key}&query={food}&number=1")
            food_id_json = id_food.json()
            food_id = food_id_json["results"][0]["id"]
            food_title = food_id_json["results"][0]["title"]
            hvjc = requests.get(f"https://api.spoonacular.com/recipes/{food_id}/summary?apiKey={Api_Key}")
            ghnv = hvjc.json()
            content = ghnv["summary"]
            return render_template("recipes.html",content = content,food = food)
        except:
          return render_template("failed.html")
      elif request.form['submit_button'] == 'random_button':
        id_food = requests.get(f"https://api.spoonacular.com/food/jokes/random?apiKey={Api_Key}&number=1")
        food_id_json = id_food.json()
        sdf = food_id_json["text"]

        hvjc = requests.get(f"https://api.spoonacular.com/food/trivia/random?apiKey={Api_Key}")
        ghnv = hvjc.json()
        sum = ghnv["text"]

        return render_template("random.html",content = sdf,food_title = sum)

      elif request.form['submit_button'] == 'subscribe_button':
        try:
            food = request.form['flow']
            email_sender = "chef.recipes.io@gmail.com"
            email_reciever = food
            passcode = email_pass

            subject = "Thanks for subscribing"
            body = """
            Here'a a joke:  'Why can't a bicycle stand on its own? It's two-tired.'
            """
            em = EmailMessage()
            em["From"] = email_sender
            em["To"] = email_reciever
            em["Subject"] = subject
            em.set_content(body)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
                smtp.login(email_sender, passcode)
                smtp.sendmail(email_sender, email_reciever, em.as_string())
            return render_template('success.html')
        except:
          return render_template('success.html')
    return render_template('pasta.html')

@app.route("/pizza", methods=['POST','GET'])
def pizza():
    configure()
    if request.method == 'POST':
      Api_Key = os.getenv("api_key")
      email_pass = os.getenv("email_password")
      if request.form['submit_button'] == 'search_button':
        try:
            food = request.form['contact']
            id_food = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?apiKey={Api_Key}&query={food}&number=1")
            food_id_json = id_food.json()
            food_id = food_id_json["results"][0]["id"]
            food_title = food_id_json["results"][0]["title"]
            hvjc = requests.get(f"https://api.spoonacular.com/recipes/{food_id}/summary?apiKey={Api_Key}")
            ghnv = hvjc.json()
            content = ghnv["summary"]
            return render_template("recipes.html",content = content,food = food)
        except:
          return render_template("failed.html")
      elif request.form['submit_button'] == 'random_button':
        id_food = requests.get(f"https://api.spoonacular.com/food/jokes/random?apiKey={Api_Key}&number=1")
        food_id_json = id_food.json()
        sdf = food_id_json["text"]

        hvjc = requests.get(f"https://api.spoonacular.com/food/trivia/random?apiKey={Api_Key}")
        ghnv = hvjc.json()
        sum = ghnv["text"]

        return render_template("random.html",content = sdf,food_title = sum)

      elif request.form['submit_button'] == 'subscribe_button':
        try:
            food = request.form['flow']
            email_sender = "chef.recipes.io@gmail.com"
            email_reciever = food
            passcode = email_pass

            subject = "Thanks for subscribing"
            body = """
            Here'a a joke:  'Why can't a bicycle stand on its own? It's two-tired.'
            """
            em = EmailMessage()
            em["From"] = email_sender
            em["To"] = email_reciever
            em["Subject"] = subject
            em.set_content(body)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
                smtp.login(email_sender, passcode)
                smtp.sendmail(email_sender, email_reciever, em.as_string())
            return render_template('success.html')
        except:
          return render_template('success.html')
    return render_template('pizza.html')

@app.route("/burger", methods=['POST','GET'])
def burger():
    configure()
    if request.method == 'POST':
      Api_Key = os.getenv("api_key")
      email_pass = os.getenv("email_password")
      if request.form['submit_button'] == 'search_button':
        try:
            food = request.form['contact']
            id_food = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?apiKey={Api_Key}&query={food}&number=1")
            food_id_json = id_food.json()
            food_id = food_id_json["results"][0]["id"]
            food_title = food_id_json["results"][0]["title"]
            hvjc = requests.get(f"https://api.spoonacular.com/recipes/{food_id}/summary?apiKey={Api_Key}")
            ghnv = hvjc.json()
            content = ghnv["summary"]
            return render_template("recipes.html",content = content,food = food)
        except:
          return render_template("failed.html")
      elif request.form['submit_button'] == 'random_button':
        id_food = requests.get(f"https://api.spoonacular.com/food/jokes/random?apiKey={Api_Key}&number=1")
        food_id_json = id_food.json()
        sdf = food_id_json["text"]

        hvjc = requests.get(f"https://api.spoonacular.com/food/trivia/random?apiKey={Api_Key}")
        ghnv = hvjc.json()
        sum = ghnv["text"]

        return render_template("random.html",content = sdf,food_title = sum)

      elif request.form['submit_button'] == 'subscribe_button':
        try:
            food = request.form['flow']
            email_sender = "chef.recipes.io@gmail.com"
            email_reciever = food
            passcode = email_pass

            subject = "Thanks for subscribing"
            body = """
            Here'a a joke:  'Why can't a bicycle stand on its own? It's two-tired.'
            """
            em = EmailMessage()
            em["From"] = email_sender
            em["To"] = email_reciever
            em["Subject"] = subject
            em.set_content(body)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
                smtp.login(email_sender, passcode)
                smtp.sendmail(email_sender, email_reciever, em.as_string())
            return render_template('success.html')
        except:
          return render_template('success.html')
    return render_template('burger.html')

if __name__ == '__main__':
    app.run()
