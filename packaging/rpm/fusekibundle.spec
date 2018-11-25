
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
Requires(pre): /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel

%description

Inofficial bundle for FUSEKI triple store. More information at: https://jena.apache.org

%prep

%build

%pre

/usr/bin/getent group fuseki > /dev/null || /usr/sbin/groupadd -r fuseki
/usr/bin/getent passwd fuseki > /dev/null || /usr/sbin/useradd -r -d /opt/apache-jena-fuseki-3.9.0 -s /sbin/nologin -g fuseki fuseki


%%install

mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/bin
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/images
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/test
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/fonts
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/services
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/controllers
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/models
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/util
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/plugins
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/addon
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/lib
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/mode
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/mode/turtle
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/mode/javascript
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/mode/sparql
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/mode/xml
mkdir -p $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/WEB-INF
mkdir -p $RPM_BUILD_ROOT/etc/systemd/system/
install -m 755 apache-jena-fuseki-3.9.0/fuseki-backup $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/fuseki-backup
install -m 644 apache-jena-fuseki-3.9.0/NOTICE $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/NOTICE
install -m 644 apache-jena-fuseki-3.9.0/fuseki.war $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/fuseki.war
install -m 644 apache-jena-fuseki-3.9.0/fuseki-server.bat $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/fuseki-server.bat
install -m 644 apache-jena-fuseki-3.9.0/fuseki.service $RPM_BUILD_ROOT/etc/systemd/system/fuseki.service
install -m 644 apache-jena-fuseki-3.9.0/fuseki.service $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/fuseki.service
install -m 644 apache-jena-fuseki-3.9.0/README $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/README
install -m 644 apache-jena-fuseki-3.9.0/fuseki-server.jar $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/fuseki-server.jar
install -m 755 apache-jena-fuseki-3.9.0/fuseki-server $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/fuseki-server
install -m 755 apache-jena-fuseki-3.9.0/fuseki $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/fuseki
install -m 644 apache-jena-fuseki-3.9.0/LICENSE $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/LICENSE
install -m 755 apache-jena-fuseki-3.9.0/bin/s-delete $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/bin/s-delete
install -m 755 apache-jena-fuseki-3.9.0/bin/s-update $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/bin/s-update
install -m 755 apache-jena-fuseki-3.9.0/bin/s-put $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/bin/s-put
install -m 755 apache-jena-fuseki-3.9.0/bin/s-update-form $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/bin/s-update-form
install -m 755 apache-jena-fuseki-3.9.0/bin/s-query $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/bin/s-query
install -m 755 apache-jena-fuseki-3.9.0/bin/s-post $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/bin/s-post
install -m 755 apache-jena-fuseki-3.9.0/bin/s-head $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/bin/s-head
install -m 755 apache-jena-fuseki-3.9.0/bin/soh $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/bin/soh
install -m 755 apache-jena-fuseki-3.9.0/bin/s-get $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/bin/s-get
install -m 644 apache-jena-fuseki-3.9.0/webapp/dataset.html $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/dataset.html
install -m 644 apache-jena-fuseki-3.9.0/webapp/manage.html $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/manage.html
install -m 644 apache-jena-fuseki-3.9.0/webapp/services.html $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/services.html
install -m 644 apache-jena-fuseki-3.9.0/webapp/admin-logs.html $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/admin-logs.html
install -m 644 apache-jena-fuseki-3.9.0/webapp/index.html $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/index.html
install -m 644 apache-jena-fuseki-3.9.0/webapp/documentation.html $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/documentation.html
install -m 644 apache-jena-fuseki-3.9.0/webapp/validate.html $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/validate.html
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/pivot.min.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/pivot.min.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/jquery.fileupload-noscript.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/jquery.fileupload-noscript.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/font-awesome.min.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/font-awesome.min.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/jquery.dataTables.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/jquery.dataTables.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/jquery.fileupload-ui-noscript.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/jquery.fileupload-ui-noscript.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/qonsole.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/qonsole.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/bootstrap.css.map $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/bootstrap.css.map
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/bootstrap-theme.min.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/bootstrap-theme.min.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/bootstrap-select.min.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/bootstrap-select.min.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/codemirror.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/codemirror.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/yasqe.min.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/yasqe.min.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/jquery.fileupload.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/jquery.fileupload.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/bootstrap-theme.css.map $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/bootstrap-theme.css.map
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/yasr.min.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/yasr.min.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/bootstrap.min.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/bootstrap.min.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/fui.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/fui.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/jquery.fileupload-ui.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/jquery.fileupload-ui.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/css/codemirror.min.css $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/css/codemirror.min.css
install -m 644 apache-jena-fuseki-3.9.0/webapp/images/sort_both.png $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/images/sort_both.png
install -m 644 apache-jena-fuseki-3.9.0/webapp/images/sort_asc_disabled.png $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/images/sort_asc_disabled.png
install -m 644 apache-jena-fuseki-3.9.0/webapp/images/wait30.gif $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/images/wait30.gif
install -m 644 apache-jena-fuseki-3.9.0/webapp/images/sort_desc_disabled.png $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/images/sort_desc_disabled.png
install -m 644 apache-jena-fuseki-3.9.0/webapp/images/sort_desc.png $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/images/sort_desc.png
install -m 644 apache-jena-fuseki-3.9.0/webapp/images/back_disabled.png $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/images/back_disabled.png
install -m 644 apache-jena-fuseki-3.9.0/webapp/images/forward_enabled.png $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/images/forward_enabled.png
install -m 644 apache-jena-fuseki-3.9.0/webapp/images/back_enabled.png $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/images/back_enabled.png
install -m 644 apache-jena-fuseki-3.9.0/webapp/images/favicon.ico $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/images/favicon.ico
install -m 644 apache-jena-fuseki-3.9.0/webapp/images/forward_enabled_hover.png $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/images/forward_enabled_hover.png
install -m 644 apache-jena-fuseki-3.9.0/webapp/images/sort_asc.png $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/images/sort_asc.png
install -m 644 apache-jena-fuseki-3.9.0/webapp/images/back_enabled_hover.png $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/images/back_enabled_hover.png
install -m 644 apache-jena-fuseki-3.9.0/webapp/images/jena-logo-notext-small.png $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/images/jena-logo-notext-small.png
install -m 644 apache-jena-fuseki-3.9.0/webapp/images/forward_disabled.png $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/images/forward_disabled.png
install -m 644 apache-jena-fuseki-3.9.0/webapp/test/test-fuseki-config.ttl $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/test/test-fuseki-config.ttl
install -m 644 apache-jena-fuseki-3.9.0/webapp/fonts/fontawesome-webfont.woff $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/fonts/fontawesome-webfont.woff
install -m 644 apache-jena-fuseki-3.9.0/webapp/fonts/FontAwesome.otf $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/fonts/FontAwesome.otf
install -m 644 apache-jena-fuseki-3.9.0/webapp/fonts/fontawesome-webfont.svg $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/fonts/fontawesome-webfont.svg
install -m 644 apache-jena-fuseki-3.9.0/webapp/fonts/glyphicons-halflings-regular.ttf $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/fonts/glyphicons-halflings-regular.ttf
install -m 644 apache-jena-fuseki-3.9.0/webapp/fonts/glyphicons-halflings-regular.svg $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/fonts/glyphicons-halflings-regular.svg
install -m 644 apache-jena-fuseki-3.9.0/webapp/fonts/glyphicons-halflings-regular.woff $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/fonts/glyphicons-halflings-regular.woff
install -m 644 apache-jena-fuseki-3.9.0/webapp/fonts/fontawesome-webfont.eot $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/fonts/fontawesome-webfont.eot
install -m 644 apache-jena-fuseki-3.9.0/webapp/fonts/fontawesome-webfont.ttf $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/fonts/fontawesome-webfont.ttf
install -m 644 apache-jena-fuseki-3.9.0/webapp/fonts/glyphicons-halflings-regular.eot $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/fonts/glyphicons-halflings-regular.eot
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/common-config.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/common-config.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/main.index.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/main.index.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/fui.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/fui.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/main.manage.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/main.manage.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/main.dataset.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/main.dataset.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/main.validation.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/main.validation.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/qonsole-config.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/qonsole-config.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/services/ping-service.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/services/ping-service.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/services/validation-service.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/services/validation-service.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/controllers/index-controller.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/controllers/index-controller.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/controllers/query-controller.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/controllers/query-controller.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/controllers/upload-controller.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/controllers/upload-controller.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/controllers/dataset-controller.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/controllers/dataset-controller.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/controllers/validation-controller.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/controllers/validation-controller.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/controllers/manage-controller.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/controllers/manage-controller.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-management.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-management.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-selection-list.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-selection-list.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/views/uploadable-file.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/uploadable-file.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/views/datasets-dropdown-list.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/datasets-dropdown-list.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-selector.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-selector.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-stats.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-stats.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-simple-create.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-simple-create.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-info.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-info.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/views/validation-options.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/validation-options.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-edit.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-edit.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/views/tabbed-view-manager.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/tabbed-view-manager.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/views/file-upload.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/file-upload.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/models/fuseki-server.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/models/fuseki-server.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/models/dataset-stats.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/models/dataset-stats.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/models/task.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/models/task.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/models/validation-options.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/models/validation-options.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/models/dataset.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/models/dataset.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/util/page-utils.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/util/page-utils.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-info.tpl $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-info.tpl
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-management.tpl $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-management.tpl
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-edit.tpl $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-edit.tpl
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-selection-list.tpl $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-selection-list.tpl
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-stats.tpl $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-stats.tpl
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-simple-create.tpl $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-simple-create.tpl
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/templates/file-upload.tpl $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/file-upload.tpl
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-selector.tpl $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-selector.tpl
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/app/templates/uploadable-file.tpl $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/uploadable-file.tpl
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.fileupload.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.fileupload.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/jquery-1.10.2.min.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery-1.10.2.min.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.fileupload.local.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.fileupload.local.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.form.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.form.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/qonsole.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/qonsole.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/bootstrap-select.min.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/bootstrap-select.min.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/require.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/require.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/yasr.min.js.map $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/yasr.min.js.map
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/refresh.sh $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/refresh.sh
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.iframe-transport.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.iframe-transport.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/underscore.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/underscore.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/require.min.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/require.min.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/bootstrap.min.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/bootstrap.min.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/sprintf-0.7-beta1.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/sprintf-0.7-beta1.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/pivot.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/pivot.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.dataTables.min.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.dataTables.min.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.ui.widget.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.ui.widget.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.xdomainrequest.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.xdomainrequest.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/pivot.min.js.map $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/pivot.min.js.map
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/backbone-min.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/backbone-min.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/backbone.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/backbone.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/jquery-1.10.2.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery-1.10.2.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/respond.min.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/respond.min.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/jquery-ui.min.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery-ui.min.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/backbone.marionette.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/backbone.marionette.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/yasr.min.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/yasr.min.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/yasqe.min.js.map $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/yasqe.min.js.map
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/yasqe.min.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/yasqe.min.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/pivot.min.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/pivot.min.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/html5shiv.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/html5shiv.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/plugins/text.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/plugins/text.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold/foldcode.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold/foldcode.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold/comment-fold.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold/comment-fold.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold/brace-fold.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold/brace-fold.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold/foldgutter.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold/foldgutter.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold/xml-fold.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold/xml-fold.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/lib/codemirror.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/lib/codemirror.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/mode/turtle/turtle.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/mode/turtle/turtle.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/mode/javascript/javascript.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/mode/javascript/javascript.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/mode/sparql/sparql.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/mode/sparql/sparql.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/js/lib/mode/xml/xml.js $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/mode/xml/xml.js
install -m 644 apache-jena-fuseki-3.9.0/webapp/WEB-INF/web.xml $RPM_BUILD_ROOT/opt/apache-jena-fuseki-3.9.0/webapp/WEB-INF/web.xml

%%post

%%clean

rm -rf $RPM_BUILD_ROOT
rm -rf %%{_tmppath}/%%{name}
rm -rf %%{_topdir}/BUILD/%%{name}

%%files
%%defattr(-,fuseki,fuseki)

/opt/apache-jena-fuseki-3.9.0/fuseki-backup
/opt/apache-jena-fuseki-3.9.0/NOTICE
/opt/apache-jena-fuseki-3.9.0/fuseki.war
/opt/apache-jena-fuseki-3.9.0/fuseki-server.bat
/opt/apache-jena-fuseki-3.9.0/fuseki.service
/opt/apache-jena-fuseki-3.9.0/README
/opt/apache-jena-fuseki-3.9.0/fuseki-server.jar
/opt/apache-jena-fuseki-3.9.0/fuseki-server
/opt/apache-jena-fuseki-3.9.0/fuseki
/opt/apache-jena-fuseki-3.9.0/LICENSE
/opt/apache-jena-fuseki-3.9.0/bin/s-delete
/opt/apache-jena-fuseki-3.9.0/bin/s-update
/opt/apache-jena-fuseki-3.9.0/bin/s-put
/opt/apache-jena-fuseki-3.9.0/bin/s-update-form
/opt/apache-jena-fuseki-3.9.0/bin/s-query
/opt/apache-jena-fuseki-3.9.0/bin/s-post
/opt/apache-jena-fuseki-3.9.0/bin/s-head
/opt/apache-jena-fuseki-3.9.0/bin/soh
/opt/apache-jena-fuseki-3.9.0/bin/s-get
/opt/apache-jena-fuseki-3.9.0/webapp/dataset.html
/opt/apache-jena-fuseki-3.9.0/webapp/manage.html
/opt/apache-jena-fuseki-3.9.0/webapp/services.html
/opt/apache-jena-fuseki-3.9.0/webapp/admin-logs.html
/opt/apache-jena-fuseki-3.9.0/webapp/index.html
/opt/apache-jena-fuseki-3.9.0/webapp/documentation.html
/opt/apache-jena-fuseki-3.9.0/webapp/validate.html
/opt/apache-jena-fuseki-3.9.0/webapp/css/pivot.min.css
/opt/apache-jena-fuseki-3.9.0/webapp/css/jquery.fileupload-noscript.css
/opt/apache-jena-fuseki-3.9.0/webapp/css/font-awesome.min.css
/opt/apache-jena-fuseki-3.9.0/webapp/css/jquery.dataTables.css
/opt/apache-jena-fuseki-3.9.0/webapp/css/jquery.fileupload-ui-noscript.css
/opt/apache-jena-fuseki-3.9.0/webapp/css/qonsole.css
/opt/apache-jena-fuseki-3.9.0/webapp/css/bootstrap.css.map
/opt/apache-jena-fuseki-3.9.0/webapp/css/bootstrap-theme.min.css
/opt/apache-jena-fuseki-3.9.0/webapp/css/bootstrap-select.min.css
/opt/apache-jena-fuseki-3.9.0/webapp/css/codemirror.css
/opt/apache-jena-fuseki-3.9.0/webapp/css/yasqe.min.css
/opt/apache-jena-fuseki-3.9.0/webapp/css/jquery.fileupload.css
/opt/apache-jena-fuseki-3.9.0/webapp/css/bootstrap-theme.css.map
/opt/apache-jena-fuseki-3.9.0/webapp/css/yasr.min.css
/opt/apache-jena-fuseki-3.9.0/webapp/css/bootstrap.min.css
/opt/apache-jena-fuseki-3.9.0/webapp/css/fui.css
/opt/apache-jena-fuseki-3.9.0/webapp/css/jquery.fileupload-ui.css
/opt/apache-jena-fuseki-3.9.0/webapp/css/codemirror.min.css
/opt/apache-jena-fuseki-3.9.0/webapp/images/sort_both.png
/opt/apache-jena-fuseki-3.9.0/webapp/images/sort_asc_disabled.png
/opt/apache-jena-fuseki-3.9.0/webapp/images/wait30.gif
/opt/apache-jena-fuseki-3.9.0/webapp/images/sort_desc_disabled.png
/opt/apache-jena-fuseki-3.9.0/webapp/images/sort_desc.png
/opt/apache-jena-fuseki-3.9.0/webapp/images/back_disabled.png
/opt/apache-jena-fuseki-3.9.0/webapp/images/forward_enabled.png
/opt/apache-jena-fuseki-3.9.0/webapp/images/back_enabled.png
/opt/apache-jena-fuseki-3.9.0/webapp/images/favicon.ico
/opt/apache-jena-fuseki-3.9.0/webapp/images/forward_enabled_hover.png
/opt/apache-jena-fuseki-3.9.0/webapp/images/sort_asc.png
/opt/apache-jena-fuseki-3.9.0/webapp/images/back_enabled_hover.png
/opt/apache-jena-fuseki-3.9.0/webapp/images/jena-logo-notext-small.png
/opt/apache-jena-fuseki-3.9.0/webapp/images/forward_disabled.png
/opt/apache-jena-fuseki-3.9.0/webapp/test/test-fuseki-config.ttl
/opt/apache-jena-fuseki-3.9.0/webapp/fonts/fontawesome-webfont.woff
/opt/apache-jena-fuseki-3.9.0/webapp/fonts/FontAwesome.otf
/opt/apache-jena-fuseki-3.9.0/webapp/fonts/fontawesome-webfont.svg
/opt/apache-jena-fuseki-3.9.0/webapp/fonts/glyphicons-halflings-regular.ttf
/opt/apache-jena-fuseki-3.9.0/webapp/fonts/glyphicons-halflings-regular.svg
/opt/apache-jena-fuseki-3.9.0/webapp/fonts/glyphicons-halflings-regular.woff
/opt/apache-jena-fuseki-3.9.0/webapp/fonts/fontawesome-webfont.eot
/opt/apache-jena-fuseki-3.9.0/webapp/fonts/fontawesome-webfont.ttf
/opt/apache-jena-fuseki-3.9.0/webapp/fonts/glyphicons-halflings-regular.eot
/opt/apache-jena-fuseki-3.9.0/webapp/js/common-config.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/main.index.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/fui.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/main.manage.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/main.dataset.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/main.validation.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/qonsole-config.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/services/ping-service.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/services/validation-service.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/controllers/index-controller.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/controllers/query-controller.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/controllers/upload-controller.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/controllers/dataset-controller.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/controllers/validation-controller.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/controllers/manage-controller.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-management.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-selection-list.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/uploadable-file.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/datasets-dropdown-list.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-selector.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-stats.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-simple-create.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-info.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/validation-options.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/dataset-edit.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/tabbed-view-manager.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/views/file-upload.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/models/fuseki-server.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/models/dataset-stats.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/models/task.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/models/validation-options.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/models/dataset.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/util/page-utils.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-info.tpl
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-management.tpl
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-edit.tpl
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-selection-list.tpl
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-stats.tpl
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-simple-create.tpl
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/file-upload.tpl
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/dataset-selector.tpl
/opt/apache-jena-fuseki-3.9.0/webapp/js/app/templates/uploadable-file.tpl
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.fileupload.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery-1.10.2.min.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.fileupload.local.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.form.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/qonsole.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/bootstrap-select.min.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/require.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/yasr.min.js.map
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/refresh.sh
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.iframe-transport.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/underscore.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/require.min.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/bootstrap.min.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/sprintf-0.7-beta1.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/pivot.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.dataTables.min.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.ui.widget.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery.xdomainrequest.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/pivot.min.js.map
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/backbone-min.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/backbone.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery-1.10.2.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/respond.min.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/jquery-ui.min.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/backbone.marionette.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/yasr.min.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/yasqe.min.js.map
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/yasqe.min.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/pivot.min.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/html5shiv.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/plugins/text.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold/foldcode.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold/comment-fold.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold/brace-fold.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold/foldgutter.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/addon/fold/xml-fold.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/lib/codemirror.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/mode/turtle/turtle.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/mode/javascript/javascript.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/mode/sparql/sparql.js
/opt/apache-jena-fuseki-3.9.0/webapp/js/lib/mode/xml/xml.js
/opt/apache-jena-fuseki-3.9.0/webapp/WEB-INF/web.xml
/etc/systemd/system/fuseki.service


%postun

rm -rf /opt/apache-jena-fuseki-3.9.0
/usr/sbin/userdel fuseki

%changelog

* Sun Nov 25 2018 Martin Czygan
- autogenerated spec
    
