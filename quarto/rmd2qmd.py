from pathlib import Path

p = Path('.')

for x in (p / 'quarto').glob('[0-9][0-9]*.rmd'):
    print(x.stem + '.qmd')
    if int(x.stem[:2]) > 5:
        with open(x, encoding="utf8") as f_rmd:
            # Consider checking if file exists, and if so deleting or setting to 'w' instead of 'a'
            with open((p / 'quarto-handbook' / (x.stem + ".qmd")), 'a', encoding="utf8") as f_qmd:
                for line in f_rmd:
                    line = line.replace('\(', '$')
                    line = line.replace('\)', '$  ')
                    line = line.replace('\[', '\n\\begin{equation*}\n')
                    line = line.replace('\]', '\n\\end{equation*}\n')

                    #print(line)
                    f_qmd.write(line)
                    

