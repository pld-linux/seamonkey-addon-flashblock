Summary:	Show flash-button, not flash-animation
Summary(pl):	Wy�wietlanie przycisku z ikon� Flash zamiast animacji flash.
%define		_realname	flashblock
Name:		seamonkey-addon-%{_realname}
Version:	1.5.2
Release:	0.1
License:	unknown
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/flashblock/%{_realname}-%{version}.xpi
# Source0-md5:	dd8d74afd97f0f913c9002e36df2ca5b
Source1:	%{_realname}-installed-chrome.txt
URL:		http://flashblock.mozdev.org/
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	seamonkey >= 1.0
Requires:	macromedia-flash
Requires:	seamonkey >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flashblock is an extension for the Mozilla, Firefox, and Netscape browsers
that takes a pessimistic approach to dealing with Macromedia Flash content
on a webpage and blocks ALL Flash content from loading. It then leaves
placeholders on the webpage that allow you to click to download and then
view the Flash content.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},%{_libdir}}/seamonkey

unzip %{SOURCE0} -d $RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/chrome
mv $RPM_BUILD_ROOT/defaults/preferences $RPM_BUILD_ROOT/defaults/pref
mv $RPM_BUILD_ROOT/{chrome,defaults} $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_datadir}/seamonkey/chrome/%{_realname}.jar
%{_datadir}/seamonkey/chrome/%{_realname}-installed-chrome.txt
%{_datadir}/seamonkey/defaults/pref/%{_realname}.js
