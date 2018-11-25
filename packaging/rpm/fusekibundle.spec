
Summary:    Inofficial bundle for FUSEKI triple store.
Name:       fusekibundle
Version:    3.9.0
Release:    0
License:    Apache Version 2.0
ExclusiveArch:  x86_64
BuildRoot:  %{_tmppath}/%{name}-build
Group:      System/Base
Vendor:     Leipzig University Library, https://www.ub.uni-leipzig.de
URL:        https://github.com/miku/fusekibundle

%description

Inofficial bundle for FUSEKI triple store. More information at: https://jena.apache.org

%prep

%build

%pre

%%install

mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/java
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena/example
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena/example/helloworld
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena/example/pizza
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/resources
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/resources/ontologies
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/resources/data
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/test
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/test/java
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/test/java/org
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/test/java/org/apache
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/test/java/org/apache/jena_examples
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/bin
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/riot
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/engine
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/update
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/constructquads
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/bgpmatching
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/propertyfunction
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/filter
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/aggregates
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/data
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/ontology
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/ontology/classHierarchy
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/ontology/describeClass
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/tdb
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/tdb/examples
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib-src
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat
install -m 644 apache-jena-3.9.0/NOTICE $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/NOTICE
install -m 644 apache-jena-3.9.0/jena-log4j.properties $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/jena-log4j.properties
install -m 644 apache-jena-3.9.0/README $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/README
install -m 644 apache-jena-3.9.0/LICENSE $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/LICENSE
install -m 755 apache-jena-3.9.0/bin/rdfxml $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/rdfxml
install -m 755 apache-jena-3.9.0/bin/rdfdiff $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/rdfdiff
install -m 755 apache-jena-3.9.0/bin/rdfcompare $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/rdfcompare
install -m 755 apache-jena-3.9.0/bin/tdbstats $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdbstats
install -m 755 apache-jena-3.9.0/bin/rdfparse $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/rdfparse
install -m 755 apache-jena-3.9.0/bin/riot $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/riot
install -m 755 apache-jena-3.9.0/bin/arq $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/arq
install -m 755 apache-jena-3.9.0/bin/rdfcopy $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/rdfcopy
install -m 755 apache-jena-3.9.0/bin/infer $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/infer
install -m 755 apache-jena-3.9.0/bin/update $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/update
install -m 755 apache-jena-3.9.0/bin/tdb2.tdbbackup $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdb2.tdbbackup
install -m 755 apache-jena-3.9.0/bin/tdbloader2common $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdbloader2common
install -m 755 apache-jena-3.9.0/bin/tdbloader2index $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdbloader2index
install -m 755 apache-jena-3.9.0/bin/qparse $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/qparse
install -m 755 apache-jena-3.9.0/bin/nquads $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/nquads
install -m 755 apache-jena-3.9.0/bin/tdb2.tdbdump $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdb2.tdbdump
install -m 755 apache-jena-3.9.0/bin/tdb2.tdbquery $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdb2.tdbquery
install -m 755 apache-jena-3.9.0/bin/rdfcat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/rdfcat
install -m 755 apache-jena-3.9.0/bin/tdbloader $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdbloader
install -m 755 apache-jena-3.9.0/bin/tdbbackup $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdbbackup
install -m 755 apache-jena-3.9.0/bin/tdbquery $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdbquery
install -m 755 apache-jena-3.9.0/bin/tdbdump $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdbdump
install -m 755 apache-jena-3.9.0/bin/wwwdec $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/wwwdec
install -m 755 apache-jena-3.9.0/bin/turtle $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/turtle
install -m 755 apache-jena-3.9.0/bin/sparql $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/sparql
install -m 755 apache-jena-3.9.0/bin/juuid $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/juuid
install -m 755 apache-jena-3.9.0/bin/tdb2.tdbcompact $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdb2.tdbcompact
install -m 755 apache-jena-3.9.0/bin/tdb2.tdbstats $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdb2.tdbstats
install -m 755 apache-jena-3.9.0/bin/trig $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/trig
install -m 755 apache-jena-3.9.0/bin/tdbupdate $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdbupdate
install -m 755 apache-jena-3.9.0/bin/wwwenc $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/wwwenc
install -m 755 apache-jena-3.9.0/bin/ntriples $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/ntriples
install -m 755 apache-jena-3.9.0/bin/schemagen $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/schemagen
install -m 755 apache-jena-3.9.0/bin/iri $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/iri
install -m 755 apache-jena-3.9.0/bin/uparse $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/uparse
install -m 755 apache-jena-3.9.0/bin/jena $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/jena
install -m 755 apache-jena-3.9.0/bin/tdb2.tdbloader $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdb2.tdbloader
install -m 755 apache-jena-3.9.0/bin/tdb2.tdbupdate $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdb2.tdbupdate
install -m 755 apache-jena-3.9.0/bin/rset $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/rset
install -m 755 apache-jena-3.9.0/bin/utf8 $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/utf8
install -m 755 apache-jena-3.9.0/bin/tdbloader2data $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdbloader2data
install -m 755 apache-jena-3.9.0/bin/tdbloader2 $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/tdbloader2
install -m 755 apache-jena-3.9.0/bin/rsparql $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/rsparql
install -m 755 apache-jena-3.9.0/bin/rupdate $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bin/rupdate
install -m 644 apache-jena-3.9.0/src-examples/jena-examples/pom.xml $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/pom.xml
install -m 644 apache-jena-3.9.0/src-examples/jena-examples/README.md $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/README.md
install -m 644 apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena/example/Base.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena/example/Base.java
install -m 644 apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena/example/CheeseBase.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena/example/CheeseBase.java
install -m 644 apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena/example/helloworld/HelloWorld.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena/example/helloworld/HelloWorld.java
install -m 644 apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena/example/pizza/PizzaSparqlNoInf.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena/example/pizza/PizzaSparqlNoInf.java
install -m 644 apache-jena-3.9.0/src-examples/jena-examples/src/main/resources/ontologies/cheese.ttl $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/resources/ontologies/cheese.ttl
install -m 644 apache-jena-3.9.0/src-examples/jena-examples/src/main/resources/data/cheeses-0.1.ttl $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/resources/data/cheeses-0.1.ttl
install -m 644 apache-jena-3.9.0/src-examples/jena-examples/src/main/resources/data/pizza.owl.rdf $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/resources/data/pizza.owl.rdf
install -m 644 apache-jena-3.9.0/src-examples/jena-examples/src/test/java/org/apache/jena_examples/AppTest.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/src/test/java/org/apache/jena_examples/AppTest.java
install -m 755 apache-jena-3.9.0/src-examples/jena-examples/bin/get-data $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena-examples/bin/get-data
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/ExampleDBpedia2.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/ExampleDBpedia2.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/AlgebraExec.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/AlgebraExec.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/ExProg2.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/ExProg2.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/ExampleDBpedia3.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/ExampleDBpedia3.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/ExampleDBpedia1.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/ExampleDBpedia1.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/ExQuerySelect1.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/ExQuerySelect1.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/ExQuerySelect2.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/ExQuerySelect2.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/AlgebraEx.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/AlgebraEx.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/ExProg1.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/ExProg1.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOTw2_writeRDF.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOTw2_writeRDF.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT3_RDFParser.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT3_RDFParser.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/riot/Ex_WriteJsonLD.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/Ex_WriteJsonLD.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT4_StreamRDF_Filter.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT4_StreamRDF_Filter.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT6_AddNewReader.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT6_AddNewReader.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT_RDFXML_ReaderProperties.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT_RDFXML_ReaderProperties.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOTw3_AddNewWriter.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOTw3_AddNewWriter.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT1_ReadModel.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT1_ReadModel.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT5_StreamRDFCollect.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT5_StreamRDFCollect.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT2_ReadDataset.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT2_ReadDataset.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT_RDFXML_WriteProperties.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT_RDFXML_WriteProperties.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT7_ParserPiped.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT7_ParserPiped.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOTw1_writeModel.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOTw1_writeModel.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/engine/MyQueryEngine.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/engine/MyQueryEngine.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/update/UpdateExecuteOperations.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/update/UpdateExecuteOperations.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/update/UpdateReadFromFile.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/update/UpdateReadFromFile.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/update/UpdateProgrammatic.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/update/UpdateProgrammatic.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/constructquads/ExampleConstructQuads.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/constructquads/ExampleConstructQuads.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/bgpmatching/StageAltMain.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/bgpmatching/StageAltMain.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/bgpmatching/OpExecutorAlt.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/bgpmatching/OpExecutorAlt.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/bgpmatching/StageGeneratorAlt.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/bgpmatching/StageGeneratorAlt.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/propertyfunction/localname.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/propertyfunction/localname.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/propertyfunction/labelSearch.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/propertyfunction/labelSearch.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/propertyfunction/uppercase.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/propertyfunction/uppercase.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/filter/classify.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/filter/classify.java
install -m 644 apache-jena-3.9.0/src-examples/arq/examples/aggregates/CustomAggregate.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/arq/examples/aggregates/CustomAggregate.java
install -m 644 apache-jena-3.9.0/src-examples/data/test1.owl $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/data/test1.owl
install -m 644 apache-jena-3.9.0/src-examples/data/camera.owl $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/data/camera.owl
install -m 644 apache-jena-3.9.0/src-examples/data/eswc-2006-09-21.rdf $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/data/eswc-2006-09-21.rdf
install -m 644 apache-jena-3.9.0/src-examples/data/test2.owl $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/data/test2.owl
install -m 644 apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial05.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial05.java
install -m 644 apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial04.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial04.java
install -m 644 apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial01.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial01.java
install -m 644 apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial03.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial03.java
install -m 644 apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial10.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial10.java
install -m 644 apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial02.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial02.java
install -m 644 apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial08.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial08.java
install -m 644 apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial09.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial09.java
install -m 644 apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial11.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial11.java
install -m 644 apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial07.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial07.java
install -m 644 apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial06.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial06.java
install -m 644 apache-jena-3.9.0/src-examples/jena/examples/ontology/classHierarchy/Main.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/ontology/classHierarchy/Main.java
install -m 644 apache-jena-3.9.0/src-examples/jena/examples/ontology/classHierarchy/ClassHierarchy.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/ontology/classHierarchy/ClassHierarchy.java
install -m 644 apache-jena-3.9.0/src-examples/jena/examples/ontology/describeClass/Main.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/ontology/describeClass/Main.java
install -m 644 apache-jena-3.9.0/src-examples/jena/examples/ontology/describeClass/DescribeClass.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/jena/examples/ontology/describeClass/DescribeClass.java
install -m 644 apache-jena-3.9.0/src-examples/tdb/examples/ExTDB2.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB2.java
install -m 644 apache-jena-3.9.0/src-examples/tdb/examples/ExTDB_Txn1.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB_Txn1.java
install -m 644 apache-jena-3.9.0/src-examples/tdb/examples/ExTDB4.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB4.java
install -m 644 apache-jena-3.9.0/src-examples/tdb/examples/ExTDB6.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB6.java
install -m 644 apache-jena-3.9.0/src-examples/tdb/examples/ExTDB1.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB1.java
install -m 644 apache-jena-3.9.0/src-examples/tdb/examples/ExQuadFilter.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExQuadFilter.java
install -m 644 apache-jena-3.9.0/src-examples/tdb/examples/ExTDB3.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB3.java
install -m 644 apache-jena-3.9.0/src-examples/tdb/examples/ExTDB_Txn3.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB_Txn3.java
install -m 644 apache-jena-3.9.0/src-examples/tdb/examples/ExTDB_Txn2.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB_Txn2.java
install -m 644 apache-jena-3.9.0/src-examples/tdb/examples/ExTDB5.java $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB5.java
install -m 644 apache-jena-3.9.0/lib-src/jena-arq-3.9.0-sources.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib-src/jena-arq-3.9.0-sources.jar
install -m 644 apache-jena-3.9.0/lib-src/jena-rdfconnection-3.9.0-sources.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib-src/jena-rdfconnection-3.9.0-sources.jar
install -m 644 apache-jena-3.9.0/lib-src/jena-tdb-3.9.0-sources.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib-src/jena-tdb-3.9.0-sources.jar
install -m 644 apache-jena-3.9.0/lib-src/jena-cmds-3.9.0-sources.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib-src/jena-cmds-3.9.0-sources.jar
install -m 644 apache-jena-3.9.0/lib-src/jena-core-3.9.0-sources.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib-src/jena-core-3.9.0-sources.jar
install -m 644 apache-jena-3.9.0/lib/jackson-core-2.9.6.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jackson-core-2.9.6.jar
install -m 644 apache-jena-3.9.0/lib/commons-csv-1.5.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/commons-csv-1.5.jar
install -m 644 apache-jena-3.9.0/lib/jena-core-3.9.0.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jena-core-3.9.0.jar
install -m 644 apache-jena-3.9.0/lib/jackson-databind-2.9.6.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jackson-databind-2.9.6.jar
install -m 644 apache-jena-3.9.0/lib/jena-shaded-guava-3.9.0.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jena-shaded-guava-3.9.0.jar
install -m 644 apache-jena-3.9.0/lib/slf4j-log4j12-1.7.25.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/slf4j-log4j12-1.7.25.jar
install -m 644 apache-jena-3.9.0/lib/httpcore-4.4.9.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/httpcore-4.4.9.jar
install -m 644 apache-jena-3.9.0/lib/jena-dboe-base-3.9.0.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jena-dboe-base-3.9.0.jar
install -m 644 apache-jena-3.9.0/lib/jena-tdb2-3.9.0.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jena-tdb2-3.9.0.jar
install -m 644 apache-jena-3.9.0/lib/jena-iri-3.9.0.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jena-iri-3.9.0.jar
install -m 644 apache-jena-3.9.0/lib/jena-base-3.9.0.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jena-base-3.9.0.jar
install -m 644 apache-jena-3.9.0/lib/jackson-annotations-2.9.0.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jackson-annotations-2.9.0.jar
install -m 644 apache-jena-3.9.0/lib/slf4j-api-1.7.25.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/slf4j-api-1.7.25.jar
install -m 644 apache-jena-3.9.0/lib/commons-lang3-3.4.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/commons-lang3-3.4.jar
install -m 644 apache-jena-3.9.0/lib/commons-io-2.6.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/commons-io-2.6.jar
install -m 644 apache-jena-3.9.0/lib/jsonld-java-0.12.1.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jsonld-java-0.12.1.jar
install -m 644 apache-jena-3.9.0/lib/log4j-1.2.17.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/log4j-1.2.17.jar
install -m 644 apache-jena-3.9.0/lib/collection-0.7.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/collection-0.7.jar
install -m 644 apache-jena-3.9.0/lib/jena-dboe-transaction-3.9.0.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jena-dboe-transaction-3.9.0.jar
install -m 644 apache-jena-3.9.0/lib/commons-compress-1.17.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/commons-compress-1.17.jar
install -m 644 apache-jena-3.9.0/lib/jena-dboe-index-3.9.0.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jena-dboe-index-3.9.0.jar
install -m 644 apache-jena-3.9.0/lib/httpclient-cache-4.5.5.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/httpclient-cache-4.5.5.jar
install -m 644 apache-jena-3.9.0/lib/jena-rdfconnection-3.9.0.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jena-rdfconnection-3.9.0.jar
install -m 644 apache-jena-3.9.0/lib/jena-tdb-3.9.0.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jena-tdb-3.9.0.jar
install -m 644 apache-jena-3.9.0/lib/commons-codec-1.11.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/commons-codec-1.11.jar
install -m 644 apache-jena-3.9.0/lib/libthrift-0.10.0.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/libthrift-0.10.0.jar
install -m 644 apache-jena-3.9.0/lib/httpclient-4.5.5.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/httpclient-4.5.5.jar
install -m 644 apache-jena-3.9.0/lib/jena-dboe-trans-data-3.9.0.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jena-dboe-trans-data-3.9.0.jar
install -m 644 apache-jena-3.9.0/lib/jena-arq-3.9.0.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jena-arq-3.9.0.jar
install -m 644 apache-jena-3.9.0/lib/jcl-over-slf4j-1.7.25.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jcl-over-slf4j-1.7.25.jar
install -m 644 apache-jena-3.9.0/lib/commons-cli-1.4.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/commons-cli-1.4.jar
install -m 644 apache-jena-3.9.0/lib/jena-cmds-3.9.0.jar $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/lib/jena-cmds-3.9.0.jar
install -m 644 apache-jena-3.9.0/bat/wwwenc.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/wwwenc.bat
install -m 644 apache-jena-3.9.0/bat/utf8.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/utf8.bat
install -m 644 apache-jena-3.9.0/bat/rdfcopy.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/rdfcopy.bat
install -m 644 apache-jena-3.9.0/bat/tdb2_tdbquery.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/tdb2_tdbquery.bat
install -m 644 apache-jena-3.9.0/bat/infer.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/infer.bat
install -m 644 apache-jena-3.9.0/bat/tdbupdate.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/tdbupdate.bat
install -m 644 apache-jena-3.9.0/bat/rsparql.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/rsparql.bat
install -m 644 apache-jena-3.9.0/bat/trig.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/trig.bat
install -m 644 apache-jena-3.9.0/bat/turtle.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/turtle.bat
install -m 644 apache-jena-3.9.0/bat/nquads.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/nquads.bat
install -m 644 apache-jena-3.9.0/bat/tdb2_tdbstats.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/tdb2_tdbstats.bat
install -m 644 apache-jena-3.9.0/bat/rdfxml.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/rdfxml.bat
install -m 644 apache-jena-3.9.0/bat/update.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/update.bat
install -m 644 apache-jena-3.9.0/bat/rset.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/rset.bat
install -m 644 apache-jena-3.9.0/bat/uparse.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/uparse.bat
install -m 644 apache-jena-3.9.0/bat/sparql.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/sparql.bat
install -m 644 apache-jena-3.9.0/bat/rdfcat.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/rdfcat.bat
install -m 644 apache-jena-3.9.0/bat/tdb2_tdbbackup.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/tdb2_tdbbackup.bat
install -m 644 apache-jena-3.9.0/bat/tdbdump.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/tdbdump.bat
install -m 644 apache-jena-3.9.0/bat/tdb2_tdbloader.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/tdb2_tdbloader.bat
install -m 644 apache-jena-3.9.0/bat/ntriples.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/ntriples.bat
install -m 644 apache-jena-3.9.0/bat/tdbbackup.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/tdbbackup.bat
install -m 644 apache-jena-3.9.0/bat/wwwdec.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/wwwdec.bat
install -m 644 apache-jena-3.9.0/bat/rdfdiff.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/rdfdiff.bat
install -m 644 apache-jena-3.9.0/bat/rdfcompare.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/rdfcompare.bat
install -m 644 apache-jena-3.9.0/bat/tdbstats.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/tdbstats.bat
install -m 644 apache-jena-3.9.0/bat/riot.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/riot.bat
install -m 644 apache-jena-3.9.0/bat/tdbloader.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/tdbloader.bat
install -m 644 apache-jena-3.9.0/bat/qparse.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/qparse.bat
install -m 644 apache-jena-3.9.0/bat/iri.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/iri.bat
install -m 644 apache-jena-3.9.0/bat/tdb2_tdbupdate.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/tdb2_tdbupdate.bat
install -m 644 apache-jena-3.9.0/bat/rupdate.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/rupdate.bat
install -m 644 apache-jena-3.9.0/bat/schemagen.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/schemagen.bat
install -m 644 apache-jena-3.9.0/bat/tdbquery.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/tdbquery.bat
install -m 644 apache-jena-3.9.0/bat/juuid.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/juuid.bat
install -m 644 apache-jena-3.9.0/bat/tdb2_tdbcompact.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/tdb2_tdbcompact.bat
install -m 644 apache-jena-3.9.0/bat/arq.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/arq.bat
install -m 644 apache-jena-3.9.0/bat/rdfparse.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/rdfparse.bat
install -m 644 apache-jena-3.9.0/bat/tdb2_tdbdump.bat $RPM_BUILD_ROOT/opt/apache-jena-3.9.0/bat/tdb2_tdbdump.bat

%%post

%%clean

rm -rf $RPM_BUILD_ROOT
rm -rf %%{_tmppath}/%%{name}
rm -rf %%{_topdir}/BUILD/%%{name}

%%files
%%defattr(-,root,root)

/opt/apache-jena-3.9.0/NOTICE
/opt/apache-jena-3.9.0/jena-log4j.properties
/opt/apache-jena-3.9.0/README
/opt/apache-jena-3.9.0/LICENSE
/opt/apache-jena-3.9.0/bin/rdfxml
/opt/apache-jena-3.9.0/bin/rdfdiff
/opt/apache-jena-3.9.0/bin/rdfcompare
/opt/apache-jena-3.9.0/bin/tdbstats
/opt/apache-jena-3.9.0/bin/rdfparse
/opt/apache-jena-3.9.0/bin/riot
/opt/apache-jena-3.9.0/bin/arq
/opt/apache-jena-3.9.0/bin/rdfcopy
/opt/apache-jena-3.9.0/bin/infer
/opt/apache-jena-3.9.0/bin/update
/opt/apache-jena-3.9.0/bin/tdb2.tdbbackup
/opt/apache-jena-3.9.0/bin/tdbloader2common
/opt/apache-jena-3.9.0/bin/tdbloader2index
/opt/apache-jena-3.9.0/bin/qparse
/opt/apache-jena-3.9.0/bin/nquads
/opt/apache-jena-3.9.0/bin/tdb2.tdbdump
/opt/apache-jena-3.9.0/bin/tdb2.tdbquery
/opt/apache-jena-3.9.0/bin/rdfcat
/opt/apache-jena-3.9.0/bin/tdbloader
/opt/apache-jena-3.9.0/bin/tdbbackup
/opt/apache-jena-3.9.0/bin/tdbquery
/opt/apache-jena-3.9.0/bin/tdbdump
/opt/apache-jena-3.9.0/bin/wwwdec
/opt/apache-jena-3.9.0/bin/turtle
/opt/apache-jena-3.9.0/bin/sparql
/opt/apache-jena-3.9.0/bin/juuid
/opt/apache-jena-3.9.0/bin/tdb2.tdbcompact
/opt/apache-jena-3.9.0/bin/tdb2.tdbstats
/opt/apache-jena-3.9.0/bin/trig
/opt/apache-jena-3.9.0/bin/tdbupdate
/opt/apache-jena-3.9.0/bin/wwwenc
/opt/apache-jena-3.9.0/bin/ntriples
/opt/apache-jena-3.9.0/bin/schemagen
/opt/apache-jena-3.9.0/bin/iri
/opt/apache-jena-3.9.0/bin/uparse
/opt/apache-jena-3.9.0/bin/jena
/opt/apache-jena-3.9.0/bin/tdb2.tdbloader
/opt/apache-jena-3.9.0/bin/tdb2.tdbupdate
/opt/apache-jena-3.9.0/bin/rset
/opt/apache-jena-3.9.0/bin/utf8
/opt/apache-jena-3.9.0/bin/tdbloader2data
/opt/apache-jena-3.9.0/bin/tdbloader2
/opt/apache-jena-3.9.0/bin/rsparql
/opt/apache-jena-3.9.0/bin/rupdate
/opt/apache-jena-3.9.0/src-examples/jena-examples/pom.xml
/opt/apache-jena-3.9.0/src-examples/jena-examples/README.md
/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena/example/Base.java
/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena/example/CheeseBase.java
/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena/example/helloworld/HelloWorld.java
/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/java/org/apache/jena/example/pizza/PizzaSparqlNoInf.java
/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/resources/ontologies/cheese.ttl
/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/resources/data/cheeses-0.1.ttl
/opt/apache-jena-3.9.0/src-examples/jena-examples/src/main/resources/data/pizza.owl.rdf
/opt/apache-jena-3.9.0/src-examples/jena-examples/src/test/java/org/apache/jena_examples/AppTest.java
/opt/apache-jena-3.9.0/src-examples/jena-examples/bin/get-data
/opt/apache-jena-3.9.0/src-examples/arq/examples/ExampleDBpedia2.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/AlgebraExec.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/ExProg2.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/ExampleDBpedia3.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/ExampleDBpedia1.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/ExQuerySelect1.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/ExQuerySelect2.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/AlgebraEx.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/ExProg1.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOTw2_writeRDF.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT3_RDFParser.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/Ex_WriteJsonLD.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT4_StreamRDF_Filter.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT6_AddNewReader.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT_RDFXML_ReaderProperties.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOTw3_AddNewWriter.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT1_ReadModel.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT5_StreamRDFCollect.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT2_ReadDataset.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT_RDFXML_WriteProperties.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOT7_ParserPiped.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/riot/ExRIOTw1_writeModel.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/engine/MyQueryEngine.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/update/UpdateExecuteOperations.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/update/UpdateReadFromFile.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/update/UpdateProgrammatic.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/constructquads/ExampleConstructQuads.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/bgpmatching/StageAltMain.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/bgpmatching/OpExecutorAlt.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/bgpmatching/StageGeneratorAlt.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/propertyfunction/localname.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/propertyfunction/labelSearch.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/propertyfunction/uppercase.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/filter/classify.java
/opt/apache-jena-3.9.0/src-examples/arq/examples/aggregates/CustomAggregate.java
/opt/apache-jena-3.9.0/src-examples/data/test1.owl
/opt/apache-jena-3.9.0/src-examples/data/camera.owl
/opt/apache-jena-3.9.0/src-examples/data/eswc-2006-09-21.rdf
/opt/apache-jena-3.9.0/src-examples/data/test2.owl
/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial05.java
/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial04.java
/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial01.java
/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial03.java
/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial10.java
/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial02.java
/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial08.java
/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial09.java
/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial11.java
/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial07.java
/opt/apache-jena-3.9.0/src-examples/jena/examples/rdf/Tutorial06.java
/opt/apache-jena-3.9.0/src-examples/jena/examples/ontology/classHierarchy/Main.java
/opt/apache-jena-3.9.0/src-examples/jena/examples/ontology/classHierarchy/ClassHierarchy.java
/opt/apache-jena-3.9.0/src-examples/jena/examples/ontology/describeClass/Main.java
/opt/apache-jena-3.9.0/src-examples/jena/examples/ontology/describeClass/DescribeClass.java
/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB2.java
/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB_Txn1.java
/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB4.java
/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB6.java
/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB1.java
/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExQuadFilter.java
/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB3.java
/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB_Txn3.java
/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB_Txn2.java
/opt/apache-jena-3.9.0/src-examples/tdb/examples/ExTDB5.java
/opt/apache-jena-3.9.0/lib-src/jena-arq-3.9.0-sources.jar
/opt/apache-jena-3.9.0/lib-src/jena-rdfconnection-3.9.0-sources.jar
/opt/apache-jena-3.9.0/lib-src/jena-tdb-3.9.0-sources.jar
/opt/apache-jena-3.9.0/lib-src/jena-cmds-3.9.0-sources.jar
/opt/apache-jena-3.9.0/lib-src/jena-core-3.9.0-sources.jar
/opt/apache-jena-3.9.0/lib/jackson-core-2.9.6.jar
/opt/apache-jena-3.9.0/lib/commons-csv-1.5.jar
/opt/apache-jena-3.9.0/lib/jena-core-3.9.0.jar
/opt/apache-jena-3.9.0/lib/jackson-databind-2.9.6.jar
/opt/apache-jena-3.9.0/lib/jena-shaded-guava-3.9.0.jar
/opt/apache-jena-3.9.0/lib/slf4j-log4j12-1.7.25.jar
/opt/apache-jena-3.9.0/lib/httpcore-4.4.9.jar
/opt/apache-jena-3.9.0/lib/jena-dboe-base-3.9.0.jar
/opt/apache-jena-3.9.0/lib/jena-tdb2-3.9.0.jar
/opt/apache-jena-3.9.0/lib/jena-iri-3.9.0.jar
/opt/apache-jena-3.9.0/lib/jena-base-3.9.0.jar
/opt/apache-jena-3.9.0/lib/jackson-annotations-2.9.0.jar
/opt/apache-jena-3.9.0/lib/slf4j-api-1.7.25.jar
/opt/apache-jena-3.9.0/lib/commons-lang3-3.4.jar
/opt/apache-jena-3.9.0/lib/commons-io-2.6.jar
/opt/apache-jena-3.9.0/lib/jsonld-java-0.12.1.jar
/opt/apache-jena-3.9.0/lib/log4j-1.2.17.jar
/opt/apache-jena-3.9.0/lib/collection-0.7.jar
/opt/apache-jena-3.9.0/lib/jena-dboe-transaction-3.9.0.jar
/opt/apache-jena-3.9.0/lib/commons-compress-1.17.jar
/opt/apache-jena-3.9.0/lib/jena-dboe-index-3.9.0.jar
/opt/apache-jena-3.9.0/lib/httpclient-cache-4.5.5.jar
/opt/apache-jena-3.9.0/lib/jena-rdfconnection-3.9.0.jar
/opt/apache-jena-3.9.0/lib/jena-tdb-3.9.0.jar
/opt/apache-jena-3.9.0/lib/commons-codec-1.11.jar
/opt/apache-jena-3.9.0/lib/libthrift-0.10.0.jar
/opt/apache-jena-3.9.0/lib/httpclient-4.5.5.jar
/opt/apache-jena-3.9.0/lib/jena-dboe-trans-data-3.9.0.jar
/opt/apache-jena-3.9.0/lib/jena-arq-3.9.0.jar
/opt/apache-jena-3.9.0/lib/jcl-over-slf4j-1.7.25.jar
/opt/apache-jena-3.9.0/lib/commons-cli-1.4.jar
/opt/apache-jena-3.9.0/lib/jena-cmds-3.9.0.jar
/opt/apache-jena-3.9.0/bat/wwwenc.bat
/opt/apache-jena-3.9.0/bat/utf8.bat
/opt/apache-jena-3.9.0/bat/rdfcopy.bat
/opt/apache-jena-3.9.0/bat/tdb2_tdbquery.bat
/opt/apache-jena-3.9.0/bat/infer.bat
/opt/apache-jena-3.9.0/bat/tdbupdate.bat
/opt/apache-jena-3.9.0/bat/rsparql.bat
/opt/apache-jena-3.9.0/bat/trig.bat
/opt/apache-jena-3.9.0/bat/turtle.bat
/opt/apache-jena-3.9.0/bat/nquads.bat
/opt/apache-jena-3.9.0/bat/tdb2_tdbstats.bat
/opt/apache-jena-3.9.0/bat/rdfxml.bat
/opt/apache-jena-3.9.0/bat/update.bat
/opt/apache-jena-3.9.0/bat/rset.bat
/opt/apache-jena-3.9.0/bat/uparse.bat
/opt/apache-jena-3.9.0/bat/sparql.bat
/opt/apache-jena-3.9.0/bat/rdfcat.bat
/opt/apache-jena-3.9.0/bat/tdb2_tdbbackup.bat
/opt/apache-jena-3.9.0/bat/tdbdump.bat
/opt/apache-jena-3.9.0/bat/tdb2_tdbloader.bat
/opt/apache-jena-3.9.0/bat/ntriples.bat
/opt/apache-jena-3.9.0/bat/tdbbackup.bat
/opt/apache-jena-3.9.0/bat/wwwdec.bat
/opt/apache-jena-3.9.0/bat/rdfdiff.bat
/opt/apache-jena-3.9.0/bat/rdfcompare.bat
/opt/apache-jena-3.9.0/bat/tdbstats.bat
/opt/apache-jena-3.9.0/bat/riot.bat
/opt/apache-jena-3.9.0/bat/tdbloader.bat
/opt/apache-jena-3.9.0/bat/qparse.bat
/opt/apache-jena-3.9.0/bat/iri.bat
/opt/apache-jena-3.9.0/bat/tdb2_tdbupdate.bat
/opt/apache-jena-3.9.0/bat/rupdate.bat
/opt/apache-jena-3.9.0/bat/schemagen.bat
/opt/apache-jena-3.9.0/bat/tdbquery.bat
/opt/apache-jena-3.9.0/bat/juuid.bat
/opt/apache-jena-3.9.0/bat/tdb2_tdbcompact.bat
/opt/apache-jena-3.9.0/bat/arq.bat
/opt/apache-jena-3.9.0/bat/rdfparse.bat
/opt/apache-jena-3.9.0/bat/tdb2_tdbdump.bat

%changelog

* Sun Nov 25 2018 Martin Czygan
- autogenerated spec
    
