# pynaja

# 快速开始


## 下载
git clone https://github.com/xiaoxiamiya/naja.git


## 安装
pip install pynaja


## 项目层级结构

```tex
├── pynaja                                      项目目录
│    ├── cache                                  缓存层
│    │    ├── base                           	缓存工具集
│    │    └── redis                          	redis工具集
│    ├── common                                 通用工具层
│    │    ├── async_base                        异步工具集
│    │    ├── base                              通用工具集
│    │    ├── error                             异常工具集
│    │    ├── metaclass                         元类工具集
│    │    ├── process                          	进程类工具集
│    │    ├── struct                          	结构类工具集
│    │    └── task                          	任务类工具集	
│    ├── database                               数据库层
│    │    ├── mongo                           	mongo工具集
│    │    └── mysql                          	mysql工具集
│    ├── enum                                   枚举层
│    │    └── base_enum                         枚举类工具集
│    ├── event                                  事件层目录
│    │    ├── async_event                       异步事件工具集
│    │    └── event                          	同步事件工具集
│    ├── frame                                  框架层
│    │    ├── fastapi                          	fastapi工具集
│    │    │    ├── base                         基础工具集
│    │    │    └── response                     响应工具集
│    │    └── logging                           日志工具类
│    ├── net                                    网络层
│    │    ├── cacert                            根证书
└────└──  └── http                          	http工具集
```