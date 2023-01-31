import sqlite3, rich, tool, vacation, hashlib

class cUser:
    def __init__(self, user_info):
        self.first_name = user_info[1]
        self.last_name = user_info[2]
        self.pseudo = user_info[3]
        self.role = cRole(user_info[4])
        self.password = user_info[5]

    def menu_alternant_info(self):
        rich.print("""    
+---+----------------++---+-------------------+
| 1 | Vacation       || 2 | Ticket            |
+---+----------------++---+-------------------+
| [bold cyan]q[/bold cyan] | Exit           || [red]c[/red] | [red]Change password[/red]   |
+---+----------------++---+-------------------+
        """)

    def menu_alternant(self):
        choose = input('> ')
        return_value = True
        if choose == '1':
            tool.clear()
            vacation.vacation_simple_menu(self.pseudo)
        elif choose == '2':
            vacation.vacation_ask(self.pseudo)
        elif choose == 'c':
            self.change_password()
        elif choose == 'q':
            print('Exit()')
            return_value = False
        return return_value

    def menu_technicien_info():
        rich.print("""    
+---+----------------++---+----------------+
| 1 | Vacation       || 2 | Ticket         |
+---+----------------++---+----------------+
| [red]3[/red] | [red]Change password[/red] || q | Exit()         |
+---+----------------++---+----------------+""")

    def menu_technicien():
        choose = input('> ')

    def menu_chef_de_service():
        rich.print("""    
    +---+----------------+
    | 1 | Vacation       |
    +---+----------------+
    | 2 | Ticket         |
    +---+----------------+
    | [red]3[/red] | [red]Change password[/red] |
    +---+----------------+
    | q | Exit()         |
    +---+----------------+
        """)
        choose = input('> ')

    def menu_chef_de_service_info():
        rich.print("""    
+---+----------------++---+------------------+
| 1 | Vacation       || 2 | Ask for vacation |
+---+----------------++---+------------------+
| 3 | Show ticket    || [red]4[/red] | [red]Change password[/red]  |
+---+----------------++---+------------------+
| q | Exit()         |
+---+----------------+""")
    
    def menu_ressources_humaines_info():
        print('')

    def menu_ressources_humaines():
        choose = input('> ')
    
    def menu_admin_info():
                rich.print("""    
+---+---------------++---+------------------+
| 1 | Show vacation || 2 | Ask for vacation |
+---+---------------++---+------------------+
| 3 | Show ticket   || [red]4[/red] | [red]Change password[/red]  |
+---+---------------++---+------------------+""")

    def menu_admin():
        choose = input('> ')

    def menu(self):
        if self.role.name == 'admin':
            return_value = self.menu_admin()
        elif self.role.name == 'Alternant':
            return_value = self.menu_alternant()
        elif self.role.name == 'Technicien':
            return_value = self.menu_technicien()
        elif self.role.name == 'Chef de service':
            return_value = self.menu_chef_de_service()
        elif self.role.name == 'Ressources Humaines':
            return_value = self.menu_ressources_humaines()
        return return_value

    def menu_info(self):
        if self.role.name == 'admin':
            self.menu_admin_info()
        elif self.role.name == 'Alternant':
            self.menu_alternant_info()
        elif self.role.name == 'Technicien':
            self.menu_technicien_info()
        elif self.role.name == 'Chef de service':
            self.menu_chef_de_service_info()
        elif self.role.name == 'Ressources Humaines':
            self.menu_ressources_humaines_info()

    def change_password(self):
        old_password = input('Old paswword : ')
        new_password = input('New password : ')
        new_new_password = input('Again new password : ')
        if new_password == new_new_password:
            if hashlib.md5(old_password.encode()).hexdigest() == self.password:
                connection = sqlite3.connect('bdd/tickPy.db')
                cursor = connection.cursor()
                hash_new_password = hashlib.md5(new_password.encode()).hexdigest()
                cursor.execute("UPDATE tickPy_users SET password=? WHERE pseudo=?", (hash_new_password, self.pseudo))
                connection.commit()
                connection.close()
                self.password = hash_new_password
            else:
                rich.print('[bold red](ERROR)[/bold red] Bad password')
        else : 
            rich.print('[bold red](ERROR)[/bold red] Password not match')
        print('Done')
        input("Press Enter to continue...")
            
class cRole:
    def __init__(self, role_name):
        connection = sqlite3.connect('bdd/tickPy.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM tickPy_roles WHERE role == ?', (role_name,))
        role_info = cursor.fetchone()
        connection.close()
        print(role_info[1])
        self.name = role_info[1]
        self.text = role_info[2]
        self.color = role_info[3]