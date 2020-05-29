# 注意事项

## 一、环境配置

1. 本项目后端使用 flask 框架，因此需要安装 `flask`
2. 由于使用 .flaskenv 作为环境配置文件，所以需要 `python-dotenv`
3. 后端为处理跨域请求，使用 `flask_cors`
4. 由于登陆时采用 jwt 处理登录信息，所以需要 `pyjwt` **（注：并非 jwt，jwt 与 pyjwt 安装后的目录相同，但却属于不同的包）**
5. 由于有数据库操作，所以需要 `PyMySQL`

如果在 `./back_end/ProTJec_backend` 利用 `flask run` 启动无效，那么应该：

```shell
cd ..
pip install .
cd ProTJec_backend
flask run
```

此后即可使用后台运行

之前加了一个 venv 文件夹，在 linux 下于 `back_end` 执行：

```shell
source /venv/bin/activate
```
就进入了虚拟环境，然后可以利用这个进行 docker 部署。

## 二、Docker 部署

把 docker 下载喽之后，就直接用这个 Dockerfile

```shell
docker build -t [image-name] .
```

这样就生成了镜像，接着：

```shell
docker run -d -p 50000:50000 [image-name]
```

但是这样是没连数据库的，还需要搞数据库。根据随便的一篇 docker 部署 MySQL 的教程就能做到搭起 MySQL。
接着：

```shell
docker cp init_1_0.sql [container-id]:/home/init_1_0.sql
docker exec -it [container-id] /bin/bash

mysql -u root -p
create user 'Serendipity'@'localhost' identified by '[password]'
grant all privileges on *.* to 'Serendipity'@'localhost'
exit
exit
```

回来之后需要做一个连接，但是好像这么做不对啊，艹了。

算了算了，直接

```shell
nohup flask run &
```

完事儿了，我不整了，吐了。