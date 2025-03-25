import cantools
from utils.signal_utils import create_duplicate_signals
from cantools.database.conversion import LinearConversion

def build_msg_2(base_id):
    message = cantools.database.Message(
        frame_id=base_id + 2,
        name="CANBoardMsg2",
        length=8,
        is_extended_frame=False,
        signals=[]
    )

    rotary_sw_sigs = create_duplicate_signals("RotarySwitch", 5, 1, 0, 4, 1, 0)
    message.signals.extend(rotary_sw_sigs)
    
    dig_in_sigs = create_duplicate_signals("DigitalInput", 8, 1, 32, 1, 1, 0)
    message.signals.extend(dig_in_sigs)
    
    analog_sw_sigs = create_duplicate_signals("AnalogSwitch", 5, 1, 40, 1, 1, 0)
    message.signals.extend(analog_sw_sigs)
    
    dig_out_sigs = create_duplicate_signals("DigitalOutput", 4, 1, 48, 1, 1, 0)
    message.signals.extend(dig_out_sigs)
    
    heartbeat_sig = cantools.database.Signal(
        name="Heartbeat",
        start=56,
        length=8,
        byte_order="little_endian",
        is_signed=False,
        conversion=LinearConversion(1, 0, False),
        minimum=0,
        maximum=255
    )
    message.signals.append(heartbeat_sig)
    
    return message