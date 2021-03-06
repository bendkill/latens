(TeX-add-style-hook
 "report"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "a4paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("subfig" "caption=false" "font=footnotesize")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "INTERSPEECH2016"
    "graphicx"
    "amssymb"
    "amsmath"
    "bm"
    "bbm"
    "hyperref"
    "textcomp"
    "algorithm"
    "algpseudocode"
    "array"
    "multirow"
    "subfig")
   (TeX-add-symbols
    "vec"
    "mat"
    "name")
   (LaTeX-add-labels
    "sec:introduction"
    "sec:related-work"
    "sec:method"
    "fig:overview"
    "sec:auto-encod-arch"
    "sec:conv-auto-encod"
    "eq:1"
    "sec:vari-auto-encod"
    "eq:3"
    "eq:2"
    "eq:4"
    "sec:t-sne-style"
    "eq:5"
    "eq:7"
    "eq:6"
    "sec:sampling-strategies"
    "alg:sampling"
    "sec:results"
    "fig:vae-encodings"
    "fig:classifier-accs"
    "fig:unbalanced-mnist-results"
    "tab:results"
    "sec:discussion"
    "sec:conclusion"
    "sec:acknowledgements")
   (LaTeX-add-bibliographies))
 :latex)

