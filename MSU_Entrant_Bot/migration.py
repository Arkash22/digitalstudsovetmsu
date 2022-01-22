import psycopg2

conn = psycopg2.connect(dbname='', user='',
                        password='', host='')
cursor = conn.cursor()  # обращаться будем через курсор
# print(cursor)

def create_migration():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users_all  (
                   id serial PRIMARY KEY,
                   chatid INTEGER,
                   username TEXT,
                   is_student BOOLEAN,
                   is_teacher BOOLEAN,
                   is_entrant BOOLEAN,
                   tg_name TEXT,
                   faculty_id INTEGER,
                   program_id INTEGER,
                   is_reg BOOLEAN
                   )
                   """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS faculty(
                    id serial PRIMARY KEY,
                    name TEXT,
                    latitude real,
                    longitude real,
                    mail_sc text,
                    tel text
                    )
                    """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS faculty_programs(
                    faculty_id integer,
                    id serial Primary Key,
                    name text,
                    ege_n integer,  
                    ege_p integer,
                    ege_list text,
                    dvi_list text,
                    dvi_min_n integer,
                    dvi_min_p integer,
                    dvi_mean_n integer,
                    dvi_mean_p integer,
                    min_score integer,
                    paid integer,
                    budget integer,
                    quota integer,
                    price text,
                    total_people integer,
                    passing_score_1v integer,
                    passing_score_2v integer,
                    people_seat integer
                    
                )
                """) # _n прошлый год 2020 _p позапрошлый год 2019
    conn.commit()
    cursor.close()


def delete_migration():
    cursor.execute("DROP TABLE users_all")
    cursor.execute("DROP TABLE faculty")
    cursor.execute("DROP TABLE faculty_programs")

    conn.commit()
    cursor.close()

create_migration()
# delete_migration()
