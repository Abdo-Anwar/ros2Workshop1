#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class UltrasonicPublisher(Node):

    def __init__(self):
        super().__init__("ultrasonic_publisher")
        self.publisher_ = self.create_publisher(Float32, 'ultrasonic_sensor_data', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  

    def timer_callback(self):
        distance = round(random.uniform(5.0, 30.0), 2) 
        msg = Float32()
        msg.data = distance
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published simulated distance: {distance:.2f} cm')

def main(args=None):
    rclpy.init(args=args)
    ultrasonic_publisher = UltrasonicPublisher()
    rclpy.spin(ultrasonic_publisher)
    ultrasonic_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
