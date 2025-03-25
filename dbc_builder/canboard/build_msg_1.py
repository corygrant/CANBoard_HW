import cantools
from utils.signal_utils import create_duplicate_signals
from cantools.database.conversion import LinearConversion

def build_msg_1(base_id):
    message = cantools.database.Message(
        frame_id=base_id + 1,
        name="CANBoardMsg1",
        length=8,
        is_extended_frame=False,
        signals=[]
    )

    adc_volt_sig = cantools.database.Signal(   
        name="ADCVolt5",
        start=0,
        length=16,
        byte_order="little_endian",
        is_signed=False,
        conversion=LinearConversion(0.001, 0, False),
        minimum=0,
        maximum=6
    )
    message.signals.append(adc_volt_sig)
    
    board_temp_sig = cantools.database.Signal(
        name="BoardTemp",
        start=48,
        length=16,
        byte_order="little_endian",
        is_signed=False,
        conversion=LinearConversion(1, 0, False),
        minimum=0,
        maximum=125
    )
    message.signals.append(board_temp_sig)
    
    return message