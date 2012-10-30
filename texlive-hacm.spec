# revision 27671
# category Package
# catalog-ctan /fonts/hacm
# catalog-date 2012-09-10 11:33:53 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-hacm
Version:	0.1
Release:	1
Summary:	Font support for the Arka language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/hacm
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hacm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hacm.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports typesetting hacm, the alphabet of the
constructed language Arka. The bundle provides nine official
fonts, in Adobe Type 1 format.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/hacm/hacm.map
%{_texmfdistdir}/fonts/tfm/public/hacm/alblant.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/defans.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/fenlil.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/fialis.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/inje.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/kardinal.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/lantia.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/nalnia.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/olivia.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/ralblant.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rdefans.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rfenlil.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rfialis.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rinje.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rkardinal.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rlantia.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rnalnia.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rolivia.tfm
%{_texmfdistdir}/fonts/type1/public/hacm/alblant.pfb
%{_texmfdistdir}/fonts/type1/public/hacm/defans.pfb
%{_texmfdistdir}/fonts/type1/public/hacm/fenlil.pfb
%{_texmfdistdir}/fonts/type1/public/hacm/fialis.pfb
%{_texmfdistdir}/fonts/type1/public/hacm/inje.pfb
%{_texmfdistdir}/fonts/type1/public/hacm/kardinal.pfb
%{_texmfdistdir}/fonts/type1/public/hacm/lantia.pfb
%{_texmfdistdir}/fonts/type1/public/hacm/nalnia.pfb
%{_texmfdistdir}/fonts/type1/public/hacm/olivia.pfb
%{_texmfdistdir}/fonts/vf/public/hacm/alblant.vf
%{_texmfdistdir}/fonts/vf/public/hacm/defans.vf
%{_texmfdistdir}/fonts/vf/public/hacm/fenlil.vf
%{_texmfdistdir}/fonts/vf/public/hacm/fialis.vf
%{_texmfdistdir}/fonts/vf/public/hacm/inje.vf
%{_texmfdistdir}/fonts/vf/public/hacm/kardinal.vf
%{_texmfdistdir}/fonts/vf/public/hacm/lantia.vf
%{_texmfdistdir}/fonts/vf/public/hacm/nalnia.vf
%{_texmfdistdir}/fonts/vf/public/hacm/olivia.vf
%{_texmfdistdir}/tex/latex/hacm/hacm.sty
%{_texmfdistdir}/tex/latex/hacm/ot1halb.fd
%{_texmfdistdir}/tex/latex/hacm/ot1hdef.fd
%{_texmfdistdir}/tex/latex/hacm/ot1hfen.fd
%{_texmfdistdir}/tex/latex/hacm/ot1hfia.fd
%{_texmfdistdir}/tex/latex/hacm/ot1hinj.fd
%{_texmfdistdir}/tex/latex/hacm/ot1hkar.fd
%{_texmfdistdir}/tex/latex/hacm/ot1hlan.fd
%doc %{_texmfdistdir}/doc/fonts/hacm/README
%doc %{_texmfdistdir}/doc/fonts/hacm/hacmdoc.pdf
%doc %{_texmfdistdir}/doc/fonts/hacm/hacmdoc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
