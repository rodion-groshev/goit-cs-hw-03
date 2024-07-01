from faker import Faker
from random import randint
import psycopg2

tasks_number = 10
users_number = 5


def generate_fake_data(tasks_number, users_number):
    fake_tasks = []
    fake_users = []
    status_options = [('new',), ('in progress',), ('completed',)]

    fake_data = Faker()

    for _ in range(tasks_number):
        fake_tasks.append((fake_data.text(5), "".join(fake_data.sentences(1)), randint(1, 3), randint(1, 5)))

    for _ in range(users_number):
        fake_users.append((fake_data.name(), fake_data.email()))

    return fake_tasks, fake_users, status_options


def insert_data_to_db(tasks, users, status):
    with psycopg2.connect(dbname="postgres",
                          user="postgres",
                          host="localhost",
                          port="5432",
                          password="1qayxsw2") as conn:
        cur = conn.cursor()

        sql_users = """INSERT INTO users(fullname, email) VALUES (%s, %s)"""
        cur.executemany(sql_users, users)

        sql_status = """INSERT INTO status(name) VALUES (%s)"""
        cur.executemany(sql_status, status)

        sql_tasks = """INSERT INTO tasks(title, description, status_id, user_id) VALUES (%s, %s, %s, %s)"""
        cur.executemany(sql_tasks, tasks)

        conn.commit()


if __name__ == '__main__':
    tasks, users, status = generate_fake_data(tasks_number, users_number)
    insert_data_to_db(tasks, users, status)
