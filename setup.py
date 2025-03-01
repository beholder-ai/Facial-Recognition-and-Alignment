from setuptools import find_packages, setup

setup(
    name='facenet_sandberg',
    version='0.0.9',
    description="Face recognition using TensorFlow",
    long_description="Face recognition with Google's FaceNet deep neural network & TensorFlow. Mirror of https://github.com/davidsandberg/facenet.",
    url='https://github.com/armanrahman22/facenet',
    packages=find_packages(),
    maintainer='Arman Rahman',
    maintainer_email='armanrahman22@gmail.com',
    include_package_data=True,
    license='MIT',
    install_requires=[
        'tensorflow',
        'scipy',
        'scikit-learn',
        'opencv-python',
        'h5py',
        'Pillow',
        'progressbar2',
        'mtcnn',
        'tensorlayer'
    ])
