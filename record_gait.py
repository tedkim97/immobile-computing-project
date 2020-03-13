import numpy as np 
import cv2

def record_video(vid_dir, fname):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('.avi'.format(vid_dir + fname), fourcc, 20.0, (640, 480))

    while(True):
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return True

if __name__ == "__main__":
    record_video("", "test")