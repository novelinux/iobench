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


## postmark

Postmark 是由著名的 NAS 提供商 NetApp 开发，用来测试其产品的后端存储性能。Postmark主要用于测试文件系统在邮件系统或电子商务系统中性能，
这类应用的特点是：需要频繁、大量地存取小 文件。 Postmark 的测试原理是创建一个测试文件池。文件的数量和最大、最小长度可以设定，数据总量是
一定的。创建完成后， Postmark 对文件池进行一系列的事务（ transaction ）操作，根据从实际应用中统计的结果，设定每一个事务包括一次创建或
删除操作和一次读或添加操作，在有些情况下，文件系统的缓存策略可能对性能造成影响， Postmark 可以通过对创建 / 删除以及读 / 添加操作的比例
进行修改来抵消这种影响。事务操作进行完毕后， Post 对文件池进行删除操作，并结束测试，输出结果。 Postmark是用随机数来产生所操作文件的序号，
从而使测试更加贴近于现实应用。输出结果中比较重要的输出数据包括测试总时间、每秒钟平均完成的事务 数、在事务处理中平均每秒创建和删除的文件数，
以及读和写的平均传输速度。

### org

https://sources.debian.org/src/postmark

### Android
