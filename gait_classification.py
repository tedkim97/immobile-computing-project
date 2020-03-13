import numpy as np
import cv2 

def record_video(vid_dir, fname):
    cap = cv2.VideoCapture(1)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('{}.avi'.format(vid_dir + fname), fourcc, 20.0, (640,480))
    
    global RECORD
    RECORD = True
    while(RECORD):
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow('gait_capture_playback', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return True

def read_from_file(vid_dir, fname):
    cap = cv2.VideoCapture(vid_dir + fname)
    if(not cap.isOpened()):
        print("Failed to open the webcam")
        return False

    while(cap.isOpened()):
        ret, frame = cap.read()
        if (ret == True):
            cv2.imshow('{} recording'.format(fname), frame)

            if(cv2.waitKey(25) & 0xFF == ord('q')):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    return True

def sample_frames(vid_dir, fname, proportion):
    cap = cv2.VideoCapture(vid_dir + fname)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    sample_n = int(frameCount * proportion)
    
    print('dim ({},{})'.format(frameHeight, frameWidth),
            'Frame Count:',frameCount, 
            'sample_count:', sample_n, '\n')

    sampled = np.empty((sample_n, frameHeight, frameWidth, 3), np.dtype('uint8'))

    fc = 0
    ret = True
    while (fc < frameCount and ret):
        ret, frame = cap.read()
        if(fc % sample_n == 0):
            print(fc)
            sampled[int(fc/sample_n)] = frame
        fc += 1

    cap.release()
    return sampled


# frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

# fc = 0
# ret = True

# while (fc < frameCount  and ret):
#     ret, buf[fc] = cap.read()
#     fc += 1

# cap.release()

# cv2.namedWindow('frame 10')
# cv2.imshow('frame 10', buf[9])

if __name__ == "__main__":
    record_video('video_data/', 'test')
    # read_from_file('video/', 'test1.avi')
    # sm = sample_frames('video/', 'test1.avi', 0.1)
    # print(sm.shape)
    # for ind in range(sm.shape[0]):
    #     cv2.imshow('test', sm[ind])
    #     cv2.waitKey(0)
        
    # cap.release()
    # cv2.destroyAllWindows()