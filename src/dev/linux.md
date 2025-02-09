# A Bite of Linux

## 为什么你应该用 Linux

> 冷知识0: 在 Linux 下一样可以玩 Windows 上的游戏, 诸如 Steam 上的各种游戏, 且很多时候性能比 Windows 更好. 你可以在 [ProtonDB](https://www.protondb.com) 上检查你 Steam 上喜欢的游戏的兼容性和性能
>
> 冷知识1: Arch Linux 的官方源里包含 Steam, 你可以直接从包管理器安装 Steam, 免去了上网和诈骗网站/Steam助手等斗智斗勇的烦恼
>
> 冷知识2: Mac(Apple Silicon) 对 Steam 的兼容性稀烂, 尤其是大型游戏

1. 贴近生产环境与开发者工具链
   - 服务器环境主导: 绝大多数服务器, 云计算平台(如 AWS, Azure), 容器技术(如 Docker/Kubernetes)均基于 Linux. 熟悉 Linux 的操作和运维是开发者必备技能.
   - 原生开发工具链: Linux 对编程语言(Python, C/C++, Java, Go 等), 编译器(GCC/Clang), 调试工具(GDB), 构建工具(Make/CMake)以及脚本环境(Bash)的支持更原生, 无需依赖第三方模拟器或兼容层.
   - 包管理高效: 通过 `apt`(Debian/Ubuntu), `dnf`(Fedora)或 `pacman`(Arch)等包管理器, 可快速安装开发库, 工具和依赖项, 避免手动下载安装的繁琐.
2. 命令行与自动化能力
   - 强大的 Shell 生态: Linux 的命令行工具(如 `grep`, `sed`, `awk`, `ssh`, `tmux`)和脚本能力(Bash/Python)是开发者的核心生产力工具, 适合处理文本, 自动化任务, 远程服务器管理.
   - 开发流程无缝衔接: 从本地代码编写, 编译, 测试到部署到服务器, Linux 提供一致的环境, 避免跨平台兼容性问题(如 Windows 换行符, 路径分隔符导致的错误).
3. 开源与可定制性
   - 系统透明可控: Linux 允许开发者深入操作系统内核, 网络协议栈, 文件系统等底层机制, 适合学习计算机原理(如操作系统, 编译原理课程).
   - 高度可定制: 开发者可以自由配置开发环境(如窗口管理器, 终端工具链), 优化性能, 甚至修改内核参数, 满足特定需求.
4. 社区与学习资源
   - 开发者导向的社区: Linux 生态的文档(如 `man` 手册, Arch Wiki), 论坛(Stack Overflow, GitHub)和开源项目资源更贴近开发者需求, 问题解决效率高.
   - 前沿技术支持: 多数开源项目(如 Kubernetes, TensorFlow, Node.js)优先适配 Linux, 新工具和框架在 Linux 上的支持更完善.
5. 轻量化与资源效率
   - 低资源占用: Linux 对硬件资源(CPU, 内存)的需求更低, 适合在虚拟机, 老旧设备或笔记本上流畅运行, 提升开发效率.
   - 稳定性与安全性: Linux 系统崩溃概率低, 病毒攻击风险小, 适合长期运行的开发任务.

> Windows 和 Linux 占用资源对比:
>
> 我同一台电脑, 桌面壁纸采用 Wallpaper engine 加载同一张动态壁纸
>
> Windows 11 进入系统, 任务管理器显示显存占用 5.9 GB
>
> Arch Linux 进入 KDE Plasma 桌面, 任务管理器显示显存占用 0.8 GB

## Linux 小知识

按理来说, 我应该好好写写 Linux 的背景知识, 发展历程, GNU 和自由软件, 开源软件什么的. 但我懒得写了, 我打算教你一些黑话, 让你可以到处装X. 😎

### Linux, GNU/Linux, Systemd/Linux

如果有人向你提起 Linux, 你可以这么跟他说: 应该是 GNU/Linux 才对. 不过按现在各大 Distro 的情况来看, 说 Systemd/Linux 也不为过.

解释:

- Linux: 一个操作系统内核, 并不等于操作系统本身
- GNU/Linux: 当初 GNU 一直缺一个可用的内核, 于是把 Linux 拉了过来. GNU 的各个组件都能运行在 Linux 上, 而 Linux 作为承载 GNU 组件的内核. 这样的组合被成为 GNU/Linux, 并沿用至今
- Systemd/Linux: Systemd 是一套服务管理工具, 在现代 Linux Distro 中, 它大包大揽了非常多的事务. Linux 如果少了 GNU 组件, 一样能找到一些好用的替代品, 但要是少了 Systemd, 可能连启动都没法启动. 考虑到 GNU/Linux 名称的来历, 我们可以按同样的方法叫 Systemd/Linux.

> Systemd 真的能引导启动, 我在用的就是 Systemd-boot 引导启动.

### Tragedy of Systemd

> [视频链接](https://www.youtube.com/watch?v=o_AIw9bGogo)

简单来说, Systemd 是 Linux 中的一个初始化系统(init system)和服务管理器, 它提供了一系列用于初始化系统, 管理系统进程, 服务, 日志, 设备, 网络和其它系统资源的工具套件.

> 回忆一下操作系统的知识: init system 是操作系统启动时运行的第一个进程(PID=1)

这么看来 Systemd 似乎很厉害, 一个软件能干这么多事情. 但这也违背了 Unix 哲学: 一个工具只做一件事. Unix 原教旨主义者普遍讨厌 Systemd All-in-One 的设计. 但我觉得吧, 在系统编程的层面, 死扣着独立设计/模块化设计的哲学也没必要, 有时候需要一些更灵活的手段. 包括 Linux 内核自己都不是所谓的微内核.

事实上, Systemd 的效率和规范化远胜于它的前任 SysVinit, 也比常见的 cron 配置文件好写得多, 反正我觉得用起来挺顺手的.

但对于系统开发者来说, Systemd 的设计是有问题的. 它在 kernel 和 user 之间插入了一层 system, 但它也没有明确地定义 system 的边界, 即 system 应该做什么, 不应该做什么. 这就使得, 如果你对 Systemd 的某个功能模块不满意, 想自己写一个更好的, 那么你要么自己实现一个完整的 Systemd 来代替掉它创建的 system 层, 要么你就只能用 Systemd, 并在它的源码上进行有限的修改. 而且大而全的 Systemd 没有保留 kernel 和 user 的直通接口, 这可能会影响到用户对系统开发的可定制性.

> 而且 Systemd 的开发者曾经开发过 pulseaudio, 是一个 bug 一堆的音频控制工具, 不如 pipewire 一根. 所以 Systemd 的代码质量是不如 Linux 内核的.

但是管他呢, 我又不是系统程序员, 用 Systemd 就用吧.

### Tragedy of GNU

与其说是 Tragedy of GNU, 不如说是 Tragedy of Free Software.

自由软件的兴起, 发展, 衰落我懒得写了, 网上讲自由软件运动的视频有很多. 曾经轰轰烈烈的自由软件运动已经被各大商业公司用*开源软件*偷梁换柱了. 现在的热词是*开源*软件, 但实际上, 开源软件和自由软件是两个概念. 具体参考[开源错失了自由软件的重点](https://www.gnu.org/philosophy/open-source-misses-the-point.html).

如果你也想成为一名**自由软件**支持者, 一个最简单的步骤就是, 在你发布你的软件和源代码时, 采用最新的 GPL 系列 License. 比如 GPL-v3 和 AGPL-v3.

### Tragedy of Linux

Linux 社区采用的开发和管理方式是仁慈君主独裁制, 即所有的 code review 都由 Linus 本人最终负责. 然而可惜的是, Linus 本人并不是一个自由软件者, 尽管 Linux 前被冠上了 GNU 的名号. 当时 GNU 和 Linux 的合作, 只是迫于 UNIX 的巨大压力下而达成的. Linus 本人并不是多么在意自由软件的理念, 比起理念, 他更像是一个实用主义者. 尽管 GNU 推出了最新版的 GPL-v3 协议和 AGPL-v3 协议, 进一步确保了软件和代码的**自由**, 并且自由软件创始人理查德·斯托曼(Richard Stallman)也曾多次建议 Linus 将 Linux 的协议从 GPL-v2 升级到 GPL-v3, 但都被 Linus 无视了.

在 2024 年 10 月 18 日, Linux 社区发生了一件足以被钉在历史耻辱柱上的事: Linus 未经社区审议和正常流程, 直接将若干个来自俄罗斯的内核模块维护者移除维护名单. 并且面对社区的质疑, Linus 本人发邮件回复, 表达了自己对俄罗斯国籍的敌意.

可悲可叹, 开源社区的精神支柱 Linus, 亲手打碎了大家树立起来的神像. 这一刻, Linus 以前爆过的所有的典, 都化成了巨大的回旋镖打在了自己脑门上.

> Linus: code is cheap, show me your nationality.

## Linux 发行版及其刻板印象

Linux 发行版(Distro)是基于 Linux 内核开发出的完整操作系统. 基于不同的设计思想和理念, 以及不同的应用场景, Linux 社区衍生出了众多的发行版. 这里我首先列举出**自由**的 [GNU/Linux 发行版](https://www.gnu.org/distros/distros.html). 一个令人悲伤的事实是, 考虑到各大商业公司的驱动, 固件等都不是自由的, 为了能满足日常流畅使用, 主流的 Linux 发行版不得不包含这些非自由的固件, 因而丧失了自己自由的性质.

![linux impressions](./image/linux-impressions-0.avif)

![linux impressions](./image/linux-impressions-1.avif)

> 刻板印象就图一乐, 认真你就输了. 😂

### Debian 系列

- Debian: 正统发行版, 曾经一度是坚定的 GNU/Linux, 可惜还是在现实的重压下低头了. 因为其标志特别像雌二醇包装盒上的标志, 因而被认为是男娘系统. 如果你在用 Debian, 那记得加我 QQ, 我喜欢香香软软的小男娘. 🥰

![Debian](./image/linux-debian.png)

- Ubuntu: 声量最大的 Linux 发行版, 曾经一度让小白以为 Ubuntu == Linux, 可能也是很多小白的第一款 Linux. 由商业公司 Canonical 开发并维护, 塞满了公司的私货(比如 snap 包管理器)以及一些神奇的政治倾向. Ubuntu 系统饱受诟病的一点就在于它十分不稳定, 动不动就给你弹一个报错. 如果你在用 Ubuntu, 那就别用了, 换个发行版吧.
- Deepin: 国产的操作系统. 很抽象, *国产*, *开源*, 这两个词竟然能凑在一起. 我只简单地尝试过, 鉴定为比 Ubuntu 还不如的东西. 如果你在用 Deepin, 那我相信你也一定在用鸿蒙.
- NixOS: 一种很新的东西, 自己重新搞了一套独立的包管理系统, 采用函数式的声明来配置整个系统. 我只是简单地用过, 懒得学习 Nix 语言, 就没用了.

### Red Hat 系列

- Red Hat Enterprise Linux(RHEL): 红帽企业版 Linux, 红帽公司推出的商业 Linux 发行版, 专注于企业商用.
- Fedora: 红帽公司推出的社区版 Linux, 专注于个人开发者. Red Hat 会将 Fedora 作为新特性的试验田, 当特性成熟稳定后会进入到 RHEL 中. 所以 Fedora 算是 RHEL 的上游.
- CentOS: 已经死掉了的 Linux 发行版, 本来是作为社区版的 RHEL 在运行的, 结果被 Red Hat 收购之后就成了 RHEL 的上游去了, 换言之, 企业商用所追求的稳定性和安全性就没有了. 如果你在用 CentOS, 那你应该是买了国内老掉牙的 Linux 入门书籍. 国内企业也是用 CentOS 居多. 很符合我对国内的刻板印象.
- OpenEULER: 华为推出的 RHEL 衍生版, 仅在做数据库实验时用过, 臭不可闻. 如果你在用 OpenEULER... 🫡😅

### Arch 系列

- Arch Linux: 我的日常操作系统, 只有你用了才知道它的好. 如果你也在用 Arch Linux, 那太棒了, 你一定是和我一样的小男娘, 快来加个 QQ 吧! 😘

![Arch](./image/linux-arch.jpg)

- Manjaro: 你是? 都用这个了, 为什么不直接一步到位用 Arch Linux 呢?
- SteamOS: 惊不惊喜, 意不意外? SteamOS 其实是 Arch Linux 的衍生版. 如果你玩 Steam Deck, 那你已经在不知不觉间用上了 Linux 了!

### Gentoo 系列

- Gentoo: 我没用过, 我不知道.

## 安装 Linux

前面我已经简单介绍了几个知名的 Linux 发行版, 相信你也选择出了你想要安装的 Linux 发行版. 我正在使用的是 Arch Linux, 我强烈推荐 Arch Linux, 后文的所有内容我也会基于 Arch Linux 撰写.

想要安装 Arch Linux, 有若干方法可供选择:

- 👍 做好文件备份, 然后把你的 Windows 丢到垃圾桶里去, 直接在物理机上安装 Arch Linux. (推荐)
- 👍 购买/组装一台新电脑, 然后安装 Arch Linux. (推荐)
- 考虑到你正在使用 Windows, 可以在 WSL2 中安装 WSL2-Arch. (推荐)
- 在 Windows 上安装虚拟机, 然后安装 Arch Linux.
- 使用双系统, 在已有 Windows 的基础上安装 Arch Linux.

### WSL2-Arch

参考[这篇文章](https://orion-zhen.github.io/article/how-to-code-on-windows)

### 完整地安装 Arch Linux

#### 准备工作

首先从[ISO镜像源](https://mirrors.tuna.tsinghua.edu.cn/archlinux/iso/latest/)找到最新的 ISO 镜像文件, 下载到本地.

> Arch Linux 采用滚动更新的策略, 所以不会像 Ubuntu 一样有特定的版本号. Arch Linux 会每隔一段时间创建一个最新的系统快照, 作为 ISO 镜像文件使用.

然后准备一个将这个镜像烧入到你准备好的启动U盘中. Windows 下可选 [Rufus](https://rufus.ie/zh), Linux 下可选 [balenaEtcher](https://etcher.balena.io).

烧录完成后, 将电脑从启动U盘启动, 即可进入 Arch Linux 安装界面.

![archinstall boot](./image/archinstall-boot.png)

> 注意, 如果是笔记本的话, 记得先在 BIOS 中关闭安全启动, 不然会无法安装.

选择第一项 **Arch Linux install medium**, 按回车键即可进入安装.

在一阵炫酷的文字滚动后, 你会进入如下界面:

![archinstall terminal](./image/archinstall-terminal.png)

现在我们已经成功进入了 Arch Linux 的安装界面. 这里我们将使用 `archinstall` 来快速且方便地安装 Arch Linux.

#### 配置网络

如果你已经通过有线网络连接到互联网, 那就不用额外配置网络连接. 如果你的笔记本没有无线网口, 那么就要使用 `iwctl` 命令来连接无线网络.

首先输入 `iwctl`, 然后按回车键, 进入 `iwctl` 命令行界面.

然后输入 `device list`, 列出所有的无线网卡. 这里假设你的无线网卡是 `<card-name>`.

然后用以下命令搜索可用的无线网络:

```shell
device <card-name> scan
device <card-name> get-network
```

搜索完成后, 找到你想要连接的网络, 假设为 `<wifi-name>`.

输入以下命令连接无线网络:

```shell
device <card-name> connect <wifi-name>
```

之后会提示你输入 WiFi 密码, 输入密码后即可连接到网络.

使用 `exit` 命令退出 `iwctl` 命令行界面.

现在你已经成功连接到网络了.

#### 换源

Arch Linux 默认采用的是国外的源, 会很慢. 所以推荐使用 `reflector` 进行换源:

```shell
reflector -c China --sort rate --latest 20 --verbose --save /etc/pacman.d/mirrorlist
```

命令解释:

- `reflector`: 是一个用来更新 pacman 源的工具.
- `-c`: 国家参数, 这里选择 China 内的镜像源
- `--sort`: 排序手段, 这里按照镜像源的下载速率从高到低排序
- `--latest`: 显示前 20 个镜像源
- `--verbose`: 显示详细信息
- `--save`: 将更新后的源列表保存到 `/etc/pacman.d/mirrorlist` 文件中

当命令完成后, 即可使用 `pacman -Syu` 命令更新系统软件.

#### 安装系统

输入:

```shell
archinstall
```

然后按回车键, 进入安装程序:

![archinstall tui](./image/archinstall-tui.png)

由于版本不同, 你看到的界面可能和我有所不同, 但需要配置的项目都是一样的. 让我们来逐一配置:

- Archinstall language: 不要动
- Locales: 不要动, 等装完了再改
- Mirrors: 不要动, 已经用 `reflector` 配置过了
- Disk configuration: 配置磁盘
  - Partitioning: 磁盘分区
    - Use a best-effort default partition layout: 使用默认分区方案, 建议选这个
      - 选择你要安装的硬盘, 然后进入 Filesystem 选择:
        - btrfs: 推荐, 支持很多高效的特性
          - use BTRFS subvolumes with a default structure: 使用 BTRFS 子卷, 并使用默认结构, 建议选择 Yes
          - use compression or disable CoW: 使用压缩或禁用 CoW, 建议选择 Use compression
          - separate partition for /home: 分离 /home 目录, 建议选择 No
        - ext4: 老牌选择, 兼容性好
        - xfs/f2fs: 没用过, 不知道
    - Manual partitioning: 手动分区
- Disk encryption: 不要动
- Swap: 不要动
- Bootloader:
  - systemd-boot: 推荐, 支持 UEFI.
  - grub: 兼容性和可配置性强. 随你.
- Hostname: 主机名, 取一个你喜欢的名字
- Root password: Root 用户密码
- User account: 配置普通用户
  - Add a user: 添加一个普通用户
    - Username: 用户名, 只能用小写字符
    - Password: 密码, 可以设置成和 Root password 一样
    - should \<username\> be a superuser (sudo)?: 是否授予 sudo 权限, 建议选择 Yes
  - Confirm and exit: 确认并退出用户配置
- Profile: 安装方案
  - Type: 安装类型
    - Desktop: 安装桌面环境, 有 GUI, 你可以选择若干桌面环境. 以下是我的选择(使用空格键勾选, 使用回车确认并退出)
      - [x] KDE Plasma
      - [x] Hyprland
      - Seat access: 权限认证工具, 我选择 `polkit`, 因为这是 KDE 内置的工具
    - Minimal: 最小化安装, 除了系统本体, 啥都没有
    - Server: 服务器安装, 会安装用于网络服务器的组件, 没有 GUI
    - Xorg: 不知道, 我没用过
    - Graphics driver: 当你选择 Desktop 选项后出现, 如果你是 N 卡用户, 则选择 Nvidia(proprietary); 否则不要动
    - Greeter: 登录界面, 不要动
- Audio: 选 pipewire
- Kernels: 不要动
- Network configuration: 安装完成后新系统配置网络的方式, 如果你选择安装的 Desktop 中有 KDE Plasma 或者 GNOME, 则可以选择 Use NetworkManager
- Additional packages: 安装一些额外的软件包, 不要动, 可以等安装完了在新系统里自己装
- Optional repositories: 额外的软件仓库, 建议勾选 multilib, 因为里面有 Steam (笑)
- Timezone: 时区, 键入 `/shanghai` 即可跳转到 `Asia/Shanghai` 时区, 回车选择确认
- Automatic time sync: 自动校时, 不要动

当一切配置完成, 你可以选择下方的 Install 选项, 回车确认后, 此时系统会自动开始安装.

#### 本地化

当 `archinstall` 安装完成后, 会提示是否 `chroot` 进入新系统. 选择 Yes 进入新系统终端, 输入命令:

```shell
vim /etc/locale.gen
```

找到并取消注释如下内容所在的行:

```text
zh_CN.UTF-8
```

保存退出后用如下命令更新本地化设置:

```shell
locale-gen
```

### Arch Install: Odyssey

虽然使用 `archinstall` 工具安装 Arch Linux 非常方便快捷, 但我还是建议你至少按照 [arch wiki](https://wiki.archlinuxcn.org/wiki/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97) 完整地手动走一遍安装流程, 这对你理解 Linux 系统的运行原理和结构有很大帮助.

## 配置 Arch Linux

在 KDE Plasma 桌面环境中, 快捷键 Crtl+Alt+T 可以快捷打开终端.

GUI 的美化千千万, 你可以自己探索你喜欢的美化设置. 这里我将主要讲解终端的美化和配置.

### 更换系统字体和语言

你不能直接将系统语言更换为中文, 因为此时系统缺少中文字体. 使用如下命令安装常用字体:

```shell
sudo pacman -S ttf-hack-nerd noto-fonts-cjk
```

然后在系统设置中, 先更改字体为 `Noto Sans CJK SC`, 再更改语言为简体中文.

### 添加第三方源

Arch Linux 有许多有用的第三方源, 可以让你不用翻墙就能安装一些好用的软件. 使用 vim 打开 `/etc/pacman.conf`, 在末尾加入以下内容:

```text
[archlinuxcn]
SigLevel = Optional TrustAll
Server = https://mirrors.cernet.edu.cn/archlinuxcn/$arch

[arch4edu]
SigLevel = Optional TrustAll
Server = https://mirrors.cernet.edu.cn/arch4edu/$arch
```

保存退出后, 使用 `sudo pacman -Syu` 更新软件源.

### 安装 AUR 助手 yay

yay<sup>archlinux-cn</sup> 是 Arch Linux 的 AUR 助手, 它可以帮助你管理 AUR 软件包, 并自动编译安装. 从 archlinuxcn 仓库安装 yay:

```shell
sudo pacman -S yay
```

需要导入密钥时, 选择同意导入.

### 安装常用软件

可以参考[安装脚本](https://github.com/Orion-zhen/dotfiles/blob/main/install.sh)中的内容, 自助选择需要安装的软件.

### 输入法设置

使用 Fcitx5 作为输入法:

```shell
sudo pacman -S fcitx5-im fcitx5-chinese-addons
```

然后在 系统设置 > 虚拟键盘 中选择 Fcitx5 作为输入法.

### 终端美化

我的美化方案需要用到以下软件:

```shell
sudo pacman -S ttf-hack-nerd zsh tmux fzf fd bat eza tldr thefuck trash-cli atuin autojump starship
```

请先将你的终端字体切换到 Hack Nerd Font, 否则无法显示某些符号.

#### 切换默认终端

将默认终端切换为 zsh:

```shell
sudo chsh -s /bin/zsh
```

#### 安装 oh-my-zsh

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

#### 安装主题和扩展

```shell
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/wfxr/forgit.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/forgit
mkdir ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/incr
curl -fsSL https://raw.githubusercontent.com/Orion-zhen/incr-zsh/main/incr.zsh -o ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/incr/incr.zsh
```

#### 配置 .zshrc

`.zshrc` 文件位于你的用户目录下, 是控制终端行为的配置文件.

```shell
curl -fsSL https://raw.githubusercontent.com/Orion-zhen/dotfiles/main/.zshrc -o ~/.zshrc
```

现在重启电脑, 你应该可以看到一个漂亮的终端了.

## Linux 入门

### 包管理器

Linux 下, 安装软件都应该从包管理器安装. 这和 Windows 下需要上网找安装包然后自行安装的方式有很大的不同. 正是这个包管理器机制, 让 Linux 下的软件安装和更新变得如此简单.

一个内容重组的包管理器软件源就显得尤为重要. 这也正是 Arch Linux 的优势区间所在. Arch 官方源中本身就有非常丰富的软件, Arch User Repository (AUR) 则是由广大 Arch 用户提供的软件仓库. 你总能找到你想要的软件包.

### pacman

Pacman软件包管理器是 Arch Linux 的一大亮点. 它将一个简单的二进制包格式和易用的构建系统结合了起来. Pacman的目标是简化对软件包的管理, 无论软件包是来自官方软件仓库还是用户自己创建的软件包.

Pacman 通过和主服务器同步软件包列表来保持系统是最新的. 这种服务器/客户端模式可使得用户使用简单的命令, 就能下载或安装软件包, 并包含其所有必需的依赖包.

Pacman 用 C 语言编写, 并使用 bsdtar(1) tar 作为打包格式.

具体参考 [archwiki -> pacman](https://wiki.archlinuxcn.org/wiki/Pacman)

### 软件源

可以向 `/etc/pacman.conf` 的末尾追加软件源. 例如前文已经向你展示了两个比较常用的软件源: archlinuxcn 和 arch4edu. 这里再补充几个好用的软件源:

- [chaotic-aur](https://aur.chaotic.cx/): 构建了很多 AUR 软件包
- [alerque](https://github.com/alerque/aur): 提供了很多字体
- [our](https://orion-zhen.github.io/our): 我自己构建的软件源, 包含了诸如 QQ, 微信, 腾讯会议, 钉钉等未被 archlinuxcn 和 archedu 收录的软件, 以及一些妙妙工具

以上提到的软件源可以如下导入:

```text
# /etc/pacman.conf
[chaotic-aur]
SigLevel = Optional TrustAll
Server = https://geo-mirror.chaotic.cx/$repo/$arch

[alerque]
SigLevel = Optional TrustAll
Server = https://arch.alerque.com/$arch

[our]
SigLevel = Optional TrustAll
Server = https://orion-zhen.github.io/our/$arch
```

### AUR 助手

安装 AUR 软件总是很麻烦: 你要将 AUR 仓库克隆下来, 然后手动编译安装. 幸运的是, 有一个叫做 yay 的 AUR 助手可以自动化这一过程. 具体参考 [archwiki -> yay](https://wiki.archlinuxcn.org/wiki/Yay)

> 当然你也可以学我, 自己打包 AUR 软件并发布软件源 😉

### Linux 文件结构

和 Windows 不同, Linux 文件系统是树状结构, 并不会区分 C 盘, D 盘 云云. 使用 `cd` 命令切换到根目录下:

```shell
cd /
```

然后使用 `ls` 命令查看根目录下的文件夹:

```shell
ls
```

让我们来逐个检查这些文件夹:

- `/bin`: binary 的缩写. 存放着对操作系统至关重要的二进制文件/可执行文件. 在现代 Linux 系统中, 这个文件夹常被作为符号链接指向 `/usr/bin` 目录
- `/sbin`: system binary 的缩写. 存放着系统管理相关的二进制文件/可执行文件, 仅应该被 root 用户或 sudo 权限使用. 在现代 Linux 系统中, 这个文件夹常被作为符号链接指向 `/usr/bin` 目录
- `/lib`: library 的缩写. 存放着系统的共享库文件. 这些文件在系统启动时被加载到内存中, 并由各个程序共享. 在现代 Linux 系统中, 这个文件夹常被作为符号链接指向 `/usr/lib` 目录
- `/lib64`, `lib32`: `/lib` 的变体, 和 `lib` 指向同样的目录
- `/usr`: Unix System Resources 的缩写. 顾名思义, 即 Unix 系统资源目录, 包含了运行系统所需要的各种重要资源, 比如命令, 库, 字体, 文档等
- `/etc`: Editable Text Configuration 的缩写. 存放着系统的配置文件, 包括各种服务的配置文件, 登录脚本, 环境变量等. 所有的系统级配置文件都应该存放在这个目录下. 里面有许多以 `.conf` 结尾的文件, 其实都是文本文件. 应用程序们读取各自对应的配置文件, 并进行相应的配置
- `/home`: 用户目录所在. 不同的用户对应不同的文件夹, 例如用户名 `sample` 的用户目录就在 `/home/sample` 目录下. 在终端中, 用户目录常可以用 `~` 符号来访问, 也可以从环境变量 `$HOME` 中获取
- `/var`: Variable 的缩写. 存放着系统运行时产生的各种数据文件, 比如日志文件, 缓存文件, 临时文件等, 这些文件在系统运行时会被频繁地修改. 另外, 系统日志文件也会被存放在这个目录下
- `/boot`: 存放着启动相关的文件, 包括内核, 引导程序, 启动脚本等. 系统启动时, 内核会被加载到内存中, 然后启动脚本就会被执行, 引导系统进入操作系统
- `/dev`: Device 的缩写. Linux 的设计思想是"一切皆文件", 因此 Linux 系统中的设备也被看作文件. 这个目录存放着 Linux 系统中所有的设备文件, 包括块设备文件和字符设备文件. 块设备文件通常用来存放硬盘, 字符设备文件通常用来存放打印机, 网络设备等. 在这个目录中有一些有意思的设备文件:
  - `/dev/null`: 黑洞设备, 所有写入到这个设备的数据都会被丢弃
  - `/dev/zero`: 零设备, 所有写入到这个设备的数据都会被填充为 0
  - `/dev/urandom`: 伪随机设备, 产生伪随机数据
- `/opt`: Optional 的缩写. 存放着第三方软件的安装目录. 例如, 你使用官方包管理器安装了 cuda 驱动, 那么 cuda 的安装目录就会被存放在 `/opt/cuda` 目录下
- `/tmp`: Temporary 的缩写. 存放着临时文件, 一般是应用程序运行时产生的临时文件. 系统重启后, 这个目录下的文件都会被删除
- `/proc`: Process 的缩写. 存放着系统的运行信息, 例如系统的内核信息, 进程列表, 网络连接信息等. 这个目录的内容是动态储存在内存中的, 并不占用磁盘空间
- `/mnt`: Mount 的缩写. 存放着临时挂载点, 即将外部设备挂载到系统的文件系统. 你可以使用 `mount` 命令将不同的设备挂载到系统中的任何位置. 不过一般都是临时挂载在这个目录下: `sudo mount /dev/sda1 /mnt`

```admonish
有时候你可能会想, 既然已经有 `/usr/bin` 和 `/usr/lib` 目录了, 为什么还要创建两个符号链接呢? 这其实也是历史遗留问题, 早期的 Linux 文件结构还没有这么清楚, 当时光是 `bin` 目录就区分了 `/bin`, `/sbin`, `/usr/bin`, `/usr/local/bin` 等等. 后来 Linux 社区意识到这个问题, 于是就把这些目录都合并到 `/usr` 目录下, 并创建了符号链接. 这样做的好处是, 系统中只需要维护一个目录, 而不需要维护多个目录.
```

```admonish
关于 `/usr` 目录, 有人误认为它是 User 的缩写, 其实是错误的. 在 Mac 中, 用户目录都存放在 `/User` 下, 而 `/usr` 仍然存在.
```

```admonish
小心 `/` 和 `./` 的区别, 前者是根目录, 后者是当前目录. 不要一不小心少打一个 `.`, 导致错误地对根目录进行了一些不妙的操作.
```

### Linux 文件

#### 文件权限

使用 `ls -l` 命令查看文件的权限:

```shell
ls -l
```

- 第一个字符表示文件类型:
- 后面三位表示文件所属用户的权限
- 再后面三位表示文件所在的用户组的权限
- 最后三位表示其他用户的权限

对于权限位, 各位的含义依次如下:

- `r`: 可读, 数字为 4
- `w`: 可写, 数字为 2
- `x`: 可执行, 数字为 1
- `-`: 没有权限, 数字为 0

将这些权限求和, 即可得到不同的数字, 每个数字唯一地表示一种权限组合. 三个数字在一起, 即是完整的文件权限. 例如, `rw-r--r--` 就是 644, `rwxr-xr-x` 就是 755.

想要改变文件的权限, 可以使用 `chmod` 命令:

```shell
chmod <access-mode> [-R] file
```

其中, `<access-mode>` 是你想要设置的权限位, 例如 `755` 就是 `rwxr-xr-x`. `-R` 选项可以递归地设置目录下所有文件的权限.

如果仅想授予某个文件可执行的权限, 可以:

```shell
chmod +x file
```

> 我曾经的个性签名是: `sudo chmod 777 -R /world`, 你知道这是什么意思吗?

#### 文件操作

##### 创建和删除

- `touch`: 创建空文件
- `mkdir`: 创建目录
- `rm`: 删除文件, 选项 `-r` 可以递归删除目录, 选项 `-f` 可以强制删除
- `cp`: 复制文件或目录, 选项 `-r` 可以递归复制目录
- `mv`: 移动文件或目录

命令示例:

```shell
mkdir test
mkdir test2
touch test.txt
cp test.txt another-test.txt
mv test.txt test1.txt
mv test1.txt test/
cp -r test test2
rm another-test.txt
rm -r test
rm -rf test2
```

##### 切换目录

- `pwd`: 显示当前目录
- `cd`: 切换目录

命令示例:

```shell
cd ~ # 切换到用户目录
pwd
```

##### 列出目录项

- `ls`: 列出目录内容
- `tree`: 递归列出目录内容

命令示例:

```shell
ls
ls -a # 显示隐藏文件
ls -l # 显示详细信息
tree .
```

##### 查看文件内容

- `cat`: 打印文件内容
- `less`: 逐页查看文件内容

命令示例:

```shell
cat test.txt
less test.txt
```

##### 查找文件和目录

- `find`: 查找文件或目录

命令格式:

```shell
find [options] <path> [expression]
```

| expression | 含义 | 示例|
| --- | --- | --- |
| `-name` | 根据文件名查找 | `-name "*.txt"` 即寻找所有以 `.txt` 结尾的文件, `*` 是通配符 |
| `-type` | 根据文件类型查找 | `-type f` 即寻找普通文件, `-type d` 即寻找目录 |
| `-size` | 根据文件大小查找 | `-size +10k` 即寻找大于 10KB 的文件, `-size -10k` 即寻找小于 10KB 的文件 |
| `-or`   | 或 | `-name "*.txt" -or -name "*.pdf"` 即寻找所有以 `.txt` 或 `.pdf` 结尾的文件 |

### Linux 用户和用户组

#### root 用户

你应该也注意到了, 之前运行 `pacman` 命令时, 总是要在前面加上 `sudo`, 这其实就是在以 root 用户的身份安装软件. 一般地, 根用户 (root 用户) 在 Linux 操作系统中拥有**最高权限**.

> 这里的最高权限是真的最高, 能完全地掌控整个电脑, 哪怕你要做危害系统的命令也行, 不像 Windows 和 MacOS, 它们的*管理员*权限根本不是系统最高权限. 最高权限被它们的公司牢牢抓在自己手里, 不肯分给用户半点.

既然 root 用户拥有最高权限, 那么它就可以对系统做任何动作, 包括你们可能早有耳闻的 `rm -rf /*` 命令. 因此, 你应该小心地使用 root 用户, 尤其是在重要的系统目录和文件上. root 用户的用户文件夹在 `/root` 下.

> 有人为了图方便, 就不创建普通用户, 平常就用 root 用户进行操作, 这样是非常危险的, 因为你不能保证你任何时候都不会失误. 而且有的命令反而要求不能以 root 身份运行.

#### 系统用户

除了你, root 用户, 还有很多系统用户. 它们一般是由系统或者相关程序创建, 用于执行服务等系统任务. 例如当你安装了 `ollama` 后, 它将自动创建一个名为 `ollama` 的用户和用户组, 用来管理 `ollama` 程序的运行. 不要随意删除这些用户, 以免系统运行出现问题.

#### 普通用户

就是你, 平时我们使用的普通用户.

#### 用户组

可以将用户分组, 以便管理. 使用 `groups` 命令, 即可查看自己所属的用户组. 一个典型的例子是 `docker` 用户组. 当你安装好 `docker` 后, 它会自动创建一个名为 `docker` 的用户组, 而一般情况下你不在这个组里, 所以你必须使用 `sudo` 才能运行 `docker` 命令. 而你可以把自己加入 `docker` 用户组:

```shell
sudo usermod -aG docker $USER
```

这样你就可以在不使用 `sudo` 的情况下运行 `docker` 命令了.

## 在 Linux 上编程

或许你们已经习惯在 IDE 上写代码, 然后按一个按钮, 代码就能自动地跑起来的体验了. Visual Studio, Clion, PyCharm, IntelliJ IDEA 等 IDE 给你们在 Windows 下提供了非常舒服的开发体验, 因为 Windows 系统并不能在系统级为你们提供编译器和解释器, 所以需要 IDE 中集成开发环境来帮你编译和运行代码.

> 让我看看还有谁在用 DevC++

但你们在运行代码的时候是否心中有一些隐忧? 这个代码是怎么跑起来的? 我的开发是不是已经被局限在 IDE 中了? 离开了 IDE, 我还有什么办法能让我的代码跑起来呢?

有的兄弟, 有的.

Linux 下提供了系统级的编译器和解释器, 我们得以脱离 IDE 的温柔乡, 将 IDE 运行代码的环节拆开, 暴露在你的面前.

### 编辑器+编译器/解释器

我们可以粗略地将开发环节分成两部分: 在编辑器里编辑代码, 然后将编辑好的代码交由编译器或者解释器运行. 编辑器就是我们敲代码的地方, 而编译器/解释器则是将代码翻译成机器语言的工具.

在很久以前, 人们使用 IDE 而不是编辑器+编译器的一大理由是, 编辑器没有代码补全和语法高亮等实用功能, 而 IDE 则提供了这些功能. 但随着技术的发展, LSP (Language Server Protocol) 横空出世, 使得编辑器可以和编译器/解释器沟通, 获得更好的代码补全和语法高亮等功能.

一个好消息是, VSCode 自带了 LSP, 你可以非常方便地在 VSCode 上体验到强大的语法高亮和代码补全功能.

接下来我将以 C/C++ 和 Python 为例, 讲解如何在 Linux 上搭建开发环境.

### C/C++

所有的 Linux 发行版都自带了 GCC (GNU Compiler Collection) 编译器. 你可以通过如下命令来检查你的 gcc 编译器:

```shell
gcc --version
```

接下来我们创建一个文件夹, 在里面新建一个 `hello.cpp` 文件:

```shell
mkdir cpp
cd cpp
touch hello.cpp
```

编辑 `hello.cpp` 文件, 输入以下代码:

```cpp
#include <iostream>

int main() 
{
    std::cout << "Hello, world!" << std::endl;
    return 0;
}
```

然后, 在命令行中运行如下命令:

```shell
gcc hello.cpp -o hello
./hello
```

你应该会看到屏幕上输出 `Hello, world!`.

#### 构建工具

上面是一个非常简单的示例, 只涉及到单文件编译和运行. 实际开发中, 我们面对的情况比这个复杂得多. 我自己常用的构建工具是 CMake, 它可以自动地生成 Makefile, 并根据你的代码生成对应的可执行文件.

至于 CMake 和 Makefile 的教程, 这里就不展开了, 你们可以自行搜索入门.

> 我在讲 Linux 下使用 VSCode 的时候提到过 CMake 的入门教程

### Python

Linux 下也自带 Python 解释器, 你可以通过如下命令来检查你的 Python 版本:

```shell
python --version
```

运行 Python 代码就更简单了:

```python
# hello.py
print("Hello, world!")
```

```shell
python hello.py
```

#### pip

pip 是 Python 的包管理工具, 你可以用它来安装第三方库:

```shell
pip install numpy
pip install --upgrade pip # 升级 pip
```

#### 依赖管理

如果你的项目有很多的依赖包, 手动一个一个一个地敲 `pip install` 命令显然不现实. 这时, 你可以使用 `requirements.txt` 文件来管理依赖:

```txt
numpy
matplotlib
torch
```

在这个依赖文件中, 每个依赖项都单独占一行. 然后, 你可以运行如下命令来安装所有依赖:

```shell
pip install -r requirements.txt
```

#### 虚拟环境

一般地, 你应该会发现你无法在全局环境下使用 `pip` 安装依赖包, 这时因为 PEP 668 规定了, 全局环境不能用 `pip` 来安装依赖包, 以免全局环境被各种不同的依赖项弄得乱七八糟. 想要往全局 Python 中安装依赖包, 需要从系统的包管理器中找到对应的包. 例如 `numpy` 对应的在包管理器中的名称是 `python-numpy`, 而 `pip` 则是 `python-pip`.

想要用 `pip` 安装依赖包, 并且保持你的 Python 环境干净整洁, 你可以使用虚拟环境来隔离不同的项目依赖. 要创建一个虚拟环境, 可以通过 Python 内置的模块:

```shell
python -m venv .venv
```

这会在当前目录中创建一个名为 `.venv` 的目录, 这个目录中存放着你刚刚创建的虚拟环境. 想要进入这个虚拟环境, 只需要:

```shell
source .venv/bin/activate
```

这时, 你应该会看到命令行提示符变成了 `(venv)` 这样的形式, 表明你已经进入了虚拟环境. 退出虚拟环境, 你只需要运行:

```shell
deactivate
```

在虚拟环境下, 你可以任意地安装依赖, 而不用担心把全局的默认环境搞乱. 要是一不小心你把虚拟环境弄脏了, 没关系, 直接删掉重建一个就好了!

```admonish
一般建议对每个项目, 都在项目根目录下创建一个虚拟环境, 这样可以避免不同项目之间依赖的冲突.
```

#### Python 版本

一般地, 系统中都会默认提供一个 Python, 比如 Arch 总是会给你提供最新版的 Python. 可是如果我有一个项目, 必须要老版本的 Python 怎么办?

这时候就体现出 Arch 的优越来了, 你可以在 AUR 中直接搜索老版本的 Python, 并直接安装:

```shell
yay python 3.10
```

这样, 你的系统中就有了老版本的 Python 了. 要使用老版本创建虚拟环境, 和正常创建差不多:

```shell
python3.10 -m venv .venv310
```

> 当然你要是不嫌麻烦的话可以装其他的虚拟环境管理工具, 里面通常会提供 Python 版本切换的功能. 但我非常不喜欢这样, 因为通过系统包管理器和 Python 自带的功能就可以实现的要求, 为什么还要引入额外的软件去做呢? 更何况诸如 anaconda 之类的东西体积太大了.

## 美化 Linux

我并不打算在这里教你如何美化你的 Linux, 因为这是一个非常复杂的主题, 而且每个人都有自己的审美观. 如果你不知道从何下手, 可以先在网上搜一搜别人的配置.

我加上这一节的目的仅在于告诉你, Linux 的界面绝对不是像你刚刚接触的那样简陋 -- 那只是个毛坯房 -- 你要用自己的双手将你的 Linux ~~调教~~美化成你的形状. 相信我, 配置美化的过程和结果一样令人着迷.

------

以上就是 A Byte of Linux 的全部内容, 感谢你能读到这里. 你已经成功地迈出了走向 Linux 的第一步, 证明你是一个有勇气的探索者. Linux 就像是一个巨大的瑞士军刀, 不仅功能强大, 还能让你在使用过程中不断地发现惊喜.

我知道, 刚开始接触 Linux 的时候, 你会感到陌生, 感到不适应, 感到它高冷且难以亲近. 我当然知道, 因为我也是这样过来的. 但请你相信, 你已经跨过了最艰难的一步: 开始使用 Linux. 随着你使用 Linux 的时间越来越长, 你会逐渐地熟悉上 Linux, 熟悉命令行的操作逻辑, 熟悉各种开发工具, 熟悉那些看似复杂却强大无比的 shell 语言.

所以不要放弃, 慢慢来.

我希望你能继续保持这份对技术的好奇和热爱. Linux 不仅仅是一个操作系统, 它更是一扇通往无限可能的大门. 跨国巨企的服务器运行在 Linux 上, 技术前沿的科研团队使用 Linux 开发, 数以亿计的开发者们在 Linux 社区里分享自己的经验. 无论是编程, 数据科学, 还是系统管理, Linux 都是你最可靠的伙伴. 期待有一天, 你能用 Linux 完成一个你自己都为之骄傲的项目.

最后, 送给你一句 Unix 世界里的经典问候:

```text
Hello, world!
```

```text
Hello, Linux!
```

------

© 2025. ICS Team. All rights reserved.
