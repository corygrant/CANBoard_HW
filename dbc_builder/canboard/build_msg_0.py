import cantools
from utils.signal_utils import create_duplicate_signals

def build_msg_0(base_id):
    message = cantools.database.Message(
        frame_id=base_id + 0,
        name="CANBoardMsg0",
        length=8,
        is_extended_frame=False,
        signals=[]
    )

    adc_volt_sigs = create_duplicate_signals("ADCVolt", 4, 1, 0, 16, 0.001, 0)
    message.signals.extend(adc_volt_sigs)
    
    return message