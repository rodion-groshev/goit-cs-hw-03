import psycopg2


def connector(sql):
    with psycopg2.connect(dbname="postgres",
                          user="postgres",
                          host="localhost",
                          port="5432",
                          password="1qayxsw2") as conn:
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        return res


def update_connector(sql):
    with psycopg2.connect(dbname="postgres",
                          user="postgres",
                          host="localhost",
                          port="5432",
                          password="1qayxsw2") as conn:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()


def tasks_by_user(user_id):
    sql = f"SELECT title, description FROM tasks WHERE user_id={user_id}"
    return connector(sql)


def tasks_by_status(status):
    sql = (f"SELECT title, description, s.name "
           f"FROM tasks as t "
           f"JOIN status as s ON s.id = t.status_id "
           f"WHERE s.name='{status}' ")
    return connector(sql)


def update_status(new_status, task_id):
    if new_status == "new":
        new_status = 1
    elif new_status == "in progress":
        new_status = 2
    elif new_status == "completed":
        new_status = 3
    else:
        return "Wrong status"

    sql = (f"UPDATE tasks SET status_id='{new_status}' "
           f"WHERE id = {task_id}")
    return update_connector(sql)


def users_without_tasks():
    sql = ("""SELECT fullname 
              FROM users
              WHERE users.id NOT IN 
              (SELECT tasks.user_id FROM tasks)""")
    return connector(sql)


def add_task(new_title, new_description, user_id):
    sql = (f"INSERT INTO tasks (user_id, title, description) "
           f"VALUES ('{user_id}', '{new_title}', '{new_description}')")
    return update_connector(sql)


def all_unresolved_tasks():
    sql = ("""SELECT title, description, s.name
              FROM tasks
              JOIN status as s ON s.id = tasks.status_id
              WHERE tasks.status_id != 3""")
    return connector(sql)


def delete_tasks_by_id(id):
    sql = f"DELETE FROM tasks WHERE id = '{id}'"
    return update_connector(sql)


def find_via_email(email):
    sql = (f"SELECT fullname, email FROM users "
           f"WHERE email LIKE '%{email}%'")
    return connector(sql)


def update_fullname(user_id, new_fullname):
    sql = (f"UPDATE users SET fullname = '{new_fullname}' "
           f"WHERE id = {user_id}")
    return update_connector(sql)


def count_status():
    sql = """SELECT name, COUNT(s.name) FROM status as s
             JOIN tasks as t ON t.status_id = s.id
             GROUP BY name"""
    return connector(sql)


def tasks_via_domain(domain):
    sql = (f"SELECT title, description, u.email "
           f"FROM tasks as t "
           f"JOIN users as u ON u.id = t.user_id "
           f"WHERE u.email like '%{domain}%'")
    return connector(sql)


def tasks_without_description():
    sql = (f"SELECT title from tasks as t "
           f"WHERE description = '[NULL]'")
    return connector(sql)


def tasks_in_progress():
    sql = """SELECT fullname, t.title, s.name
              FROM users as u
              INNER JOIN tasks as t ON t.user_id = u.id
              INNER JOIN status as s ON t.status_id = s.id
              WHERE t.status_id = 2"""
    return connector(sql)


def count_tasks_by_user():
    sql = """SELECT fullname, COUNT(title)
             FROM users as u
             LEFT JOIN tasks as t ON t.user_id = u.id
             GROUP BY fullname"""
    return connector(sql)

if __name__ == '__main__':
    print(tasks_by_user(2))
    print(tasks_by_status("completed"))
    # update_status("completed", 2)
    print(users_without_tasks())
    # add_task("Call", "Ask developers about bug", 2)
    print(all_unresolved_tasks())
    # delete_tasks_by_id(12)
    print(find_via_email("richard"))
    # update_fullname(5, "Richard Hamilton")
    print(count_status())
    print(tasks_via_domain("@example.org"))
    print(tasks_without_description())
    print(tasks_in_progress())
    print(count_tasks_by_user())