# Porting Handbook from `bookdown` to `Quarto`

## Installing `Quarto`

<https://quarto.org/docs/get-started/>

1. Download Quarto CLI, <https://github.com/quarto-dev/quarto-cli/releases/download/v1.0.38/quarto-1.0.38-win.msi> on 2022-08-06-1300−05
2. Run `msi` installer
    1. Install "just for you"
    2. Install in User Local Appdata (no admin required)
    3. That's it
3. Restart command lines and IDEs
4. "Choose your Tool"
    1. [VS Code](https://quarto.org/docs/get-started/hello/vscode.html) <-- I'll be using this
    2. [RStudio](https://quarto.org/docs/get-started/hello/rstudio.html)
    3. [Jupyter](https://quarto.org/docs/get-started/hello/jupyter.html)
    4. [Text Editor](https://quarto.org/docs/get-started/hello/text-editor.html)

## VS Code `Tutorial: Hello Quarto`

1. Install [`Quarto` VS Code extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto)
2. Create a text file [`hello.qmd`](hello.qmd)
3. Paste in [sample code](https://quarto.org/docs/get-started/hello/vscode.html#render-and-preview)
4. Update VS Code settings to include Quarto path
    - `Quarto: Path`
    - C:\Users$$self]\AppData\Local\Programs\Quarto\bin
5. No bueno. Added GitHub issue comment <https://github.com/quarto-dev/quarto-web/issues/304>

## Text Editor

1. Using text editor commands in PowerShell instead until VS Code is fixed <https://github.com/quarto-dev/quarto-web/issues/304>
2. Successful renders to
    1. [html](hello.html)
    2. [docx](hello.docx)
3. Successful preview using `quarto preview hello.qmd`

## New GitHub Repo

1. Created <https://github.com/Society-of-Flight-Test-Engineers/quarto-handbook>
2. Followed mirror instructions at <https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository>

## Starting port

1. Start with blank book per <https://quarto.org/docs/books/#getting-started>, called `quarto-handbook`
2. Copied media folder so image references would work
3. Transfer information from `index.rmd` to both `_quarto.yml` and `index.qmd` then run `quarto preview quarto-handbook`
4. Transfer information from `*.rmd` to `*.qmd`
    1. Add `*.qmd` to `_quarto.yml` `chapters:` list
    2. `{block` --> `<!-- -->`\
    3. `\( insert LaTeX here \)` --> `$insert LateX here$`
        1. In VS Code, `CTRL-H` allows find and replace using regex
        2. Find `\\\(` and replace with `$`
        3. Find `\\\)` and replace with `$\s\s` (Some tables require specific spacing, so need to make up for two fewer characters for LaTeX conversion)
        4. Find `\s\$\s` and `\s\$\n` and manually fix. Quarto doesn't like whitespace between `$` and equation contents
        5. Search rendered HTML preview for `$` and manually fix
    4. `\[ insert LaTeX here \]` --> `\begin{equation*}insert LateX here\end{equation*}`
        1. Find `\\\[` and replace with `\n\begin{equation*}\n`
        2. Find `\\\]` and replace with `\n\end{equation*}\n`
    5. Run `quarto preview quarto-handbook`
5. Add notes callouts and cross-references to `21-displayguidelines.qmd` to better match intent of original Word document

Wrote `rmd2qmd.py` to speed up the process

## Setup new github.io static page with GitHub actions
