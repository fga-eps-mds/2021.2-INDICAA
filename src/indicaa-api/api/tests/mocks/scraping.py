from datetime import datetime
from decimal import Decimal


SCRAPING = {
    'materias': [{'codigoMateria': 'FGA0003', 'nome': 'COMPILADORES 1'},
               {'codigoMateria': 'FGA0006',
                'nome': 'FUNDAMENTOS DE EQUAÇÕES DIFERENCIAIS PARA ENGENHARIA'},
               {'codigoMateria': 'FGA0008', 'nome': 'SISTEMAS AEROESPACIAIS'},
               {'codigoMateria': 'FGA0015',
                'nome': 'PROCESSAMENTO DIGITAL DE IMAGENS'},
               {'codigoMateria': 'FGA0017',
                'nome': 'PROJETOS DE CIRCUITOS INTEGRADOS 1'},
               {'codigoMateria': 'FGA0023', 'nome': 'DINÂMICA DOS MECANISMOS'},
               {'codigoMateria': 'FGA0025',
                'nome': 'SISTEMAS DE ENERGIA SOLAR E EÓLICA'},
               {'codigoMateria': 'FGA0030', 'nome': 'ESTRUTURAS DE DADOS 2'},
               {'codigoMateria': 'FGA0037',
                'nome': 'TÓPICOS ESPECIAIS EM ENGENHARIA AEROESPACIAL'},
               {'codigoMateria': 'FGA0038',
                'nome': 'AERODINÂMICA DE SISTEMAS AEROESPACIAIS'},
               {'codigoMateria': 'FGA0039',
                'nome': 'MECÂNICA DE ESTRUTURAS AEROESPACIAIS'},
               {'codigoMateria': 'FGA0040',
                'nome': 'SISTEMAS DE CONTROLE AUTOMOTIVO'},
               {'codigoMateria': 'FGA0043',
                'nome': 'DINÂMICA DOS GASES PARA SISTEMAS AEROESPACIAIS'},
               {'codigoMateria': 'FGA0045', 'nome': 'MECÂNICA DO VÔO'},
               {'codigoMateria': 'FGA0046',
                'nome': 'MÉTODOS E TÉCNICAS DA ESCRITA CIENTÍFICA'},
               {'codigoMateria': 'FGA0048', 'nome': 'MECÂNICA DO VOO ESPACIAL'},
               {'codigoMateria': 'FGA0050',
                'nome': 'DINÂMICA DE ESTRUTURAS AEROESPACIAIS'},
               {'codigoMateria': 'FGA0052', 'nome': 'PROPULSÃO AEROESPACIAL'},
               {'codigoMateria': 'FGA0053',
                'nome': 'TÓPICOS ESPECIAIS EM PROGRAMAÇÃO'},
               {'codigoMateria': 'FGA0055',
                'nome': 'TECNOLOGIAS DE FABRICAÇÃO 1'},
               {'codigoMateria': 'FGA0056',
                'nome': 'TECNOLOGIAS DE FABRICAÇÃO 2'},
               {'codigoMateria': 'FGA0060',
                'nome': 'SISTEMAS DE BANCO DE DADOS 2'},
               {'codigoMateria': 'FGA0063', 'nome': 'PROPULSÃO AERONÁUTICA'},
               {'codigoMateria': 'FGA0065', 'nome': 'PROPULSÃO ELÉTRICA'},
               {'codigoMateria': 'FGA0067',
                'nome': 'TEORIA DE CIRCUITOS ELETRÔNICOS 1'},
               {'codigoMateria': 'FGA0068',
                'nome': 'TEORIA DE CIRCUITOS ELETRÔNICOS 2'},
               {'codigoMateria': 'FGA0069',
                'nome': 'PRÁTICA DE CIRCUITOS ELETRÔNICOS 1'},
               {'codigoMateria': 'FGA0070',
                'nome': 'PRÁTICA DE CIRCUITOS ELETRÔNICOS 2'},
               {'codigoMateria': 'FGA0071',
                'nome': 'PRÁTICA DE ELETRÔNICA DIGITAL 1'},
               {'codigoMateria': 'FGA0072',
                'nome': 'PRÁTICA DE ELETRÔNICA DIGITAL 2'},
               {'codigoMateria': 'FGA0073',
                'nome': 'TEORIA DE ELETRÔNICA DIGITAL 1'},
               {'codigoMateria': 'FGA0074',
                'nome': 'TEORIA DE ELETRÔNICA DIGITAL 2'},
               {'codigoMateria': 'FGA0075',
                'nome': 'LABORATÓRIO DE MATERIAIS DE CONSTRUÇÃO'},
               {'codigoMateria': 'FGA0076',
                'nome': 'EQUIPAMENTOS TERMOFLUIDOS AUTOMOTIVOS'},
               {'codigoMateria': 'FGA0077', 'nome': 'INTRODUÇÃO AO DESGASTE'},
               {'codigoMateria': 'FGA0078',
                'nome': 'TEORIA DE MATERIAIS DE CONSTRUÇÃO'},
               {'codigoMateria': 'FGA0083', 'nome': 'APRENDIZADO DE MÁQUINA'},
               {'codigoMateria': 'FGA0084',
                'nome': 'DESENVOLVIMENTO DE SOFTWARE'},
               {'codigoMateria': 'FGA0085', 'nome': 'MATEMÁTICA DISCRETA 1'},
               {'codigoMateria': 'FGA0086',
                'nome': 'TEORIA DE ELETRICIDADE APLICADA'},
               {'codigoMateria': 'FGA0087',
                'nome': 'LABORATÓRIO DE ELETRICIDADE APLICADA'},
               {'codigoMateria': 'FGA0088',
                'nome': 'TEORIA DE SISTEMAS DE CONVERSÃO DE ENERGIA'},
               {'codigoMateria': 'FGA0089',
                'nome': 'LABORATÓRIO DE SISTEMAS DE CONVERSÃO DE ENERGIA'},
               {'codigoMateria': 'FGA0090',
                'nome': 'ONDULATÓRIA E FÍSICA TÉRMICA PARA ENGENHARIA'},
               {'codigoMateria': 'FGA0091', 'nome': 'MÁQUINAS DE FLUIDO'},
               {'codigoMateria': 'FGA0092',
                'nome': 'PRINCÍPIOS DE COMUNICAÇÃO PARA ENGENHARIA'},
               {'codigoMateria': 'FGA0093', 'nome': 'PRINCÍPIOS DE CONTROLE'},
               {'codigoMateria': 'FGA0094', 'nome': 'ANTENAS IMPRESSAS'},
               {'codigoMateria': 'FGA0096', 'nome': 'ELETRÔNICA EMBARCADA'},
               {'codigoMateria': 'FGA0098',
                'nome': 'PRÁTICA DE CIRCUITOS ELETRÔNICOS 3'},
               {'codigoMateria': 'FGA0099',
                'nome': 'TEORIA DE CIRCUITOS ELETRÔNICOS 3'},
               {'codigoMateria': 'FGA0100',
                'nome': 'PRÁTICA DE FÍSICA DOS DISPOSITIVOS ELETRÔNICOS'},
               {'codigoMateria': 'FGA0101',
                'nome': 'TEORIA DE FÍSICA DOS DISPOSITIVOS ELETRÔNICOS'},
               {'codigoMateria': 'FGA0102',
                'nome': 'SINAIS E SISTEMAS PARA ENGENHARIA'},
               {'codigoMateria': 'FGA0103',
                'nome': 'SISTEMAS OPERACIONAIS EMBARCADOS'},
               {'codigoMateria': 'FGA0104',
                'nome': 'QUÍMICA ORGÂNICA APLICADA À ENGENHARIA'},
               {'codigoMateria': 'FGA0108', 'nome': 'MATEMÁTICA DISCRETA 2'},
               {'codigoMateria': 'FGA0109',
                'nome': 'FUNDAMENTOS DE SISTEMAS EMBARCADOS'},
               {'codigoMateria': 'FGA0118',
                'nome': 'SISTEMAS DE INFORMAÇÃO GEOGRÁFICA PARA ENGENHARIA'},
               {'codigoMateria': 'FGA0119',
                'nome': 'TEORIA DE ELETROMAGNETISMO'},
               {'codigoMateria': 'FGA0120',
                'nome': 'PRÁTICA DE ELETROMAGNETISMO'},
               {'codigoMateria': 'FGA0121',
                'nome': 'TÓPICOS ESPECIAIS 4 EM ENGENHARIA AEROESPACIAL'},
               {'codigoMateria': 'FGA0124', 'nome': 'PROJETO DE ALGORITMOS'},
               {'codigoMateria': 'FGA0129',
                'nome': 'PROCESSAMENTO DIGITAL DE SINAIS FINANCEIROS'},
               {'codigoMateria': 'FGA0130',
                'nome': 'REGULAÇÃO AMBIENTAL NO SETOR ENERGÉTICO'},
               {'codigoMateria': 'FGA0131',
                'nome': 'ENGENHARIA DE SOFTWARE AUTOMOTIVO'},
               {'codigoMateria': 'FGA0132',
                'nome': 'INSTRUMENTAÇÃO ELETRÔNICA PARA ENGENHARIA'},
               {'codigoMateria': 'FGA0133', 'nome': 'ENGENHARIA ECONÔMICA'},
               {'codigoMateria': 'FGA0134',
                'nome': 'TÓPICOS ESPECIAIS DE ENGENHARIA DE SOFTWARE'},
               {'codigoMateria': 'FGA0137',
                'nome': 'SISTEMAS DE BANCO DE DADOS 1'},
               {'codigoMateria': 'FGA0138',
                'nome': 'MÉTODOS DE DESENVOLVIMENTO DE SOFTWARE'},
               {'codigoMateria': 'FGA0141',
                'nome': 'GESTÃO AMBIENTAL NO SETOR ENERGÉTICO'},
               {'codigoMateria': 'FGA0142',
                'nome': 'FUNDAMENTOS DE ARQUITETURA DE COMPUTADORES'},
               {'codigoMateria': 'FGA0147',
                'nome': 'ESTRUTURA DE DADOS E ALGORITMOS'},
               {'codigoMateria': 'FGA0148',
                'nome': 'ENGENHARIA DE SEGURANÇA DO TRABALHO'},
               {'codigoMateria': 'FGA0150',
                'nome': 'PROJETO INTEGRADOR DE ENGENHARIA 1'},
               {'codigoMateria': 'FGA0152', 'nome': 'ERGONOMIA DO PRODUTO'},
               {'codigoMateria': 'FGA0154',
                'nome': 'MECANICA DOS SÓLIDOS 1 PARA ENGENHARIA'},
               {'codigoMateria': 'FGA0155',
                'nome': 'INTRODUÇÃO AO DESIGN E CONCEPÇÃO DE VEÍCULOS'},
               {'codigoMateria': 'FGA0156',
                'nome': 'COMBUSTÍVEIS E BIOCOMBUSTÍVEIS'},
               {'codigoMateria': 'FGA0157',
                'nome': 'PROBABILIDADE E ESTATÍSTICA APLICADO A ENGENHARIA'},
               {'codigoMateria': 'FGA0158', 'nome': 'ORIENTAÇÃO A OBJETOS'},
               {'codigoMateria': 'FGA0160',
                'nome': 'MÉTODOS NUMÉRICOS PARA ENGENHARIA'},
               {'codigoMateria': 'FGA0161', 'nome': 'ENGENHARIA E AMBIENTE'},
               {'codigoMateria': 'FGA0163', 'nome': 'INTRODUÇÃO À ENGENHARIA'},
               {'codigoMateria': 'FGA0164', 'nome': 'HUMANIDADES E CIDADANIA'},
               {'codigoMateria': 'FGA0166',
                'nome': 'ELEMENTOS E MÉTODOS EM ELETRÔNICA'},
               {'codigoMateria': 'FGA0167', 'nome': 'SISTEMAS AUTOMOTIVOS'},
               {'codigoMateria': 'FGA0168',
                'nome': 'DESENHO INDUSTRIAL ASSISTIDO POR COMPUTADOR'},
               {'codigoMateria': 'FGA0169',
                'nome': 'FONTES DE ENERGIA E TECNOLOGIAS DE CONVERSÃO'},
               {'codigoMateria': 'FGA0170',
                'nome': 'FUNDAMENTOS DE SISTEMAS OPERACIONAIS'},
               {'codigoMateria': 'FGA0172', 'nome': 'REQUISITOS DE SOFTWARE'},
               {'codigoMateria': 'FGA0173',
                'nome': 'INTERAÇÃO HUMANO COMPUTADOR'},
               {'codigoMateria': 'FGA0175',
                'nome': 'ENGENHARIA DE PETRÓLEO E GÁS'},
               {'codigoMateria': 'FGA0177',
                'nome': 'ANÁLISE INSTRUMENTAL DE COMBUSTÍVEIS'},
               {'codigoMateria': 'FGA0179',
                'nome': 'MECANICA DOS SÓLIDOS 2 PARA ENGENHARIA'},
               {'codigoMateria': 'FGA0184',
                'nome': 'GESTÃO DA PRODUÇÃO E QUALIDADE'},
               {'codigoMateria': 'FGA0188',
                'nome': 'MÉTODOS EXPERIMENTAIS PARA ENGENHARIA'},
               {'codigoMateria': 'FGA0190',
                'nome': 'PROJETO DE ELEMENTOS AUTOMOTIVOS'},
               {'codigoMateria': 'FGA0191',
                'nome': 'MATERIAIS COMPOSTOS E PLÁSTICOS'},
               {'codigoMateria': 'FGA0194',
                'nome': 'ARQUITETURA DE MOTORES DE COMBUSTÃO INTERNA'},
               {'codigoMateria': 'FGA0195',
                'nome': 'GESTÃO DA PRODUÇÃO AUTOMOTIVA'},
               {'codigoMateria': 'FGA0197', 'nome': 'SISTEMAS DE CONTROLE'},
               {'codigoMateria': 'FGA0201',
                'nome': 'PROJETO DE CIRCUITOS INTEGRADOS DIGITAIS'},
               {'codigoMateria': 'FGA0204', 'nome': 'DINÂMICA DOS FLUÍDOS'},
               {'codigoMateria': 'FGA0206',
                'nome': 'ENGENHARIA DE PRODUTO DE SOFTWARE'},
               {'codigoMateria': 'FGA0208',
                'nome': 'ARQUITETURA E DESENHO DE SOFTWARE'},
               {'codigoMateria': 'FGA0210', 'nome': 'PARADIGMAS DE PROGRAMAÇÃO'},
               {'codigoMateria': 'FGA0211',
                'nome': 'FUNDAMENTOS DE REDES DE COMPUTADORES'},
               {'codigoMateria': 'FGA0219', 'nome': 'PROCESSAMENTO DE SINAIS'},
               {'codigoMateria': 'FGA0221', 'nome': 'INTELIGÊNCIA ARTIFICIAL'},
               {'codigoMateria': 'FGA0224',
                'nome': 'COMUNICAÇÕES DIGITAIS PARA ENGENHARIA'},
               {'codigoMateria': 'FGA0226', 'nome': 'ELETRÔNICA VEICULAR'},
               {'codigoMateria': 'FGA0228',
                'nome': 'PROJETO DE SISTEMAS AUTOMOTIVOS'},
               {'codigoMateria': 'FGA0229',
                'nome': 'ANÁLISE ESTRUTURAL MÉTODO DOS ELEMENTOS FINITOS'},
               {'codigoMateria': 'FGA0230', 'nome': 'DINÂMICA DE VEÍCULOS'},
               {'codigoMateria': 'FGA0232', 'nome': 'INTEGRAÇÃO E TESTES'},
               {'codigoMateria': 'FGA0233', 'nome': 'SENSORES E TRANSDUTORES'},
               {'codigoMateria': 'FGA0235',
                'nome': 'TÓPICOS ESPECIAIS 1 EM ENGENHARIA DE ENERGIA'},
               {'codigoMateria': 'FGA0236', 'nome': 'BIORREFINARIAS'},
               {'codigoMateria': 'FGA0238', 'nome': 'TESTES DE SOFTWARE'},
               {'codigoMateria': 'FGA0240',
                'nome': 'GERÊNCIA DE CONFIGURAÇÃO E EVOLUÇÃO DE SOFTWARE'},
               {'codigoMateria': 'FGA0242',
                'nome': 'TÉCNICAS DE PROGRAMAÇÃO EM PLATAFORMAS EMERGENTES'},
               {'codigoMateria': 'FGA0244',
                'nome': 'PROGRAMAÇÃO PARA SISTEMAS PARALELOS E DISTRIBUÍDOS'},
               {'codigoMateria': 'FGA0247', 'nome': 'MÁQUINAS DE FLUXO'},
               {'codigoMateria': 'FGA0250',
                'nome': 'PROJETO INTEGRADOR DE ENGENHARIA 2'},
               {'codigoMateria': 'FGA0252', 'nome': 'SISTEMAS HIDROELÉTRICOS'},
               {'codigoMateria': 'FGA0254', 'nome': 'CIÊNCIAS AEROESPACIAIS'},
               {'codigoMateria': 'FGA0258',
                'nome': 'INSTRUMENTAÇÃO BIOMÉDICA 2'},
               {'codigoMateria': 'FGA0259',
                'nome': 'MODELAGEM DE SISTEMAS BIOLÓGICOS'},
               {'codigoMateria': 'FGA0261',
                'nome': 'TÓPICOS ESPECIAIS EM ELETRONICA'},
               {'codigoMateria': 'FGA0262',
                'nome': 'TRANSMISSÃO E DISTRIBUIÇÃO DE ENERGIA ELÉTRICA'},
               {'codigoMateria': 'FGA0265', 'nome': 'ECONOMIA DE ENERGIA'},
               {'codigoMateria': 'FGA0266',
                'nome': 'ACÚSTICA E VIBRAÇÕES VEICULARES'},
               {'codigoMateria': 'FGA0267',
                'nome': 'PROJETO DE ESTRUTURAS DE VEICULOS'},
               {'codigoMateria': 'FGA0270',
                'nome': 'SISTEMAS HIDRÁULICOS E PNEUMÁTICOS'},
               {'codigoMateria': 'FGA0273',
                'nome': 'MELHORIA DE PROCESSOS DE SOFTWARE'},
               {'codigoMateria': 'FGA0274',
                'nome': 'PRODUTIVIDADE E PROFISSIONALISMO EM ENGENHARIA DE '
                        'SOFTWARE'},
               {'codigoMateria': 'FGA0275',
                'nome': 'ENGENHARIA DE SOFTWARE EXPERIMENTAL'},
               {'codigoMateria': 'FGA0278', 'nome': 'QUALIDADE DE SOFTWARE 1'},
               {'codigoMateria': 'FGA0280',
                'nome': 'PROJETO DE CIRCUITOS ELETRÔNICOS INTEGRADOS 2'},
               {'codigoMateria': 'FGA0282',
                'nome': 'FUNDAMENTOS DO PROJETO DE AERONAVES'},
               {'codigoMateria': 'FGA0283',
                'nome': 'MECÂNICA DOS MATERIAIS COMPÓSITOS'},
               {'codigoMateria': 'FGA0285',
                'nome': 'INTRODUÇÃO À MECÂNICA DA FRATURA'},
               {'codigoMateria': 'FGA0286',
                'nome': 'FUNDAMENTOS DO MÉTODO DOS ELEMENTOS FINITOS'},
               {'codigoMateria': 'FGA0289',
                'nome': 'SISTEMAS DE PROPULSÃO SÓLIDA E HÍBRIDA'}],
  'nome': 'Faculdade do Gama'
}
