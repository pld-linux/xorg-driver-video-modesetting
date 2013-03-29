Summary:	X.org generic video modesetting driver
Summary(pl.UTF-8):	Ogólny sterownik obrazu X.org oparty na funkcji modesetting
Name:		xorg-driver-video-modesetting
Version:	0.7.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-modesetting-%{version}.tar.bz2
# Source0-md5:	38e64eb09cef9bdf1de400bbe9818321
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.2
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	udev-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.10
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel
%{?requires_xorg_xserver_videodrv}
Requires:	libdrm >= 2.2
Requires:	xorg-lib-libpciaccess >= 0.10
Requires:	xorg-xserver-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an X.org video driver for KMS devices. This is a
non-accelerated driver, the following framebuffer depths are
supported: 8, 15, 16, 24. All visual types are supported for depth 8,
and TrueColor visual is supported for the other depths.  RandR 1.2 is
supported.

%description -l pl.UTF-8
Ten pakiet zawiera ogólny sterownik obrazu X.org dla urządzeń
obsługiwanych przez KMS w jądrze Linuksa. Sterownik jest nie
akcelerowany, obsługiwane są następujące głębie framebuffera: 8, 15,
16, 24 bity na piksel. Dla 8 bitów obsługiwane są wszystkie rodzaje
ekranów, dla pozostałych TrueColor. RandR 1.2 też jest obsługiwany.

%prep
%setup -q -n xf86-video-modesetting-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/modesetting_drv.so
%{_mandir}/man4/modesetting.4*
