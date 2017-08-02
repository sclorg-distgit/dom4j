%{?scl:%scl_package dom4j}
%{!?scl:%global pkg_name %{name}}

# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Name:           %{?scl_prefix}dom4j
Version:        2.0.0
Release:        1.1%{?dist}
Epoch:          0
Summary:        Open Source XML framework for Java
License:        BSD
URL:            https://dom4j.github.io/
BuildArch:      noarch

Source0:        https://github.com/%{pkg_name}/%{pkg_name}/archive/v%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/%{pkg_name}/%{pkg_name}/%{version}/%{pkg_name}-%{version}.pom


BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(jaxen:jaxen)
BuildRequires:  %{?scl_prefix}mvn(javax.xml.stream:stax-api)
BuildRequires:  %{?scl_prefix}mvn(net.java.dev.msv:xsdlib)
BuildRequires:  %{?scl_prefix}mvn(xpp3:xpp3)
BuildRequires:  %{?scl_prefix}mvn(javax.xml.bind:jaxb-api)

# Test deps
BuildRequires:  %{?scl_prefix}mvn(org.testng:testng)
BuildRequires:  %{?scl_prefix}mvn(xerces:xercesImpl)
BuildRequires:  %{?scl_prefix}mvn(xalan:xalan)

%description
dom4j is an Open Source XML framework for Java. dom4j allows you to read,
write, navigate, create and modify XML documents. dom4j integrates with
DOM and SAX and is seamlessly integrated with full XPath support.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
Javadoc for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q

%mvn_alias org.%{pkg_name}:%{pkg_name} %{pkg_name}:%{pkg_name}
%mvn_file : %{pkg_name}/%{pkg_name} %{pkg_name}

cp %{SOURCE1} pom.xml

# optional deps missing from pom
%pom_add_dep javax.xml.stream:stax-api::provided
%pom_add_dep net.java.dev.msv:xsdlib::provided
%pom_add_dep xpp3:xpp3::provided
%pom_add_dep javax.xml.bind:jaxb-api::provided

# Remove support for ancient xpp2 (deprecated and not developed since 2003)
rm -r src/main/java/org/dom4j/xpp
rm src/main/java/org/dom4j/io/XPPReader.java

# non-deterministic test
rm src/test/java/org/dom4j/util/PerThreadSingletonTest.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 0:2.0.0-1.1
- Automated package import and SCL-ization

* Wed Mar 29 2017 Michael Simacek <msimacek@redhat.com> - 0:2.0.0-1
- Upgrade to upstream version 2.0.0

* Wed Mar 22 2017 Michael Simacek <msimacek@redhat.com> - 0:1.6.1-30
- Drop support for ancient xpp2

* Tue Mar  7 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.6.1-29
- Don't hardcode package name

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.6.1-27
- Fix build-dependency on jaxen

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.6.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Michal Srb <msrb@redhat.com> - 0:1.6.1-24
- Add symlink for backward compatibility

* Mon Jun 08 2015 Michal Srb <msrb@redhat.com> - 0:1.6.1-23
- Adapt to current guidelines

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.6.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.6.1-21
- Use .mfiles generated during build

* Fri Dec 06 2013 Michal Srb <msrb@redhat.com> - 0:1.6.1-20
- Add ability to disable HTML handling

* Wed Oct 16 2013 Michal Srb <msrb@redhat.com> - 0:1.6.1-19
- Port to JAXP 1.4

* Wed Aug 07 2013 Michal Srb <msrb@redhat.com> - 0:1.6.1-18
- Unversioned doc dir (Resolves: #993729)
- See: http://fedoraproject.org/wiki/Changes/UnversionedDocdirs

* Fri Aug 02 2013 Michal Srb <msrb@redhat.com> - 0:1.6.1-17
- Add create-tarball.sh script to SRPM

* Thu Jul 25 2013 Michal Srb <msrb@redhat.com> - 0:1.6.1-16
- Properly remove references to ConcurrentReaderHashMap

* Tue Jul 02 2013 Michal Srb <msrb@redhat.com> - 0:1.6.1-15
- Remove file with unclear licensing (Resolves: rhbz#976180)

* Wed Jun 19 2013 Michal Srb <msrb@redhat.com> - 0:1.6.1-14
- Install license file with javadoc subpackage

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov  1 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.6.1-12
- Add maven POM

* Mon Oct 29 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.6.1-11
- Cleanup source tarball from non-free content
- Resolves: rhbz#848875

* Fri Oct 12 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.6.1-10
- Disable test dependencies because tests are skipped

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 6 2012 Alexander Kurtakov <akurtako@redhat.com> 0:1.6.1-8
- Simplify packaging and remove old things.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.6.1-3
- drop repotag

* Wed Oct 17 2007 Deepak Bhole <dbhole@redhat.com> 1.6.1-2jpp.3
- Resaolve bz#302321: Add copyright header that was accidentally removed.

* Mon Mar 26 2007 Nuno Santos <nsantos@redhat.com> - 0:1.6.1-2jpp.2
- fix unowned directory

* Wed Feb 14 2007 Jeff Johnston <jjohnstn@redhat.com> - 0:1.6.1-2jpp.1
- Resolves: #227049
- Updated per Fedora package review process
- Modified dom4j-1.6.1-build_xml.patch to include jaxp 1.2 apis on
  boot classpath
- Added new patch for javadocs
- Add buildrequires for jaxp = 1.2

* Mon Jan 30 2006 Ralph Apel <r.apel@r-apel.de> - 0:1.6.1-2jpp
- Change STAX dependency to free bea-stax and bea-stax-api

* Wed Aug 17 2005 Ralph Apel <r.apel@r-apel.de> - 0:1.6.1-1jpp
- Upgrade to 1.6.1
- Now requires xpp3 additionally to xpp2

* Thu Sep 09 2004 Ralph Apel <r.apel@r-apel.de> - 0:1.5-1jpp
- Upgrade to 1.5
- Drop saxpath requirement as this is now included in jaxen

* Fri Aug 20 2004 Ralph Apel <r.apel@r-apel.de> - 0:1.4-3jpp
- Upgrade to Ant 1.6.X
- Build with ant-1.6.2

* Tue Jul 06 2004 Ralph Apel <r.apel@r-apel.de> - 0:1.4-2jpp
- Replace non-free msv with free relaxngDatatype xsdlib isorelax msv-strict
- Relax some versioned dependencies

* Mon Jan 19 2004 Ralph Apel <r.apel@r-apel.de> - 0:1.4-1jpp
- First JPackage release
