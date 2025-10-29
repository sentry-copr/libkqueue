Name:           libkqueue
Version:        2.6.3
Release:        1%{?dist}
Summary:        kqueue compatibility library

License:        MIT and BSD
URL:            https://github.com/mheily/libkqueue
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake

%package static
Summary:        Static library for %{name}

%description static
Static library for %{name}

%package devel
Summary:        Development files for %{name}

%description devel
Development files for %{name}

%description
A user space implementation of the kqueue kernel event notification mechanism libkqueue acts
as a translator between the kevent structure and the native kernel facilities on Linux, Android,
Solaris, and Windows.

%prep
%autosetup


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md BUGS.md
%{_libdir}/libkqueue.so.0

%files static
%{_libdir}/libkqueue.a

%files devel
%{_includedir}/kqueue/
%{_libdir}/libkqueue.so
%{_libdir}/pkgconfig/libkqueue.pc
%{_mandir}/man2/kqueue.2.*

%changelog
* Wed Oct 29 2025 Jan200101 <sentrycraft123@gmail.com> - 2.6.3-1
- Update to 2.6.3

* Wed Apr 19 2023 Jan Drögehoff <sentrycraft123@gmail.com> - 2.6.1-1
- Update to 2.6.1

* Sun Mar 06 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 2.5.0-1
- initial spec

