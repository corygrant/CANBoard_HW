import cantools
from utils.signal_utils import create_duplicate_signals
from cantools.database.conversion import LinearConversion

def build_msg_3(base_id):
    message = cantools.database.Message(
        frame_id=base_id + 3,
        name="CANBoardMsg3",
        length=8,
        is_extended_frame=False,
        signals=[]
    )

    output1_sig = cantools.database.Signal(
        name="Output1",
        start=0,
        length=1,
        byte_order="little_endian",
        is_signed=False,
        conversion=LinearConversion(1, 0, False),
        minimum=0,
        maximum=1
    )
    message.signals.append(output1_sig)

    output2_sig = cantools.database.Signal(
        name="Output1",
        start=8,
        length=1,
        byte_order="little_endian",
        is_signed=False,
        conversion=LinearConversion(1, 0, False),
        minimum=0,
        maximum=1
    )
    message.signals.append(output2_sig)

    output3_sig = cantools.database.Signal(
        name="Output1",
        start=16,
        length=1,
        byte_order="little_endian",
        is_signed=False,
        conversion=LinearConversion(1, 0, False),
        minimum=0,
        maximum=1
    )
    message.signals.append(output3_sig)

    output4_sig = cantools.database.Signal(
        name="Output4",
        start=24,
        length=1,
        byte_order="little_endian",
        is_signed=False,
        conversion=LinearConversion(1, 0, False),
        minimum=0,
        maximum=1
    )
    message.signals.append(output4_sig)
    
    return message