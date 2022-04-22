import numpy as np

def begin(file, title = None, headL = None, headR = None, headC = None, footL = None, footC = None, footR = None):
    # give the file input, then choose if you want some headers etc
    
    file.write('\\documentclass[oneside]{article}\n\\linespread{1.25}\n\\usepackage[open, openlevel=1]{bookmark}\n\\usepackage{listingsutf8}\n\\usepackage[english]{babel}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amsfonts,amssymb,mathtools}\n\\usepackage{listings}\n\\usepackage{caption}\n\\usepackage{subfig}\n\\usepackage{graphicx}\n\\usepackage{tabularx}\n\\usepackage{float}\n\\usepackage{enumitem}\n\\usepackage{array, ltablex, multirow}\n\\usepackage{fancyhdr}\n\\usepackage[top=2.5cm, bottom=2.5cm,left=2.5cm, right=2.5cm]{geometry}\n\\pagestyle{fancy}\n\\renewcommand{\headrulewidth}{0pt}\n')
    head = [headL, headC, headR]
    where = ['L','C','R']
    for i in range(0,3):
        if head[i] is not None:
            file.write('\\fancyhead['+where[i]+']{'+head[i]+'}\n')
            
    foot = [footL, footC, footR]
    for i in range(0,3):
        if foot[i] is not None:
            file.write('\\fancyfoot['+where[i]+']{'+foot[i]+'}\n')
        
    
    file.write('\n\\begin{document}\n')

def title(file, title = None, subtitle = None, author = None):
    if title is not None:
        file.write('\n\\thispagestyle{empty}\n\\begin{center}\n\\huge{\\bf '+title+'}\\\\\n')
        if subtitle is not None:
            file.write('{\\bf '+subtitle+'}\\\\\n')
    if author is not None:
        file.write('\n\\large author: ' +author)
    file.write('\n\\end{center}\n\\newpage\n')    

def write(file, text):
    text = text.replace('è', "e'")
    text = text.replace('\n', '\\\\\n\\ ')
    file.write('\n\\ '+text+'\\\\\n')

def totab(var, file, fr=None, fc = None, caption = None, rnd = 2):

    # var: matrix with data (numeric and text) 
    # file: name of the text file
    # fr: list of strings which are the first row of the table entries. It can be long as the data 
    # matrix or one coefficient longer. In the first case the table as only the array, in the second
    # a first empty column appears with the required label
    # fc: list of strings which are the entries of the first column. It's as long as the array height
    # rnd: number of decimals in table, 2 by default
    # caption: caption for the table, no caption if omitted
    # example: tec.totab(matrix, report_tec, fr = ['exp', 'P', 'D'],...
    # fc = ['one', 'two'], caption = ['nice table'], rnd = 4)
    
    
    a = np.shape(var)
    if fr is None:
        if fc is None:
            file.write('\n\\begin{tabularx}{\\textwidth}{'+'|c'*a[1]+'|}\n')

                
            for i in range(0, a[0]):
                file.write('    \\hline\n    ')

                for j in range(0, a[1]):
                    if j ==a[1]-1:
                        file.write(str(round(var[i,j],rnd))+'\\\\\n')
                    else:
                        file.write(str(round(var[i,j],rnd))+'&')     
                                       
        else:
            file.write('\\begin{tabularx}{\\textwidth}{'+'|c'*(a[1]+1)+'|}\n')

            for i in range(0, a[0]):
                file.write('    \\hline\n    '+fc[i] +'&')   

                for j in range(0, a[1]):
                    if j ==a[1]-1:
                        file.write( str(round(var[i,j]))+'\\\\\n')
                    else:
                        file.write( str(round(var[i,j]))+'&')
        
    else:
        b = len(fr)
           
        if fc is None:
            if a[1] ==b:
                
                file.write('\\begin{tabularx}{\\textwidth}{'+'|c'*(a[1])+'|}\n')
                file.write('    \\hline\n')
                ee = str('')
            else:
                file.write('\\begin{tabularx}{\\textwidth}{'+'|c'*(a[1]+1)+'|}\n')
                file.write('    \\hline\n')    
                ee = str('&')  

            for i in range(0,b):
                if i == b-1:
                    file .write(fr[i]+'\\\\\n')
                else:
                    file.write(fr[i] + '&')
                        
                
            for i in range(0, a[0]):
                file.write('    \\hline\n    '+ee)   
                
                for j in range(0, a[1]):

                    if j ==a[1]-1:
                        file.write(str(round(var[i,j],rnd))+'\\\\\n')
                    else:
                        file.write(str(round(var[i,j],rnd))+'&')     
                                       
        else:

            file.write('\\begin{tabularx}{\\textwidth}{'+'|c'*(a[1]+1)+'|}\n')
            file.write('    \\hline\n    ')                    
            for i in range(0,b):
                if i == b-1:
                    file .write(fr[i]+'\\\\\n')
                else:
                    file.write(fr[i] + '&')
                                            
            for i in range(0, a[0]):
                file.write('    \\hline\n    '+fc[i] +'&')   
                
                for j in range(0, a[1]):
                    if j ==a[1]-1:
                        file.write( str(round(var[i,j]))+'\\\\\n')
                    else:
                        file.write(str(round(var[i,j]))+'&')

    if caption is None:
        file.write('    \\hline\n\\end{tabularx}\n\n')            
    else:
        caption = caption.replace('è', '\’e')
        
        file.write('    \\hline\n    \\caption{'+str(caption)+'}\n\\end{tabularx}\n\n')

  
def tofig(name,file, caption=None, scale = 0.5 ):
    # name: name of the plot saved and extension
    # file: name of the text file
    # caption: caption for the figure (non necessary)
    file.write('\n\\begin{figure}[h!]\n\centering\n    \\includegraphics[scale ='+ str(scale)+']{'+str(name)+'}\n')
    
    if caption is None:
        file.write('\\end{figure}\n\n')
    
    else:
        caption = caption.replace('è', '\’e')

        file.write('    \\caption{'+str(caption)+'}\n\\end{figure}\n\n')
   

def toeq(file, string):
    
    # feel free to add extra replacements you need
    string = str( '$' + string+'$')
    string = string.replace('è', '\’e')
    string = string.replace('**','^' )
    string= string.replace('(', '{')
    string= string.replace(')', '}')
    string = string.replace('*', '\\,\\,')
    string = string.replace('alpha', '\\alpha')
    string = string.replace('Delta', '\Delta')
    string = string.replace('beta', '\\beta')
    string = string.replace('gamma', '\gamma')
    string = string.replace('sigma', '\sigma')    
    string = string.replace('lambda', '\lambda')        
    string = string.replace('np.sqrt', '\sqrt')
    
    keff  = 0
    string2 = str('')
    for i in range(0,len(string)):
    
        if string[i] == '/':
            closed = 0
            opened = 0        
            # string = string[0:i] + string[i+1::]
            
            for k in range(i-1,0,-1):
    
                if string[k] == '}':
                    closed +=1
                    
                elif string[k] == '{':
                    opened +=1
                    if closed == opened:
                        string2 = string2[0:k+keff] + '\dfrac' + string2[k+keff::]
                        keff +=5
                        break
    
        else:
            string2 = string2 + string[i] 
        
    file.write('\n' + string2 + '\n')
    


def end(file):
    file.write('\n\\end{document}')