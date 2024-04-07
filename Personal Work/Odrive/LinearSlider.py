import odrive, pyautogui, EzValueProcess

myDrive = odrive.find_any()

while True:
    mouseX, mouseY = pyautogui.position()
    constrainedPos = EzValueProcess.warp(mouseY, 0, 1111, 0, -3)
    myDrive.axis0.controller.input_pos = constrainedPos

