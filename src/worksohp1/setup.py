from setuptools import find_packages, setup

package_name = 'worksohp1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='anwar',
    maintainer_email='anwar@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "ultrasonic_subscriber = worksohp1.ultrasonic_subscriber:main",
            "ultrasonic_publisher = worksohp1.ultrasonic_publisher:main",
        ],
    },
)
