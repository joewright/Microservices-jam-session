# Microservices
Just a microservice presentation

This repository is just to learn how microservices work in various different languages. This code will eventually show every single language that I feel comfortable using in a microservice architecture
If you want more information then just message me on linkedin https://www.linkedin.com/in/ian-mizer-039843155/

## JW Edits

At a PyATL jam session meetup, I made some edits to this so that 2 web servers each serve their own page. Server A receives comms and displays all received messages. Server B is a GUI to show a button to send date stamps to Server A. Pressing a button on Server B will result in a message being displayed on server A.

### Run it
This assumes you've installed [Python](https://www.python.org/) version 3.9+.

Pull the repo and install dependencies
```sh
pip install requests flask
```

In terminal A, run
```sh
flask --app receiver_app.py run --host 0.0.0.0 --port 5003
```

In terminal B, run
```sh
flask --app time_form_app.py run --host 0.0.0.0 --port 5004
```

Now you can
- View [Site A](http://localhost:5003) in your browser
- View [Site B](http://localhost:5003) in your browser
- click the button in site B
- look at the message in site A
- enjoy