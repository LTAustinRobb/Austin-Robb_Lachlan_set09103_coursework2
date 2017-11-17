from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
#secret key- learn this?
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def main():
  return render_template('main.html')

@app.route('/anxiety')
def anxiety():
  return render_template('test.html',page="'/anxiety'")

@app.route('/depression')
def depression():
  return render_template('test.html',page="'/depression'")

@app.route('/lgbt')
def lgbt():
  return render_template('test.html',page="'/lgbt'")

@app.route('/relationships')
def relationships():
  return render_template('test.html',page="'/relationships'")

@app.route('/other1')
def other1():
  return render_template('test.html',page="'/other1'")

@app.route('/other2')
def other2():
  return render_template('test.html',page="'/other2'")



@socketio.on('message',namespace='/anxiety')
def handleMessage(data):
  #print message
  print ('message:'+data[0])
  #broadcast, send message out to all other users
  send(data, broadcast=True)

@socketio.on('message',namespace='/depression')
def handleMessage(data):
  #print message
  print ('message:'+data[0])
  #broadcast, send message out to all other users
  send(data, broadcast=True)


@socketio.on('message',namespace='/lgbt')
def handleMessage(data):
  #print message
  print ('message:'+data[0])
  #broadcast, send message out to all other users
  send(data, broadcast=True)



@socketio.on('message',namespace='/relationships')
def handleMessage(data):
  #print message
  print ('message:'+data[0])
  #broadcast, send message out to all other users
  send(data, broadcast=True)



@socketio.on('message',namespace='/other1')
def handleMessage(data):
  #print message
  print ('message:'+data[0])
  #broadcast, send message out to all other users
  send(data, broadcast=True)



@socketio.on('message',namespace='/other2')
def handleMessage(data):
  #print message
  print ('message:'+data[0])
  #broadcast, send message out to all other users
  send(data, broadcast=True)


if __name__ == '__main__':
  socketio.run(app)
