#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class UltrasonicSubscriber(Node):

    def __init__(self):
        super().__init__("ultrasonic_subscriber") 
        self.create_subscription(
            Float32,
            'ultrasonic_sensor_data',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        distance = msg.data
        self.get_logger().info(f'Received simulated distance: {distance} cm')

        if distance < 10.0:
            self.get_logger().info('Object is too close! Taking action.')
        elif distance < 25.0:
            self.get_logger().info('Object is close, be cautious.')
        else:
            self.get_logger().info('Safe distance.')

def main(args=None):
    rclpy.init(args=args)
    ultrasonic_subscriber = UltrasonicSubscriber()
    rclpy.spin(ultrasonic_subscriber)
    ultrasonic_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
