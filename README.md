# Simple ML Flask Example

Exemplo simplificado de como implementar uma API para servir um modelo de ML, utilizando o Framework Flask.

## Como Instalar Dependências
```
pip install -r requirements.txt
```

## Como Executar

Para subir a aplicacão, basta executar:

```python
python main.py
```

Um servidor web local (de debug) será inicializado em http://localhost:5000

## Autenticação
```
user: john
pass: doe
```

## Endpoints

### Analise de Sentimento em uma Frase

    /sentimento/<frase>

- Método: GET

- Parâmetro: Qualquer frase em português.


### Cotacão do valor de uma casa


    /cotacao

    
- Método: POST
- Conteudo: application/json
- Formato: 
    ```json
    {
        "tamanho": 150.0,
        "ano": 2003,
        "garagem": 2
    }
    ```


## Treino do Modelo de RLM

Antes de subir a aplicação, verifique se o modelo serializado está no diretório "model/lr_model.pkl".

Caso não exista, o modelo deverá ser treinado novamente, utilzando o [notebook de treino](LR_Train_House_Pricing.ipynb).
