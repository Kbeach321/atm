#### IMPORTS #########
import records
db = records.Database("postgres://localhost/atm")

######## Create Table ############
db.query("DROP TABLE IF EXISTS atm_table;")
create_query = """
CREATE TABLE atm_table (
    id SERIAL PRIMARY KEY,
    transactions NUMERIC(20)
);
"""
db.query(create_query)

########## Insert Data ##############
insert_query = """
INSERT INTO atm_table (transactions) VALUES (0);
"""
db.query(insert_query)
