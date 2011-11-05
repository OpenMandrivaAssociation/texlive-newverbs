# revision 23342
# category Package
# catalog-ctan /macros/latex/contrib/newverbs
# catalog-date 2011-07-25 14:34:08 +0200
# catalog-license lppl1.3
# catalog-version 1.3
Name:		texlive-newverbs
Version:	1.3
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/newverbs/newverbs.sty
%doc %{_texmfdistdir}/doc/latex/newverbs/README
%doc %{_texmfdistdir}/doc/latex/newverbs/newverbs.pdf
#- source
%doc %{_texmfdistdir}/source/latex/newverbs/newverbs.dtx
%doc %{_texmfdistdir}/source/latex/newverbs/newverbs.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
