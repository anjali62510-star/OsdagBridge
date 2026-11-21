"""Centralized LaTeX styling for OsdagBridge design reports.

Keep shared page, table, and brand formatting values here so report
chapters use one consistent visual system.
"""

# Page layout
PAGE_GEOMETRY = r"\usepackage[a4paper, margin=1in]{geometry}"

# Brand color
LATEX_BRAND_COLOR = r"\definecolor{osdagGreen}{HTML}{91B014}"

# Default report table layout
LATEX_TABLE_DEFAULTS = r"""% Shared table layout and spacing
\setlength{\tabcolsep}{6pt}
\renewcommand{\arraystretch}{1.12}
\setlength{\LTpre}{0pt}
\setlength{\LTpost}{6pt}
\setlength{\arrayrulewidth}{0.5pt}
\setlength{\extrarowheight}{0.6pt}
\setlength{\footskip}{42pt}
\setlength{\headheight}{18pt}"""

# Compact analysis-demand table layout
COMPACT_TABLE_LAYOUT = r"""\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.25}"""

# Chapter-level tables that need the standard horizontal cell padding
LATEX_TABLE_CELL_PADDING = r"\setlength{\tabcolsep}{6pt}"
