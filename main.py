# Classifique cada item:

# CI, CD (Entrega) ou CD (Implantação). 

# 1. A cada pull request, os testes de pytest rodam automaticamente.

#    Classificação: CI
#    Por quê: Porque executa a tarefa, depois realiza a entrega. 

# 2. Após os testes passarem, um novo container Docker é gerado
#    e armazenado no registry, aguardando aprovação para ir a produção.

#    Classificação: CD
#    Por quê: Porque faz a tarefa de implantação, depois executa.

# 3. Quando o branch main recebe um merge, a API é publicada
#    automaticamente no servidor de produção sem nenhuma aprovação manual.

#    Classificação: CD
#    Por quê: porque publica a API, executa a implantação.  

# 4. O pipeline verifica se o requirements.txt está atualizado
#    em relação às importações do código.
#    Classificação:CD
#    Por quê: Porque automatiza o arquivo txt com a atualização, depois executa. 

# 5. Após o merge, o model.pkl mais recente é baixado do Hugging Face
#    Hub e os testes de predição são executados com ele.
#    Classificação:CI
#    Por quê: Porque executa o modelo, depois entrega. 