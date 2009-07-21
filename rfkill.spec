#
# Until we get a real release, we use git snapshots
%define gitdate	20090705
%define rel	1

Name:		rfkill
Summary:	Simple /dev/rfkill userspace tool
Version:	%{gitdate}
Release: 	%mkrel %{rel}
License: 	GPLv2+
Group: 		System/Base
Source0: 	%{name}-%{gitdate}.tar.bz2
URL:		http://git.sipsolutions.net/?p=rfkill.git
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Rfkill is a simple userspace tool to manipulate /dev/rfkill.
It's needed to enable and disable wireless and bluetooth from userspace
beginning with 2.6.31 series kernels.

%prep
%setup -q -n %{name}

%build
%make

%install
rm -rf %{buildroot}
%{makeinstall} \
	PREFIX=%{buildroot} \
	BINDIR=%{buildroot}/sbin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/sbin/rfkill
%doc COPYING README
