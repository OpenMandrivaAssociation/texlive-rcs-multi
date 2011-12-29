# revision 21939
# category Package
# catalog-ctan /macros/latex/contrib/rcs-multi
# catalog-date 2011-04-03 16:27:03 +0200
# catalog-license lppl
# catalog-version 0.1a
Name:		texlive-rcs-multi
Version:	0.1a
Release:	1
Summary:	Typeset RCS version control in multiple-file documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rcs-multi
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rcs-multi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rcs-multi.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rcs-multi.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to typeset version control
information provided by RCS keywords (e.g., $ID: ... $) in
LaTeX documents that contain multiple TeX files. The package is
based on the author's svn-multi package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rcs-multi/rcs-multi.sty
%doc %{_texmfdistdir}/doc/latex/rcs-multi/example.pdf
%doc %{_texmfdistdir}/doc/latex/rcs-multi/rcs-multi.pdf
#- source
%doc %{_texmfdistdir}/source/latex/rcs-multi/Makefile
%doc %{_texmfdistdir}/source/latex/rcs-multi/example.tex
%doc %{_texmfdistdir}/source/latex/rcs-multi/rcs-multi.dtx
%doc %{_texmfdistdir}/source/latex/rcs-multi/rcs-multi.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
