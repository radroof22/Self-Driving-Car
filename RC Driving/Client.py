import requests

server = "192.168.1.159"
port = "5000"

def send_image(greyed_image):
    print("http://{}:{}/{}".format(server, port, greyed_image))
    direction_response = requests.get("http://{}:{}/{}".format(server, port, greyed_image)).text
    return direction_response

def test():
    test_data = [1, 2, 4]
    direction = send_image(test_data)
    print(direction)

test()