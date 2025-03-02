\ProvidesClass{include/src/sbu-report}[2025/02/15 Stony Brook Report Class]

% Load base class
\LoadClass[12pt,letterpaper]{article}

% Required packages
\RequirePackage[total={6.5in, 9in}]{geometry}  % Set document margins
\RequirePackage{amsmath}  % Math symbols and formatting
\RequirePackage{siunitx}  % SI units formatting
\RequirePackage{graphicx} % Graphics support
\RequirePackage{pdfpages} % Include PDFs
\RequirePackage{float}    % Floating elements (figures, tables)
\RequirePackage[normalem]{ulem} % Underlining and text emphasis
\RequirePackage{fancyhdr} % Headers and footers
\RequirePackage{titlesec} % Enhanced section styling
\RequirePackage{xcolor}   % Color for styling
\RequirePackage{mathpazo} % Font

% Increase head height to avoid fancyhdr warning
\setlength{\headheight}{14.5pt}

% Define paths for included files
\newcommand{\includepdfpath}{./include/pdf/}  % For PDFs
\newcommand{\imagepath}{./include/img/}   % Separate image path
\graphicspath{{./include/img/}}           % Works only for \includegraphics{}

% === Custom Title Page Parameters ===
\newcommand{\coursename}{Course Name}
\newcommand{\semester}{Semester and Year}
\newcommand{\reporttitle}{Report title line 1 \& Report title line 2}
\newcommand{\professor}{Professor Name}
\newcommand{\studentname}{Student Name}
\newcommand{\studentid}{000000000}
\newcommand{\reportdate}{\today}

% === Custom Commands to Set Title Page Parameters ===
\newcommand{\setcoursename}[1]{\renewcommand{\coursename}{#1}}
\newcommand{\setsemester}[1]{\renewcommand{\semester}{#1}}
\newcommand{\setreporttitle}[1]{\renewcommand{\reporttitle}{#1}}
\newcommand{\setprofessor}[1]{\renewcommand{\professor}{#1}}
\newcommand{\setstudentname}[1]{\renewcommand{\studentname}{#1}}
\newcommand{\setstudentid}[1]{\renewcommand{\studentid}{#1}}
\newcommand{\setreportdate}[1]{\renewcommand{\reportdate}{#1}}

% === Command to Set and Include Assignment PDF ===
\newcommand{\includeassignment}[1]{\def\assignmentfile{\includepdfpath#1}}
% === Command to Set and Include logo ===
\newcommand{\includelogo}[1]{\def\logofile{#1}}

% === Fancy Header & Footer ===
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\coursename}
\fancyhead[C]{\reporttitle}
\fancyhead[R]{\reportdate}
\fancyfoot[C]{\thepage}

% === Custom Section Styling ===
\titleformat{\section}
    {\Large\bfseries\color{black}} % Large, bold
    {\thesection}{1em}{}

\titleformat{\subsection}
    {\large\bfseries\color{black}} % Smaller, bold
    {\thesubsection}{1em}{}

% === Custom Title Page ===
\renewcommand{\maketitle}{
    \begin{titlepage}
        \centering
        \vspace*{1cm}

        % Include logo if provided
        \ifdefined\logofile
            \ifx\logofile\empty
                % Do nothing if empty
            \else
                \includegraphics[width=0.45\textwidth]{\imagepath\logofile}
                \vspace{3cm}
            \fi
        \fi
        
        {\Large \textsc{\coursename}}\par
        \vspace{0.5cm}
        {\large \textsc{\semester}}\par
        \vspace{1.5cm}
        
        {\LARGE \textsc{\reporttitle}}\par
        \vspace{2cm}

        {\large\textsc{\studentname}}\par 
        {\small{ID: \studentid}}\par
        \vfill

        \text{Professor}\par \professor

        \vfill
        {\small \reportdate\par}

        \vspace{1cm}
    \end{titlepage}

    % Include assignment if provided
    \ifdefined\assignmentfile
        \ifx\assignmentfile\empty
            % Do nothing if empty
        \else
            \includepdf[pages=-,pagecommand=\section*{Copy of Original Assignment}]{\assignmentfile}
        \fi
    \fi
}



\endinput
