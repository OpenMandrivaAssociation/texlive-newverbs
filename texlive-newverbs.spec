%global tl_name newverbs
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6a
Release:	%{tl_revision}.1
Summary:	Define new versions of \verb, including short verb versions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/newverbs
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newverbs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newverbs.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newverbs.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the definition of \verb variants which add TeX code
before and after the verbatim text (e.g., quotes or surrounding
\fbox{}). When used together with the shortvrb package it allows the
definition of short verbatim characters which use this package's variant
instead of the normal \verb. In addition, it is possible to collect an
argument verbatim to either typeset or write it into a file. The
\Verbdef command defines verbatim text to a macro which can later be
used to write the verbatim text to a file.

