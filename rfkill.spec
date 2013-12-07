Name:		rfkill
Summary:	Simple /dev/rfkill userspace tool
Epoch:		1
Version:	0.5
Release:	2
License:	GPLv2+
Group:		System/Base
Source0:	http://wireless.kernel.org/download/%{name}/%{name}-%{version}.tar.xz
Source1:	%{name}.pam
Source2:	%{name}.consoleapp
URL:		http://wireless.kernel.org/en/users/Documentation/rfkill

%description
Rfkill is a simple userspace tool to manipulate /dev/rfkill.
It's needed to enable and disable wireless and bluetooth from 
userspace beginning with 2.6.31 series kernels.

%prep
%setup -q

%build
%make

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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.4-3mdv2011.0
+ Revision: 669421
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.4-2mdv2011.0
+ Revision: 607364
- rebuild

* Sat Feb 06 2010 Thomas Backlund <tmb@mandriva.org> 1:0.4-1mdv2010.1
+ Revision: 501381
- update to 0.4

* Thu Sep 03 2009 Thomas Backlund <tmb@mandriva.org> 1:0.3-1mdv2010.0
+ Revision: 427583
- update to 0.3

* Tue Aug 25 2009 Thomas Backlund <tmb@mandriva.org> 1:0.2-1mdv2010.0
+ Revision: 421256
- update to 0.2
- drop patch0
- add manpage

* Thu Aug 13 2009 Thomas Backlund <tmb@mandriva.org> 1:0.1-2mdv2010.0
+ Revision: 416106
- update to git 2009-07-23

* Thu Jul 23 2009 Thomas Backlund <tmb@mandriva.org> 1:0.1-1mdv2010.0
+ Revision: 398752
- add consolehelper support
- update url
- first official version is out

* Tue Jul 21 2009 Thomas Backlund <tmb@mandriva.org> 20090705-1mdv2010.0
+ Revision: 398374
- initial release, git snapshot 20090705
- Created package structure for rfkill.

