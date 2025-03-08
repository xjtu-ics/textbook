# Chapter 3.1 A Historical Perspective

## Intrduction
 
 本章将带领你进入计算机底层的世界，从机器层面了解我们编写的程序，近距离地观察具有可读性的机器代码——汇编代码。😍
 
 什么？开始头晕眼花了？相信我，学完本章，你就能成为一名优秀的拆弹专家！ Bomb lab is waiting for you~
 
 ## Intel x86 Processor
 
 首先，让我们先从历史的角度，了解一下我们手中计算机的处理器的发展沿革，通过历史激起你学习汇编语言的动力。😎
 
 Intel处理器系列俗称x86，它经历了一个长期的、不断进化的发展过程。
 
 1978年，Intel推出具有划时代意义的8086微处理器，它是第一代单芯片、16位微处理器之一。一年后简化版的8088推出，它在8086的基础上支持8位数据总线，IBM公司1981年生产的第一台电脑使用的就是这种芯片。这也标志着x86架构和IBM PC 兼容电脑的产生。此后，x86不断地成长，利用进步的技术满足更高性能和支持更高级操作系统的需求。
 
 下表展示了Intel处理器体系发展过程中的几个里程碑：
 
 Name         |Evolution                                  |Date        |Transistors   |MHz
 :-----------:|:-----------------------------------------:|:----------:|:------------:|:----------------:
 8086         |First 16-bit Intel processor               |1978        |29K           |5-10
 386          |First 32-bit Intel processor(IA32)         |1985        |275K          |16-33 
 Pentium 4E   |First 64-bit Intel x86 processor(x86-64)   |2004        |125M          |2800-3800
 Core 2       |First multicore Intel processor            |2006        |291M          |1060-3333
 Core i7      |Four cores                                 |2008        |731M          |1600-4400
 
 
 可以看到，Intel处理器在近五十年的发展中，晶体管数量大约以每年37%的速率增加。虽然不像Intel创始人Gordon Moore设想的“晶体管数量每年翻一番”那样迅猛，不过在超过五十年中，半导体工业一直能够使晶体管数目每18个月翻一倍。
 
 同时，在发展中，Intel处理器还增加了更多更强大的特性，体系结构从16位扩展到32位乃至如今的64位，核数也由单核转向多核，并且支持多媒体操作和高效的条件指令。
 
 一个非常人性化的设计是，为了便于用户（~~苦命的程序员~~）使用，每个后继处理器的设计都是**后向兼容**(Backwards compatibility)的，即较早版本上编译的代码可以在较新的处理器上运行。这使得Intel使用的x86架构指令集中有多种格式的许多不同指令，它也因此被反对者诟病为**CISC**(Complex Instruction Set Computer)。
 
 与之相对的是**RISC**(Reduced Instruction Set Computer)，主张"*very few* instructions, with *very few* modes for each"，优点是高效率和低功耗。但由于兼容性的问题，很长时间以来仍然是Intel的CISC在市场中占据优势。
 
 不过近年来，由于移动时代用户对于低能耗的需求，RISC又流行起来，在移动设备和嵌入式系统中得到了广泛应用。
 
 ##  x86 Clones: Advanced Micro Devices (AMD)
 
 既然讲了Intel的发展，那么我们就不得不提到它的死对头——AMD。😂
 
 数年来，AMD一直充当Intel的小弟，在技术上紧随Intel，执行的市场策略是：生产性能稍低但价格更便宜的处理器。
 
 1996年，AMD收购了芯片设计公司NexGen，之后推出K6处理器以及迭代产品K6-2、K6-3，以产品廉价和高性价比抢占了极大市场份额，打破了Intel在处理器市场的垄断局面，同时进入笔记本市场对Intel进行挑战。
 
 2002年，AMD率先突破了可商用微处理器的1GHz的时钟速度屏障，并引用了IA32的64位扩展x86-64。2003年推出皓龙（Opteron）服务器处理器，又为AMD打开了部分服务器市场份额。此后AMD微处理器市场份额持续上升，成为Intel的强劲对手。
 
 不过故事并没有结束，在AMD收购了合作伙伴NVIDIA在 GPU 领域的死对头 ATI之后，NVIDIA一怒之下转向Intel，而Intel也在2006年推出新一代处理器Core 2以及4核CPU，重新占据主导地位。
 
 近年来，TSMC成为世界领先的半导体晶圆厂，Intel再次落后。
 
 2017年3月，AMD以Zen架构为核心的锐龙（Ryzen）系列处理器正式发行，迅速抢占CPU市场份额。此后，AMD在CPU和GPU市场双线作战，Zen架构的持续迭代和性能进步显著，在纸面参数上超越英特尔十代酷睿处理器，动摇了英特尔在CPU市场的长期霸权。
 
 AMD和Intel的大型商战还在继续......
 
 ## Our Coverage
 
 本课程仅采用x86-64架构进行描述。参考教材CS:APP3e的[Web Asides](http://csapp.cs.cmu.edu/3e/waside.html)有对IA-32编程的介绍。
 
 
 ```admonish info
 IA-32(Intel Archtecture 32-bit): 是一个32位架构，使用传统的 x86 指令集。
 
 x86-64: 在 x86 指令集的基础上进行了扩展，增加了新的指令以支持 64 位操作。x86-64 架构仍然可以执行 IA-32 的指令，这保证了向后兼容性。
 ```

------

© 2025. ICS Team. All rights reserved.