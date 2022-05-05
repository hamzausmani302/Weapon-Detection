import cv2
import time;
class DataSetCreator:
    @staticmethod
    def ConvVideoToFrame(path):
        i = 0;
        video = cv2.VideoCapture(path);
        if(video):
            while(True):
                ret , frame = video.read()
                cv2.imshow("video feed" ,frame);
                # print(frame.shape);
                if(i%5 == 0):
                    pass
                    # cv2.imwrite(f'Dataset/Images/Pistol/pistol-{i}.png' , frame);  
                i+=1;
                if(cv2.waitKey(1)  == ord('q')):
                    break;
        video.release()
        cv2.destroyAllWindows();            

if __name__ == "main":
    pass