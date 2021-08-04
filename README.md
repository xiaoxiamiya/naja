# naja

# 快速开始


## 下载
git clone https://github.com/xiaoxiamiya/naja.git


## 安装
pip install naja


## 项目层级结构

```tex
├── naja                                        项目目录
│    ├── abc_base                               项目抽象基类层
│    │    ├── model                           	抽象模型层
│    │    ├── service                           抽象服务层
│    │    └── view                          	抽象视图层
│    ├── apps                                   项目应用目录
│    │    ├── example_app                       单一应用
│    │ 	  │  	├── sql_logs                    该应用sql修改记录
│    │ 	  │  	├── enum.py                     该应用枚举类常量
│    │ 	  │  	├── model.py                    该应用模型文件
│    │ 	  │ 	├── service.py                  该应用服务文件
│    │    │  	└── view.py                     该应用视图文件	
│    ├── utils                                  项目工具层目录
│    │    ├── cache                           	缓存&redis工具集
│    │    ├── common                        	通用工具集
│    │    ├── database                          数据库工具集
│    │    ├── enum                              枚举类工具集
│    │    ├── event                          	事件类工具集
│    │    ├── frame                          	fastapi框架工具集
│    │    └── net                          	网络层工具集
│    ├── conf                                   项目配置层目录
│    │    ├── dynamic.conf                      本地动态配置文件
│    │    ├── dynamic.dev.conf                  dev环境动态配置文件
│    │    ├── dynamic.rel.conf                  生产环境动态配置文件
│    │    ├── static.conf                       本地静态配置文件
│    │    ├── static.dev.conf                   dev环境静态配置文件
│    │    ├── static.rel.conf                   生产环境静态配置文件
│    │    └── gunicorn.conf                     gunicorn配置文件
│    ├── services                               项目独立/三方服务目录
│    ├── main.py                                fastapi实例对象入口
└────└── router.py                              项目路由集
```