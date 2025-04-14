
# # import subprocess

# # try:
# #     subprocess.Popen(r'C:\Users\balaj\Downloads\Paint.exe')
# #     print("Paint launched successfully.")
# # except Exception as e:
# #     print(f"Error opening Paint: {e}")


# from pywinauto import Application
# import time

# try:
#     # Start Paint with full path
#     paint_app = Application(backend="win32").start(r'C:\Program Files\WindowsApps\Microsoft.Paint_11.2502.161.0_x64__8wekyb3d8bbwe\PaintApp\mspaint.exe')
    
#     # Wait for the window to appear (this may help avoid the error)
#     time.sleep(2)  # Allow some time for Paint to open

#     # Now you can interact with the application
#     paint_app = Application(backend="win32").connect(path=r'C:\Program Files\WindowsApps\Microsoft.Paint_11.2502.161.0_x64__8wekyb3d8bbwe\PaintApp\mspaint.exe')
#     print("Paint launched successfully.")
    
# except Exception as e:
#     print(f"Error opening Paint: {e}")


import time
paint_window = paint_app.window(class_name='MSPaintApp')
canvas = paint_window.child_window(class_name='MSPaintView')
# Start drawing: press mouse button at the starting coordinates
canvas.press_mouse_input(coords=(x1, y1))

# Wait for a short time to simulate human delay if needed
time.sleep(0.1)

# Move the mouse to the endpoint of the rectangle
canvas.move_mouse_input(coords=(x2, y2))

# Release the mouse button to finish the drawing action
canvas.release_mouse_input(coords=(x2, y2))