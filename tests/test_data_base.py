import sqlite3
import os
import shutil
from resources.constants import *

if os.path.exists(TEMPORAL_DIR):
    shutil.rmtree(TEMPORAL_DIR)

os.mkdir(TEMPORAL_DIR)


def test_create_data_base():
    dir_database = os.path.join(TEMPORAL_DIR, TEST_DATABASE)
    db = sqlite3.connect(dir_database)
    cursor = db.cursor()

    with open(PROJECT_DATABASE_SQL) as file:
        sql = "".join(file.readlines())

    cursor.executescript(sql)

    assert True
