from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
#secret key- learn this?
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def main():
  return render_template('main.html')

@app.route('/test')
def test():
  return render_template('test.html',page="'/test'")

@app.route('/main')
def room2():
  return render_template('test.html',page='/main')

@socketio.on('message',namespace='/test')
def handleMessage(data):
  #print message
  print ('message:'+data[0])
  #broadcast, send message out to all other users
  send(data, broadcast=True)

@socketio.on('message',namespace='/main')
def handleMessage(data):
  #print message
  print ('message:'+data[0])
  #broadcast, send message out to all other users
  send(data, broadcast=True)

if __name__ == '__main__':
  socketio.run(app)
