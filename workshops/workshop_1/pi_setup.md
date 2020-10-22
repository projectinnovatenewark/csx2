<div align=center><h1>Setting up your Raspberry Pi</h1></div>

In this workshop, you (the student) will assemble the Raspberry Pi single-board computer and install the nexessary software for the rest of the semester.

<div align=center><h2>Setting up your Raspberry Pi</h2></div>

1. First we are going to add the heat sinks to the Raspberry Pi (going forward it will be referred to as the Pi.)

    a. As you can see, your Pi comes with 3 heat sinks designed to keep **[INSERT 3 COMPONENTS HEAT SINKS ARE USED ON]** cool. The below picture labels where each heat sink belongs on the Pi.
        
    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/2_pi_with_sinks.jpg" width="400" height="auto" />
    </div>

    b. Place Pi guard #3 as pictured below on the pi to help place the heat sinks on the Pi. 

    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/7_pi_guards.jpg" width="400" height="auto" />
    <img src="./Raspberry_Pi_setup_images/3_use_guard_for_sinks.jpg" width="400" height="auto" />
    </div>

    c. After placing the heat sinks on the Pi, you should see the folling:
    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/5_pi_with_sinks.jpg" width="400" height="auto" />
    </div>

> Heat sinks keep the Pi cool to prevent it from overheating.

2. Insert the microSD card into the port on the bottom of the Pi.
    <!-- Images are JPEG  -->
    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/22_micro_sd.jpeg" width="400" height="auto" />
    <img src="./Raspberry_Pi_setup_images/21_insert_sd.jpeg" width="400" height="auto" />
    </div>

3. Remove the washers from the back of the display monitor. Make sure to keep these in a safe spot as they will be needed later.
    
    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/6_remove_washers.jpg" width="400" height="auto" />
    </div>

4. Place Pi guard #1 on the back of the display as shown below:

    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/7_pi_guards.jpg" width="400" height="auto" />
    <img src="./Raspberry_Pi_setup_images/8_place_first_guard.jpg" width="400" height="auto" />
    </div>

5. Place the Pi on top of the guard on the back of the display monitor.
    * The ethernet and USB ports should be facing away from the middle of the display.

    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/9_place_pi.jpg" width="400" height="auto" />
    </div>

6. Place the plastic guard (#2) followed by the final guard (#3) on top of the Pi. Then screw each washer back on so that the Pi is secure without too much pressure being on the Pi.
    
    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/10_pi_guard_2.jpg" width="auto" height="300" />
    <img src="./Raspberry_Pi_setup_images/11_pi_guard_3.jpg" width="auto" height="300" />
    </div>

7. Below are the USB-C cable and the micro-HDMI cables as well as their corresponding Pi ports.
    a. The USB-C provides power to the Pi.
    b. The micro-HDMI cable is used to display the GUI of the Pi.

    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/12_usbC_and_hdmi.jpg" width="auto" height="250" />
    <img src="./Raspberry_Pi_setup_images/13_port_view_of_pi.jpg" width="auto" height="250" />
    </div>

8. Plug in the USB-C into the display and then into the Pi as shown below:

    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/14_plug_in_usbC_in_disp.jpg" width="400" height="auto" />
    <img src="./Raspberry_Pi_setup_images/15_plug_in_usbC_in_pi.jpg" width="400" height="auto" />
    </div>

9. Repeat step 9 for the micro-HDMI cable as shown below:

    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/16_plug_hdmi_display.jpg" width="400" height="auto" />
    <img src="./Raspberry_Pi_setup_images/17_plug_hdmi_pi.jpg" width="400" height="auto" />
    </div>

10. Below is the power supply chord for the display which in turn also provides power for the Pi. Plug in to the display and a wall outlet to get started for the next section.

    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/18_power.jpg" width="400" height="auto" />
    <img src="./Raspberry_Pi_setup_images/20_plug_in_power.jpg" width="400" height="auto" />
    </div>

<div align=center><h2>Installing the Necessary Softwares</h2></div>

Pwer on your Raspberry Pi by holding the power button on the back of your monitor for about 5 seconds. 

<div class=mdImage align=center>
<img src="./Raspberry_Pi_setup_images/26_power_on.jpg" width="400" height="auto" />
</div>

<div align=center><h3>Installing Debian/Raspberry Pi OS</h3></div>

Now that everything is connected and the Pi is powered on, you should see something similar to the following screen:

<div class=mdImage align=center>
<img src="./Raspberry_Pi_setup_images/23_installing_rasp_os.jpg" width="400" height="auto" />
</div>

11. Setup up your wifi network by selecting the “Wifi networks (w)” button ciricled in the picture belowand follow the steps to connect to your local network.

<div class=mdImage align=center>
<img src="./Raspberry_Pi_setup_images/24_wifi_setup.jpeg" width="400" height="auto" />
</div>

12. Select the language at the bottom of the screen to be “English (US)”. Then click on the install button in the top left corner and check the box next to “Raspberry Pi OS FUll (32-bit) (RECOMMENDED)”. Then click the install button in the top left corner again.

<div class=mdImage align=center>
<img src="./Raspberry_Pi_setup_images/25_rasp_os.jpeg" width="400" height="auto" />
</div>

Now the OS should be installing onto your Raspberry Pi. This should take a few minutes until a popup appears to let you know that the OS has installed successfully.

13. There should be a prompt to update abd restart the Raspberry Pi. It is recommended to do so.

<div align=center><h3>Installing VS Code and Git</h3></div>

14. We will be using an open source version of VS Code that is compatible with the Pi. Click the terminal icon in the to left portion of your screen as circled below.

<div class=mdImage align=center>
<img src="./Raspberry_Pi_setup_images/27_rasp_term_icon.png" width="400" height="auto" />
</div>

You will see the following screen open:

<div class=mdImage align=center>
<img src="./Raspberry_Pi_setup_images/28_rasp_term.png" width="400" height="auto" />
</div>

15. In the terminal, execute the following command:

`https://packagecloud.io/headmelted/codebuilds/gpgkey -O - | sudo apt-key add -.`

