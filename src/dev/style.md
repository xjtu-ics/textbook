# Google Style Guide

你有没有过这样的经历: 打开自己三个月前写的代码, 拔剑四顾心茫然...

再来一个经典场景: 小组项目里, 你用 `camelCase`, 他用 `snake_case`, 她再把变量名直接 `a`, `b`, `c`, `temp1`, `temp2`... 最后合并代码的那个人直接原地起飞...

这就是为什么我们需要**代码风格指南 (Style Guide)**.

本文基于 [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html) 和 [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html), 挑选了最重要、最实用的规则, 帮你养成良好的编码习惯. 旨在帮助大家打好基础, 便于后续积极参与开源社区建设

Acknowledgements:

- [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [clang-format Documentation](https://clang.llvm.org/docs/ClangFormat.html)
- [Black: The Uncompromising Code Formatter](https://black.readthedocs.io/)

## 为什么要有代码风格?

先说一个扎心的事实:

> **代码被阅读的次数远远多于被编写的次数.** —— Google C++ Style Guide

你写一段代码可能花 10 分钟, 但之后你自己、你的队友、你的助教可能要反复阅读它很多次. 如果代码风格混乱, 每次阅读都是一场折磨.

**好的代码风格能带来什么?**

- **可读性**: 别人 (even 未来的你) 能快速理解你的代码
- **一致性**: 团队协作时, 大家的代码看起来像是一个人写的
- **减少 bug**: 清晰的代码更容易发现和修复错误
- **专业感**: 面试/实习时, 代码风格好会让面试官眼前一亮 ✨

Google Style Guide 是业界最广泛采用的代码风格指南之一. 我们将围绕这份指南展开, 本文面向零基础、编码经验不多的本科学生.

## C++ Style

### 命名规范

命名是代码风格中**最重要**的部分, 没有之一. 好的命名让代码自己会说话.

```cpp
// ❌ 看不懂系列
int a, b, c;
void f(int x);
class myclass;

// ✅ Google Style
int student_count;          // 变量: snake_case (下划线格式)
int num_errors;

void ComputeAverage();      // 函数: PascalCase (大驼峰格式)
void SendMessage();

class LinkedList;           // 类: PascalCase
class StudentRecord;

const int kMaxRetries = 3;  // 常量: k 开头 + PascalCase
const double kPi = 3.14159;
```

TLDR:

| 类型 | 风格 | 示例 |
|------|------|------|
| 变量 | `snake_case` | `student_count` |
| 函数 | `PascalCase` | `ComputeAverage()` |
| 类 | `PascalCase` | `LinkedList` |
| 常量 | `k` + `PascalCase` | `kMaxSize` |
| 命名空间 | `snake_case` | `my_project` |
| 类成员变量 | `snake_case_` (末尾下划线) | `table_name_` |

### 头文件

每个 `.cc` 文件通常对应一个 `.h` 头文件. 头文件需要用 **include guard** 防止重复包含:

```cpp
// file: my_project/student.h

#ifndef MY_PROJECT_STUDENT_H_    // include guard 开始
#define MY_PROJECT_STUDENT_H_

class Student {
 public:
    std::string GetName() const;
 private:
    std::string name_;
};

#endif  // MY_PROJECT_STUDENT_H_  // include guard 结束
```

`#include` 的顺序也有讲究, 按以下分组排列 (组与组之间空一行):

```cpp
// 1. 对应的头文件
#include "my_project/student.h"

// 2. C 系统头文件
#include <cstdio>

// 3. C++ 标准库
#include <string>
#include <vector>

// 4. 第三方库
#include "absl/strings/str_cat.h"

// 5. 本项目其他头文件
#include "my_project/util.h"
```

### 作用域

**变量声明尽量靠近它第一次被使用的地方**, 作用域越小越好:

```cpp
// ❌ 所有变量堆在函数开头 (C89 风格, 别这样)
void Process() {
    int i;
    int sum;
    std::string name;
    // ... 隔了 50 行才用到 name ...
}

// ✅ 用到时再声明
void Process() {
    int sum = 0;
    for (int i = 0; i < 10; ++i) {
        sum += i;
    }
    std::string name = GetUserName();  // 需要时才声明
}
```

### 类

几个关键原则:

```cpp
class Student {
 public:
    // 构造函数
    Student(const std::string& name, int age)
        : name_(name), age_(age) {}

    // Getter: 用 const 修饰
    std::string GetName() const { return name_; }
    int GetAge() const { return age_; }

 private:
    // 数据成员设为 private, 末尾加下划线
    std::string name_;
    int age_;
};
```

要点:

- **数据成员设为 `private`**: 
    - 通过 public 方法访问, 保护数据安全
- **成员变量名末尾加下划线**: 
    - 如 `name_`, `age_`, 一眼就能区分局部变量和成员变量
- **`struct` vs `class`**:
    - `struct` 用于纯数据的集合 (没有复杂逻辑); 有行为的用 `class`

### 函数

```cpp
// ❌ 函数又臭又长, 一大堆"副作用"
void DoEverything(/* 100 行代码 */);

// ✅ 一个函数只做一件事, 保持短小 ("副作用最小原则")
int ComputeSum(const std::vector<int>& numbers) {
    int sum = 0;
    for (int n : numbers) {
        sum += n;
    }
    return sum;
}

// 输入参数在前, 输出参数在后
// 输入参数用 const 引用, 避免拷贝
void ProcessData(const std::string& input, std::string* output);
```

### 注释

注释应该解释 **"为什么"**, 而不是 **"做了什么"** —— 良好的代码自身会说话.

```cpp
// ❌ 废话注释
i = i + 1;  // i 加 1

// ❌ 还是废话
// 遍历数组
for (int i = 0; i < n; ++i) { ... }

// ✅ 解释为什么这样做
// 从后向前遍历, 因为后面的元素依赖前面的计算结果
for (int i = n - 1; i >= 0; --i) {
    dp[i] = dp[i + 1] + cost[i];
}

// ✅ 函数声明前的文档注释
// Computes the shortest path from source to all other nodes
// using Dijkstra's algorithm. Returns a map from node to distance.
std::map<int, int> ComputeShortestPath(const Graph& graph, int source);
```

### 格式

```cpp
// 缩进: 2 个空格 (Google 风格, 不是 4 个)
if (condition) {
  DoSomething();      // 2 空格缩进
  DoSomethingElse();
}

// 花括号: 不另起一行 (K&R 风格)
if (x > 0) {
  // ...
} else {
  // ...
}

// 行宽: 不超过 80 个字符
// 太长就换行:
bool result = ReallyLongFunctionName(
    first_argument, second_argument,
    third_argument);
```

### 现代 C++ 实践

Google Style Guide 鼓励使用现代 C++ 特性:

```cpp
// 用 auto 简化类型 (类型很明显时)
auto students = GetStudentList();  // 返回值类型清楚

// 用范围 for 循环
for (const auto& student : students) {
    std::cout << student.GetName() << std::endl;
}

// 用 nullptr 而不是 NULL
Student* p = nullptr;  // ✅
Student* p = NULL;     // ❌ C 风格
Student* p = 0;        // ❌ 更糟

// 用智能指针代替裸指针管理内存
auto student = std::make_unique<Student>("Alice", 20);  // ✅ 自动释放
Student* student = new Student("Alice", 20);  // ❌ 容易忘记 delete
```

## Python Style

### 命名规范

Python 的命名规范比 C++ 简单一些, 基本就是 `snake_case` 的天下:

```python
# 变量和函数: snake_case
student_count = 42
def compute_average(scores):
    return sum(scores) / len(scores)

# 类: PascalCase (和 C++ 一样)
class StudentRecord:
    pass

# 常量: UPPER_SNAKE_CASE (全大写)
MAX_RETRY_COUNT = 5
DEFAULT_TIMEOUT = 30
```

TLDR:

| 类型 | 风格 | 示例 |
|------|------|------|
| 变量 | `snake_case` | `student_count` |
| 函数 | `snake_case` | `compute_average()` |
| 类 | `PascalCase` | `StudentRecord` |
| 常量 | `UPPER_SNAKE_CASE` | `MAX_SIZE` |
| 模块 (文件名) | `snake_case` | `student_utils.py` |
| 内部/保护成员 | `_leading_underscore` | `_internal_method()` |

### 导入

```python
# ✅ 按顺序分组, 组之间空一行
# 1. 标准库
import os
import sys

# 2. 第三方库
import numpy as np

# 3. 本项目
from my_project import utils

# ❌ 不要用通配符导入
from os import *  # 你都不知道导入了啥...

# ✅ 明确导入需要的东西
from collections.abc import Mapping, Sequence
```

### 缩进与格式

```python
# 缩进: 4 个空格, 永远不要用 Tab!
# 行宽: 不超过 80 个字符

# 长函数调用换行的两种方式:
# 方式一: 与左括号对齐
result = some_long_function(argument_one, argument_two,
                            argument_three)

# 方式二: 悬挂缩进 (笔者推荐)
result = some_long_function(
    argument_one,
    argument_two,
    argument_three,
)

# 不要用反斜杠 \ 续行, 用括号!
# ❌
total = first_variable + \
        second_variable + \
        third_variable

# ✅
total = (first_variable
         + second_variable
         + third_variable)
```

### 注释与文档字符串

Python 用 `"""` 三引号写文档字符串, 这是最重要的注释形式:

```python
def compute_gpa(scores, credits):
    """根据成绩和学分计算 GPA.

    Args:
        scores: 各科成绩的列表, 每个元素为 0-100 的整数.
        credits: 各科学分的列表, 与 scores 等长.

    Returns:
        加权平均 GPA, 为 float 类型.

    Raises:
        ValueError: 如果 scores 和 credits 长度不一致.
    """
    if len(scores) != len(credits):
        raise ValueError("scores 和 credits 长度必须一致")
    total = sum(s * c for s, c in zip(scores, credits))
    return total / sum(credits)
```

类的文档字符串:

```python
class Student:
    """表示一个学生的信息.

    Attributes:
        name: 学生姓名.
        age: 学生年龄.
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
```

### 类型注解

Python 3.5+ 支持类型注解, Google 强烈推荐使用:

```python
# 函数参数和返回值加上类型注解
def greet(name: str) -> str:
    return f"Hello, {name}!"

def find_students(
    min_age: int,
    max_age: int,
    department: str | None = None,
) -> list[str]:
    """查找符合条件的学生."""
    ...
```

类型注解的好处: IDE 能给你更好的自动补全和错误提示, 相当于免费的 bug 检测器!

### 函数

```python
# 函数要短小, 只做一件事 (依旧是上述的"最小副作用"原则)

# ❌ 可变默认参数 —— 经典 Python 坑!
def add_student(name, student_list=[]):
    student_list.append(name)
    return student_list

# ✅ 用 None 代替可变默认参数
def add_student(name, student_list=None):
    if student_list is None:
        student_list = []
    student_list.append(name)
    return student_list
```

### 字符串

```python
# ✅ f-string (Python 3.6+, 最推荐)
name = "Alice"
age = 20
print(f"{name} is {age} years old")

# ✅ % 格式化
print("%s is %d years old" % (name, age))

# ❌ 不要用 + 拼接 (尤其在循环里, 性能巨差)
result = "Name: " + name + ", Age: " + str(age)

# 循环中拼接字符串? 用 join!
# ❌
result = ""
for name in names:
    result += name + ", "

# ✅
result = ", ".join(names)
```

### 文件操作与异常处理

```python
# ✅ 永远用 with 语句操作文件 (自动关闭, 不怕忘)
with open("data.txt") as f:
    for line in f:
        process(line)

# ❌ 手动开关文件 (容易忘记关, 出异常也关不了)
f = open("data.txt")
data = f.read()
f.close()

# 异常处理: 精确捕获, 不要偷懒
# ❌ 裸 except, 啥错都吞了
try:
    do_something()
except:
    pass  # 这种写法毫无意义...

# ✅ 捕获具体的异常类型
try:
    value = int(user_input)
except ValueError:
    print("请输入一个有效的整数")
```

### 列表推导式

```python
# ✅ 简单的推导式, 清晰明了
squares = [x * x for x in range(10)]
even_numbers = [x for x in numbers if x % 2 == 0]

# ❌ 太复杂的推导式, 不如写普通循环
result = [(x, y) for x in range(10) for y in range(10)
          if x != y if x + y > 5]

# ✅ 复杂逻辑老老实实写循环
result = []
for x in range(10):
    for y in range(10):
        if x != y and x + y > 5:
            result.append((x, y))
```

## C++ vs Python 命名对比

两种语言的命名规范有相似也有不同, 放在一起对比一下:

| 类型 | C++ (Google Style) | Python (Google Style) |
|------|-------|--------|
| 变量 | `snake_case` | `snake_case` |
| 函数 | `PascalCase` | `snake_case` |
| 类 | `PascalCase` | `PascalCase` |
| 常量 | `kPascalCase` | `UPPER_SNAKE_CASE` |
| 缩进 | 2 空格 | 4 空格 |
| 行宽 | 80 字符 | 80 字符 |

最大的区别是编写习惯:

**C++ 函数用 `PascalCase`, Python 函数用 `snake_case`**!

## 总结与展望

恭喜你看到这里! 🎉 让我们回顾一下核心要点:

1. **好的命名胜过好的注释**: 变量名和函数名要有意义, 让代码自己说话
2. **保持一致性**: 选定一种风格就坚持到底, 不要混搭
3. **函数要短小精悍**: 一个函数只做一件事, 不超过 40 行
4. **好的代码自己会说话, 注释着重"为什么"**: 别解释代码在干什么, 解释你为什么这样写
5. **善用语言特性**: C++ 用智能指针, Python 用 `with` 语句和类型注解

## 下一步: 到开源社区去学习!

读 Style Guide 是第一步, 但真正让你代码水平飞升的方法是 —— **阅读优秀的开源代码**.

你会发现, 那些 star 数上万的项目, 代码风格都非常统一和漂亮. 这不是巧合, 而是严格遵循 Style Guide 的结果.

**推荐路径:**

1. **找一个你感兴趣的开源项目**, 先读它的 `CONTRIBUTING.md`, 了解它的代码规范
2. **从小事做起**: 修个 typo, 改个文档, 提个小 bug fix —— 这些都是很好的入门方式
3. **认真阅读 Code Review 的反馈**: 开源社区的 maintainer 会在 PR review 中指出你的风格问题, 这是免费的一对一辅导!
4. **使用工具辅助**:
    * C++: `clang-format` 自动格式化, `clang-tidy` 静态检查
    * Python: `black` / `autopep8` 自动格式化, `pylint` / `ruff` 静态检查
    * 感兴趣的同学可自行搜索 github 上一些关于 `linting` 的工具! (笔者自己用的是 [**czg**](https://github.com/Zhengqbbb/cz-git), 供参考)

记住: **代码是写给人看的, 顺便让机器执行.** 养成好习惯, 从现在开始!

------

© 2026. ICS Team. All rights reserved.
