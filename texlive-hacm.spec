%global tl_name hacm
%global tl_revision 27671

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Font support for the Arka language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/hacm
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hacm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hacm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package supports typesetting hacm, the alphabet of the constructed
language Arka. The bundle provides nine official fonts, in Adobe Type 1
format.

