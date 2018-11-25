# fusekibundle (WIP)

One stop deployment of FUSEKI triple store and data.

```
$ git clone https://github.com/miku/fusekibundle.git
$ cd fusekibundle
```

Create database from textual triple data.

```
$ tdb2.tdbloader --loc ds0 rdf.xml.gz
```

Adjust configuration.

```
$ ...
```

Create RPMs for FUSEKI and the dataset

```
$ make rpm
```

You should have two RPM files available, server and data (named after dataset).

```
$ ls
fusekibundle-3.9.0-0.x86_64.rpm
fusekibundle-data-ds0-0.1.0.x86_64.rpm
```

Install rpm on target:

```
$ yum install fusekibundle-3.9.0-0.x86_64.rpm
```

The `Environment=FUSEKI_BASE=/etc/fuseki`. Manage fuseki.service via `systemctl`.
