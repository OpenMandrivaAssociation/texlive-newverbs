# revision 26258
# category Package
# catalog-ctan /macros/latex/contrib/newverbs
# catalog-date 2012-05-08 15:35:13 +0200
# catalog-license lppl1.3
# catalog-version 1.3a
Name:		texlive-newverbs
Version:	1.3a
Release:	11
Summary:	Define new versions of \verb, including short verb versions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/newverbs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newverbs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newverbs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newverbs.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the definition of \verb variants which add
TeX code before and after the verbatim text (e.g., quotes or
surrounding \fbox{}). When used together with the shortvrb
package it allows the definition of short verbatim characters
which use this package's variant instead of the normal \verb.
In addition, it is possible to collect an argument verbatim to
either typeset or write it into a file. The \Verbdef command
defines verbatim text to a macro which can later be used to
write the verbatim text to a file.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/newverbs/newverbs.sty
%doc %{_texmfdistdir}/doc/latex/newverbs/README
%doc %{_texmfdistdir}/doc/latex/newverbs/newverbs.pdf
#- source
%doc %{_texmfdistdir}/source/latex/newverbs/newverbs.dtx
%doc %{_texmfdistdir}/source/latex/newverbs/newverbs.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3a-1
+ Revision: 804954
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 754341
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 719116
- texlive-newverbs
- texlive-newverbs
- texlive-newverbs
- texlive-newverbs

