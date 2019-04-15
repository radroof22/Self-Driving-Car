from flask import Flask
app = Flask(__name__)

@app.route("/<image_data>")
def image_handle(image_data):
    return random_direction(image_data)


def random_direction(data):
    #junk
    return "Left"


@app.route('/hello')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run('0.0.0.0')