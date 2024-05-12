Name:           gluster-exporter
Version:        1.0
Release:        2%{?dist}
Summary:        Test build rpm

License:        GPLv2.1
#URL:            
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang
Requires:       glusterfs-server >= 11.0

Provides:       %{name} = %{version}

%description
The project gluster-prometheus provides set of metrics collectors which
would be run on gluster storage nodes. These would generate metrics for
consumption by prometheus server.

%global debug_package %{nil}

%prep
%autosetup


%build
go build -ldflags "-X main.exporterVersion=%{version} -X main.defaultConfFile=/etc/gluster-explorer/gluster-explorer.toml -w -s" -v -o %{name}

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 dep/%{name}.toml %{buildroot}%{_sysconfdir}/%{name}/gluster-exporter.toml
install -Dpm 0644 dep/%{name}.service %{buildroot}%{_unitdir}/%{name}.service

%files
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.toml


%changelog
* Sun May 12 2024 Ivan Ivanov <kasper_wps@mail.ru>
- First release
