def connect():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

        cur = conn.cursor()

        cur.execute("SELECT DISTINCT id
	FROM (SELECT userid,COUNT(Einkommen)
	FROM mfb_user
	GROUP BY id
	ORDER BY COUNT(Einkommen) DESC
	LIMIT 1)")

        result = cur.fetchone()[0]
    cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
	return result
