from django.shortcuts import render

def inicio(request):
    textos = {
        "objetivo": {
            "titulo": "Qual o objetivo desse site?",
            "conteudo": """Este site foi criado para preservar e compartilhar a herança cultural e histórica dos povos indígenas do Rio Grande do Norte, garantindo que seus saberes e memórias não se percam. Ele surge como resposta à necessidade de registrar e organizar informações sobre essas culturas, muitas vezes negligenciadas, servindo como um repositório digital acessível que promove o reconhecimento e o respeito por essas comunidades."""
        },
        "importancia": {
            "titulo": "Qual a importância desse site?",
            "conteudo": """Além de funcionar como um arquivo digital, o site busca aproximar pessoas e culturas, fornecendo informações organizadas que estimulam a curiosidade e o aprendizado. Ao educar e informar, contribui para a valorização e proteção do conhecimento indígena, fortalecendo a memória cultural e incentivando um maior entendimento entre diferentes grupos."""
        },
        "quem_somos": {
            "titulo": "Quem Somos?",
            "conteudo": """Somos Rebeca Lourenço Fernandes Bento e Ruan Henry Silva Carlos, concluintes do curso técnico em Informática do IFRN - Campus Pau dos Ferros. Este site foi desenvolvido como nosso Trabalho de Conclusão de Curso (TCC), com o objetivo de contribuir para a preservação e divulgação da cultura indígena do Rio Grande do Norte, unindo nossos conhecimentos técnicos à valorização da história e tradições dos povos originários de nossa região."""
        }
    }

    return render(request, 'dashboard/inicio.html', {
        "page": "inicio",
        "textos": textos
    })


def povos(request):
    povos = {
        "catu": {
            "titulo": "Catu",
            "conteudo": """A comunidade indígena Potiguara do Catu, cujo significado é “bom” ou “agradável”, faz parte da divisão Tupi. Viveram na região de Igramació, mas, em busca de um novo lugar, migraram para os atuais municípios de Canguaretama e Goianinha. A comunidade conta com 726 membros e enfrenta dificuldades devido à exploração agrícola e do desmatamento, já que a principal atividade econômica é a agricultura. O povo aproveita o solo fértil, e a caça e a pesca viraram segundo plano. Existe também a Festa da Batata, que representa um exemplo de resistência e adaptação cultural, eles lutam para preservar suas tradições e fortalecer a sua identidade potiguara por meio da educação e da cultura."""
        },
        "tapuia": {
            "titulo": "Tapuia Paiacu",
            "conteudo": """Os indígenas Tapuia Paiacu foram os primeiros habitantes do território de Apodi, no Rio Grande do Norte. Eles viviam em aldeias às margens da Lagoa de Apodi e eram nômades, mudando-se durante as secas e retornando com as chuvas. Usavam sandálias de casca de caraguá, pintavam-se com jenipapo e urucum, e construíam ocas de madeira cobertas de palha. Sua alimentação incluía caça, pesca, mel, frutas e raízes.

            A colonização começou em 1680 com a concessão de sesmarias, gerando conflitos com os indígenas, culminando na Guerra dos Bárbaros (1683-1720). Em 1700, jesuítas catequizaram parte dos índios, incluindo Luísa Cantofa, uma guerreira indígena que foi morta rezando o rosário.
            
            Atualmente, Lúcia Paiacu Tabajara, descendente indígena, luta pela preservação dessa história, tendo fundado o Museu do Índio Luíza Cantofa e o Centro Histórico-Cultural Tapuia Paiacu da Lagoa do Apodi."""
        }
    }

    return render(request, 'dashboard/povos.html', {"page": "povos", "povos": povos})


def conhecimentos(request):
    textos_conhecimentos = {
        'introd': {
            "introducao_conheci": """Apesar do Rio Grande do Norte ter um grande histórico de chacina e apagamento dos povos indígenas, ainda permanecem várias tradições de origem indígena no nosso estado no cotidiano, evidenciando que sobreviveram à passagem do tempo. O indígena não se "apagou" totalmente; tanto suas comunidades quanto a sua cultura ainda resistem e convivem no nosso cotidiano, como nas festas, comidas típicas, nomes de cidades, alimentos e palavras usadas no nosso vocabulário diário.  A seguir algumas das tradições e conhecimentos: """
        }
    }

    return render(request, 'dashboard/conhecimentos.html', {"page": "conhecimentos", "textos_conhecimentos": textos_conhecimentos})


def agradecimentos(request):
    return render(request, 'dashboard/agradecimentos.html', {"page": "agradecimentos"})