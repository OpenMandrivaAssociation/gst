%global uuid    com.leinardi.%{name}

Name:           gst
Version:        0.6.1
Release:        1
Summary:        System utility designed to stress and monitoring various hardware components

License:        GPLv3+
URL:            https://gitlab.com/leinardi/gst
Source0:        https://gitlab.com/leinardi/gst/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  meson
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  python-devel
Requires:       dbus
Requires:       dmidecode
Requires:       hicolor-icon-theme
Requires:       python3dist(cairocffi)
Requires:       python3dist(pip)
Requires:       python3dist(pygobject)
Requires:       python3dist(python-dateutil)
Requires:       python-humanfriendly
Requires:       python-injector
Requires:       python-matplotlib-gtk
Requires:       python-peewee
Requires:       python-psutil
Requires:       python-pyxdg
Requires:       python-pyyaml
Requires:       python-requests
Requires:       python-rx
Requires:       stress-ng
Requires:       libaio
Requires:       lm_sensors
Requires:       zlib


%description
GST is a GTK system utility designed to stress and monitoring various hardware
components like CPU and RAM.

- Run different CPU and memory stress tests
- Run multi and single core benchmark
- Show Processor information (name, cores, threads, family, model, stepping,
  flags,bugs, etc)
- Show Processor's cache information
- Show Motherboard information (vendor, model, bios version, bios date, etc)
- Show RAM information (size, speed, rank, manufacturer, part number, etc)
- Show CPU usage (core %, user %, load avg, etc)
- Show Memory usage
- Show CPU's physical's core clock (current, min, max)
- Show Hardware monitor (info provided by sys/class/hwmon)


%prep
%autosetup
sed -e '/meson_post_install/d' -i meson.build


%build
%meson
%meson_build


%install
%meson_install
rm -r %{buildroot}%{_datadir}/icons/hicolor/*@2x/


#check
#appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
#desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING.txt
%doc CHANGELOG.md README.md RELEASING.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/symbolic/*/*.svg
%{_metainfodir}/*.xml
%{python_sitelib}/%{name}/
