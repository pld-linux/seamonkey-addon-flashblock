Summary:	Show flash-button, not flash-animation
Summary(pl.UTF-8):	Wyświetlanie przycisku z ikoną Flash zamiast animacji flash
%define		_realname	flashblock
Name:		seamonkey-addon-%{_realname}
Version:	1.5.8
Release:	1
License:	MPL 1.1/GPL 2.0/LGPL 2.1
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/flashblock/%{_realname}-%{version}.xpi
# Source0-md5:	0fd33324aa41b213ccf40170d753168e
Source1:	gen-installed-chrome.sh
URL:		http://flashblock.mozdev.org/
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	seamonkey >= 1.0
Requires:	seamonkey >= 1.0
#Suggests:	browser(flash)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/seamonkey/chrome

%description
Flashblock is an extension for the Mozilla, Firefox, and Netscape
browsers that takes a pessimistic approach to dealing with Macromedia
Flash content on a webpage and blocks ALL Flash content from loading.
It then leaves placeholders on the webpage that allow you to click to
download and then view the Flash content.

%description -l pl.UTF-8
Flashblock to rozszerzenie dla przeglądarek Mozilla, Firefox i
Netscape przyjmujące pesymistyczne podejście do obsługi treści w
formacie Macromedia Flash na stronach i blokujące wczytywanie
WSZYSTKICH elementów we Flashu. Zamiast nich pojawiają się zaślepki,
które można kliknąć w celu ściągnięcia i obejrzenia treści we Flashu.

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
