from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def main():
  return render_template('main.html')

@app.route('/anxiety')
def anxiety():
  return render_template('test.html',page="'/anxiety'",title="Anxiety")

@app.route('/depression')
def depression():
  return render_template('test.html',page="'/depression'",title="Depression")

@app.route('/lgbt')
def lgbt():
  return render_template('test.html',page="'/lgbt'",title="LGBT")

@app.route('/relationships')
def relationships():
  return render_template('test.html',page="'/relationships'",title="Relationships")

@app.route('/stress')
def stress():
  return render_template('test.html',page="'/stress'",title="Stress")

@app.route('/offtopic')
def offtopic():
  return render_template('test.html',page="'/offtopic'",title="Off Topic")



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
