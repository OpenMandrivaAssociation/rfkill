Name:		rfkill
Summary:	Simple /dev/rfkill userspace tool
Version:	0.1
Release: 	%mkrel 1
License: 	GPLv2+
Group:		System/Base
Source0:	http://wireless.kernel.org/download/%{name}/%{name}-%{version}.tar.bz2
URL:		http://git.sipsolutions.net/?p=rfkill.git
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Rfkill is a simple userspace tool to manipulate /dev/rfkill.
It's needed to enable and disable wireless and bluetooth from 
userspace beginning with 2.6.31 series kernels.

%prep
%setup -q

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
