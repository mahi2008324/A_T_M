import psycopg2

class Connecting_DB:
    def connections(self):
        try:
            # Connect to the PostgreSQL database
            db_conn = psycopg2.connect(
                dbname="BANK",
                user='postgres',  # fixed username
                host='localhost',
                password='root',
                port=5432
            )
            print("Connected successfully.")

            # Create a cursor object
            curs = db_conn.cursor()

            # Execute a sample SQL query (e.g., fetch all from a table named 'accounts')
            print("Fetching table data:")
            #Perform INSERT operation so we have to use commit
            #curs.execute("INSERT INTO BANK VALUES (121212121212,112411570011,4000000,9854102367001111,9984,'ROHIT')")  # make sure this table exists
            #curs.execute("UPDATE BANK SET INTREST=BALANCE*0.01 WHERE BALANCE > 100000")
            #curs.execute("UPDATE BANK SET TOTAL_BALANCE=INTREST+BALANCE")
            #curs.execute("ALTER TABLE BANK ADD COLUMN LOAN BIGINT")
            #curs.execute("UPDATE BANK SET LOAN=INTREST*400 WHERE PIN < 5000;")
            curs.execute("UPDATE BANK SET LOAN = 0 WHERE PIN > 5000 ; ")
            db_conn.commit()
            curs.execute("SELECT * FROM BANK")
            
            for row in curs.fetchall():
                print(row)

        except Exception as e:
            print("Error:", e)

        finally:
            # Safely close resources
            curs.close()
            db_conn.close()

# Create an object and call the method
db = Connecting_DB()
db.connections()

