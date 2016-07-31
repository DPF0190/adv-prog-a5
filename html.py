from flask import Flask
from json import dumps
app = Flask(__name__)
@app.route('/<oid>', methods=['GET'])
def findObject(oid):
  #DB lookup code goes here
  db = client['my database']
  return dumps({'oid': oid, 'attr': 'object_data'})
@app.route('/<oid>', methods=['POST', 'PUT'])
def updateObject(oid):
  #DB Update/Upsert code goes here
  obj_srch = {'oid': oid}
  my_object = my_collecion.findOne(obj_srch)
  if my_object is None:
      my_object = obj_srch.copy()
  my_collection.update(obj_srch, my_object, upsert=True)
  print 'I got a post request!'
  return ""
if __name__ == '__main__':
  with app.test_client() as c:
    get_resp = c.get('/blah')
    print 'get status: %s' % get_resp.status
    print 'get response: %s' % get_resp.get_data()
    post_resp = c.post('/blah')
