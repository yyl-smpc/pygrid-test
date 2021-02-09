# pygrid-test
pygrid平台安装和测试

## 步骤
- [安装dokcer](#docker安装)
- [克隆pygrid代码](#克隆pygrid代码)
- [创建node节点image](#node节点image)
- [创建network节点image](#network节点image)
- [修改compose文件](#修改compose文件)
- [启动集群](#启动集群)
- [测试](#测试)

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
git branch  -a    //查看所有分支
git checkout dev
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
openmined/grid-network:production改为grid:network
openmined/grid-node:production改为grid:nodework
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
conda activate pysyft   //  切换环境
python pygrid-test.py   //执行代码
```