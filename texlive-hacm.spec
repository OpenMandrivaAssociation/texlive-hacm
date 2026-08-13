%global tl_name hacm
%global tl_revision 27671
%global tl_version 0.1

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Font support for the Arka language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/hacm
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hacm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hacm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package supports typesetting hacm, the alphabet of the constructed
language Arka. The bundle provides nine official fonts, in Adobe Type 1
format.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from hacm:
Map hacm.map
TL_DROPIN_EOF
