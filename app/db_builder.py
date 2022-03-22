import sqlite3   
import random 
import json

DB_FILE="data.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events


def dbsetup():

  command = "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, cash INTEGER, upgrades TEXT, progress INTEGER, gaming BOOLEAN)"
  c.execute(command)

  #command = "CREATE TABLE IF NOT EXISTS upgrades(user_id"

  db.commit()

def signup(username, password):
  c.execute("""SELECT username FROM users WHERE username=?""",[username])
  result = c.fetchone()

  if result:
      return True

  else:
      c.execute('INSERT INTO users VALUES (null, ?, ?, ?, ?, ?, ?)', (username, password, 0, "000000000", 0, False))
      
      db.commit()
      # Uses empty quotes since it will return false when checked as a boolean
      return  ""

# Tries to check if the username and password are valid
def login(username, password):

  c.execute("""SELECT username FROM users WHERE username=? AND password=?""",[username, password])
  result = c.fetchone()

  if result:
      ##access this specifc user data
      return False

  else:
      return True

def save(username, data):
  saveData = data.split(",")
  print(saveData)
  # c.execute("""UPDATE users SET WHERE username=?""", username)
