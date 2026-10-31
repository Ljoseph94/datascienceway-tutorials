"""Code from "SQL GROUP BY and HAVING: Summarising Data Properly"
https://datascienceway.com/sql-group-by-having/
Author: Lucky Joseph. MIT licence.
"""

import sqlite3
from pathlib import Path

here = Path(__file__).parent
con = sqlite3.connect(":memory:")
con.executescript((here / "schema.sql").read_text())
sql = (here / "queries.sql").read_text()
buf = ""
for line in sql.splitlines(keepends=True):
    buf += line
    if sqlite3.complete_statement(buf):
        stmt = buf.strip()
        buf = ""
        code = "\n".join(l for l in stmt.splitlines() if not l.strip().startswith("--")).strip()
        if not code:
            continue
        print("\n" + stmt)
        cur = con.execute(stmt)
        if cur.description:
            print(" | ".join(d[0] for d in cur.description))
            for row in cur.fetchall():
                print(" | ".join(str(v) for v in row))
