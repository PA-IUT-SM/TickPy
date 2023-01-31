#coding:utf-8
import sqlite3, hashlib, rich, tool, cUser

status = True

title = """
████████╗██╗ ██████╗██╗  ██╗██████╗ ██╗   ██╗
╚══██╔══╝██║██╔════╝██║ ██╔╝██╔══██╗╚██╗ ██╔╝
   ██║   ██║██║     █████╔╝ ██████╔╝ ╚████╔╝ 
   ██║   ██║██║     ██╔═██╗ ██╔═══╝   ╚██╔╝  
   ██║   ██║╚██████╗██║  ██╗██║        ██║   
   ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝        ╚═╝                                               
"""

def login():
    tool.clear()
    rich.print(f'[blue]{title}[/blue]')
    #input_username = input('What is your username: ')
    #input_password = hashlib.md5(input('What is your password: ').encode()).hexdigest()
    input_username = 'myron.gonzalez'
    input_password = hashlib.md5('aa123!'.encode()).hexdigest()
    connection = sqlite3.connect('bdd/tickPy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tickPy_users WHERE pseudo = ? AND password = ?', (input_username, input_password))
    user_info = cursor.fetchone()
    connection.close()
    if user_info == None:
        login()
    else:
        return cUser.cUser(user_info)

def welcome(user):
    tool.clear()
    rich.print(f'[blue]{title}[/blue]')
    rich.print(f'Welcome {user.first_name} your session has [{user.role.color}]{user.role.name.lower()}[/{user.role.color}].')
    rich.print(f'Remember {user.role.text.lower()}')

user = login()
loged = True
welcome(user)

while loged:
    user.menu_info()
    loged = user.menu()
    tool.clear()
