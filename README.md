# CANBoard_HW
CANBoard is a simple CAN enabled IO board, specifically designed to be used in devices like steering wheels/button boxes/panels/etc.

* 8 digital inputs
    * Ground switching
* 5 analog inputs
    * 5V max
* 4 digital outputs
    * Low side switch (open collector)
    * 0.5A max each
* CAN output message format compatible with ECUMaster CAN Switch Board
* STM32F303K8
* KiCad 7.0.0

# Goals
- Create a low cost device that my friends and I can use in our project cars
- Use components that are easily soldered by hand (hence 0805) and are preferably from my stock of frequently used parts (ex: LD1117S33CTR)
- Format the CAN messages in a similar way to the ECUMaster CAN Switch board
- Share my work with others for reference, inspiration or collaboration. 

If this project does help you in any way, I'd appreciate a message!

# Disclaimer
This is a personal hobby project. I am not a professional. Use at your own risk. 

# Schematic
[Schematic PDF](/Export/V2/CANBoard_HW_V2.pdf)

# Images
![Top](/Images/CANBoard_Top.jpg)

![Bottom](/Images/CANBoard_Bottom.jpg)

![Connections](/Images/CANBoard_V2_Connections.png)

# Jumpers
**CAN Term** : Soldering this jumper enables the 120 ohm terminating resistor across CANL/CANH

**CAN ID Jumpers 1 and 2** : Soldering these jumpers allows different CAN IDs to be selected when using multiple CANBoards in the same bus
| 1      | 2      | CAN ID (Hex)|
| ------ | ------ | ----- |
| Open   | Open   | 0x640 |
| Closed | Open   | 0x641 |
| Open   | Closed | 0x642 |
| Closed | Closed | 0x643 |

# Firmware
[CANBoard firmware](https://github.com/corygrant/CANBoard_FW)

# Initial Programming
Use [Tag Connect TC2030 cable](https://www.tag-connect.com/product/tc2030-ctx-nl-stdc14-for-use-with-stm32-processors-with-stlink-v3) 