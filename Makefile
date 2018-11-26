SHELL = /bin/bash

PKGNAME = fusekibundle
VERSION = 3.9.0

rpm: packaging/rpm/fusekibundle.spec
	rm -rf $(HOME)/rpmbuild/BUILD/fuseki # FIXME: where does this come from?
	mkdir -p $(HOME)/rpmbuild/{BUILD,SOURCES,SPECS,RPMS}
	cp ./packaging/rpm/$(PKGNAME).spec $(HOME)/rpmbuild/SPECS
	cp -r apache-jena-fuseki-$(VERSION) $(HOME)/rpmbuild/BUILD
	mv $(HOME)/rpmbuild/BUILD/apache-jena-fuseki-$(VERSION) $(HOME)/rpmbuild/BUILD/fuseki
	./packaging/rpm/buildrpm.sh $(PKGNAME)
	cp $(HOME)/rpmbuild/RPMS/x86_64/$(PKGNAME)*.rpm .

apache-jena-fuseki-$(VERSION):
	echo "Download from https://jena.apache.org/download/index.cgi"

packaging/rpm/fusekibundle.spec: apache-jena-fuseki-$(VERSION)
	python rpmutil.py apache-jena-fuseki-$(VERSION) > $@


clean:
	rm -f packaging/rpm/fusekibundle.spec
	rm -f fusekibundle*rpm


