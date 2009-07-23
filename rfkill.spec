Name:		rfkill
Summary:	Simple /dev/rfkill userspace tool
Epoch:		1
Version:	0.1
Release: 	%mkrel 1
License: 	GPLv2+
Group:		System/Base
Source0:	http://wireless.kernel.org/download/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}.pam
Source2:	%{name}.consoleapp
URL:		http://wireless.kernel.org/en/users/Documentation/rfkill
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

# Consolehelper
%{__mkdir_p} %{buildroot}%{_bindir}
%{__ln_s} consolehelper %{buildroot}%{_bindir}/%{name}
%{__install} -m 0644 %{SOURCE1} -D %{buildroot}%{_sysconfdir}/pam.d/%{name}
%{__install} -m 0644 %{SOURCE2} -D %{buildroot}%{_sysconfdir}/security/console.apps/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README
%attr(0755,root,root) /sbin/%{name}
%attr(0755,root,root) %{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/security/console.apps/%{name}
