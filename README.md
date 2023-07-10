# ProjetoFinal-LeoHpRosa

# API de Gerenciamento de Plataforma de Cursos

## Documentação:
https://endprojectdjango.onrender.com/api/docs/redoc/

## Introdução

Esta API tem como objetivo gerenciar uma plataforma de cursos com seus devidos conteúdos.

## Produto Mínimo Viável (MVP)

### Usuários
- Para o funcionamento correto, deverá ter 2 níveis de usuário:
  - Estudante
  - Instrutor

### Cursos
- Os usuários deverão ter uma rota para listar os cursos que estão participando.
- Na criação de cursos, deverão ser enviadas informações essenciais como nome, andamento da turma (Não iniciado, em progresso e concluído), data de início e previsão de conclusão.
- Os instrutores poderão estar em vários cursos simultaneamente, porém somente poderão estar em um único curso que está em progresso.
- Os cursos poderão ter vários estudantes e aulas.

### Aulas
- Deverão conter nome, temas abordados nas aulas, conteúdo, link de vídeo (não precisa ser enviado na criação, mas pode ser adicionado posteriormente) e status (se a aula já foi vista/consumida ou não).

### Funcionalidades permitidas aos instrutores
- Poderão criar, atualizar, listar e excluir cursos e aulas.
- Atualizar, listar e excluir estudantes.
- Inserir estudantes aos cursos, sendo que deve haver validação para verificar se os alunos que foram enviados são de fato estudantes.

### Funcionalidades permitidas aos estudantes
- Visualizar e atualizar suas informações de perfil.
- Filtrar detalhes sobre um curso, podendo ver as aulas atreladas a ele.
