Summary: X.Org X11 libXfont2 runtime library
Name: libXfont2
Version: 2.0.6
Release: 5%{?dist}.3
License: BSD-2-Clause AND BSD-4-Clause-UC AND HPND-sell-variant AND MIT-open-group AND SMLNJ AND X11
URL: http://www.x.org

Source0: http://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(fontsproto)
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-xtrans-devel >= 1.0.3-3
BuildRequires: libfontenc-devel
BuildRequires: freetype-devel

Patch:         0001-bitscale-fix-integer-overflow-in-BitmapScaleBitmaps-.patch
Patch:         0002-pcfread-validate-bitmap-sizes-and-offsets-against-pe.patch
Patch:         0003-bitscale-add-bounds-check-to-computeProps-for-proper.patch
# https://gitlab.freedesktop.org/xorg/lib/libxfont/-/commit/c2d222bb22c623d8a40f3275077fc7e6617f2c8a
Patch:         0004-fserve-bounds-check-cumulative-glyph-data-writes-in-.patch
# https://redhat.atlassian.net/browse/RHEL-221949
# https://gitlab.freedesktop.org/xorg/lib/libxfont/-/commit/668fea81f40bcb48ec67fb55d0b851049d265290
Patch:         libXfont2-2.0.6-CVE-2026-59679.patch

%description
X.Org X11 libXfont2 runtime library

%package devel
Summary: X.Org X11 libXfont2 development package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libfontenc-devel%{?_isa}

%description devel
X.Org X11 libXfont development package

%prep
%autosetup -p1

%build
autoreconf -v --install --force
export CFLAGS="$RPM_OPT_FLAGS -Os"
%configure --disable-static
make %{?_smp_mflags}  

%install
%make_install

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%license COPYING
%doc AUTHORS README.md ChangeLog
%{_libdir}/libXfont2.so.2*

%files devel
%{_includedir}/X11/fonts/libxfont2.h
%{_libdir}/libXfont2.so
%{_libdir}/pkgconfig/xfont2.pc

%changelog
* Thu Aug 06 2026 RHEL Packaging Agent <redhat-ymir-agent@redhat.com> - 2.0.6-5.3
- CVE fix for: CVE-2026-59679
  Resolves: https://redhat.atlassian.net/browse/RHEL-221949

* Thu Aug 06 2026 RHEL Packaging Agent <redhat-ymir-agent@redhat.com> - 2.0.6-5.2
- CVE fix for: CVE-2026-44950
  Resolves: https://redhat.atlassian.net/browse/RHEL-222024

* Wed Jul 08 2026 Olivier Fourdan <ofourdan@redhat.com> - 2.0.6-5.1
- CVE fix for: CVE-2026-56001, CVE-2026-56002, CVE-2026-56003
  Resolves: https://redhat.atlassian.net/browse/RHEL-191882
  Resolves: https://redhat.atlassian.net/browse/RHEL-191930
  Resolves: https://redhat.atlassian.net/browse/RHEL-191949

* Tue Oct 29 2024 Troy Dawson <tdawson@redhat.com> - 2.0.6-5
- Bump release for October 2024 mass rebuild:
  Resolves: RHEL-64018

* Mon Jun 24 2024 Troy Dawson <tdawson@redhat.com> - 2.0.6-4
- Bump release for June 2024 mass rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 05 2023 José Expósito <jexposit@redhat.com> - 2.0.6-1
- libXfont2 2.0.6

* Thu Sep 07 2023 José Expósito <jexposit@redhat.com> - 2.0.3-16
- SPDX Migration

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 11:25:30 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 2.0.3-9
- Add BuildRequires for make

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Adam Jackson <ajax@redhat.com> - 2.0.3-5
- Rebuild for xtrans 1.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Adam Jackson <ajax@redhat.com> - 2.0.3-2
- Use ldconfig scriptlet macros

* Mon Feb 26 2018 Benjamin Tissoires <benjamin.tissoires@redhat.com> 2.0.3-1
- libXfont 2.0.3 (CVE-2017-16611)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Adam Jackson <ajax@redhat.com> - 2.0.2-1
- libXfont 2.0.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 28 2016 Hans de Goede <hdegoede@redhat.com> - 2.0.1-2
- Add some fixes from upstream git master

* Wed Jun 08 2016 Adam Jackson <ajax@redhat.com> - 2.0.2-1
- Initial packaging forked from libXfont

