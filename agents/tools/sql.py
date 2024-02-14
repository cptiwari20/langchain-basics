import sqlite3
from pydantic.v1 import BaseModel
from typing import List
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
    
def describe_tables(*table_names):
    try:
        c = conn.cursor()
        tables = ", ".join("'" + table + "'" for table in table_names)
        rows = c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name IN ({tables});")
        return "\n".join(row[0] for row in rows if row[0] is not None)

    except sqlite3.OperationalError as err:
        return f"Something went wrong while executing query: {err} /n" 


class DefineRunQueryArgsSchema(BaseModel):
    query: str

run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="Run the sqlite function",
    func=run_sqlite_query,
    args_schema=DefineRunQueryArgsSchema
)

class DefineDescribeTableArgsSchema(BaseModel):
    table_names: List[str]

run_describe_tables = Tool.from_function(
    name="describe_tables",
    description="It takes a list of table names and it will return a list of table schema",
    func=describe_tables
)