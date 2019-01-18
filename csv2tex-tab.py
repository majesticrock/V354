#Usage:
#csv2textable
#<pathToFile>:  Input the path to your input file
#<caption>:     The caption you'd like to have for the table
#<label>:       The label you'd like to have for the table. This is also the name for the output file
#<format>:      The table format. For expample cccc for a for four columns with centered entries
#<delimiter>:   The delimiter of the csv-file. If you don't give this argument, the standard value is set to ";"
#
#The csv-file should be formated like this:
#headline1;headline2;headline3
#entry11;entry12;entry13
#entry21;entry22;entry33
#etc
#
#You should have an equal amount of colums in every row. The rows should not end with your delimiter.
#If you want to use multicolumns you can of course do so. In this case they of course count as that number of columns as
#restrictions comes from latex and not from this script.
#
#This script probably won't work on Windows systems. Install a linux distribution.
#
#csv_read
#<pathToFile>:  Input the path to your input file
#<delimiter>:   The delimiter of the csv-file. If you don't give this argument, the standard value is set to ";"

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def csv2textable(pathToFile, caption, label, format, delimiter=";"):
    content = csv_read(pathToFile, delimiter)
    
    tableHead = "\\begin{table}[!htp]\n" + "\\centering\n" + "\\caption{" + caption + "}\n" + "\\label{tab:" + label + "}\n"
    tabularHead = "\\begin{tabular}{" + format + "}\n" + "\\toprule\n"

    fileEnd = "\\end{tabular}\n" + "\\end{table}"

#Add a folder here if you want your output-file anywhere special.
    with open("content/" + label + ".tex", "w") as f:
        f.write(tableHead)
        f.write(tabularHead)
        for i in range(len(content)):
            for j in range(len(content[i])):
                if(i == 0):
                    f.write(content[i][j] + " ")
                    if(j == (len(content[i]) - 1)):
                        f.write("\\\\\n")
                        f.write("\\midrule\n")
                    else:
                        f.write("& ")
                else:
                    f.write(content[i][j])
                    if(j == (len(content[i]) - 1)):
                        f.write(" \\\\\n")
                    else:
                        f.write(" & ")
        
        f.write("\\bottomrule\n")
        f.write(fileEnd)

#pathToFile = "csv/geräte-daten.csv"
#caption    = "Die angegebenen Gerätedaten."
#label      = "geraetedaten"
#format     = "S[table-format=1.2] @{${}\pm{}$} S[table-format=1.2] S[table-format=1.3] @{${}\pm{}$} S[table-format=1.3] S[table-format=2.1] @{${}\pm{}$} S[table-format=1.1] S[table-format=3.1] @{${}\pm{}$} S[table-format=1.1]"

#pathToFile = "csv/zeit-amplitude.csv"
#caption    = "Die Daten der Amplitudenmessung bei der gedämpften Schwingung."
#label      = "zeit-amplitude"
#format     = "S[table-format=3.0] S[table-format=1.2]"

pathToFile = "csv/var-freqU=6.55.csv"
caption    = "Daten der Messung mit variabler Frequenz mit $U_0 = 6.55$ V."
label      = "var-freq"
format     = "S[table-format=2] S[table-format=2.1] S[table-format=1.2]"

csv2textable(pathToFile, caption, label, format)