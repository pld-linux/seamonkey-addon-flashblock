Summary:	Show flash-button, not flash-animation
Summary(pl.UTF-8):	Wyświetlanie przycisku z ikoną Flash zamiast animacji flash.
%define		_realname	flashblock
Name:		seamonkey-addon-%{_realname}
Version:	1.3.5
Release:	0.1
License:	unknown
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/flashblock/%{_realname}-%{version}.xpi
# Source0-md5:	fa589cc2482da81870c21a38d210c008
Source1:	gen-installed-chrome.sh
URL:		http://flashblock.mozdev.org/
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	seamonkey >= 1.0
#Requires:	macromedia-flash
Requires:	seamonkey >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Flashblock is an extension for the Mozilla, Firefox, and Netscape browsers
that takes a pessimistic approach to dealing with Macromedia Flash content
on a webpage and blocks ALL Flash content from loading. It then leaves
placeholders on the webpage that allow you to click to download and then
view the Flash content.

%prep
%setup -qc
install %{SOURCE1} .
./gen-installed-chrome.sh locale chrome/%{_realname}.jar \
	| sed '/content/s/^locale/content/; /skin/s/^locale/skin/;' \
		> %{_realname}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/%{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}
install %{_realname}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r defaults $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
%{_datadir}/seamonkey/defaults/preferences/%{_realname}.js
