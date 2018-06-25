# revision 25689
# category Package
# catalog-ctan /language/cherokee/ocherokee
# catalog-date 2007-03-12 00:37:02 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-ocherokee
Version:	20180303
Release:	1
Summary:	LaTeX Support for the Cherokee language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/cherokee/ocherokee
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocherokee.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocherokee.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Macros and Type 1 fonts for Typesetting the Cherokee language
with the Omega version of LaTeX (known as Lambda).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/ocherokee/Cherokee-Bold.afm
%{_texmfdistdir}/fonts/afm/public/ocherokee/Cherokee.afm
%{_texmfdistdir}/fonts/map/dvips/ocherokee/cherokee.map
%{_texmfdistdir}/fonts/ofm/public/ocherokee/OCherokee.ofm
%{_texmfdistdir}/fonts/ofm/public/ocherokee/OCherokeeb.ofm
%{_texmfdistdir}/fonts/ofm/public/ocherokee/OCherokeebo.ofm
%{_texmfdistdir}/fonts/ofm/public/ocherokee/OCherokeeo.ofm
%{_texmfdistdir}/fonts/ovf/public/ocherokee/OCherokee.ovf
%{_texmfdistdir}/fonts/ovf/public/ocherokee/OCherokeeb.ovf
%{_texmfdistdir}/fonts/ovf/public/ocherokee/OCherokeebo.ovf
%{_texmfdistdir}/fonts/ovf/public/ocherokee/OCherokeeo.ovf
%{_texmfdistdir}/fonts/ovp/public/ocherokee/OCherokee.ovp
%{_texmfdistdir}/fonts/ovp/public/ocherokee/OCherokeeb.ovp
%{_texmfdistdir}/fonts/ovp/public/ocherokee/OCherokeebo.ovp
%{_texmfdistdir}/fonts/ovp/public/ocherokee/OCherokeeo.ovp
%{_texmfdistdir}/fonts/tfm/public/ocherokee/Cherokee.tfm
%{_texmfdistdir}/fonts/tfm/public/ocherokee/Cherokeeb.tfm
%{_texmfdistdir}/fonts/tfm/public/ocherokee/Cherokeebo.tfm
%{_texmfdistdir}/fonts/tfm/public/ocherokee/Cherokeeo.tfm
%{_texmfdistdir}/fonts/type1/public/ocherokee/Cherokee-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/ocherokee/Cherokee.pfb
%{_texmfdistdir}/omega/ocp/ocherokee/cher2uni.ocp
%{_texmfdistdir}/omega/otp/ocherokee/cher2uni.otp
%{_texmfdistdir}/tex/lambda/ocherokee/lchcmr.fd
%{_texmfdistdir}/tex/lambda/ocherokee/lchenc.def
%{_texmfdistdir}/tex/lambda/ocherokee/ocherokee.sty
%doc %{_texmfdistdir}/doc/omega/ocherokee/READ.ME
%doc %{_texmfdistdir}/doc/omega/ocherokee/cherokee.pdf
%doc %{_texmfdistdir}/doc/omega/ocherokee/chief.tex
%doc %{_texmfdistdir}/doc/omega/ocherokee/proverb.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts omega tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070312-3
+ Revision: 787696
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070312-2
+ Revision: 754499
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070312-1
+ Revision: 719149
- texlive-ocherokee
- texlive-ocherokee
- texlive-ocherokee
- texlive-ocherokee

