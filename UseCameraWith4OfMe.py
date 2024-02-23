import cv2
import numpy as np




# class ig sameey videocaputre.. : 0 waxay u taagantahay camera computerka..
cap = cv2.VideoCapture(0)

while True:
    # 2 var soo celinee: 1: re: return true if the frame works, 2: frame: the video(the image)
    ret,frame = cap.read()

# height iyo widthka videoga
    width = int(cap.get(3))
    height = int(cap.get(4))


    image = np.zeros(frame.shape, np.uint8)

# 4 qeebood ukala qaybi screenka..
    smaller_frame = cv2.resize(frame,(0,0), fx = 0.5, fy=0.5)

# top left
    image[:height//2, :width//2] = smaller_frame
# bottom left..
    image[height//2:, :width//2] = smaller_frame
# top right..
    image[:height//2, width//2:] = smaller_frame
# bottom right
    image[height//2:, width//2:] = smaller_frame

# soo bandhig videoga........
    cv2.imshow("Frame", image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()