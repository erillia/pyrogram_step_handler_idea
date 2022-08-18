
import json
from pyrogram import filters 


class mjson: # ? handle json file in text class
  def __init__(self,name):
    
    self.name=name
    open(name , '+a').close()
    
  def read(self):
    with open(self.name, mode="r") as f:
      if f.read().strip() == '':
        fs = open(self.name , '+a')
        fs.write('{}')
        fs.close()
      data = json.load(f)
    return data
    
  def write(self,data):
    with open(self.name, mode="w") as f:
      json.dump(data, f, indent=4)
    
  def reads(self,text):
    return json.loads(text)


class step:
    def __init__(self) -> None:
        """Create an object from step"""
        self.users = {}
    
    def add(self , uid , state):
        self.users[uid] = state
    
    def remove(self , uid):

        self.users.pop(uid)

    def clear_all_steps(self):
        self.users = {}

    def on(self , state):
        def user(_,__,message):
            if message.from_user.id in self.users:
                if self.users[message.from_user.id] == state:
                    return True
            return False
        return filters.create(user)

class text:
    def __init__(self , json_name) -> None:
        self.db = mjson(json_name)
        self.data = self.db.read()
        self.save = lambda : self.db.write(self.data)
    def __add__(self , x):
        self.data[x[0]] = x[1]
        self.save()
    
    def __getattr__(self , x):
        return self.data[x]

