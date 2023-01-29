# qemucov  
  
use static qemu user mode binary collect binary coverage information.  


## Build

```
./build-qemucov.sh  

```  

## Usage

* qemu will generate qemucov_cov.log.
* put './qemucov/lighthouse' under IDA plugin directory with lighthouse plugin.
* IDA will be able to use lighthouse to parse qemucov_cov.log.  


```
./build/qemu-x86_64 ./qemucov/testcases/cov_debug  
cat qemucov_cov.log  

```


## Example  


```
QEMUCOV_COV VERSION: 1
Module Table: version 1, count 26
Columns: id, base, end, entry, checksum, timestamp, path
25, 0xFFFFFFFFFF600000, 0xFFFFFFFFFF601000, 0, 0, 0, [vsyscall]
24, 0x00007FFE433A8000, 0x00007FFE433AA000, 0, 0, 0, [vdso]
23, 0x00007FFE433A4000, 0x00007FFE433A8000, 0, 0, 0, [vvar]
22, 0x00007FFE43312000, 0x00007FFE43333000, 0, 0, 0, [stack]
21, 0x00007F1DC8659000, 0x00007F1DC867E000, 0, 0, 0, 
20, 0x00007F1DC8641000, 0x00007F1DC8659000, 0, 0, 0, /home/s0duku/src/qemuida/build/qemu-x86_64
19, 0x00007F1DC85DB000, 0x00007F1DC8641000, 0, 0, 0, /home/s0duku/src/qemuida/build/qemu-x86_64
18, 0x00007F1DC8103000, 0x00007F1DC85DA000, 0, 0, 0, /home/s0duku/src/qemuida/build/qemu-x86_64
17, 0x00007F1DC7CF9000, 0x00007F1DC8103000, 0, 0, 0, /home/s0duku/src/qemuida/build/qemu-x86_64
16, 0x00007F1DC7C66000, 0x00007F1DC7CF9000, 0, 0, 0, /home/s0duku/src/qemuida/build/qemu-x86_64
15, 0x00007F1DC7466000, 0x00007F1DC7C66000, 0, 0, 0, 
14, 0x00007F1DC7465000, 0x00007F1DC7466000, 0, 0, 0, 
13, 0x00007F1DC73E4000, 0x00007F1DC7465000, 0, 0, 0, 
12, 0x00007F1DC0021000, 0x00007F1DC4000000, 0, 0, 0, 
11, 0x00007F1DC0000000, 0x00007F1DC0021000, 0, 0, 0, 
10, 0x00007F1DBFFFF000, 0x00007F1DC0000000, 0, 0, 0, 
 9, 0x00007F1DB8000000, 0x00007F1DBFFFF000, 0, 0, 0, 
 8, 0x00005555557AC000, 0x00005555558BA000, 0, 0, 0, [heap]
 7, 0x0000004002842000, 0x0000004002844000, 0, 0, 0, 
 6, 0x000000400283E000, 0x0000004002842000, 0, 0, 0, /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
 5, 0x000000400283D000, 0x000000400283E000, 0, 0, 0, 
 4, 0x0000004002806000, 0x000000400283D000, 0, 0, 0, /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
 3, 0x0000004002006000, 0x0000004002806000, 0, 0, 0, 
 2, 0x0000004002005000, 0x0000004002006000, 0, 0, 0, 
 1, 0x0000004000003000, 0x0000004000005000, 0, 0, 0, /home/s0duku/src/qemuida/qemucov/testcases/cov_debug
 0, 0x0000004000000000, 0x0000004000003000, 0, 0, 0, /home/s0duku/src/qemuida/qemucov/testcases/cov_debug
BB Table:
 0, 0x0000000000001000
 0, 0x0000000000001016
 0, 0x0000000000001080
 0, 0x0000000000001090
 0, 0x00000000000010B0
 0, 0x00000000000010C0
 0, 0x00000000000010D0
 ...
```  
  
  
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9e02be46-41a5-4e2b-b661-bd857685606a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230129T025451Z&X-Amz-Expires=86400&X-Amz-Signature=16aca6b832f81013c859a687bcb2384e3a8f605b9b1992116d836937716c573a&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)  


