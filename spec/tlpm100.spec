Name:		tlpm100
Version:	1.0
Release:	1%{?dist}
Summary:	UDEV rules for Thorlabs PM100 USB devices

Group:		System Environment/Base
License:	GPL
URL:		https://bitbucket.org/europeanspallationsource/m-epics-tlpm100
Source0:	%{name}-%{version}.tar.gz

%description
The UDEV rules file shall adjust the permissions of the /dev node such
that regular user shall be able to access the USB device in read/write
mode.

%prep
%setup -q

%build

%install
install -m 0755 -d $RPM_BUILD_ROOT/etc/udev/rules.d
install -m 0644 88-thorlabs-pm100.rules $RPM_BUILD_ROOT/etc/udev/rules.d

%post
udevadm control --reload

%files
%dir /etc/udev/rules.d
/etc/udev/rules.d/88-thorlabs-pm100.rules

%clean
rm -fr $RPM_BUILD_ROOT

%changelog
* Thu Dec 22 2016 Hinko Kocevar <hinko.kocevar@esss.se> 1.0-1
- Initial packaging.
