import cv2
import time
import sys
import argparse
parser = argparse.ArgumentParser(description='Process some ')
parent_parser.add_argument('--source', type=str)
parent_parser.add_argument('--dest', type=str)
parent_parser.add_argument('--sec', type=str)
exit_=0
count=0
out=0
cap=cv2.VideoCapture(parse['--source'])
no_of_frame=0
_,frame=cap.read()
height,width,__=frame.shape
def video_creator(count):
    global cap,out
    fp=(no_of_frame*count)
    fps_= fp/(video_time*4.55)
    print(fps_,fp)
    out=cv2.VideoWriter(parser['--dest'],cv2.VideoWriter_fourcc(*'DIVX'),fps_,(width,height))
    #print(out)
    cap=cv2.VideoCapture(parse['--source'])
    retrieve(t=t,pcap=1)
    out.release()
    cap.release()
video_time=parser['--sec']

def retrieve(t,pcap):

    global exit_,count,out,cap
    while cap.isOpened()==True:
        _,frame=cap.read()
        if not _ :
            print(video_end-actual_time)
            #act=video_end-actual_time
            cap.release()
            break
        video_start=time.time()
        video_end=time.time()
        count=0
        while video_end-video_start<=t-0.005:
            count+=1
            video_end=time.time()
            if pcap==1:
                #print("highlight")
                out.write(frame)
            #print(video_start-video_end)
            #cv2.imshow('frame',frame)
            key=cv2.waitKey(1)
            if key==27 or key==ord('q'):
                exit_=1
                cv2.destroyAllWindows()
                break
        if pcap!=1 or exit_==1:
            break

def fps(t):

    global count,cap
    cap=cv2.VideoCapture(parse['--source'])
    retrieve(t=t,pcap=2)
    video_creator(count)

while cap.isOpened()==True:
    _,frame=cap.read()
    no_of_frame+=1
    if not _:
        t=video_time/no_of_frame
        print(t)
        cap.release()
        actual_time=time.time()
        fps(t)
