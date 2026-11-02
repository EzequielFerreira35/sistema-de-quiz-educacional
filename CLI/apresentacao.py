def desenhar_tabela(cabecalhos, colunas_larguras, linhas_dados):
    TOPO_ESQ, TOPO_DIR = "┌", "┐"
    BASE_ESQ, BASE_DIR = "└", "┘"
    INTER_TOPO, INTER_BASE = "┬", "┴"
    CRUZ, LINHA_HORIZ, LINHA_VERT = "┼", "─", "│"
    LADO_ESQ, LADO_DIR = "├", "┤"

    topo = TOPO_ESQ + INTER_TOPO.join(LINHA_HORIZ * w for w in colunas_larguras) + TOPO_DIR
    print(topo)

    cabecalho_formatado = LINHA_VERT + LINHA_VERT.join(f" \033[1m{col:^{w-2}}\033[0m " for col, w in zip(cabecalhos, colunas_larguras)) + LINHA_VERT
    print(cabecalho_formatado)

    separador_cabecalho = LADO_ESQ + CRUZ.join(LINHA_HORIZ * w for w in colunas_larguras) + LADO_DIR
    print(separador_cabecalho)

    for idx, linha in enumerate(linhas_dados):
        dados_formatados = []
        for dado, w in zip(linha, colunas_larguras):
            texto = str(dado)
            if len(texto) > (w - 2):
                texto = texto[:(w - 5)] + "..."
            
            if len(texto) <= 8 or texto.count("-") == 4: 
                dados_formatados.append(f" {texto:^{w-2}} ")
            else:
                dados_formatados.append(f" {texto:<{w-2}} ")

        print(LINHA_VERT + LINHA_VERT.join(dados_formatados) + LINHA_VERT)

        if idx < len(linhas_dados) - 1:
            separador_linha = LADO_ESQ + CRUZ.join(LINHA_HORIZ * w for w in colunas_larguras) + LADO_DIR
            print(separador_linha)

    base = BASE_ESQ + INTER_BASE.join(LINHA_HORIZ * w for w in colunas_larguras) + BASE_DIR
    print(base)

def desenhar_card():
    ...