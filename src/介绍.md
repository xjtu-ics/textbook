# Markdown

### 代码块


```
```rust,editable
fn main() {
    println!("Hello, mdBook!");
}
```
你可以展示代码块，修改或运行它们：

```rust,editable
fn main() {
    println!("Hello, mdBook!");
}
```

计算斐波那契数列
```rust
fn fib(n: u32) -> u32 {
    match n {
        0 => 0,
        1 => 1,
        _ => fib(n - 1) + fib(n - 2),
    }
}

fn main() {
    for i in 0..10 {
        println!("fib({}) = {}", i, fib(i));
    }
}

```

- **[mdBook GitHub 仓库](https://github.com/rust-lang/mdBook)**
- **[mdBook 官方文档](https://rust-lang.github.io/mdBook/)**
### 以下翻译自[https://https://rust-lang.github.io/mdBook/format/markdown.html](https://https://rust-lang.github.io/mdBook/format/markdown.html/)

mdBook 的[解析器](https://github.com/raphlinus/pulldown-cmark)遵循 [CommonMark](https://commonmark.org/) 规范，并在下面描述了一些扩展。
你可以快速上手[教程](https://commonmark.org/help/tutorial/)，或者[尝试](https://spec.commonmark.org/dingus/)实时体验 CommonMark。完整的 Markdown 概述超出了本文档的范围，但下面是一些基础知识的高层次概述。想要更深入的体验，请查看 [Markdown 指南](https://www.markdownguide.org)。

## 文本和段落

文本的渲染相对可预测：

```markdown
这是一行文本。

这是一个新行。
```

将会按照你期望的样子显示：

这是一行文本。

这是一个新行。

## 标题

标题使用 `#` 标记，并应该单独占一行。更多的 `#` 表示更小的标题：

```
### 一个标题 

一些文本。

#### 一个更小的标题 

更多文本。
```

### 一个标题

一些文本。

#### 一个更小的标题

更多文本。

## 列表

列表可以是无序或有序的。有序列表将会自动排序：

```
* 牛奶
* 鸡蛋
* 黄油

1. 胡萝卜
1. 芹菜
1. 小萝卜
```

- 牛奶
- 鸡蛋
- 黄油

1. 胡萝卜
2. 芹菜
3. 小萝卜

## 链接

链接到 URL 或本地文件很简单：

```
markdownCopy code使用 [mdBook](https://github.com/rust-lang/mdBook)。 

阅读关于 [mdBook](mdbook.md) 的信息。

一个裸露的 url：<https://www.rust-lang.org>。
```

使用 [mdBook](https://github.com/rust-lang/mdBook)。


一个裸露的 url：[https://www.rust-lang.org](https://www.rust-lang.org/)。

------

以 `.md` 结尾的相对链接将被转换为 `.html` 扩展名。 建议尽可能使用 `.md` 链接。 当在 mdBook 之外查看 Markdown 文件时（例如在自动渲染 Markdown 的 GitHub 或 GitLab 上），这很有用。

链接到 `README.md` 将被转换为 `index.html`。 这样做是因为像 GitHub 这样的服务会自动渲染 README 文件，但网络服务器通常期望根文件被称为 `index.html`。

你可以用 `#` 片段链接到单独的标题。 例如，`mdbook.md#text-and-paragraphs` 将链接到上面的[文本和段落]部分。 ID 是通过转换标题创建的，比如转换为小写并用破折号替换空格。 你可以点击任何标题并查看浏览器中的 URL 以查看片段的样子。

## 图片

包含图片只是像在_链接_部分上面提到的那样包含它们的链接。以下 markdown 包含在与此文件同一级别的 `images` 目录中找到的 Rust logo SVG 图片：

```
![Rust Logo](images/rust-logo-blk.svg)
```

用 mdBook 构建时会产生以下 HTML：

```
htmlCopy code
<p><img src="images/rust-logo-blk.svg" alt="Rust Logo" /></p>
```

当然，会这样显示图片：

![Rust Logo](./images/rust-logo-blk.svg)

## 扩展

mdBook 除了标准 CommonMark 规范之外还有几个扩展。

### 删除线

通过在文本两侧各添加一个或两个波浪号字符，可以使文本呈现中间带有水平线的效果：

```
删除线文本的一个例子~~删除线文本~~。
```

这个例子将会渲染为：

> 删除线文本的一个例子~~删除线文本~~。

这遵循了 [GitHub 删除线扩展](https://github.github.com/gfm/#strikethrough-extension-)。

### 脚注

脚注在文本中生成一个小编号链接，点击时会将读者带到页面底部的脚注文本处。脚注标签类似于链接引用，前面带有脱字符。脚注文本像链接引用定义那样编写，文本跟在标签后面。例如：

```
这是一个脚注的例子[^note]。

[^note]: 这是脚注的文本，将在页面底部渲染。
```

这个例子将会渲染为：

> 这是一个脚注的例子。

脚注会根据编写脚注的顺序自动编号。

### 表格

表格可以使用竖线和破折号来绘制表格的行和列。这些将被转换为匹配形状的 HTML 表格。例如：

```
| 标题1  | 标题2  |
|-------|-------|
| abc   | def   |
```

这个例子将会类似于这样渲染：

| 标题1 | 标题2 |
| ----- | ----- |
| abc   | def   |

有关支持的确切语法的更多详细信息，请参阅 [GitHub 表格扩展](https://github.github.com/gfm/#tables-extension-) 规范。

### 任务列表

任务列表可用作已完成项目的检查列表。例如：

```
- [x] 完成任务
- [ ] 未完成任务
```

这将渲染为：

> -  完成任务
> -  未完成任务

有关更多详细信息，请参阅 [任务列表扩展](https://github.github.com/gfm/#task-list-items-extension-) 规范。

### 智能标点

某些 ASCII 标点序列将自动转换为的 Unicode 字符：

| ASCII 序列 | Unicode              |
| ---------- | -------------------- |
| `--`       | –                    |
| `---`      | —                    |
| `...`      | …                    |
| `"`        | “ 或 ”，取决于上下文 |
| `'`        | ‘ 或 ’，取决于上下文 |

所以，不需要手动输入那些 Unicode 字符！



### 标题属性

标题可以有自定义的 HTML ID 和类。这让你即使更改标题文本也可以保持相同的 ID，它还让你可以在标题中添加多个类。

示例：

```
# 示例标题 { #first .class1 .class2 }
```

这使得等级 1 标题包含内容“示例标题”，ID 为“first”，以及类“class1”和“class2”。请注意，属性应该用空格分隔。

有关更多信息，请参阅 [标题属性规范页面](https://github.com/raphlinus/pulldown-cmark/blob/master/pulldown-cmark/specs/heading_attrs.txt)。

