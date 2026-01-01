import cv2
import numpy as np
import mss
import mediapipe as mp
import pyautogui
from pathlib import Path
from utils.takeScreenshots_utils import take_fullscreen_screenshot
from utils.cloudinary_utils import upload_image
from utils.get_answer import get_answer_to_question
from utils.paste_output import move_coursor
import langchain
from pydantic import Field,BaseModel
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
import time
import asyncio

cv2.namedWindow("Screen", cv2.WINDOW_NORMAL)  # Create a window
cv2.resizeWindow("Screen", 1, 1) 

with mss.mss() as sct:
    screen = sct.monitors[1]
    while True:
        screenshot = sct.grab(screen)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)      
        cv2.imshow("Screen", img)
        key=cv2.waitKey(1) & 0xFF

        if key == ord('q'):  # Press 'q' to quit
            break
        elif key == ord('s'):  # Press 's' to take a screenshot
            take_fullscreen_screenshot()  # Call your function
            dir_path=Path.cwd()
            screenshots_dir = dir_path / "screenshots"
            screenshot_path = screenshots_dir / "full_screen.png"
            image_url= (upload_image(screenshot_path))
            time.sleep(5) 
            try:
                get_answer=(get_answer_to_question(image_url['secure_url']))
                print(get_answer)
                move_coursor(get_answer)
            except Exception as e:
                print("Error occurred:", e)
      


cv2.destroyAllWindows()
