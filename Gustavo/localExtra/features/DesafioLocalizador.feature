#language: pt

Funcionalidade: Checar a loja mais próxima de minha localização

    Cenario: Localizar a loja mais próxima

        Dado Estou na tela principal do Extra

        Quando Clico na opção localizador de lojas

        Então A página de localização de loja se abrirá

        E Estou na página de localização de loja

        Quando insiro minha localização

        E clico na opção procurar

        Então a loja mais próxima a mim será mostrada