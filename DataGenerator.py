import win32gui
import numpy as np
import win32ui
import win32con
import time
import mss
from PIL import Image
import cv2
from Dinput import PressKey,ReleaseKey,ChangeView
from threading import Thread

# define hight, width, and program started Time
last_time = time.time()
w = 800
h = 600
i = 0
delay = 0.090000511111
key = 1

def FrontFrameCapture():
    # --------------------------------------- Front Frame ----------------------------------------------------------
    # get The Screen window
    Fhwnd = win32gui.GetDesktopWindow()
    FwDC = win32gui.GetWindowDC(Fhwnd)

    # create DC object for
    FdcObj = win32ui.CreateDCFromHandle(FwDC)
    FcDC = FdcObj.CreateCompatibleDC()

    # bitmapping The captured Frame
    FdataBitMap = win32ui.CreateBitmap()
    FdataBitMap.CreateCompatibleBitmap(FdcObj, w, h)

    # Cropping Window
    FcDC.SelectObject(FdataBitMap)
    FcDC.BitBlt((0, 0), (w, h), FdcObj, (0, 30), win32con.SRCCOPY)

    # dataBitMap.SaveBitmapFile(cDC, 'Test.jpg')
    bmpinfo = FdataBitMap.GetInfo()
    bmpstr = FdataBitMap.GetBitmapBits(True)
    im1 = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)
    Front = np.array(im1)
    Front = cv2.cvtColor(Front, cv2.COLOR_BGR2RGB)
    PressKey(ChangeView)
    time.sleep(delay)
    ReleaseKey(ChangeView)
    # time.sleep(0.0000000000000001)
    # Cleaning Some memory (Avoid Exception)
    FdcObj.DeleteDC()
    FcDC.DeleteDC()
    win32gui.ReleaseDC(Fhwnd, FwDC)
    win32gui.DeleteObject(FdataBitMap.GetHandle())
    return Front
    # --------------------------------------- End -----------------------------------------------------------------

def LeftFrameCapture():
    # --------------------------------------- Left Frame ----------------------------------------------------------
    # get The Screen window
    hwnd = win32gui.GetDesktopWindow()
    wDC = win32gui.GetWindowDC(hwnd)

    # create DC object for
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()

    # bitmapping The captured Frame
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)

    # Cropping Window
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (0, 30), win32con.SRCCOPY)

    # dataBitMap.SaveBitmapFile(cDC, 'Test.jpg')
    bmpinfo = dataBitMap.GetInfo()
    bmpstr = dataBitMap.GetBitmapBits(True)
    im2 = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)
    Left = np.array(im2)
    Left = cv2.cvtColor(Left, cv2.COLOR_BGR2RGB)
    PressKey(ChangeView)
    time.sleep(delay)
    ReleaseKey(ChangeView)
    # time.sleep(0.0000000000000001)

    # Cleaning Some memory (Avoid Exception)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    return Left
    # --------------------------------------- End ----------------------------------------------------------

def BackFrameCapture():
    # ---------------------------------------- Back Frame ---------------------------------------------------
    # get The Screen window
    hwnd = win32gui.GetDesktopWindow()
    wDC = win32gui.GetWindowDC(hwnd)

    # create DC object for
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()

    # bitmapping The captured Frame
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)

    # Cropping Window
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (0, 30), win32con.SRCCOPY)

    # dataBitMap.SaveBitmapFile(cDC, 'Test.jpg')
    bmpinfo = dataBitMap.GetInfo()
    bmpstr = dataBitMap.GetBitmapBits(True)
    im3 = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    Back = np.array(im3)
    Back = cv2.cvtColor(Back, cv2.COLOR_BGR2RGB)
    PressKey(ChangeView)
    time.sleep(delay)
    ReleaseKey(ChangeView)
    # time.sleep(0.0000000000000001)
    # Cleaning Some memory (Avoid Exception)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    return Back
    # --------------------------------------- End ----------------------------------------------------------

def RightFrameCapture():
    # ----------------------------------------- Right Frame -------------------------------------------------
    # get The Screen window
    hwnd = win32gui.GetDesktopWindow()
    wDC = win32gui.GetWindowDC(hwnd)

    # create DC object for
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()

    # bitmapping The captured Frame
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)

    # Cropping Window
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (0, 30), win32con.SRCCOPY)

    # dataBitMap.SaveBitmapFile(cDC, 'Test.jpg')
    bmpinfo = dataBitMap.GetInfo()
    bmpstr = dataBitMap.GetBitmapBits(True)
    im4 = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    Right = np.array(im4)
    Right = cv2.cvtColor(Right, cv2.COLOR_BGR2RGB)
    PressKey(ChangeView)
    time.sleep(delay)
    ReleaseKey(ChangeView)
    # time.sleep(0.0000000000000001)
    # Cleaning Some memory (Avoid Exception)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    return Right
    # --------------------------------------- End ----------------------------------------------------------

for i in list(range(10))[::-1]:
    print(i + 1)
    time.sleep(1)

cv2.namedWindow('Left')
cv2.moveWindow('Left', 1600, 400)

cv2.namedWindow('Front')
cv2.moveWindow('Front', 800, 0)

cv2.namedWindow('Back')
cv2.moveWindow('Back', 800, 600)

cv2.namedWindow('Right')
cv2.moveWindow('Right', 0, 600)

i = 13
if __name__ == '__main__':
    while True:

        i = i + 1

        FrontFrame = FrontFrameCapture()
        cv2.imwrite(('Frames\\Front\\data_'+ str(i) +'.jpg'), FrontFrame)
        cv2.imshow('Front', FrontFrame)
        cv2.waitKey(1)

        LeftFrame = LeftFrameCapture()
        cv2.imwrite(('Frames\\Left\\data_'+ str(i) +'.jpg'), LeftFrame)
        cv2.imshow('Left', LeftFrame)
        cv2.waitKey(1)

        BackFrame = BackFrameCapture()
        cv2.imwrite('Frames\\Back\\data_'+ str(i) +'.jpg', BackFrame)
        cv2.imshow('Back', BackFrame)
        cv2.waitKey(1)

        RightFrame = RightFrameCapture()
        cv2.imwrite('Frames\\Right\\data_'+ str(i) +'.jpg', RightFrame)
        cv2.imshow('Right', RightFrame)
        cv2.waitKey(1)

	
        if 0xFF == ord('q'):
            cv2.destroyAllWindows()
            ReleaseKey(ChangeView)
            break

        print('Loop took {} Seconds'.format(time.time() - last_time))
        last_time = time.time()