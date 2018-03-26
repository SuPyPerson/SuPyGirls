from control.home import application
import bottle

_ = application

if __name__ == "__main__":
    bottle.run(host='localhost', port=8080)
