#!/usr/bin/env python3

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

# Initialize the necessary variables and objects
bridge = CvBridge()  # To convert ROS Image messages to OpenCV images
output_video_file = "logi6.mp4"
topic_name = "/logi6/image_raw"
frame_rate = 10  # Specify the frame rate of the video

# Define a callback function to process the image_raw messages
def image_callback(msg):
    cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")  # Convert ROS Image to OpenCV image
    video_writer.write(cv_image)  # Write the frame to the video file

# Initialize the ROS node and create a video writer object
rospy.init_node('rosbag_to_video')
video_writer = cv2.VideoWriter(output_video_file, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (1920,1080))

# Subscribe to the image_raw topic and start processing the ROS bag
rospy.Subscriber(topic_name, Image, image_callback)
rospy.spin()  # Keep the script running until interrupted

# Release the video writer and print a message indicating the conversion is complete
video_writer.release()
print("Video conversion complete!")
import rospy

