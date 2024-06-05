cd /opt/binary/patchelf
./bootstrap.sh
./configure
make
make check
sudo make install