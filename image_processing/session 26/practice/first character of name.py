import cv2
import numpy as np
char1 = ["A", "E", "F", "H", "I", "K", "L", "M", "N", "T", "V", "W", "X", "Y", "Z"]
char2 = ["B", "C", "D", "G", "J", "O", "P", "Q", "R", "S", "U"]
tryagain = True
width=hight=400
color = (0, 0, 0)
while tryagain:
    char = input("enter first character of youre name:\n")
    char = char.upper()
    img = np.ones((width, hight), dtype = np.uint8)
    img [:,:] = 255
    if char in char1:
        if char == "A":
            cv2.line(img, (50, 350), (200, 50), color, 30) 
            cv2.line(img, (200, 50), (350, 350), color, 30) 
            cv2.line(img, (150, 200), (250, 200), color, 30) 

        elif char == "E":
            cv2.line(img, (125, 50), (275, 50), color, 30) 
            cv2.line(img, (125, 200), (275, 200), color, 30) 
            cv2.line(img, (125, 350), (275, 350), color, 30) 
            cv2.line(img, (125, 50), (125, 350), color, 30) 

        elif char == "F":
            cv2.line(img, (50, 50), (50, 350), color, 30) 
            cv2.line(img, (50, 50), (250, 50), color, 30) 
            cv2.line(img, (50, 200), (200, 200), color, 30)

        elif char == "H":
            cv2.line(img, (50, 50), (50, 350), color, 30) 
            cv2.line(img, (350, 50), (350, 350), color, 30) 
            cv2.line(img, (50, 200), (350, 200), color, 30) 

        elif char == "I":
            cv2.line(img, (50, 50), (350, 50), color, 30) 
            cv2.line(img, (200, 50), (200, 350), color, 30) 
            cv2.line(img, (50, 350), (350, 350), color, 30) 

        elif char == "K":
            cv2.line(img, (50, 50), (50, 350), color, 30) 
            cv2.line(img, (250, 50), (50, 275), color, 30) 
            cv2.line(img, (120, 200), (250, 350), color, 30) 

        elif char == "L":
            cv2.line(img, (50, 50), (50, 350), color, 30) 
            cv2.line(img, (50, 350), (250, 350), color, 30)

        elif char == "M":
            cv2.line(img, (50, 350), (125, 50), color, 30) 
            cv2.line(img, (125, 50), (200, 350), color, 30) 
            cv2.line(img, (200, 350), (275, 50), color, 30) 
            cv2.line(img, (275, 50), (350, 350), color, 30)

        elif char == "N":
            cv2.line(img, (50, 350), (50, 50), color, 30) 
            cv2.line(img, (50, 50), (350, 350), color, 30) 
            cv2.line(img, (350, 350), (350, 50), color, 30) 

        elif char == "T":
            cv2.line(img, (50, 50), (350, 50), color, 30)
            cv2.line(img, (200, 50), (200, 350), color, 30)

        elif char == "V":
            cv2.line(img, (100, 50), (200, 350), color, 30) 
            cv2.line(img, (200, 350), (300, 50), color, 30) 

        elif char == "W":
            cv2.line(img, (50, 50), (125, 350), color, 30) 
            cv2.line(img, (125, 350), (200, 50), color, 30) 
            cv2.line(img, (200, 50), (275, 350), color, 30) 
            cv2.line(img, (275, 350), (350, 50), color, 30) 

        elif char == "X":
            cv2.line(img, (50, 50), (350, 350), color, 30) 
            cv2.line(img, (350, 50), (50, 350), color, 30) 

        elif char == "Y":
            cv2.line(img, (100, 50), (200, 150), color, 30) 
            cv2.line(img, (200, 150), (300, 50), color, 30) 
            cv2.line(img, (200, 150), (200, 350), color, 30) 
            # or
            # img[180:200, 120:160] = 0
            # img[200:220, 140:180] = 0
            # img[220:240, 160:200]= 0
            # img[240:260, 180:260]= 0
            # img[220:240, 240:280]= 0
            # img[200:220, 260:300]= 0
            # img[180:200, 280:320]= 0
            # img[260:340, 200:240]= 0

        elif char == "Z":
            cv2.line(img, (50, 50), (350, 50), color, 30) 
            cv2.line(img, (350, 50), (50, 350), color, 30) 
            cv2.line(img, (50, 350), (350, 350), color, 30) 

    elif char in char2:
        if char == "B":
            cv2.line(img, (50, 330), (50, 30), color, 30) 
            cv2.ellipse(img, (80, 90), (60, 60), 60, 200, 400, (0,0,0), thickness=30)
            cv2.ellipse(img, (90, 240), (80, 80), 60, 200, 400, (0,0,0), thickness=30)
        
        elif char == "C":
            cv2.ellipse(img, (200, 200), (100, 100), 210, 200, 450, (0,0,0), thickness=30)

        elif char == "D":
            cv2.line(img, (50, 350), (50, 50), color, 30) 
            cv2.ellipse(img, (90, 200), (150, 150), 60, 200, 400, (0,0,0), thickness=30)
        
        elif char == "G":
            cv2.line(img, (290, 230), (200, 230), color, 30) 
            cv2.ellipse(img, (200, 200), (100, 100), 300, 90, 360, (0,0,0), thickness=30)
        
        elif char == "J":
            cv2.line(img, (320, 100), (180, 100), color, 30)
            cv2.line(img, (270, 100), (270, 290), color, 30) 
            cv2.ellipse(img, (200, 300), (70, 70), 180, 180, 360, (0,0,0), thickness=30)
       
        elif char == "O":
            cv2.circle(img=img, center = (200,200), radius =100, color =color, thickness=30)

        elif char == "P":
            cv2.line(img, (50, 350), (50, 50), color, 30) 
            cv2.ellipse(img, (90, 110), (70, 70), 60, 200, 400, (0,0,0), thickness=30)
        
        elif char == "Q":
            cv2.circle(img=img, center = (200,200), radius =100, color =(0,0,0), thickness=30)
            cv2.line(img, (220, 250), (350, 350), color, 30) 

        elif char == "R":
            cv2.line(img, (50, 350), (50, 50), color, 30) 
            cv2.ellipse(img, (90, 120), (80, 80), 60, 200, 400, (0,0,0), thickness=30)
            cv2.line(img, (50, 200), (200, 350), color, 30) 
        
        elif char == "S":
            cv2.ellipse(img, (230, 165), (70, 70), -50, 140, 360, (0,0,0), thickness=30)
            cv2.ellipse(img, (180, 290), (70, 70), 140, 140, 360, (0,0,0), thickness=30)
            
        elif char == "U":
            cv2.line(img, (130, 100), (130, 290), color, 30)
            cv2.line(img, (270, 100), (270, 290), color, 30) 
            cv2.ellipse(img, (200, 300), (70, 70), 180, 180, 360, (0,0,0), thickness=30)
    else:
        print(f"{char} is not find")

    cv2.imshow(f'{char}', img)
    cv2.waitKey()
    ask_for_tryagain = input("do you want to try again?(y or n):\n")
    if ask_for_tryagain == "y":
        tryagain = True
    else:
        tryagain = False