#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-StackTrace
Version  : 2.02
Release  : 2
URL      : http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Devel-StackTrace-2.02.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Devel-StackTrace-2.02.tar.gz
Summary  : 'An object representing a stack trace'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Devel-StackTrace-doc

%description
# NAME
Devel::StackTrace - An object representing a stack trace
# VERSION
version 2.02

%package doc
Summary: doc components for the perl-Devel-StackTrace package.
Group: Documentation

%description doc
doc components for the perl-Devel-StackTrace package.


%prep
%setup -q -n Devel-StackTrace-2.02

%build
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/Devel/StackTrace.pm
/usr/lib/perl5/site_perl/5.24.0/Devel/StackTrace/Frame.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
