# Constans for tests

TEMPORAL_DIR = "admin_taxi_api/tests/temp"
TEST_DATABASE = "test_db.db"
PROJECT_DATABASE_SQL = "admin_taxi_api/models/data_base/data_base.sql"
SYNTHETIC_INFORMATION_SQL = "admin_taxi_api/tests/resources/synthetic_information.sql"
SQLALCHEMY_DATABASE_URL = "sqlite:///./" + TEMPORAL_DIR + "/" + TEST_DATABASE
