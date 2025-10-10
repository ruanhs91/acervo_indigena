from django.shortcuts import render

def inicio(request):
    textos = {
        "objetivo": {
            "titulo": "Qual o objetivo desse site?",
            "conteudo": """A invenção da escrita marcou um momento crucial na preservação e transmissão do conhecimento humano. 
            A necessidade de registrar e conservar os saberes e costumes levou à criação de sites dedicadas ao cuidado e organização 
            de documentos e memórias. No contexto dos povos indígenas do Rio Grande do Norte, o desenvolvimento deste site surge como 
            uma resposta a essa necessidade histórica, proporcionando um espaço digital para registrar a herança cultural e histórica 
            dos povos tradicionais do RN. Nosso objetivo é garantir que o conhecimento e histórias desses povos não se percam no tempo, 
            mas sejam preservadas e compartilhadas de maneira acessível."""
        },
        "desenvolvimento": {
            "titulo": "Por que desenvolvemos esse site?",
            "conteudo": """Esse site foi desenvolvido com o intuito de atender ao aumento da demanda por informações e registros sobre 
            as culturas indígenas, que muitas vezes são esquecidas ou mal compreendidas. Ao reunir informações valiosas sobre a história, 
            a cultura e os desafios enfrentados pelos povos indígenas do Rio Grande do Norte, buscamos não apenas preservar esse conhecimento, 
            mas também promover uma maior compreensão e valorização. Este espaço serve como um repositório virtual que apoia o reconhecimento 
            e o respeito por estas comunidades, refletindo a importância de manter viva a memória cultural."""
        },
        "importancia": {
            "titulo": "Qual a importância desse site?",
            "conteudo": """Além de sua função como arquivo digital, o site tem o papel de facilitar a aproximação entre diferentes grupos de pessoas. 
            Ao oferecer acesso a informações bem organizadas, pretendemos estimular a curiosidade e o interesse em conhecer mais sobre os povos 
            indígenas e suas tradições. Acreditamos que, ao promover a educação e a informação, podemos contribuir para um mundo onde o conhecimento 
            cultural dos povos indígenas do RN é protegido e lembrado."""
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

    }

    return render(request, 'dashboard/povos.html', {"page": "povos", "povos": povos} )

def conhecimentos(request):
    textos_conhecimentos = {
        'introd': {
            "introducao_conheci":    """Apesar do Rio Grande do Norte ter um grande histórico de chacina e apagamento dos povos indígenas, ainda permanecem várias tradições de origem indígena no nosso estado no cotidiano, evidenciando que sobreviveram à passagem do tempo. O indígena não se “apagou” totalmente; tanto suas comunidades quanto a sua cultura ainda resistem e convivem no nosso cotidiano, como nas festas, comidas típicas, nomes de cidades, alimentos e palavras usadas no nosso vocabulário diário.  A seguir algumas das tradições e conhecimentos: """
        }
        }

    
    return render(request, 'dashboard/conhecimentos.html', {"page": "conhecimentos", "textos_conhecimentos": textos_conhecimentos} )

def agradecimentos(request):
    return render(request, 'dashboard/agradecimentos.html', {"page": "agradecimentos"} )