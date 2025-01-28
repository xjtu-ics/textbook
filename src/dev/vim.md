# VSCode? Vim!

半年前倒腾过很长时间的vim配置，后来转懒人族直接使用[lazynvim](https://www.lazyvim.org/)，最近geek瘾又犯了，想在[UCB给的服务器](https://cs61c.org/fa24/labs/lab00/#appendix)上使用曾经配置好的Vim

这段时间做lab，我刻意回避vscode这类“接地气”的文本编辑器，强制使用vim :)

## 配置文件

`~/.vimrc`文件内容，你可以直接在[我的仓库](https://github.com/root-hbx/Config-Vim-Neovim/blob/master/vimrc)复制：

## 如何配置

```lua
vim ~/.vimrc
```

复制上述文件内容，`:wq`保存退出。

然后再进入vim，输入`:PluginInstall`，等待插件安装完成即可（如有提醒直接按`Enter`即可）。

现在就可以直接使用了

## 常用指法

> 免责申明：下面的指法部分只适用于我的vimrc配置

???+ tips

    现在使用我的vimrc，你会发现有几个最方便的点：

    1. 可以用鼠标/触控板进行光标移动
    2. 复制/粘贴可以直接用鼠标, 且对复制全文进行了快捷键定义(`空格 + a`)
    3. 默认 tab 缩进是4

    其实已经失去了vim的灵魂了🤡

    像语法高亮/状态栏/搜索高亮之类的就不用说了...

## 基础操作

### Normal Mode

> 这一部分不会的话，......

__插入__

```lua
i -- enter insert mode and begin inserting or deleting text
a -- enter insert mode, one space after cursor position
<escape> -- enter normal mode
```

__保存退出__

```lua
<:q!> -- quit without writing
<:wq> -- write and quit
```

__移动__

```lua
<Up/Down/Left/Right> -- 方向键
```

```lua
number + <Up/Down/Left/Right> -- 向上/下/左/右移动几number格
```

__词单元__

```lua
<w> -- next word 
<b> -- beginning of word
<e> -- end of word
<0> (zero) -- move to beginning of line
<$> -- move to end of line
<^> -- first non-null part of the line
```

我已经将`<0>` and `<$>` 重定向成 `shift -` and `shift +`了, 很明显我的开箱即用教程已经最大程度地减轻需要记忆的负担 :)

```lua
<number w,b> -- eg: <4w> - moves forward 4 words
```

__跳转__

```lua
<G> -- go to end of file
<gg> -- go to beginning of file
```

```lua
<ctrl u> -- scroll up (half a page)
<ctrl d> -- scroll down (half a page)
```

__查找__

```lua
< /search_item > -- searches for all occurrences in the file
<n> -- jumps to the next occurrence
<N> -- jumps to the previous occurrence
```

__删除__

```lua
dd -- delete this line
cc -- delete this line and into `Insert` mode
```

__撤销和回退__

```lua
<u> -- undo edit
<ctrl r> -- redo edit
```

__复制和粘贴__

```lua
<yy> -- yanks(or copies) current line
<p> -- pastes copied item
y5<Right> -- 复制右边的5个字符

<space>a -- 复制全文进入系统粘贴板
```

__注释/解注释__

我是用 [NerdCommenter](https://github.com/preservim/nerdcommenter) 做的

并且将快捷键全部改成了 `<shift> /`

- 行注释/解注释: 来到对应行, 使用 `<shift> /`即可
- 段注释: `V`进入visual模式，选中所需区域，使用 `<shift> /`即可

__分屏__

> s + 方向键

```lua
s <Right> -- 向右分屏
s <Left> -- 向左分屏
s <Up> -- 向上分屏
s <Down> -- 向下分屏
```

__分屏时切换光标的区域__

> q + 方向键

```lua
q <Right> <C-w>l
q <Left>  <C-w>h
q <Up>    <C-w>k
q <Down>  <C-w>j
```

__在vim打开的file中执行终端命令__

```lua
:!<command> -- eg: :!ls 就会在终端中执行命令
```

### Visual Mode

```lua
<V> -- enter multi-lined visual line mode
<v> -- enter single-lined visual mode
```

Actions:

```lua
<y> -- copy current item
<d> -- delete current item -> automatically goes to clipboard, so you can <p> to paste it
<escape> -- go back to normal mode
```

## 彩蛋

__显示文件系统结构__

```lua
ff -- 按下ff就会自动显示文件系统结构，鼠标点击即可打开细节
```

__代码分层显示__

```lua
T -- 按下 shift + t 会显示代码中的Tag，分好层级
```

显示效果应该如下：

![alt text](./image/vim-0.png)

__一些别的指法__

重新开一个iterm2窗口(左右分屏)

```lua
<cmd + d> -- 水平分屏
```

重新开一个iterm2窗口(上下分屏)

```lua
<cmd + shift + d> -- 垂直分屏
```

下面是一些mac常用的指法：

```sh
<control> + <d> 退出（logout），常用于服务器/虚拟机退出
<control> + <l> 等价于清屏命令clear
<control> + <c> 暂停，programmer都知道
```



------

© 2025. ICS Team. All rights reserved.