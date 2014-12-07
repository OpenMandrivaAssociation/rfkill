Summary:	Simple /dev/rfkill userspace tool
Name:		rfkill
Epoch:		1
Version:	0.5
Release:	8
License:	GPLv2+
Group:		System/Base
Url:		http://wireless.kernel.org/en/users/Documentation/rfkill
Source0:	http://wireless.kernel.org/download/%{name}/%{name}-%{version}.tar.xz
Source1:	%{name}.pam
Source2:	%{name}.consoleapp

%description
Rfkill is a simple userspace tool to manipulate /dev/rfkill.
It's needed to enable and disable wireless and bluetooth from 
userspace beginning with 2.6.31 series kernels.

%prep
%setup -q

%build
%make CC=%{__cc}

%install
%makeinstall \
	PREFIX=%{buildroot} \
	BINDIR=%{buildroot}/sbin \
	MANDIR=%{buildroot}/%{_mandir}

# Consolehelper
mkdir -p %{buildroot}%{_bindir}
ln -s consolehelper %{buildroot}%{_bindir}/%{name}
install -m 0644 %{SOURCE1} -D %{buildroot}%{_sysconfdir}/pam.d/%{name}
install -m 0644 %{SOURCE2} -D %{buildroot}%{_sysconfdir}/security/console.apps/%{name}

%files
%doc README
%attr(0755,root,root) /sbin/%{name}
%attr(0755,root,root) %{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/security/console.apps/%{name}
%{_mandir}/man8/%{name}.8.*

