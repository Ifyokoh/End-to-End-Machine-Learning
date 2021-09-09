import psycopg2


class Database():
    def __init__(self):
        """
        Connection to work with the remote database on Heroku platform.
        :return: connection
        """
        self.__connection = psycopg2.connect(
                database="ddt86fqfteau87",
                user="jbnnnlzzyzkhci",
                password="70cdffbd005c5cd0ac4cec6f4f7525aa28b3b30338d3dbde2389ee3be4aadc9a",
                host="ec2-52-19-164-214.eu-west-1.compute.amazonaws.com",
                port="5432"
        )
        # self.__connection = psycopg2.connect(
        #         database="db",
        #         user="user",
        #         password="password",
        #         host="host",
        #         port="port"
        # )

    def create_table(self) -> None:
        """
        Create table for storing predictions in database.
        :return: None
        """
        with self.__connection.cursor() as cur:
            cur.execute('''
                CREATE TABLE IF NOT EXISTS predictions (
                    id SERIAL PRIMARY KEY,
                    date TIMESTAMP DEFAULT NOW(),
                    input_values VARCHAR,
                    predicted_values VARCHAR
                );
        ''')
            self.__connection.commit()

    def insert_record(self, request: str, response: str) -> None:
        """
        Inserts the input provided by the user and the output by the model to the created table
        :return: None
        """
        with self.__connection.cursor() as cur:
            cur.execute("INSERT INTO predictions (input_values, predicted_values)\
                VALUES (%s, %s)" ,(request, response)) 
            self.__connection.commit()
    

    def get_recent_records(self, number_of_records) -> list:
        """
        Returns the desired number of most recent results consisting in input-output pairs
        :return:
        """
        with self.__connection.cursor() as cur:
            cur.execute('''
            SELECT input_values, predicted_values
            FROM Predictions
            ORDER BY date DESC
            LIMIT %(number)s
            ''',
                        {
                            "number": number_of_records
                        })
            return cur.fetchall()


if __name__ == "__main__":
    database = Database()
    database.create_table()