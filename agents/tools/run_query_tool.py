import sqlite3
from langchain.tools import Tool

conn = sqlite3.connect("db.sqlite")

def get_tables():
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = c.fetchall()
    return "\n".join(row[0] for row in rows)


def run_sqlite_query(query):
    try:
        c = conn.cursor()
        c.execute(query)
        return c.fetchall()
    except sqlite3.OperationalError as err:
        return f"Something went wrong while executing query: {err} /n"


run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="Run the sqlite function",
    func=run_sqlite_query
)