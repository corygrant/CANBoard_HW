import cantools
import canboard

base_id = 1648

if __name__ == "__main__":
    db = canboard.build_db(base_id)

    with open("./dbc/" + db.name + "_" + db.version + ".dbc", 'w') as f:
        f.write(db.as_dbc_string()) 
    