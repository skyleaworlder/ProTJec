# ProTJec

本着 “凡是跟同济大学沾点关系的东西一定要把 ‘同’ 和 ‘济’ 两个字有机结合” 的大纲，这里将 `Project` 简单包装，变为 `ProTJec`，那么显然和项目有关了。



本项目由 3 个文件夹组成。

首先是 `prepare`。

其中放入了一些杂项文件，比如：

* **定义前后端接口** 的 `API.json`
* **MySQL数据库脚本** `init_1_0.sql` 和 其 ANSI 编码版本 `ansi_1_0.sql`
* **项目开发日志** `dev_note.md`
* **数据库模型** `ProTJec.mwb` 及其副本 `ProTJec.mwb.bak`
* **UI原型图** `设计原型图.bmpr`



其次是 `front_end`。

其中是前端项目。是从 `vue-element-admin` 直接搬过来的一些东西。

值得注意的是其中还嵌套了一层，因为本来打算外面再放一些文件的，但是后来都转入了 `prepare` 中，于是再也没有改过。



<span  style="color:red"><u>对 `front_end` 文件夹中内容进行修改之前，必须在 git 上输入以下命令。</u></span>

```git
git config core.autocrlf false
```

自动生成的 `package.json` 默认为 LF，add 时会出问题。





最后是 `back_end`。

后端项目所在位置，同样嵌套了一层。

没有使用多余的 `flask` 插件，基本纯手写，锻炼自己的 `SQL`（其实根本没有，因为涉及的查询太简单了

