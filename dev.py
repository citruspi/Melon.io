import os
from flask import Flask, request
from melonio import melonio

app   = Flask(__name__)
app.debug = True

keys = ['aB9K25bLvq4i54iQEA3RKmR6AgMH4FG1',
        'C3Hz1C9Mh4NOrN825G7n9P1aarXqPkWH',
        'Mk5a3J55D8HnQ36ii797faZBd8WbAKQ6']


@app.route('/', methods=['GET', 'POST'])
def hello():

    if request.method == "GET":

        return "Send requests via POST."

    if request.method == "POST":

        if request.headers.get('api_key') not in keys:

            return 'Your application is invalid or unregistered.'

        else:

            return melonio.solve(request.form['query'])


if __name__ == '__main__':
    
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
