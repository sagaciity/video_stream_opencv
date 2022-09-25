#!/usr/bin/env python

import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import datetime
import os
import csv

class image_converter:

  def __init__(self):

    self.bridge = CvBridge()

    self.index1 = 0
    self.index2 = 0

  def callback_img1(self,data):
    try:
      cv_image1 = self.bridge.imgmsg_to_cv2(data, "bgr8")
      self.index1 += 1
    except CvBridgeError as e:
      print(e)

    localtime1 = datetime.datetime.now()
    (rows,cols,channels) = cv_image1.shape
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image1, (50,50), 10, 255)
    

    #print(os.path.dirname(os.path.realpath(__file__)))
    #cv2.imshow("Image window 113", cv_image)

    frame_name = "cam113_frame_" + str(self.index1)+ "_" + str(localtime1) + ".png"
    csv_entry = [str(self.index1) , frame_name, str(localtime1)]

    try:
      cv2.imwrite(os.path.dirname(os.path.realpath(__file__)) + "/cam113_frames/" + frame_name, cv_image1)
      with open(os.path.dirname(os.path.realpath(__file__))+'/cam113_saved_frame_record.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(csv_entry)
      cv2.waitKey(3)
    except CvBridgeError as e:
      print(e)


  def callback_img2(self,data):
    try:
      cv_image2 = self.bridge.imgmsg_to_cv2(data, "bgr8")
      self.index2 += 1
    except CvBridgeError as e:
      print(e)

    localtime2 = datetime.datetime.now()
    (rows,cols,channels) = cv_image2.shape
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image2, (50,50), 10, 255)

    #cv2.imshow("Image window 114", cv_image)

    frame_name = "cam114_frame_" + str(self.index2)+ "_" + str(localtime2) + ".png"
    csv_entry = [str(self.index2) , frame_name, str(localtime2)]

    try:
      cv2.imwrite(os.path.dirname(os.path.realpath(__file__)) + "/cam114_frames/" + frame_name, cv_image2)
      with open(os.path.dirname(os.path.realpath(__file__))+'/cam114_saved_frame_record.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(csv_entry)
      cv2.waitKey(3)
    except CvBridgeError as e:
      print(e)


def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)

  rospy.Subscriber("/rtsp2/image_raw", Image, ic.callback_img1)
  rospy.Subscriber("/rtsp3/image_raw", Image, ic.callback_img2)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)




# import roslib
# import rospy
# from sensor_msgs.msg import Image
# import cv2
# import numpy as np
# from cv_bridge import CvBridge, CvBridgeError



# class DualCam:
#     def __init__(self):
#         self.cam113_currentFrame = None
#         self.cam114_currentFrame = None
#         self.a=0
#         self.bridge = CvBridge()

#     def cam113_callback(self, msg):
#         # "Store" message received.
#         self.cam113_currentFrame = msg

#         try:
#           cv_image2 = self.bridge.imgmsg_to_cv2(self.cam113_currentFrame, "bgr8")
#         except CvBridgeError as e:
#           print(e)

#         # Compute stuff.
#         self.do_stuff(self,cv_image2)

#     def cam114_callback(self, msg):
#         # "Store" the message received.
#         self.cam114_currentFrame = msg
#         try:
#           cv_image3 = self.bridge.imgmsg_to_cv2(self.cam114_currentFrame, "bgr8")
#         except CvBridgeError as e:
#           print(e)

#         # Compute stuff.
#         self.do_stuff(self,cv_image3)

#     def do_stuff(self, cv_img113, cv_img114):
#         if self.cam113_currentFrame is not None and self.cam114_currentFrame is not None and cv_img114 is not None and cv_img113 is not None :
#             if (self.a==0):
#               cv2.imshow("Image window", cv_img113)
#               print(cv_img113)
#             self.a=1
            
        
#         # cv2.imshow("Image window", self.cam113_currentFrame)

#         # (rows,cols,channels) = cv_img113.shape
#         # if cols > 60 and rows > 60 :
#         #    cv2.circle(cv_image, (50,50), 10, 255)
#         # cv2.imshow("Image window", cv_image)
#         # cv2.waitKey(3)



# if __name__ == '__main__':
#     rospy.init_node('record_frames')

#     camObj = DualCam()

#     rospy.Subscriber('/rtsp2/image_raw', Image, camObj.cam113_callback)
#     rospy.Subscriber('/rtsp3/image_raw', Image, camObj.cam114_callback)

#     #rospy.loginfo("a= "+str(a))

#     rospy.spin()
