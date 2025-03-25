
import cantools
import canboard

def build_db(base_id):
    db = cantools.database.Database()
    db.name = "CANBoard"
    db.version = "2.1.1" #FW version
    
    db.messages.append(canboard.build_msg_0(base_id))
    db.messages.append(canboard.build_msg_1(base_id))
    db.messages.append(canboard.build_msg_2(base_id))

    return db