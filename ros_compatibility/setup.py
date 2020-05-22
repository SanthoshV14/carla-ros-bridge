import os

ROS_VERSION = int(os.environ['ROS_VERSION'])

if ROS_VERSION == 1:
    from distutils.core import setup
    from catkin_pkg.python_setup import generate_distutils_setup

    d = generate_distutils_setup(
        packages=['ros_compatibility'],
        package_dir={'': 'src'}
    )

    setup(**d)

elif ROS_VERSION == 2:
    from setuptools import setup

    package_name = 'ros_compatibility'

    setup(
        name=package_name,
        version='0.0.0',
        packages=['src/' + package_name],
        py_modules=[
            'src.ros_compatibility.ros_compatible_node'],
            data_files=[
            ('share/ament_index/resource_index/packages',
             ['resource/' + package_name]),
            ('share/' + package_name, ['package.xml']),
        ],
        install_requires=['setuptools'],
        zip_safe=True,
        maintainer='CARLA Simulator Team',
        maintainer_email='carla.simulator@gmail.com',
        description='The ros_compatibility package',
        license='MIT',
        tests_require=['pytest'],
        entry_points={
            'console_scripts': [
                'ros_compatible_node = src.ros_compatibility.ros_compatible_node:main'
            ],
        },
    )
