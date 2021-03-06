# pygrid-test
pygrid平台安装和测试

## 步骤
- [pygrid-test](#pygrid-test)
  - [步骤](#步骤)
  - [## docker安装](#-docker安装)
  - [## 克隆pygrid代码](#-克隆pygrid代码)
  - [## 创建node节点image](#-创建node节点image)
  - [## 创建network节点image](#-创建network节点image)
  - [## 修改docker-compose.yml文件](#-修改docker-composeyml文件)
  - [## 修改etc/hosts文件](#-修改etchosts文件)
  - [## 启动集群](#-启动集群)
  - [## 测试](#-测试)

## docker安装
---
我们使用docker容器的方式启动pygrid的节点，所以首先需要安装docker,去[docker官网](https://www.docker.com/get-started)下载docker安装包一键安装即可

*note*: windows家庭版安装docker需要一些特殊操作，[这里](https://docs.docker.com/docker-for-windows/install-windows-home/)

## 克隆pygrid代码
---
1.克隆
```
git clone git@github.com:OpenMined/PyGrid.git 
```
2.切换分支
```
cd pygrid   //进入项目目录
git checkout master  //切换分支
```
## 创建node节点image
---
```
docker build ./apps/node/ -f ./apps/node/Dockerfile -t pygrid:node
```
## 创建network节点image
---
```
docker build ./apps/network/ -f ./apps/network/Dockerfile -t pygrid:network
```
## 修改docker-compose.yml文件
---
openmined/grid-network:production改为pygrid:network

openmined/grid-node:production改为pygrid:node

## 修改etc/hosts文件
---
docker-compose集群使用了alice等域名，需要添加进host文件

用管理员身份打开C:\Windows\System32\drivers\etc\hosts

或则右键该文件，属性，修改普通user的操作权限

复制下面内容进入并保存
```
127.0.0.1 network
127.0.0.1 alice
127.0.0.1 bob
127.0.0.1 bill
127.0.0.1 james
```

## 启动集群
---
查看node和network image是不是已经准备好了

```
docker images
```

启动集群
```
docker-compose up
```
## 测试
---
测试需要用到syft库所以需要先[安装syft](https://github.com/yyl-smpc/pysyft-test)
假设我们已经在conda pysyft环境下安装了syft

执行测试
```
conda activate syft-test   //  切换环境
python dataowner.py   //执行数据所有者的代码，上传数据
python datascientist.py //执行数据科学家的代码，搜索数据并执行计算
```
