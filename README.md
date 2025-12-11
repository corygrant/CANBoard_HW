# CANBoard_HW
CANBoard is a simple CAN enabled IO board, specifically designed to be used in devices like steering wheels/button boxes/panels/etc.

* 8 digital inputs
    * Ground switching
* 5 analog inputs
    * 5V max
* 4 digital outputs
    * Low side switch (open collector)
    * 0.5A max each
* STM32F303K8
* KiCad 7.0.0

# Goals
- Create a low cost device that my friends and I can use in our project cars
- Use components that are easily soldered by hand (hence 0805) and are preferably from my stock of frequently used parts (ex: LD1117S33CTR)
- Share my work with others for reference, inspiration or collaboration. 

If this project does help you in any way, I'd appreciate a message!

# [Store](https://dingo-electronics.square.site/product/canboard/3)

# Disclaimer
Please note that this product has been designed by a hobbyist, not a professional. It is intended for off-road and testing use only. Users should operate the product at their own discretion and risk. The designer explicitly disclaims any responsibility for damage or injury that may result from the use of this product.

# Schematic
[Schematic PDF](/Export/V2/CANBoard_HW_V2.pdf)

# DBC

DBC file can be found [here](https://github.com/corygrant/CANBoard_FW/tree/main/dbc)

# BOM

[Interactive BOM](https://htmlpreview.github.io/?https://github.com/corygrant/CANBoard_HW/tree/main/docs/bom/ibom.html)

# Jumpers
**CAN Term** : Soldering this jumper enables the 120 ohm terminating resistor across CANL/CANH

**CAN ID Jumpers 1 and 2** : Soldering these jumpers allows different base CAN IDs to be selected when using multiple CANBoards in the same bus
| 1      | 2      | Base CAN ID (Hex)|
| ------ | ------ | ----- |
| Open   | Open   | 0x640 |
| Closed | Open   | 0x650 |
| Open   | Closed | 0x660 |
| Closed | Closed | 0x670 |

# Firmware
[CANBoard firmware](https://github.com/corygrant/CANBoard_FW)

# Updating Firmware
Use [Tag Connect TC2030 cable](https://www.tag-connect.com/product/tc2030-ctx-nl-stdc14-for-use-with-stm32-processors-with-stlink-v3) 


# Images
![Top](/Images/Top.jpg)

![Bottom](/Images/Bottom.jpg)

![Connections](/Images/CANBoard_V2_Connections.png)

