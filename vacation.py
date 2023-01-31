import sqlite3, cUser, rich, tool, datetime

def vacation_simple_menu(user_pseudo):
    rich.print("""    
+---+----------------++---+-------------------+
| 1 | Show           || 2 | Remove            |
+---+----------------++---+-------------------+
| 3 | Ask            || [bold cyan]q[/bold cyan] | Exit              |
+---+----------------++---+-------------------+""")
    choose = input('> ')
    if choose == '1':
        vacation_show(vacation_init(user_pseudo))
    elif choose == '2':
        vacation_remove(vacation_init(user_pseudo))
    elif choose == '3':
        vacation_ask(user_pseudo)
    elif choose == 'q':
        print('')
    else :
        rich.print('[bold red](ERROR)[/bold red] Bad request')

def vacation_init(user_pseudo):
        vacation_list = []
        connection = sqlite3.connect('bdd/tickPy.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM tickPy_vacations WHERE owner == ?', (user_pseudo,))
        vacations_data = cursor.fetchall()
        connection.close()
        for vacation in vacations_data:
            vacation_list.append(cVacation(vacation))
        return vacation_list

def vacation_show(vacation_list):
    if vacation_list == []:
        print(f'You don’t have registered vacancy')
    else :
            rich.print("""
+------------+------------+----------+-----------
|  [bold]Starting[/bold]  |   [bold]Ending[/bold]   | [bold]Approved[/bold] | [bold]Validator[/bold]
+------------+------------+----------+-----------""")
            for vacation in vacation_list:
                print(f"""\
| {vacation.date_start} | {vacation.date_end} |     {vacation.approved}    | {vacation.validator}
+------------+------------+----------+-----------""")
    input("Press Enter to continue...")

def vacation_ask(user_pseudo):
    date_start = input('When start your vacation DD/MM/YYYY ? ')
    date_end = input('When finnish your vacation DD/MM/YYYY ? ')
    validator = input('Who approves your vacation (pseudo) ? ')
    if vacation_ask_validator_check(validator) :
        connection = sqlite3.connect('bdd/tickPy.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO tickPy_vacations(owner, date_start, date_end, validator, approved) VALUES(?,?,?,?,?)', (user_pseudo, date_start, date_end, validator, False))
        connection.commit()
        connection.close()
        print('Request Send')
    input("Press Enter to continue...")

def vacation_ask_date_check(start, end):
    start_list = start.split('/')
    end_list = end.split('/')

    date_start = datetime.datetime(start_list[2], start_list[1], start_list[0])
    date_end = datetime.datetime(end_list[2], end_list[1], end_list[0])



def vacation_ask_validator_check(validator_pseudo):
    connection = sqlite3.connect('bdd/tickPy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tickPy_users WHERE pseudo == ?', (validator_pseudo,))
    validator_info = cursor.fetchone()
    connection.close()
    if validator_info == None or cUser.cUser(validator_info).role.name != 'Ressources Humaines':
        rich.print('[bold red](ERROR)[/bold red] Bad validator')
        return_value = False
    else :
        return_value = True
    return return_value

def vacation_remove(vacation_list):
    rich.print("""
+----+------------+------------+----------+-----------
| [bold]ID[/bold] |  [bold]Starting[/bold]  |   [bold]Ending[/bold]   | [bold]Approved[/bold] | [bold]Validator[/bold]
+----+------------+------------+----------+-----------""")
    for vacation in vacation_list:
        print(f"""\
| {vacation.id} | {vacation.date_start} | {vacation.date_end} |     {vacation.approved}    | {vacation.validator}
+----+------------+------------+----------+-----------""")
    id = input('Which vacation to remove (ID) ? ')

    connection = sqlite3.connect('bdd/tickPy.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM 'tickPy_vacations' WHERE id = ?", (int(id),))
    connection.commit()
    connection.close()

    print('Done')
    input("Press Enter to continue...")

class cVacation:
    def __init__(self, vacation_info):
        self.id = vacation_info[0]
        self.owner = vacation_info[1]
        self.date_start = vacation_info[2]
        self.date_end = vacation_info[3]
        self.validator = vacation_info[4]
        self.approved = vacation_info[5]
    