FROM arm64v8/amazonlinux:latest

MAINTAINER Yash Indane

EXPOSE 85

RUN yum install python3 -y && \
    yum install gcc-c++ -y && \
    yum install python3-devel -y && \
    pip3 install flask==2.0.1 && \
    pip3 install Pillow==8.2.0 && \
    pip3 install numpy==1.20.3 && \
    pip3 install joblib==1.0.1 && \
    pip3 install scikit-learn && \
    pip3 install scikit-build && \
    pip3 install opencv-python  && \
    yum install opencv opencv-devel opencv-python -y && \
    pip3 install kociemba && \
    mkdir /webcube

COPY . /webcube

WORKDIR /webcube

ENTRYPOINT python3 app.py
