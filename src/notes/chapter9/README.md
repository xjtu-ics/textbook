# Chapter 9 Virtual Memory

本章旨在完整地阐述虚拟内存（Virtual Memory, VM）这一关键抽象。我们将研究硬件（MMU）和操作系统内核如何协作，为每个进程提供一个独立的、一致的、线性的地址空间，并探讨这一机制如何高效地管理内存。

对于程序员而言，理解VM是进行高级调试、优化内存密集型应用、以及深入掌握动态内存分配（malloc）和文件I/O背后原理的必经之路。

TL: DR:

1. 虚拟内存的特点与优势
    1. Cache角度
    2. 内存管理角度
    3. 内存保护角度
2. 地址翻译
    1. 页表 (Page Table)
    2. 快表 (TLB)
    3. 一整套机制
3. 与其他知识的链接
    1. Memory Mapping
    2. DMA: 动态内存分配



------

© 2026. ICS Team. All rights reserved.
