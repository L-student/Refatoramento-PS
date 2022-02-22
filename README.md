# Refatoramento-PS
Este repositório remete á AB2 da disciplina Projeto de Sofware. A seguir estão alguns dos problemas encontrados nos códigos antigos e logo em seguida, as suas solução.

# Duplicate code
No meu projeto, repeti muito código em classes subjacentes por não ter criado uma classe que contenham as mínimas características comuns. 

### Solução: Factory Method
O Factory Method é um padrão criacional de projeto que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados. No meu projeto, repeti muito código em classes subjacentes por não ter criado uma classe que contenham as mínimas características comuns. A seguir, um exemplo: 

- Classe Assalariado com muitas características básicas comuns a outras classes:

![image](https://user-images.githubusercontent.com/61876988/155203377-6a6f725b-6d6b-4fe4-8c9c-4aded3eccd1a.png)

- Classe criada, limpando a classe Assalariado a deixnado com o essencial:

![image](https://user-images.githubusercontent.com/61876988/155203047-30b8147e-1a6e-43fd-9c80-6cffb76d0e12.png)

![image](https://user-images.githubusercontent.com/61876988/155203134-f20d77d5-fd63-49b9-8da5-2fdeacc9c660.png)

# If Statements
Recorrentemente, usei muitos if's repetidos por ser um vício ao programar. 

### Solução: Dispatch Table
- Muitos ifs

![image](https://user-images.githubusercontent.com/61876988/155205307-8977d261-1701-4b37-9862-af8ae44188f9.png)
 
 - Solução criada eliminando if's execcisvos e facilitando a implementação de outras alternativas:

![image](https://user-images.githubusercontent.com/61876988/155207593-0270eb35-999e-41cf-bf2d-00905322798a.png)

Além desses dois citados a cima, também foram implementados alguns outros como o Builder.
Uma nova diferença nesse projeto do passado é que o código foi revisado e implemntado quase que por completo uma GUI.
