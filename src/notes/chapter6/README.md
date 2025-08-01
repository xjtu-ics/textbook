# Chapter 6  The Memory Hierarchy

本章旨在解决计算机系统中最为核心的性能瓶颈之一：处理器与主存之间巨大的速度鸿沟。我们将深入剖析现代计算机通过构建内存层次结构来缓解此问题的机制。

对于程序员而言，本章的直接目标是建立一个关于系统内存行为的精确模型，并基于此模型编写出具有良好“局部性”、能够最大化缓存命中率的“缓存友好型”代码。

TL; DR:

1. 常见的存储
    1. RAM: DRAM and SRAM
    2. Disk
2. 程序的局部性原理
3. 内存基础知识
    1. Cache Hit and Cache Miss
    2. 常见的 Cache Miss 及原因
4. 内存组织设计
    1. 全相联
    2. 直接相联
    3. 组相联
    4. Write的方法
5. 矩阵乘法
    1. 实例测试: Cache如何影响程序优化



------

© 2025. ICS Team. All rights reserved.