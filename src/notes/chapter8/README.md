# Chapter 8 Exceptional Control Flow

本章将引入一个更完整、更现实的模型：异常控制流（Exceptional Control Flow, ECF）。ECF存在于系统的每一个层面，它使得系统能够对各种突发、异步或错误事件做出反应。理解ECF是掌握操作系统如何实现进程、并发和I/O的基础，也是编写健壮、高效的系统级软件的前提。

TL; DR:

1. Exceptions: 硬件与操作系统的接口
    1. 控制权的突然转移，从用户程序到操作系统内核中的一个预定义处理程序
2. Processes: 基于ECF的关键抽象
    1. 程序的一次执行实例: 独立逻辑流 + 私有的地址空间
    2. 上下文切换
    3. 进程控制: `fork()` / `exec()` / `exit()` / `wait() && waitpid()`
3. Signals: 应用层的ECF
    1. 在内核和用户进程之间，或进程与进程之间传递小型消息
4. Non-local Jumps



------

© 2026. ICS Team. All rights reserved.