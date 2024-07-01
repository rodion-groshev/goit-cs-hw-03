import psycopg2


def create_db():
    conn = psycopg2.connect(dbname="postgres",
                            user="postgres",
                            host="localhost",
                            port="5432",
                            password="1qayxsw2"
                            )
    cur = conn.cursor()

    with open("request.sql", "r") as f:
        create_sql = f.read()

    cur.execute(create_sql)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    create_db()
