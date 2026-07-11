%global tl_name ocherokee
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX Support for the Cherokee language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/cherokee/ocherokee
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ocherokee.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ocherokee.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Macros and Type 1 fonts for Typesetting the Cherokee language with the
Omega version of LaTeX (known as Lambda).

