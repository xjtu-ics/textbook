# SSH

现在是5202年，你在无数学长学姐的安利下选择了《计算机系统导论》，并被告知这门课有可能是你在沙坡村学院能够上到的最有用的课。

在被沙坡村学院折磨了许久之后，你像抓住了救命稻草一般，准备再度踏上计算机学习的正轨... 📚 💪

突然，你的手机震动一下，打开一看是助教在ICS课程群里发送了消息：

“...我们为大家准备了服务器，并创建了账号密码，需要使用服务器的同学请SSH到服务器上...”

然而，你没有听说过SSH，也不知道它如何使用，只是盯着自己电脑上的Dev C++发呆，🤔 😭

“算了，先开一把瓦吧”，你对自己说到... 😆

这篇文章，我们将手把手教你如何使用SSH，常见的SSH使用场景，如何编写SSH配置文件...

此外，我们还会介绍SSH的底层工作原理，供对底层感兴趣的同学进行学习 🎉

当然，笔者不过是比你们多上了两年学的学长/学姐，对于SSH的理解难免出现偏差 ⚠️ 或错误 ☠️  ，欢迎各位同学批评指正 🌹

## 什么是SSH？

SSH(Secure Shell)是一个**应用层协议**，旨在在不安全的网络上提供安全的远程访问和网络服务。

在SSH出现之前，一般是使用Telnet和FTP等进行远程登陆和文件传输。

然而这些传输方式均采用**明文**进行传输，相当于直接公开自己传输的信息，十分不安全。

SSH使用**加密技术**在两台通信主机之间建立了一个安全的通信信道，因此更加适合现代网络环境。

<img src="./image/ssh-0.png" alt="ssh overview" width="100%" />

```admonish   
**明文**和**密文**是密码学中的两种术语。  
假设两台主机之间需要传递的内容称为信息，则明文指没有任何修饰的（例如加密）原始信息，密文则指使用加密技术进行加密之后的信息。
```

```admonish  
SSH一般指协议标准，而我们日常用的SSH工具一般是OpenSSH，这是SSH协议的开源实现。
```

## SSH的常见使用场景

一般而言，SSH主要有下面几种应用场景：
- 远程登陆
- 安全文件传输
- 端口转发

### SSH登陆远程服务器

SSH远程登陆类似于Windows系统上的远程桌面，不过不同的是，没有桌面环境，只有一个命令行终端。

使用SSH登陆服务器之后，你可以像在本地使用终端一样来操作服务器，这在网络管理和远程开发中十分常见。

由于笔者使用的是物理机Arch Linux，因此下面主要以Linux系统为例介绍命令。

```admonish
本文后续统一将自己本地的主机称为客户端，将远程主机称作服务器。无特殊说明时，客户端和服务器均为Linux系统。
```

#### For Linux

SSH的登陆验证方式主要有**用户密码**验证和**密钥验证**两种

##### 用户密码登陆

用户密码登陆是常见的身份验证方式，一般使用以下的命令格式：

```bash
ssh user@host [-p port]
```

详细解释一下上述命令：
- `ssh`：表示使用`ssh`命令
- `user`：表示需要远程登陆的主机上的用户名，如果用户名和本地用户名相同，则这一部分可以省略
- `host`：表示要登陆的主机名，可以是主机的域名，也可以是主机的IP地址（公网IP或者局域网内私有IP）
- `-p port`：可选，用于指定端口，默认端口为22，如果SSH服务器监听默认端口，则可以省略这一部分

输入上述命令之后，如果没有问题，终端会提示让你输入密码（首次登陆密码一般会告知你，或者按照自己重新设置的密码），

```admonish
输入密码的时候，终端不会有任何显示，不会显示密码原文或是*，防止别人窃取密码内容或密码长度。
```

正确输入密码之后，终端上如果输出一堆系统信息，然后打印出远程主机的终端提示符，则说明我们成功登陆了 🎉

````admonish tip
首次登陆时终端会显示类似这样的一段话（例如ssh首次登陆github）：  
```text
The authenticity of host '[ssh.github.com]:443 (<no hostip for proxy command>)' can't be established.  
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.  
This key is not known by any other names.  
Are you sure you want to continue connecting (yes/no/[fingerprint])?  
```
这段话的目的就是告诉你，客户端知道了这台服务器的公钥的fingerprint，但是无法验证服务器的身份，主要是用于防止中间人攻击。  
你需要输入`yes`，`no`或者`fingerprint`来跳过验证直接连接，拒绝连接或者使用`fingerprint`来验证。  
大部分安全（相信我，没人会攻击你每月几块钱的云服务器的 :blush:）的情况下，可以直接输入`yes`。  
对于公开的服务器，比如Github，官方一般会提供`fingerprint`供用户验证，例如[Github SSH Key fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints) 。   
输入fingerprint并按下回车，这时终端会提示：  
```text
Please type 'yes', 'no' or the fingerprint:
```
此时输入官方提供的fingerprint，如果验证通过，则终端会提示：  
```text
Warning: Permanently added '[ssh.github.com]:443' (ED25519) to the list of known hosts.
```
表示这台服务器通过了认证，并且会永久添加到`known_hosts`，这是`~/.ssh/`目录下的一个文件。  
这个文件中记录了所有通过认证的服务器，当下次连接服务器时，若服务器在`known_hosts`中出现，则会将服务器公钥的fingerprint和这个文件中记录的fingerprint比较，若匹配成功则连接继续，否则会发出警告，提醒你服务器fingerprint改变，需要用户自己确认服务器身份。
````

```admonish tip
fingerprint指公钥的**数字指纹**，由服务器公钥通过特定哈希算法（如SHA256）生成，这样长度比较短小，方便比较。  
对于公开的大型服务器，如Github等，一般会给出自己服务器公钥的fingerprint，用于用户验证服务器身份。  
如果是自己的公网服务器，可以登陆上服务器查看公钥fingerprint，服务器公钥一般位于`/etc/ssh/`目录下，命名为`ssh_host_xxx_key.pub`，xxx是算法类型，比如使用rsa算法生成的公钥文件就是`ssh_host_rsa_key.pub`。  
服务器在第一次安装ssh服务器时会生成这些文件，使用命令`ssh-keygen -lf /etc/ssh/ssh_host_rsa_key.pub`
可以查看公钥的fingerprint。
```

```admonish danger  
用户密码登陆方式存在安全性问题，尽管用户密码会通过加密传输，如果用户设置的密码比较简单（尤其是root用户的密码），很容易被黑客通过暴力破解出来，因此十分建议配置ssh文件，使用密钥进行登陆，这样不仅提高了安全性，每次登陆时也不用输入密码，实现免密登陆。  
如果需要将服务器部署在公网，通过建议在第一次登陆之后就**禁用密码登陆**或者**限制尝试次数**，以及**修改ssh默认端口**等一系列复杂的操作来确保安全。
```

```admonish tip
登陆之前确保在远程服务器上已经安装了ssh服务器，通常是openssh-server，如果没有安装的话根据自己的linux发行版google如何安装吧，这里就不展开讲了。
```

```admonish tip
如果出现了`Permission denied (publickey).`，通常是远程服务器**禁用**了密码登陆服务器，这时候必须使用密钥验证进行登陆。  
  
如果你可以操作远程主机打开密码登陆，则修改ssh服务器的配置文件`/etc/ssh/sshd_config`，找到`PasswordAuthentication no`这一行，将其注释掉，然后使用`sudo systemctl restart ssh`重启ssh服务。
```

```admonish example
这里给出一个登陆的例子，假设我的本地主机和远程主机在同一个局域网内，远程主机ip为192.168.110.242，假如不知道远程主机ip的话，可以在远程主机上使用`ifconfig`命令查看。  

现在远程主机创建了一个用户叫做ttang，接着输入ssh命令进行连接，出现以下内容：  

<img src="./image/ssh-25.png" alt="vscode remote" width="80%" />

上述欢迎界面说明登陆成功。  

如果是公网服务器等，将远程ip换成对应的公网ip或者域名，如不知道，请联系相应的服务器管理员。
```

##### 密钥登陆

前面提到，用户密码登陆的方式并不安全，因此更加建议使用密钥进行身份验证。同时，这种方式也无需每次都输入密码，使用起来更加方便。

首先我们需要在本地创建一对公钥和私钥，可以使用下面这条命令进行创建：

```bash
ssh-keygen
```

这条命令默认使用ED25519算法生成长度为256位的密钥对

```admonish
OpenSSH较新的版本已经将默认的rsa密钥生成算法改成了ed25519，这时更加现代的做法，兼顾了安全性和效率。
```

一些常用可选项：
- `[-t rsa | dsa | ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa]`：指定加密算法，不同加密算法复杂性和安全性也不同
- `[-b bits]`指定密钥长度，有些加密算法，如rsa，密钥长度是可以变化的

```admonish
对于 RSA 算法, 常见的长度是 2048, 3072, 4096. 一般推荐 3072 长度, 是安全性和性能的最佳平衡，4096 长度的密钥能提供最高的安全性, 但是加解密的时间会显著增加。不过在现代计算机上, 椭圆加密的 ed25519 是更好的选择, 因为它兼顾了安全性和性能.
```

输入以下命令了解更多：
```bash
ssh-keygen --help
```

输入上述命令之后，不出意外的话，会提示指定密钥存放路径，默认为`～/.ssh/id_rsa`（如果使用rsa算法），若你不想指定其他路径的话，直接按回车即可。

接着会提示你输入密码和确认密码，这个密码是每次使用密钥需要输入的，如果不想设置密码，直接按两次回车即可。

于是我们的ssh密钥对就生成好了 💪

通过`ls`查看`～/.ssh`目录或者你自己指定的存放目录

```bash
ls /your/path/to/ssh/keypair
```

目录下会存在两个文件`keypair.pub`和`keypair`，其中**keypair**是你自己指定的文件名，或者使用特定算法生成的默认名，例如`id_rsa`，带有`pub`后缀的是公钥，不带后缀的是私钥。

```admonish danger
注意私钥一定不要透露给任何人，否则加密就失效了
```

然后我们需要将公钥复制到服务器上，这可以使用以下命令：

```bash
ssh_copy_id [-i /your/path/to/ssh/keypair.pub] user@host
```

上述命令`-i`选项指定公钥文件目录，如果你没有自己指定密钥名，则可以省略这个选项

拷贝成功之后，就可以免密登陆啦 🎉

```bash
ssh user@host [-i /your/path/to/ssh/keypair]
```

如果你不是默认路径，使用`-i`选项指定路径即可

```admonish example
接着上面的例子，首先在本地生成ssh密钥对：  

<img src="./image/ssh-29.png" alt="vscode remote" width="80%" />

查看一下生成的公钥：  

<img src="./image/ssh-30.png" alt="vscode remote" width="80%" />

将公钥复制到服务器上：  

<img src="./image/ssh-26.png" alt="vscode remote" width="80%" />

使用ssh进行免密登陆：  

<img src="./image/ssh-27.png" alt="vscode remote" width="80%" />

```

##### 配置config文件快速登陆

尽管使用公钥登陆的方式免去了密码，但是每次登陆还是需要输入很长一串东西，太繁琐

作为计算机专业的同学，当然是要学会编写各种配置简化使用，下面我们介绍如何配置ssh以更高效的使用

ssh的配置文件位于`~/.ssh/config`，如果没有就创建一个，使用编辑器（推荐`vim/neovim`，毕竟是神之编辑器）打开这个文件，然后输入以下内容（具体内容替换成自己的）

```text
Host hostname
    HostName host
    User user
    Port port
    IdentifyFile /your/path/to/ssh/keypair
```

详细解释一下上述的每个字段：
- `Host`：给你自己要连接的服务器随便起个名
- `HostName`：这里host填入实际服务器的域名，或者公网IP，或者局域网内的私有IP
- `User`：填入自己服务器上的用户名
- `Port`：SSH服务器监听的端口，默认为22，如果SSH服务器监听22，可以去掉这一行
- `IdentifyFile`填入自己的私钥文件的地址

全部配置完成之后，输入以下命令：

```bash
ssh hostname
```

即可成功登陆，是不是简单了很多呢

````admonish example
编写ssh配置文件如下：  

```text
Host myhost
    HostName 192.168.110.242
    User ttang
    #IdentityFile "~/.ssh/id_rsa"
```

直接使用myhost进行登陆：  

<img src="./image/ssh-28.png" alt="vscode remote" width="80%" />

````

#### For MacOS

MacOS系统的步骤和Linux完全相同，这里就不再赘述了。

#### For Windows

### SCP安全传输文件

在两台主机之间**安全**的传输文件一般有scp和sftp两种方式，不过笔者没太用过sftp，对其不太熟悉，因此主要介绍一下scp。

scp类似cp，不同的是scp可以在两台联网主机之间进行文件传输，并且**基于ssh进行加密传输**。

scp的用法包括：
- **在本地和远程主机之间文件传输**：文件可以从远程主机下载到本地，或者从本地上传到远程主机
- **传输文件夹**：scp支持使用 -r 参数复制整个目录
- **两台远程主机之间进行传输**：scp可以直接指定两台远程主机之间进行文件传输，而无需先下载到本地。

scp针对上述用法有不同的命令，不过结构上都很相似。

将本地文件上传至远程主机时：

```bash
scp [-P port] [-i /path/to/your/key] /local/file/path [-r] user@host:/remote/file/path 
```

其中：
- **[-P]**指定端口，默认端口22，注意**P要大写**
- **[-i]**指定私钥文件路径，如果需要使用密钥验证的话，否则将使用默认私钥路径或者密码验证
- **[-r]**如果目标文件是目录则需要指定

注意远程路径格式为**主机名:远程主机的路径名**。

先出现的路径是**源路径**，后出现的是**目的路径**。

因此，从远程服务器下载时：

```bash
scp [-P port] [-i /path/to/your/key] user@host:/remote/file/path /local/file/path
```

在两台远程主机之间传输时：

```bash
scp [-P port] [-i /path/to/your/key] user1@host1:/remote/file/path user2@host2:/remote/file/path 
```

```admonish
如果你使用了ssh配置文件，那么上述的主机名均可直接替换成你在配置文件中指定的**Host**名，也不再需要输入密码或者是指定私钥路径等，这也是推荐的做法。
```

## SSH的工作流程和原理

这一部分详细讲解有关SSH协议的工作流程。

```admonish warning
这部分涉及到有关**操作系统**，**计算机网络**，**密码学**等相关知识，如果不熟悉这部分知识理解起来会有难度。  
如果你只是希望了解ssh的有关应用，直接跳过这一节即可。
```

### SSH Overview

<img src="./image/ssh-1.png" alt="ssh protocol arch" width="100%" />

SSH协议结构如上如所示，主要分为以下几个部分：
- **传输层协议**： SSH传输层协议主要确保**服务器身份验证**，**数据加密**和**数据完整性**。注意这个传输层协议应该和OSI标准的7层网络协议栈中定义的传输层协议区分开，SSH传输层协议直接运行在TCP/IP协议栈之上，通常基于TCP进行可靠数据传输，默认端口22。
- **用户身份认证协议**： 这个协议用于验证用户身份，最常见的两种方式为**用户密码验证**和**公钥认证**，或是二者结合的方式。
- **连接协议**： 连接协议**多路复用**了单个ssh客户端-服务器组成的ssh通道。换句话说，这个协议创建不同的数据流和多个逻辑通道。

<img src="./image/ssh-2.png" alt="ssh connection" width="80%" />

SSH协议基于**客户端-服务器（C/S）**模型，其通常使用TCP协议作为传输层协议，使用TCP时，默认监听22端口。SSH最终使用密钥对用户传输的数据进行**加密传输**，因此实现了在不安全的网络上进行安全传输，SSH从建立连接到数据加密传输的流程大致如上图，主要有以下几个阶段：
- **连接建立**： 客户端首先发起TCP连接，经过三次握手之后，TCP连接成功建立。之后客户端服务器互相协商可用的SSH版本。
- **密钥交换**： 这一部分主要任务是**协商加密算法**（对称/非对称加密，哈希），然后通过**密钥交换算法**生成用于加密信息的会话密钥，这一阶段同时还包含了**服务器端的身份认证**，以防止**中间人攻击**。
- **用户身份认证**： 这一阶段用于验证**客户端身份信息**，也就是前面提到的登陆阶段。
- **信息加密传输**： 这一阶段连接双方的身份信息均已验证，后续的数据传输均采用之前生成的会话密钥进行加密解密。

```admonish
**协议**是计算机网络中的一个重要概念，其规定了通信双方进行数据交换时应该遵守的一组规则。  
**协议栈**则是计算机网络中一系列协议的集合，不同协议位于不同层次，旨在解决不同层次上的问题，低层次的协议为高层次提供服务。  
两大经典协议栈是**OSI模型**和**TCP/IP模型**：  
OSI模型分为了7层，分别是应用层，表示层，会话层，传输层，网络层，数据链路层和物理层。  
TCP/IP模型分为了4层，分别是应用层，传输层，网际层和网络接口层。  
在一般的计算机网络教学中，为了方便，一般分为应用层，传输层，网络层，数据链路层和物理层。  
```

```admonish
TCP协议是**传输层**中的一个重要协议，其为应用层提供了**可靠数据传输服务**，即应用层可以确信TCP会将数据**按序，不丢包**的发送给对端，常用于需要数据可靠传输的应用层协议（如电子邮件，文件传输）中，但时延较高。  
与之相对的是UDP协议，UDP不保证数据可靠传输，因此性能好，常用于需要保证低时延等高性能场景，如流媒体，音视频流等。
```

```admonish
**进程**是操作系统中的一个重要抽象，简单来说，进程可以看作一个**运行中的程序**。以C语言为例，编译系统会将一个或多个C源程序编译链接成一个可执行程序，到目前为止，这个可执行程序仍然驻留在磁盘上，本质上是**静态的一堆机器指令的集合**。当运行这个可执行程序时，加载器在内核中会创建一个进程，将代码正确映射到进程的地址空间中，设置好各个寄存器，最后CPU开始运行，此时**程序从磁盘被加载到了内存**。  
一个进程可以看作一个容器，管理了很多资源，包括寄存器，地址空间以及各种信息，通常叫做**进程上下文**。进程中执行代码的部分可以看作一个执行流，通常叫做**线程**，一个进程可以包括一个或多个线程。  
简单概括，进程更加注重**资源管理**，线程则聚焦于**命令执行**，可以直接被CPU进行调度，因此线程更加轻量。
```

```admonish
**客户端-服务器**模型是主流的通信模型，其余通信模型包括P2P（Peer to Peer）等。客户端和服务器都可以视为运行在主机上的一个进程。其通过网络进行通信，这是一种常见的**进程间通信**方式。在客户端-服务器模型中，客户端作为主动发起连接的一方，而服务器被动
接受来自客户端的连接。
```

```admonish
计算机网络中，用于标记一个主机的身份通常需要**IP地址**和**端口**，更准确的说，IP地址用于识别主机，是网络层中的概念。端口号用于识别主机上运行的不同进程，是传输层的概念。例如，同一台主机上可能既运行了HTTP服务器，监听80端口，也可能同时运行了ssh服务器，监听22端口，他们共享内核中实现的TCP模块，TCP模块接受一个数据包时，根据端口号将数据包分发给不同的进程。
```

```admonish
密码学中加密方式主要有**对称加密**，**非对称加密**和**哈希**三种，三种加密方式分别应用于不同的情况。  

<img src="./image/ssh-7.png" alt="symmetric encryption" width="90%" />

**对称加密**又叫做**共享密钥加密**，其基本特征是，发送方和接收方均采用同一个密钥对数据进行加密和解密，就像用同一把钥匙上锁和开锁一样。这种加密方式简单且高效，但是共享密钥的保管是个问题，因为一旦存在第三者得到了共享密钥，其就能对加密内容进行解密，安全性就荡然无存。因此，若需要在网络中传递共享密钥，需要**对共享密钥进行加密**。  

<img src="./image/ssh-8.png" alt="symmetric encryption" width="90%" />

**非对称加密**使用**一对密钥**进行加密和解密，而不是单个密钥。发送方生成一对密钥，分别叫做**公钥**和**私钥**，其中公钥可以安全的公开，私钥则只能自己知道，并且任何人**不能从公钥轻易的推出私钥**。非对称加密拥有的一个重要性质是：**公钥加密的内容只能由私钥进行解密，反之，私钥加密的内容只能由公钥进行解密**。二者分别应用于不同场景，对于信息加密传输的场景，需要采用公钥加密私钥解密的方式，因为公钥是公开的，若使用私钥加密则任何人都可以使用公钥解密，加密就失效了。而私钥加密公钥解密通常应用于身份验证，比如**数字签名**。  

<img src="./image/ssh-9.png" alt="symmetric encryption" width="70%" />
 
**哈希**是另外一种加密方式，哈希加密通常以消息作为输入，并且对于不同的输入可以生成**唯一且定长**的哈希内容，又叫做消息的**摘要**，且哈希算法必须保证**无法从哈希值推出原始信息内容**。哈希加密与上述两种加密不同的是其**不需要解密**，因此是单向的，通常用于验证**数据完整性**，确保数据没有被篡改，比如MAC等。通信的双方只需要知道原始信息和使用的哈希算法就能够验证哈希值是否相同。  
  
SSH加密技术经常混合使用上述三种方式。比如，非对称加密用于生成会话密钥，而会话密钥是对称加密，负责后续所有数据传输的加密。哈希加密用于确保数据完整性，在会话密钥生成之后，数据传输还需要附上由<会话密钥，数据包ID，实际信息内容>由MAC算法生成的摘要。
```

```admonish
**数字签名**在密码学中用于验证身份信息，发送方可以将需要发送的信息以及附加信息进行哈希生成，然后使用自己的私钥对此摘要进行加密，然后将签名附在原有信息后面进行传输，这样任何拥有发送方公钥的用户可以解密这个签名，由于能够进行加密和解密的公钥和私钥是配对的，而发送方私钥不公开，因此接收方可以证明数据真实来源与发送方。这样做的效果就像你在合同上签名，然后对方通过签名可以判断合同是你签的。  
  
尽管数字签名可以验证身份，但是其会受到中间人攻击的影响，假如黑客窃取了原有的数据包，然后用发送方的公钥进行了解密得到原始信息，之后使用自己的私钥将信息加密，再发送自己的公钥。这样接收方同样可以解密，但是发送方的身份就无法得到验证。为了应对这种攻击，需要**对发送方的公钥也进行验证**，这通常通过CA（Certificate Authority）完成，即发送方的公钥必须得到CA的验证，具体方式为，CA使用自己的私钥将发送方的公钥以及附加信息进行签名，接收方使用CA的公钥进行解密，得到发送方公钥，在使用这个公钥对发送方签名进行解密，从而进行验证。由于CA的公钥一般不可能作假，因此使用这种方式只要信息被中间人窃听并篡改，接受方就能立刻验证失败。这就好比有人仿照你的字迹进行签名，而你在签名边上再附上一位权威人士的签名，证明你的签名是真的。
```

### 服务器身份认证

<img src="./image/ssh-3.png" alt="server auth" width="80%" />

在SSH建立连接之后，客户端需要验证服务器的身份，以防止**中间人攻击**。在这个阶段，服务器会将自己的公钥（通常位于`/etc/ssh/`）目录下，发送给客户端，客户端接收公钥并计算其指纹。如果客户端保存了服务器的公钥指纹（在`~/.ssh/known_hosts`文件中存在），则会进行比对，若比对成功则连接继续，否则警告用户指纹不匹配，需要用户自己确认身份。这也就是为什么第一次连接时会发出警告，告诉用户需要自己验证服务器的指纹，因为SSH服务器使用的公钥没办法通过CA进行认证，无法自动确认服务器的真假。

```admonish
**中间人攻击(Man In the Middle Attack)**是网络安全中的一中常见攻击方式，方式为存在第三者隐藏并且窃听通信双方的内容，充当代理转发的作用，从而窃取通信内容或者恶意篡改通信内容，而通信双方察觉不到这个中间人的存在。
```

### 算法协商

算法协商阶段，客户端和服务器各自生成自己支持的算法列表，然后双方根据列表选择大家都支持的算法，需要协商的算法包括**对称加密算法**，**非对称加密算法**和**哈希算法**等。SSH协议**混合使用**了各种加密算法，以享受不同加密算法在不同场景下的优势，比如对称加密使用简单快速，因此用于**会话密钥**，而非对称加密使用比较复杂，但安全性高，因此常用于生成会话密钥以及身份验证，而哈希算法通常用于生成短小的指纹或者消息的摘要等。当所有类型的算法全部协商完成之后，协商阶段结束，若任意一个阶段双方无法找到共同的算法，则协商阶段失败。

### 密钥交换

密钥交换指一类算法，其目的是**生成会话密钥**。在SSH中，会话密钥通常使用的是对称加密算法，因此需要保证客户端和服务器双方的会话密钥是一致的，常见的算法有DH，ECDH等。

```admonish example

<img src="./image/ssh-4.png" alt="dh algo" width="80%" />

经典的DH（Diffie-Hellman）密钥交换算法流程如下所示： 
1. 客户端和服务器约定好一个大素数p（几百位）和素数g（g通常比较小，且满足g < p），p和g可以安全公开
2. 客户端选择一个很大的自然数a作为私钥（满足a < p），并计算出客户端的公钥A = (g^a) mod p
3. 服务端选择一个很大的自然数b作为私钥（满足b < p），并计算出服务器的公钥B = (g^b) mod p
4. 双方各自公开并交换自己的公钥A和B
5. 客户端根据自己的私钥a，服务器公钥B和p计算会话密钥S = (B^a) mod p
6. 服务器根据自己的私钥b，客户端公钥A和p计算绘画密钥S = (A^b) mod p

DH算法核心基于**离散对数**，数学上可以证明客户端和服务器计算得到的会话密钥S是相同的。  
DH算法从根本上**移除了会话密钥在网络中传输**的步骤，而保证通信双方得到相同的会话密钥，因此大大提高了安全性。
```

### 用户身份验证

前面提到，用户身份验证阶段通常分为**用户密码登陆**和**密钥登陆**两种，这两种方式的验证机制并不相同，接下来分别解释两种验证方式。

#### 用户密码登陆

<img src="./image/ssh-5.png" alt="user password" width="80%" />

使用用户密码方式时，客户端发送登陆请求给服务器，告知服务器使用密码登陆的方式。接着用**会话密钥**将用户名，密码等信息进行加密，服务器端收到加密后的信息之后，用会话密钥进行解密得到用户名和密码，并且与本地存储的用户名密码信息比对，若匹配成功则向客户端报告登陆成功，否则客户端继续尝试登陆。

#### 密钥验证

<img src="./image/ssh-6.png" alt="public key" width="80%" />

使用密钥验证时，客户端发送登陆请求给服务器，告知服务器使用密钥验证的方式，并且会附上密钥对的ID。服务器受到信息后，根据ID查找本地保存客户端密钥的文件（通常是`~/.ssh/authorized_keys`）,如果发现了对应的客户端公钥，则服务器生成一个随机数，使用**客户端公钥**进行加密，并发送给客户端，客户端收到信息后，使用自己的私钥进行解密，解密之后得到相应的随机数，接着使用哈希算法（一般是MD5算法）通过这个字符串生成摘要，并发送给服务器。服务器收到客户端的摘要之后，自己也使用相同的哈希算法应用于生成的随机数，和客户端的摘要进行比较，若比较通过，则验证成功。否则客户端登陆失败并重试。

## 其他SSH使用场景

### vscode使用SSH进行远程开发

如果说vscode相比于其他一体化的IDE的优势，那么vscode强大的**远程开发**功能必然榜上有名。

远程开发可以**将本地环境和开发环境隔离**，避免了本地的开发环境配置问题（比如windows配置c++开发环境非常困难），同时解除了本地环境和开发环境的地理限制。

如果你手边没有Linux环境，那么我强烈建议你搭建一个Linux开发环境，尤其是使用windows的同学（macOS同学看个人喜好）。

一方面Linux相比windows，更加适用于搭建开发环境，另一方面，使用Linux环境可以不知不觉中强化自己对Linux命令的使用（你一点不会Linux？那么请移步这一篇 ）。

不过，在使用Linux的同时，我个人还是建议你手边准备一台windows**以备不时之需**（比如办公，游戏等，更重要的是**预防学校某些实验课要安装的臭不可闻的软件**）

Linux的环境一般有以下几种选择：
- 租一个云服务器（个人不推荐，但是如果你有强烈的公网环境需求或者算力需求或是学校或机构有丰富服务器资源，那么当我没说）
- Linux物理机（推荐，如果你觉得自己无法驾驭，那还是算了）
- Linux/windows双系统（都双系统了，还是一步到位物理机了吧）
- windows+linux虚拟机（推荐，但是更建议wsl）
- windows+wsl（推荐，毕竟曾经被称为最好的linux发行版）

如果你比较激进，而且喜欢折腾，或者手边不止一台电脑，那么直接安装linux物理机再好不过。

如果你有强烈的windows需求，而且只有一台电脑，那么我建议你使用windows+linux，linux可以使用windows下的虚拟机环境（vmware等），或者wsl2。

如果你决定选择使用vmware等虚拟机软件，那么我建议**不要安装linux的图形界面**，将linux作为一个命令行终端的接口来使用。

常用的方式是使用vscode远程开发功能连接自己的服务器或者虚拟机或者wsl。这样既保留了windows环境，又支持使用linux开发环境。

好了，让我们回归正题，如何使用vscode进行远程开发：

vscode远程开发基于ssh连接，ssh在本地vscode客户端和远程vscode服务器上建立了一条连接通道，这里借用[vscode docs](https://code.visualstudio.com/docs/remote/ssh)的图片来解释：

<img src="./image/ssh-14.png" alt="vscode remote" width="80%" />

vscode客户端就是本地下载安装的vscode，而vscode server是远程主机上的一个进程，当进行远程连接时，客户端会复用自己的一些主题插件，而服务器会自动下载安装一些开发环境相关的插件。

首先，你需要安装一个名为**Remote-SSH**的插件：

<img src="./image/ssh-15.png" alt="vscode remote" width="80%" />

安装完成之后，你的插件列表应该会出现了3个已安装的插件：

<img src="./image/ssh-16.png" alt="vscode remote" width="80%" />

第一个插件，Remote - SSH，帮助你连接到远程主机。

第二个插件，Remote - SSH: Editing Configuration Files，用于修改ssh配置文件

第三个插件，Remote Explorer，这个就很牛逼了，提供图形化界面用于访问远程主机的目录等，让用户感觉自就好像在本地开发一样。

现在你的左侧栏应该会出现一个远程主机的图标，点开他，在右侧会出现REMOTES的菜单栏，点开外层下拉框，里面会出现名为SSH的下拉框，继续点开SSH，即可呈现所有的远程主机列表，这是根据你的SSH配置文件决定的。

如果你发现你要连接的主机不再列表中，这时候需要添加远程主机，

将光标移到SSH那一栏，点击右边的+，这个是添加远程主机的选项，然后你的vscode界面上方应该会出现一个下拉框：

<img src="./image/ssh-17.png" alt="vscode remote" width="80%" />

这个输入框让你输入ssh的登陆命令，就像在命令行内进行登陆一样。

输入相关的ssh命令，这时候vscode会提示选择需要更新的ssh配置文件，选择自己用户目录下的那个文件（`/home/username/.ssh/config`），按下enter，然后vscode会提示host added!

<img src="./image/ssh-18.png" alt="vscode remote" width="80%" />

这时候打开ssh配置界面，发现vscode已经自动添加了主机的配置文件：

<img src="./image/ssh-22.png" alt="vscode remote" width="80%" />

当然，你可以将Host那一栏的ip地址换成自己喜欢的名字，比如myhost。

然后，在左侧的remote exploer里面会出现新的主机：

<img src="./image/ssh-23.png" alt="vscode remote" width="80%" />

将光标移到目标主机那一行上，右侧会出现 -> (在当前窗口内连接)和 + (新开一个窗口进行连接)，根据你的需求选择一个，

然后vscode会打开窗口，并且弹出一个框提示你输入密码，输入密码之后，vscode则开始连接。

```admonish
如果你自己的远程主机上没有安装vscode-server，那么远程连接时会自动安装，并且vscode会弹出如下提示：  
<img src="./image/ssh-19.png" alt="vscode remote" width="80%" />
```

连接成功后在新的窗口内会显示：

<img src="./image/ssh-20.png" alt="vscode remote" width="80%" />

观察左下角会显示**SSH: HOSTNAME**，说明当前已经处在远程环境中，在左上角工具栏中打开终端，会显示远程系统中的终端（即使你的本地环境是windows，远程主机是linux，那么就会使用你linux系统下的终端）。

点击左侧的文件图标（Explorer）将打开你的远程主机的工作目录，由于现在没有打开任何一个目录，因此会提示我们open a folder，

随便选择一个目录，比如用户的家目录，然后打开，远程窗口会变为：

<img src="./image/ssh-21.png" alt="vscode remote" width="80%" />

这样就和本地开发几乎一模一样了。

当然，vscode会帮我们记住上次打开的目录，这样下次连接就可以直接打开对于的远程目录了。

<img src="./image/ssh-24.png" alt="vscode remote" width="80%" />

上述方式连接每次都要输入密码，如果想改成使用密钥登陆，也非常简单，只需要将ssh关于远程主机的配置修改为：

```text
Host myhost
	HostName 192.168.110.242
	User ttang
	IdentityFile "~/.ssh/id_rsa"
```

注意将私钥路径改成自己的，这样就可以使用密钥进行登陆了。

```admonish warning
使用免密登陆之前一定确保将公钥正确的上传至远程主机，上传的方法见SSH密钥登陆那一节，如果没上传公钥，vscode还是会提示输入密码进行登陆。
```

### Github使用SSH

到了这个阶段，相信你已经接触过了github（什么？你没用过github，那么请移步[这一篇](./github.md)），且已经学会了科学上网（不知道什么是科学上网？那我没法教你了，自行搜索或者问同学吧，或者带杯奶茶来**面基**助教也是可以的）。

出于众所周知的原因，大量的境外网站我们是无法访问的，github作为一个例外（可以不挂梯子直接访问，但是由于DNS污染，以及最近网速肉眼可见的变慢，建议还是使用梯子访问），给我们提供了天然的中转地，因此这一部分教大家如何使用代理和ssh方式访问github。

Github作为全世界有名的~~同性交流网站~~代码托管平台，可以和git搭配使用从而进行十分方便的代码托管和版本控制。

这其中最重要的两个操作莫过于`git pull`和`git clone`以及`git `等。前者从github拉取代码或者下载完整副本，后者将本地仓库代码上传至github远程仓库。

github对于上述操作提供了两种访问方式，分别是**https**和**ssh**。比如，当我们需要clone一个仓库到本地时，点击仓库右上角的code，会分别提供https和ssh的链接

<img src="./image/ssh-10.png" alt="git clone" width="80%" />

将上述链接复制，然后输入：

```bash
git clone git@github.com:xjtu-ics/textbook.git 
```

即可复制远程仓库到本地，并且在本地自动关联远程仓库。

在不使用代理的情况下，实测发现使用https的成功率可以忽略不计，使用ssh的成功率则高很多（最近不知道什么原因，ssh的成功率也可以忽略不计）。当然，当你无法使用代理时，你也可以点击Download zip手动下载压缩包并解压。不过，既然能使用代理解决，何必多此一举呢。

下面我们教大家如何设置https的代理和ssh的代理，并且更推荐使用ssh。

假设你已经准备好了代理，不管用什么方式，首先记录下代理的端口，比如这是我笔记本上的：

<img src="./image/ssh-11.png" alt="git clone" width="80%" />

使用http协议的端口为20171，socks5协议端口为20170。

如果要使用https与github进行交互，那么代理几乎是必挂的，使用以下两条命令为git添加github的代理（更推荐使用socks5代理，如果使用http代理，则将代理url的协议名改成http）

```bash
git config --global http.https://github.com.proxy socks5://127.0.0.1:20170
git config --global https.https://github.com.proxy socks5://127.0.0.1:20170
```

上述方式**指定了为域名https://github.com设置代理**，其他域名的流量不走代理，因此是推荐的做法。

如果你嫌麻烦，那么设置全局代理也是可以的：

```bash
git config --global http.proxy socks5://127.0.0.1:20170
git config --global https.proxy socks5://127.0.0.1:20170
```

不过这种方式将git的**全部流量都从代理进行转发**，当你用git访问一些不需要挂代理的网站（比如gitee等），就需要关闭代理，特别麻烦，因此并不推荐这么做。

如果要取消设置，使用：

```bash
git config --global --unset http.https://github.com.proxy
git config --global --unset https.https://github.com.proxy
```

如果你设置的是全局代理，那么这样取消设置：

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

查看一下git的设置：

```bash
git config --list
```

如果包含类似下面两行，说明代理设置成功了：

```text
http.https://github.com.proxy=socks5://127.0.0.1:20170
https.https://github.com.proxy=socks5://127.0.0.1:20170
```

只要代理工作正常，基本上就可以使用https进行clone了，且速度还挺快的。

不过，使用https的方式，**每次和github交互都需要输入密码**，十分不方便且安全性也不高，因此更加建议使用ssh进行连接。

ssh的使用和ssh远程登陆的流程差不太多，首先在本地生成ssh密钥对，然后将公钥上传至github。

进入github官网 -> 右上角自己头像 -> 下拉菜单选择**设置** -> 左边栏选择**SSH and GPG keys** 进入SSH key管理页面：

<img src="./image/ssh-12.png" alt="git clone" width="80%" />

点击右上角**New SSH key**，随便输入一个title, 将自己本地的公钥内容复制到key里面（注意key的格式要求，不要复制少了！一般将`id_rsa.pub`文件的内容全部复制就行）：

<img src="./image/ssh-13.png" alt="git clone" width="80%" />

最后点击**Add SSH key**，退回到ssh key管理界面，就可以看到自己最新添加的公钥了。

接着修改SSH配置文件，加入下面的内容：

```text
Host github.com
    HostName github.com
    User git
    # using socks5 proxy
    ProxyCommand ncat --proxy 127.0.0.1:20170 --proxy-type socks5 %h %p
    # private key path(change it to your own path)
    IdentityFile "~/.ssh/id_rsa"
```

具体解释一下代理设置的那一行：
- `ProxyCommand`选项表示使用代理，SSH连接时会执行这个选项后面的命令
- `ncat`是一个命令行工具，具体根据自己的linux发行版进行安装，可以指定使用代理连接特定的服务器
- `--proxy`指定本地代理服务器，实际使用时**替换成自己的服务器地址，尤其是端口号**
- `--proxy-type`指定代理类型，可以使用http或者socks5
- `%h %p`是占位符，表示主机名和端口，实际连接时会自动替换成ssh的目标主机名和端口号

修改完成后，使用`ssh -T git@github.com`进行测试，如果出现类似以下结果，则表示ssh连接成功：

```text
Hi Scorpicathe! You've successfully authenticated, but GitHub does not provide shell access.
```

有些环境中，比如某些企业的内网会设置防火墙阻止ssh流量通过22端口进行转发，万幸的是，github提供了一种方式可以使用https端口，即443端口建立ssh连接。

首先测试443端口是否可行：

```bash
ssh -T -p 443 git@ssh.github.com
```

注意，443端口的github域名为`ssh.github.com`，使用时注意修改。

如果出现类似以下内容，说明端口有效：

```text
Hi Scorpicathe! You've successfully authenticated, but GitHub does not provide shell access.
```

否则的话，查阅[Github官方文档](https://docs.github.com/zh/authentication/troubleshooting-ssh/error-permission-denied-publickey)进行错误排查。

于是，当需要使用ssh的时候，将github的地址`github.com`改为`ssh.github.com`即可，比如：

```bash
git clone ssh://git@ssh.github.com:443/xjtu-ics/textbook.git 
```

不过每次clone时修改url显然是一件很烦的事，可以修改ssh配置文件来避免：

将配置文件改成以下内容：

```text
Host github.com
    HostName ssh.github.com
    Port 443
    User git
    # using socks5 proxy
    ProxyCommand ncat --proxy 127.0.0.1:20170 --proxy-type socks5 %h %p
    # private key path
    IdentityFile "~/.ssh/id_rsa"
```

这样设置强制ssh每次连接通过443端口来进行，因此可以绕过防火墙。

上述不过是ssh连接github的冰山一角，更多信息请咨询[GitHub Docs](https://docs.github.com/zh/authentication/connecting-to-github-with-ssh/about-ssh)

------

© 2025. ICS Team. All rights reserved.
