import sqlite3, rich, datetime

def ticket_init(user_pseudo):
        ticket_list = []
        connection = sqlite3.connect('bdd/tickPy.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM tickPy_s WHERE owner == ?', (user_pseudo,))
        tickets_data = cursor.fetchall()
        connection.close()
        for ticket in tickets_data:
            ticket_list.append(cTicket(ticket))
        return ticket_list

def ticket_show(ticket_list):
        if ticket_list == []:
            print(f'You don’t have ticket')
        else :
                rich.print("""
+------------+------------+----------+-----------
|  [bold]Starting[/bold]  |   [bold]Ending[/bold]   | [bold]Approved[/bold] | [bold]Validator[/bold]
+------------+------------+----------+-----------""")
                for ticket in ticket_list:
                    print(f"""\
| {ticket.date_start} | {ticket.date_end} |     {ticket.approved}    | {ticket.validator}
+------------+------------+----------+-----------""")
        input('')

def ticket_new(user_pseudo):
    date_start = input('When start your ticket DD/MM/YYYY ? ')
    date_end = input('When finnish your ticket DD/MM/YYYY ? ')
    validator = input('Who approves your ticket (pseudo) ? ')
    if ticket_validator_check(validator) :
        connection = sqlite3.connect('bdd/tickPy.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO tickPy_tickets(owner, date_start, date_end, validator, approved) VALUES(?,?,?,?,?)', (user_pseudo, date_start, date_end, validator, False))
        connection.commit()
        connection.close()
        print('Request Send')
    input('')

def ticket_owner_check(validator_pseudo):
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

def tecket_remove(ticket_list):
    rich.print("""
+----+------------+------------+----------+-----------
| [bold]ID[/bold] |  [bold]Starting[/bold]  |   [bold]Ending[/bold]   | [bold]Approved[/bold] | [bold]Validator[/bold]
+----+------------+------------+----------+-----------""")
    for ticket in ticket_list:
        print(f"""\
| {ticket.id} | {ticket.date_start} | {ticket.date_end} |     {ticket.approved}    | {ticket.validator}
+----+------------+------------+----------+-----------""")
    id = input('Which ticket to remove (ID) ? ')

    connection = sqlite3.connect('bdd/tickPy.db')
    cursor = connection.cursor()
    #cursor.execute('DELETE FROM tickPy_tickets WHERE id == ?', (int(id),)) TODO
    validator_info = cursor.fetchone()
    connection.close()

    print('Done')
    input('')

class cTicket:
    def __init__(self, ticket_info):
        self.id = ticket_info[0]
        self.name = ticket_info[1]
        self.last_modif = ticket_info[2]
        self.owner = ticket_info[3]
        self.status = ticket_info[4]
