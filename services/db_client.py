import sqlite3


conn=sqlite3.connect('market_agent.db')
cur=conn.cursor()
cur.execute('''create table if not exists company(
                symbol text primary key,
                name text not null)''')

# cur.execute('Delete from company')
# cur.execute('Select* from company')
# print(cur.fetchall())
# conn.commit()
# conn.close()




class DbClient():
    def __init__(self) -> None:
        self.conn=sqlite3.connect('market_agent.db')


    def add_company(self,symbol:str,name:str) -> None:
        with self.conn:
            self.conn.execute("Insert into company values(:symbol, :name)",{'symbol':symbol,'name':name})


    def delete_company(self,symbol:str) -> None:
        with self.conn:
            self.conn.execute("Delete from company where symbol=:symbol",{'symbol':symbol})


    def get_companies(self) -> list:
        cur=self.conn.cursor()
        cur.execute("Select symbol from company")
        return [company[0] for company in cur.fetchall()]


    def show_table(self)-> None:
        cur=self.conn.cursor()
        cur.execute("Select * from company")
        print(cur.fetchall())

        