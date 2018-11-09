配置新网站
=======================

## 依赖

* nginx
* Python 3.6
* virtualenv + pip
* Git

## Nginx服务器

* 参考nginx.templates.conf
* 把SITENAME替换为所需的域名，如staging.my-domain.com

## Systemd服务

* gunicorn-systemd.templates.conf
* 把SITENAME替换为所需的域名，如staging.my-domain.com

## 目录结构
假设有用户账户，home目录为/home/username

/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv
