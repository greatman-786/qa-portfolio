import sqlite3


def test_user_saved_in_database():
    conn = sqlite3.connect("test.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (email TEXT)")
    conn.execute("INSERT INTO users VALUES ('asad@email.com')")
    conn.commit()

    result = conn.execute(
        "SELECT * FROM users WHERE email = 'asad@email.com'"
    ).fetchone()

    assert result is not None
    conn.close()