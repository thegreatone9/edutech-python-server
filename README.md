# edutech-python-server
Python based features for edutechbd

First build a caffe docker image (CPU)

```
docker build -t caffe:cpu https://raw.githubusercontent.com/BVLC/caffe/master/docker/cpu/Dockerfile
```

Check the caffe installation

```
docker run caffe:cpu caffe --version
caffe version 1.0.0-rc3
```

Run the docker image with a volume mapped to your open_nsfw repository. Your test_image.jpg should be located in this same directory.

```
cd open_nsfw
docker run --volume=$(pwd):/workspace caffe:cpu \
python ./classify_nsfw.py \
--model_def nsfw_model/deploy.prototxt \
--pretrained_model nsfw_model/resnet_50_1by2_nsfw.caffemodel \
test_image.jpg
```

We will get the NSFW score returned:

```
NSFW score:   0.14057905972
```

