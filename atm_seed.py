#### IMPORTS #########
import records
db = records.Database("postgres://localhost/atm")

######## Create Table ############
db.query("DROP TABLE IF EXISTS atm_table;")
create_query = """
CREATE TABLE atm_table (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(200),
    bank_value VARCHAR(30),
    transactions NUMERIC(20)
);
"""
db.query(create_query)

########## Insert Data ##############
insert_query = """
INSERT INTO atm_table (user_name, bank_value, transactions) VALUES ('Kevin Beach', '1,000', 0);
"""
db.query(insert_query)
