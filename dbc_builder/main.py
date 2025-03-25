import cantools
import canboard

base_id = 1648

if __name__ == "__main__":
    dbs = []
    dbs.append(canboard.build_db(base_id))
    
    for db in dbs:
        filename = "./dbc/" + db.name + "_" + db.version + ".dbc"
        with open(filename, "w") as f:
            f.write(db.as_dbc_string())
        print(db.name + " v" + db.version + " DBC file created successfully!")
    