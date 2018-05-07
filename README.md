# install-ffmpeg-raspberry-pi
### From http://hannes.enjoys.it/blog/2016/03/ffmpeg-on-raspbian-raspberry-pi/
        # build and install x264
        git clone --depth 1 git://git.videolan.org/x264
        cd x264
        ./configure --host=arm-unknown-linux-gnueabi --enable-static --disable-opencl
        make -j 4
        sudo make install

        # build and make ffmpeg
        git clone --depth=1 git://source.ffmpeg.org/ffmpeg.git
        cd ffmpeg
        ./configure --arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree
        make -j4
        sudo make install
