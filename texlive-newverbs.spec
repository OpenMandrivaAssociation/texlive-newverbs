Name:		texlive-newverbs
Version:	64833
Release:	1
Summary:	Define new versions of \verb, including short verb versions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/newverbs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newverbs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newverbs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newverbs.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/newverbs
%doc %{_texmfdistdir}/doc/latex/newverbs
#- source
%doc %{_texmfdistdir}/source/latex/newverbs

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
