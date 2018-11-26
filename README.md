# fusekibundle (WIP)

One stop deployment of FUSEKI triple store server.

```
$ git clone https://github.com/miku/fusekibundle.git
$ cd fusekibundle
```

Download a Apache Fuseki distribution:

```
$ wget http://ftp.halifax.rwth-aachen.de/apache/jena/binaries/apache-jena-3.9.0.tar.gz
$ tar xvzf apache-jena-3.9.0.tar.gz
```

Create an RPM for FUSEKI:

```
$ make rpm
```

If all is well, an RPM is build:

```
$ ls
fusekibundle-3.9.0-0.x86_64.rpm
```

Install rpm on target:

```
$ yum install fusekibundle-3.9.0-0.x86_64.rpm
```

A used `fuseki` is added (and removed when uninstalled). The server can be started with:

```
# systemctl start fuseki.service
```

The configuration directory is `/etc/fuseki`.
