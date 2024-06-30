# sociedade_galactica

Esta é a segunda versão do projeto de Laboratório de Bases de Dados, utilizando: framework Django, PostgreSQL e Docker.

A Primeira versão foi realizada com SGBD Oracle e Django.


--------------------------------------


This is the second version of the Database Laboratory project, using Django framework, PostgreSQL, and Docker.

The first version was implemented with Oracle DBMS and Django.


--------------------------------------

## Detalhes do projeto

### Descrição base de dados

**Estrelas** são corpos celestes identificados pela sua designação de catálogo estelar, além de conter informações como nome, classificação estelar, e massa. Além disso, estrelas possuem coordenadas celestes, que também podem ser utilizadas para referenciar estrelas de forma única. Estrelas dão origem a **Sistemas**, onde cada um é identificado pela sua estrela principal, podendo também ter um nome associado. **Planetas** compõem outra classificação de corpos celestes, usualmente orbitando estrelas, sendo identificados pelas suas respectivas designações astronômicas, além de conter informações como massa, raio, composição atmosférica, e classificação planetária. Tanto planetas quanto estrelas podem orbitar alguma estrela, onde são armazenadas informações sobre a órbita, tais como distância mínima e máxima de entre os dois corpos, e o período de translação. Toda estrela deve obrigatoriamente compor um sistema ou orbitar direta/indiretamente uma estrela que compõe um sistema. Podem existir planetas errantes, i.e., que não orbitam estrelas, e planetas que orbitam mais de uma estrela, i.e., em sistemas múltiplos.

  
Na galáxia, existem **Espécies** de seres vivos, podendo ser inteligentes ou não, identificadas pelos seus nomes científicos. Toda espécie tem um planeta de origem. Conjuntos substanciais de membros da mesma espécie inteligente podem formar **Comunidades**, identificadas pelas suas respectivas espécies e nomes, onde pode-se armazenar informações adicionais como a quantidade de habitantes de cada comunidade. As comunidades normalmente habitam planetas, onde é armazenado o histórico de **Habitações**, com seus respectivos planetas, comunidades, e datas de início e fim. Um planeta pode abrigar múltiplas comunidades em um determinado período de tempo, e comunidades podem migrar ou ser realocadas entre planetas.

  
As **Federações** são grandes organizações formadas por várias nações, sendo identificadas pelo seu nome e contendo a informação sobre a sua data de fundação. Uma **Nação** é qualquer entidade governamental presente na galáxia, sendo identificada pelo seu nome, além de conter informações sobre a quantidade de planetas controlados por ela. Cada nação só pode estar associada a uma federação, e a federação só pode existir se tiver pelo menos uma nação associada. Os planetas cadastrados no sistema podem ser dominados por nações, sendo mantido um histórico de **Dominância**, composta pela nação, pelo planeta e pelas datas de início e fim dessa dominância.

  
Na galáxia, existem ainda **Facções**, que são grupos ideológicos que podem estar presentes em diversas nações, as quais também abrigam várias facções. Elas são identificadas pelo seu nome, e contém informações da quantidade de nações em que está presente e sobre qual a sua ideologia predominante, podendo ser: progressista, totalitária, tradicionalista. As comunidades dos planetas também podem se filiar a uma facção, sendo esta capaz de atender várias comunidades em nações que a abrigam.

  
Entre as diversas nações existentes, podem existir **Líderes**, membros influentes das nações que desempenham papéis-chave para o seu desenvolvimento. Líderes são identificados pelos seus respectivos Cadastros de Pessoa Intergalática (CPIs), além de terem informações armazenadas como nome, cargo, nação, facção, e espécie. Um Líder cadastrado no sistema sempre deve estar associado a uma nação. Os cargos de líderes representam de maneira geral seus papéis em suas respectivas nações, podendo ser: comandante, oficial ou cientista. Cada facção deve ter um único líder para comandá-la, este sendo associado a uma nação onde a facção está presente, e um líder pode participar de apenas de uma facção.


![Imagem Modelo Relacional](sociedade_galactica/djangoapp/app/templates/app/relacional.png)

