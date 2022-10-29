class Users:
    def __init__(self, CORE):
        self.db = CORE.db


    # Удаляет пользователя по id
    def delete(self, id):
        sql = "DELETE FROM users WHERE id=%s"
        self.db.execute(sql, (id))
        return self.db.fetchone()


    # Возвращает пользователей
    def getUsersList(self):
        self.db.execute("SELECT * FROM users ORDER BY ordering")
        return self.db.fetchall()


    # Возвращает пользователя по id
    def getUser(self, id):
        sql = "SELECT * FROM users WHERE id=%s"
        self.db.execute(sql, (id))
        return self.db.fetchone()


    # Возвращает id по email
    def getUserByEmail(self, email):
        sql = "SELECT id FROM users WHERE email=%s"
        self.db.execute(sql, (email))
        return self.db.fetchone()


    # Добавляет пользователя в БД
    def insert(self, data):
        sql = "INSERT INTO users SET name = %s, surname = %s, email = %s, psw = %s, text = %s, phone = %s, ordering = %s, status = %s"
        self.db.execute(sql, (
            data['name'],
            data['surname'],
            data['email'],
            data['psw'],
            data['text'],
            data['phone'],
            data['ordering'],
            data['status']
        ))


    # Обновляет пользователя в БД
    def update(self, data):
        sql = "UPDATE users SET name = %s, surname = %s, email = %s, text = %s, phone = %s, ordering = %s, status = %s WHERE id = %s"
        self.db.execute(sql, (
            data['name'],
            data['surname'], 
            data['email'], 
            data['text'], 
            data['phone'],
            data['ordering'],
            data['status'],
            data['id']
        ))


    # Обновляет статус
    def setStatus(self, id, status):
        sql = "UPDATE users SET status = %s WHERE id = %s"
        self.db.execute(sql, (status, id))


    # Устанавливает порядок следования
    def setOrdering(self, id, act):
        users = self.getUsersList()
        ordering = 0
        for i, user in enumerate(users):
            if int(user['id']) == int(id):
                ordering = i

        arr = {}

        if act == 'up':
            if ordering == 0:
                return
            prev_id = users[ordering-1]['id']
            current_id = users[ordering]['id']
            arr[ordering - 1] = current_id
            arr[ordering] = prev_id
        else:
            if (ordering >= len(users) - 1):
                return
            next_id = users[ordering+1]['id']
            current_id = users[ordering]['id']
            arr[ordering + 1] = current_id
            arr[ordering] = next_id

        for i in arr:
            sql = "UPDATE users SET ordering = %s WHERE id = %s"
            self.db.execute(sql, (i+1, arr[i]))