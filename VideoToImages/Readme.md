# Video to Images
Pyhton code used for extracting images from vedio files and storing them as image_(serial counter)

**mov2img.py**

Arguments:

**'--jpg'** :fullpath of img folders',default='png'

**'--i'** : Input MOV File name(including extension)

**'--o'** : Output File location folder


### Version
1.0.1

### Installation
##### General : Usually preintalled
* numpy
* matplotlib
* scipy
* argparse
* pickle

##### Additional dependencies
* mov2img
    * ffmpeg

### Example
Consider a test file test.mov whole images need to be extracted to outputfolder located in current directory
```sh
./mov2img.py --i test.mov --o outfolder/
```
  


