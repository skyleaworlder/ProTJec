# 前端部署

首先确定开发环境需要的工具版本：

1. node>=12.17
2. npm>=6.5

```shell
node -v
npm -v
```

如果版本过低，建议直接：

```shell
npm install npm -g
wget https://nodejs.org/dist/v12.17.0/node-v12.17.0-linux-x64.tar.xz
```

如果发现 npm 和 node 的版本号在更新后没有发生变化，建议清一下缓存

```shell
hash -r
```

如果是仍旧找不到命令的话，建议加一下软链接，链接的路径可能不一样。
版本正常了之后：

```shell
npm install
npm i -D webpack-cli
```
