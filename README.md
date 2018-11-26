# fusekibundle (WIP)

One stop deployment of FUSEKI triple store server.

## TL;DR

> I have a CentOS box and want a FUSEKI triple store that I want to manage it via `systemctl`.

```
# yum install https://github.com/miku/fusekibundle/releases/download/v3.9.0/fusekibundle-3.9.0-0.x86_64.rpm
```

----

## Building the RPM


```
$ git clone https://github.com/miku/fusekibundle.git
$ cd fusekibundle
```

Download a Apache Fuseki distribution:

```
$ wget http://ftp.halifax.rwth-aachen.de/apache/jena/binaries/apache-jena-3.9.0.tar.gz
$ tar xvzf apache-jena-3.9.0.tar.gz
```

Create an RPM for FUSEKI. For this step, you will have to have `rpm` installed on the machine.

```
$ make rpm
```

If all is well, an RPM is build:

```
$ ls
fusekibundle-3.9.0-0.x86_64.rpm
```

Copy and install rpm on target:

```
$ yum install fusekibundle-3.9.0-0.x86_64.rpm
```

A used `fuseki` is added (and removed when uninstalled). The server can be started with:

```
# systemctl start fuseki.service
```

The configuration directory is `/etc/fuseki`.
