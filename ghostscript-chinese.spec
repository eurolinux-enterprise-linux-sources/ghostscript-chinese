%global common_desc \
ghostscript font configuration files for Chinese fonts.


%global gsdir            %{_datadir}/ghostscript/conf.d
%global umingver         0.2.20080216.1
%global ukaiver          0.2.20080216.1
%global zenheiver        0.9.45

Name:           ghostscript-chinese
Version:        0.4.0
Release:        3%{?dist}
Summary:        Common files for ghostscript-chinese
Group:          User Interface/X
License:        GPLv2+
URL:            http://www.freedesktop.org/wiki/Software/CJKUnifonts
Source0:        http://pwu.fedorapeople.org/ghostscript-chinese/%{name}-%{version}.tar.gz
BuildArch:      noarch

#BuildRequires:
Provides:     cjkuni-fonts-ghostscript = %{version}
Obsoletes:    cjkuni-fonts-ghostscript < 0.2.20080216.1-45
%description
%common_desc

This package consists of files used by other %{name} packages.

%package zh_CN
Summary:      Ghostscript Simplified Chinese fonts configuration files
Group:        User Interface/X
Requires:     ghostscript
Requires:     wqy-zenhei-fonts >= %{zenheiver}
Requires:     %{name} = %{version}-%{release}

%description zh_CN
%common_desc

For Simplified Chinese.

%package zh_TW
Summary:      Ghostscript Traditional Chinese fonts configuration files
Group:        User Interface/X
Requires:     ghostscript
Requires:     cjkuni-uming-fonts = %{umingver}
Requires:     cjkuni-ukai-fonts = %{ukaiver}
Requires:     %{name} = %{version}-%{release}

%description zh_TW
%common_desc

For Traditional Chinese.

%prep
%setup -q -c -n %{name}-%{version}


%build
%{nil}


%install
install -m 0755 -d %{buildroot}%{gsdir}

for gscid in `ls *.zh_CN *.zh_TW`
do
    install -m 0644 -p $gscid %{buildroot}%{gsdir}
done


%files
%defattr(-,root,root,-)
%doc COPYING
%doc README

%files zh_CN
%defattr(-,root,root,-)
%{gsdir}/FAPIcidfmap.zh_CN
%{gsdir}/cidfmap.zh_CN
%{gsdir}/CIDFnmap.zh_CN

%files zh_TW
%defattr(-,root,root,-)
%{gsdir}/FAPIcidfmap.zh_TW
%{gsdir}/cidfmap.zh_TW
%{gsdir}/CIDFnmap.zh_TW


%changelog
* Tue Mar 19 2013 Peng Wu <pwu@redhat.com> - 0.4.0-3
- Fixes summary

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 15 2012 Peng Wu <pwu@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011  Peng Wu <pwu@redhat.com> - 0.3.1-2
- Fixes wqy-zenhei-fonts deps.

* Tue Aug 10 2010  Peng Wu <pwu@redhat.com> - 0.3.1-1
- Renamed from cjkuni-fonts-ghostscript.

* Fri Jul 23 2010  Peng Wu <pwu@redhat.com> - 0.3-1
- Add license file.

* Mon Jul 19 2010  Peng Wu <pwu@redhat.com> - 0.2.20080216.1-44
- Clean up the spec.

* Tue Jul 13 2010  Peng Wu <pwu@redhat.com> - 0.2.20080216.1-43
- The Initial Version.
  Split from cjkuni-fonts.
