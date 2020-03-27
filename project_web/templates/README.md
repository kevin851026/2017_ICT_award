# SentiMap (情緒地圖)[![Build Status](https://travis-ci.org/Stufinite/Crawler-NCHU-course.svg?branch=master)](https://travis-ci.org/NCHUSG/Python-Crawler)

2016參加XXX專題競賽的作品

## Getting Started

第一次使用python的使用者請先執行 `Prerequisities`把python環境安裝起來

不然就可以直接跳到 `Installing`

### Prerequisities

```
sudo apt-get update
sudo apt-get install python2 python2-dev virtualenv
```

### Installing

1. 使用虛擬環境安裝 `django`：virtualenv venv
2. 啟動虛擬環境：`. venv/bin/activate`
3. 安裝專案：
  * Windows：
    * `pip install django==1.9`
    * `django-admin.py startproject 『自己取的名字』`
    * `cd 『自己取的名字』`
    * `git clone https://github.com/david30907d/django-EntryTemplate.git`
    * 記得把SentiMap丟進去django的project，他才讀的到這個app
    * 設定django：
      * urls.py：加入這一行 `url(r'^SentiMap/', include('SentiMap.urls',namespace="SentiMap")),`
      * settings.py：在INSTALLED_APPS裏面新增 `'SentiMap'`
  * Linux/OS X：
    * `make install`

## Deployment

佈署方式和一般的django專案一樣

Deploy SentiMap is the same as normal Django project.

### Result

![Demo](/static/SentiMap/img/readme/Selection_018.png)

## Built With

* python 2.7
* django 1.9
* leaflet 1.0.1

## Versioning

For the versions available, see the [tags on this repository](https://github.com/NCHUSG/Python-Crawler/tags).

## Contributors

* **張泰瑋** [david](https://github.com/david30907d)
* **黃翔宇** [j9963232q](https://github.com/j9963232q)

## Acknowledgments

* 感謝 **范耀中** 老師的費心指導以及 **UDIC實驗室** 學長姊們的幫助

## License

This project is licensed under the **GNU 3.0** License - see the [LICENSE.md](LICENSE.md) file for details
