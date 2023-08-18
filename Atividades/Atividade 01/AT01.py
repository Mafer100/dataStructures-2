import sys
import sortType as sort

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Debug Flags
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
debugFastFile  = True
debugMsg       = True
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# TO:DO LIST
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#       Ingestão dos arquivos
#       Leitura das opções nos arquivos
#       Formatação do Output
#       Tempo de processamento
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Verificação de erros
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
if not fastDebug and len(sys.argv) == 3:
    inputFile  = sys.argv[1]
    outputFile = sys.argv[2]
elif not fastDebug and len(sys.argv) != 3:
    print("[ERROR]: Invalid number of arguments!")
    exit()
else:
    print("[INFO]: Fast Debug ON")
    print("[INFO]: Disabling arguments file names!")
    print("[INFO]: Input and Output file name are inside the code!")
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def main(input,output):
    if debugMsg:
        print("[INFO]: Input name:",input)
        print("[INFO]: Output name:",output)

    
if __name__ == '__main__':
    if fastDebug:
        main("test.txt","output.txt")
    else:
        main(inputFile,outputFile)