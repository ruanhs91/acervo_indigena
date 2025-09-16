### Site: Povos Indígenas do Rio Grande do Norte

Esse site foi desenvolvido com o intuito de atender ao aumento da demanda por informações e registros sobre as culturas indígenas, que muitas vezes são esquecidas ou mal compreendidas. Ao reunir informações valiosas sobre a história, a cultura e os desafios enfrentados pelos povos indígenas do Rio Grande do Norte, buscamos não apenas preservar esse conhecimento, mas também promover uma maior compreensão e valorização. Este espaço serve como um repositório virtual que apoia o reconhecimento e o respeito por estas comunidades, refletindo a importância de manter viva a memória cultural.

### Passos para a instalação: 

1. *Clone o repositório*
```bash
https://github.com/ruanhs91/acervo_indigena.git 
```

2. *Crie um ambiente virtual*
```bash 
python -m venv venv 
```

3. *Ative o ambiente virtual*
```bash 
.\venv\Scripts\activate
```

4. *Instale as dependências*
```bash 
pip install -r requirements.txt 
```

5. *Execute as migrações do banco de dados*
```bash
python manage.py makemigrations 
python manage.py migrate
python manage.py loaddata db.json 
```

6. *Inicie o servidor*
```bash
python manage.py runserver 
```
