./configure \
--enable-debug \
--extra-cflags="-DQEMUCOV_PATCH" \
--static \
--disable-system \
--enable-linux-user && \
make -j8 && \
gcc -g ./qemucov/testcases/cov_debug.c -o ./qemucov/testcases/cov_debug