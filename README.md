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

# Disclaimer
This is a personal hobby project. I am not a professional. Use at your own risk. 

# Schematic
[Schematic PDF](/Export/V2/CANBoard_HW_V2.pdf)

# Images
![Top](/Images/Top.jpg)

![Bottom](/Images/Bottom.jpg)

![Connections](/Images/CANBoard_V2_Connections.png)

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

# Initial Programming
Use [Tag Connect TC2030 cable](https://www.tag-connect.com/product/tc2030-ctx-nl-stdc14-for-use-with-stm32-processors-with-stlink-v3) 

# JLCPCB
Here are screenshots from the JLCPCB ordering process

From the main page [JLCPCB](https://jlcpcb.com/)

Click Add gerber

![AddGerber](/Images/JLCPCB/AddGerber.jpg)

You should see these board dimensions

Select your PCB quantity here

![BoardDims](/Images/JLCPCB/BoardDims.jpg)

Set your PCB specs (I usually select TG155)

![PCBSpecs](/Images//JLCPCB/PCBSpecs.jpg)

I also like to select "Confirm Production File"

![HighSpec](/Images/JLCPCB/HighSpec.jpg)

Click the PCB Assembly slider and set the settings below

Select "Confirm Parts Placement"

![Assembly](/Images/JLCPCB/Assembly.jpg)

Upload the BOM and CPL files from the [Export/V2/JLCPCB](/Export/V2/JLCPCB/) directory

Or from the directory of whichever version you would like to make

![Upload](/Images/JLCPCB/Upload.jpg)

V2 should have 70 parts detected

*Note: If there are values under "parts not selected" they are likely out of stock and they cannot be populated by JLCPCB*

*Either substitutes need to be found on their [parts database](https://jlcpcb.com/parts) or you will need to wait for them to restock*

![Detected](/Images/JLCPCB/Detected.jpg)

Review the BOM to make sure all of the parts are correct (not all parts shown here)

![BOMReview](/Images/JLCPCB/BOMReview.jpg)

***----IMPORTANT---***

Review the the part placement (rotation)

It should look exactly as it does below

***TAKE NOTE OF THE PINK CIRCLES THAT INDICATE PIN 1***

***MAKE SURE THE LED IS FACING THE CORRECT WAY - SMALL PINK LINE***

![PartPlacement](/Images/JLCPCB/PartPlacement.jpg)

Now you can add the board to your cart and place your order, have fun!
