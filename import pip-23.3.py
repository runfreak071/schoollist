import pyautogui
import time
import schedule
import threading

# Function to automate pressing the down button
def press_down_button(num_clicks, interval=0.3):
    for _ in range(num_clicks):
        pyautogui.press('down')
        time.sleep(interval)

# Set the coordinates
omega_six_coords = (114, 656)
single_click_coords = (581, 308)
double_click_coords_1 = (62, 339)
single_click_coords_2 = (399, 144)
down_button_coords = (399, 144)  # Coordinates assumed; adjust as needed
type_coords = (846, 144)
click_coords = (1076, 667)

# Open Omega Six
pyautogui.doubleClick(omega_six_coords)

# Wait for 3 seconds and single-click
time.sleep(6)
pyautogui.click(single_click_coords)

# Wait for 7 seconds and double-click
time.sleep(14)
pyautogui.doubleClick(double_click_coords_1)

# Wait for 4 seconds and single-click
time.sleep(6)
pyautogui.click(single_click_coords_2)

# Automate pressing the down button 74 times with a 0.3-second interval
press_down_button(74)

# Move to the specified coordinates and click once
pyautogui.moveTo(type_coords)
pyautogui.click()

# Type "SP2024"
pyautogui.write("SP2024")

# Move to the coordinates and click once
pyautogui.moveTo(click_coords)
pyautogui.click()
# ... Previous code ...
time.sleep(6)
# Set the coordinates
double_click_coords = (333, 276)

# Double-click at the specified coordinates
pyautogui.doubleClick(double_click_coords)
# Wait for 9 seconds
time.sleep(9)

# Move to the coordinates and single-click
pyautogui.moveTo((520, 490))
pyautogui.click()

# Wait for 2 seconds
time.sleep(4)

# Move to the coordinates and click on the "Yes" icon if it pops up
pyautogui.moveTo((825, 377))
pyautogui.click()

# Wait for 30 seconds
time.sleep(30)

import pyautogui
import time
time.sleep(4)
# Move to the coordinates and right-click
pyautogui.moveTo((12, 233))
pyautogui.click()
pyautogui.rightClick()



# Function to automate pressing the down button
def press_down_button(num_clicks, interval=0.3):
    for _ in range(num_clicks):
        pyautogui.press('down')
        time.sleep(interval)

# Initial 4-second wait time
time.sleep(4)

import pyautogui
import time

# Replace these coordinates with your desired values
hide_button_coords = (59, 547)

# Simulate pressing the down button 11 times
for _ in range(11):
    pyautogui.press('down')
    time.sleep(0.5)  # Adjust the sleep duration if needed

# Press Enter
pyautogui.press('enter')

# Click the A column of the spreadsheet at coordinates (81, 214)
pyautogui.click(81, 214)

# Click the warning button at coordinates (143, 234)
pyautogui.click(143, 234)

# Click the "Convert to Number" action at coordinates (142, 287)
pyautogui.click(142, 287)

# Go to the coordinates (1357, 672)
pyautogui.moveTo(1357, 672)

# Hold down the left click button for 22 seconds
pyautogui.mouseDown()

# Wait for 35 seconds
time.sleep(35)

# Release the left click button
pyautogui.mouseUp()
# ... Previous code ...

# Additional actions
# Wait for 3 seconds
time.sleep(3)

# Click on the Chrome extension at coordinates (176, 746)
pyautogui.click(176, 746, duration=1)

# Wait for 2 seconds
time.sleep(2)

# Click on the tab to open at coordinates (503, 638)
pyautogui.click(503, 638, duration=1)

# Wait for 2 seconds
time.sleep(2)

# Click the "Non Reg" tab in Chrome at coordinates (376, 14)
pyautogui.click(376, 14, duration=1)

# ... Continue with the rest of your code ...
import pyautogui
import time

# Pause for 4 seconds
time.sleep(4)

# Click and hold at coordinates (159, 263)
pyautogui.mouseDown(159, 263)

# Wait for a moment (adjust as needed)
time.sleep(1)

# Move to coordinates (451, 259) while holding the left click button
pyautogui.moveTo(451, 259)

# Release the left click button
pyautogui.mouseUp()

# Hold down the 'Ctrl' key and press 'C'
pyautogui.keyDown('ctrl')
pyautogui.press('c')
pyautogui.keyUp('ctrl')

import pyautogui
import time

# Pause for 4 seconds
time.sleep(4)

# Click the Excel file at coordinates (565, 750)
pyautogui.click(565, 750, duration=2)

# Pause for 2 seconds
time.sleep(2)

# Click the cell at coordinates (61, 658)
pyautogui.click(61, 658, duration=1)

# Hold down the 'Ctrl' key and press 'V' to paste
pyautogui.keyDown('ctrl')
pyautogui.press('v')
pyautogui.keyUp('ctrl')
import pyautogui
import time

# Pause for 4 seconds
time.sleep(4)

import pyautogui
import time

# Pause for 4 seconds
time.sleep(4)

# Click the whole sheet at coordinates (16,212)
pyautogui.click(16, 212, duration=2)

# Right-click at coordinates (267, 298)
pyautogui.rightClick(267, 298, duration=1)

# Pause for 1 second
time.sleep(1)

# Simulate clicking the down button 12 times
for _ in range(12):
    pyautogui.press('down')
    time.sleep(0.5)  # Adjust the sleep duration if needed

# Press "Enter" on the "Unhide" option
pyautogui.press('enter')
import pyautogui
import time

# Pause for 4 seconds
time.sleep(4)

# Click the A column at coordinates (78, 215)
pyautogui.click(78, 215, duration=1)

# Click the "Data" tab at coordinates (392, 44)
pyautogui.click(392, 44, duration=1)

# Click the filter icon at coordinates (830, 88)
pyautogui.click(830, 88, duration=1)
import pyautogui
import time

# Pause for 4 seconds
time.sleep(4)

# Click and hold at coordinates (1355, 215) for 30 seconds
pyautogui.mouseDown(1355, 215)

# Wait for 37 seconds
time.sleep(37)

# Release the left click button
pyautogui.mouseUp()

import pyautogui
import time

# Pause for 4 seconds
time.sleep(4)

# Click the filter button at coordinates (125, 234)
pyautogui.click(125, 234, duration=1)

# Pause for 1 second
time.sleep(1)

# Press the down button once
pyautogui.press('down')

# Pause for 1 second
time.sleep(1)

# Press "Enter"
pyautogui.press('enter')

# Pause for 1 second
time.sleep(1)

# Press "Enter" again
pyautogui.press('enter')
import pyautogui
import time



# Click the home icon at coordinates (79, 50)
pyautogui.click(79, 50, duration=1)

# Click the conditional formatting tab at coordinates (813, 119)
pyautogui.click(813, 119, duration=1)

# Press the down button once
pyautogui.press('down')

# Press the right arrow button once
pyautogui.press('right')

# Press the down button 6 times
for _ in range(6):
    pyautogui.press('down')
    time.sleep(0.5)  # Adjust the sleep duration if needed

# Press "Enter"
pyautogui.press('enter')

# Pause for 1 second
time.sleep(1)

# Press "Enter" again
pyautogui.press('enter')

import pyautogui
import time
time.sleep(3)
# Replace these coordinates with your desired values
target_coords = (126, 234)

# Single left click at the specified coordinates
pyautogui.click(target_coords)

# Simulate pressing the down button three times
for _ in range(3):
    pyautogui.press('down')
    time.sleep(0.5)  # Adjust the sleep duration if needed

# Simulate pressing the right button once
pyautogui.press('right')
time.sleep(0.5)  # Adjust the sleep duration if needed


# Press Enter
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
import pyautogui
import time
time.sleep(3)
# Replace these coordinates with your desired values
target_coords = (126, 234)

# Single left click at the specified coordinates
pyautogui.click(target_coords)

# Simulate pressing the down button six times
for _ in range(6):
    pyautogui.press('down')
    time.sleep(0.5)  # Adjust the sleep duration if needed

    # Simulate pressing the right button once
pyautogui.press('right')
time.sleep(0.5)  # Adjust the sleep duration if needed


# Press Enter
pyautogui.press('enter')
