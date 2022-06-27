import os 
import xml.etree.ElementTree as ET 

def menu():
    """
    Printa um menu com as opções de pesquisa disponiveis e com a
    opção de parar a execução do script.
    """

    while True:
        print("-"*100)
        print("OPÇÕES DE PESQUISA")
        print("[1] NUMERO DA NF")
        print("[2] CODIGO DE PRODUTO")
        print("[3] NUMERO DE SÉRIE")
        print("[S] SAIR")
        print("-"*100)
        escolha = str(input(">>> ").upper())
        if escolha in ("1", "2", "3", "S" ):
            return escolha
        else: 
            print("-"*100)
            print("Por favor escolha uma das opções disponiveis informando seu numero correspondente.")
            print("-"*100)

def pesquisa(tag_xml):

    """Realiza uma busca nos arquivos xml disponiveis com 
    base na chave de pesquisa especificada e retorna uma lista 
    contendo os arquivos encontrados"""

    nFe_encontradas = []
    for diretorio, subpastas, arquivos in os.walk("."):
        for arquivo in arquivos:
            dados_nfe = []
            if arquivo.endswith(".xml"):
                with open(arquivo, "r") as Nfe:
                    for linha in Nfe:
                        linha = linha.strip('\n')
                        if tag_xml in linha:
                            try:
                                tree = ET.parse(arquivo)
                                root = tree.getroot()
                                prefix = "{http://www.portalfiscal.inf.br/nfe}"
                                data = prefix+"dhEmi"
                                num_nfe = prefix+"nNF"
                                serie_nfe = prefix+"serie"
                                chave = prefix+"chNFe"
                                valor_nota = prefix+"vNF"
                                campos = [data, num_nfe, serie_nfe, chave, valor_nota]
                                for campo in campos:
                                    for child in root.iter(campo):
                                        dados_nfe.append(child.text)
                                
                                nFe_encontradas.append(dados_nfe)
                                break
                            except:
                                break

                                
                        else:
                            pass
        return nFe_encontradas


if __name__ == "__main__":
    while True:
        escolha_menu = menu()
        if escolha_menu == "S":
            break

        elif escolha_menu == "1":
            num_nota = str(input("Informe o numero da nota fiscal\n>>>"))
            tag = (f"<nNF>{num_nota}</nNF>")
            resultado_pesquisa = pesquisa(tag)
            if len(resultado_pesquisa) == 0:
                print(f"Nenhuma nota encotrada com o numero de nota especificado:({num_nota})")
            else:
                for count, item in enumerate(resultado_pesquisa):
                    print("-"*100)
                    print(f"{count+1} - DADOS DA NOTA FISCAL")
                    print("-"*100)
                    print(f"Chave: {item[3]}")
                    print(f"Numero: {item[1]}")
                    print(f"Série: {item[2]}")
                    print(f"Valor: {item[4]}")
                    print("-"*100)

        elif escolha_menu == "2":
            cod_produto = str(input("Informe o codigo do produto\n>>> "))
            tag = (f"<cProd>{cod_produto}</cProd>")
            resultado_pesquisa = pesquisa(tag)
            if len(resultado_pesquisa) == 0:
                print(f"Nenhuma nota encotrada com codigo de produto especificado:({cod_produto})")
            else:
                for count, item in enumerate(resultado_pesquisa):
                    print("-"*100)
                    print(f"{count+1} - DADOS DA NOTA FISCAL")
                    print("-"*100)
                    print(f"Chave: {item[3]}")
                    print(f"Numero: {item[1]}")
                    print(f"Série: {item[2]}")
                    print(f"Valor: {item[4]}")
                    print("-"*100)
        
        elif escolha_menu == "3":
            num_serie = str(input("Informe o numero de serie da nota\n>>> "))
            tag = (f"<serie>{num_serie}</serie>")
            resultado_pesquisa = pesquisa(tag)
            if len(resultado_pesquisa) == 0:
                print(f"Nenhuma nota encotrada com o numero de serie especificado:({num_serie})")
            else:
                for count, item in enumerate(resultado_pesquisa):
                    try:
                        print("-"*100)
                        print(f"{count+1} - DADOS DA NOTA FISCAL")
                        print("-"*100)
                        print(f"Chave: {item[3]}")
                        print(f"Numero: {item[1]}")
                        print(f"Série: {item[2]}")
                        print(f"Valor: {item[4]}")
                        print("-"*100)
                    except Exception as erro:
                        continue