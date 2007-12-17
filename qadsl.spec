%define	name	qadsl
%define	version	1.3.3
%define	release	%mkrel 3

Summary:	Autologin & Keep-Alive Daemon for Internet Connections
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Servers 
URL:		http://savannah.nongnu.org/projects/qadsl/
Source:		%{name}-%{version}.tar.bz2

%description
qADSL is an auto-login & keep-alive daemon for Internet connections.
It was created to automate the annoying login process of several
Swedish ISP's, e.g., Telia ADSL, COMHEM and Tiscali. All of which use
the Orbyte Wireless System from Swedish company ServiceFactory AB --
see <http://www.servicefactory.se> for more info.

If our dear ISP's could keep better tabs on their ports vs. their
subscribers then this program would be obsolete. Would we all not be
a lot happier to simply pay for our Internet connection and be online
as long as our NIC and the ISP's switch have a linkup?

%prep

%setup -q

%build

%configure2_5x --sbindir=/sbin

%make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std

# clean up
rm -rf %{buildroot}%{_infodir}

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc INSTALL
%config(noreplace) %{_sysconfdir}/%{name}.conf
/sbin/%{name}
%{_mandir}/man5/*
%{_mandir}/man8/*

