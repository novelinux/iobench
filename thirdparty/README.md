# Third Party Tools

## bonnie

对于多CPU的系统，bonnie++并没有发挥CPU的最大潜力，也就是说bonnie++发出的I/O请求 通常不够达到CPU和磁盘的最大压力，
这时候显示的吞吐量就不是存储设备能够达到的最大值。因此，这些数字智能作为在单CPU系统中操作的有效性指标。

### org

* http://sourceforge.net/projects/bonnie/
* http://www.textuality.com/bonnie/

### Android

* https://github.com/leeminghao/bonnie-64_trunk

## fio

fio是一个I/O标准测试和硬件压力验证工具，它支持13种不同类型的I/O引擎（sync, mmap, libaio,
posixaio, SG v3, splice, null, network, syslet, guasi, solarisaio等），I/O priorities
(for newer Linux kernels), rate I/O, forked or threaded jobs等等。fio可以支持块设备和文件系统测试，
广泛用于标准测试、QA、验证测试等，支持Linux, FreeBSD, NetBSD, OS X, OpenSolaris, AIX, HP-UX, Windows等操作系统。

### org

http://freecode.com/projects/fio

### Android

* https://github.com/leeminghao/fio

## iozone

Iozone是目前应用非常广泛的文件系统测试标准工具，它能够产生并测量各种的操作性能，包括read, write,
re-read, re-write, read backwards, read strided, fread, fwrite, random read, pread ,mmap, aio_read, aio_write等操作

### org

http://www.iozone.org/

### Android

https://github.com/leeminghao/iozone

## ltp

LTP(Linux Test Project)是由SGI和IBM联合发起的项目，提供一套验证Linux系统可靠性、健壮性、稳定性的测试套件，
也可用来进行POSIX兼容测试和功 能性测试。LTP提供了2000多个测试工具，可以根据需要自行进行定制。同时，
LTP还是一个优秀的自动化测试框架，基于它通过设计测试用例和测试工具 可以实现更多功能的测试自动化。

### org

https://linux-test-project.github.io/

### Android
