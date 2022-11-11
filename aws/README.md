# Amazon Web Services

- Nessa parte vamos explica as principais ferramentas existentes na AWS para os **engenheiro de dados** e vamos indicar suas **funcionalidades** e oque cada uma faz em um sistema sempre vamos colocar de modo que gere um **datalake** no processo de ferramentas.

- Para informaçoes mais detalhadas podemos acessar a [Documentation](https://docs.aws.amazon.com/index.html)

> Oque e um datalake ?

- Um data lake é um repositório centralizado que permite armazenar todos os seus dados estruturados e não estruturados em qualquer escala. Você pode armazenar seus dados como estão, sem precisar primeiro estruturá-los e executar diferentes tipos de análise, desde painéis e visualizações até processamento de big data, análise em tempo real e machine learning para orientar melhores decisões.

> Dicas e Ideias

- Interesante criar um usuario e grupo para cada serviço ultilizado
- usar os serviços de forma separada

# Bucket S3!

[S3](s3/S3%20logo.png)

[Documentação](https://docs.aws.amazon.com/s3/?icmpid=docs_homepage_featuredsvcs)
[Preço](https://aws.amazon.com/pt/s3/pricing/)

O Amazon Simple Storage Service (Amazon S3) é um serviço de armazenamento de objetos que oferece escalabilidade líder do setor, disponibilidade de dados, segurança e performance. Clientes de todos os tamanhos e setores podem usar o Amazon S3 para armazenar e proteger qualquer volume de dados para uma variedade de casos de uso, como data lakes, sites, aplicações móveis, backup e restauração, arquivamento, aplicações corporativas, dispositivos IoT e análises de big data. O Amazon S3 fornece recursos de gerenciamento para que você possa otimizar, organizar e configurar o acesso aos seus dados para atender aos seus requisitos específicos de negócios, organizacionais e de compatibilidade.

- aramazena objetos (csv,excel,imagem)
- arquivos nao publicos tem que colocar a permisao e fazer uma politica de permisao com json
- a politica de permisao e como se fosse um yml so que json
- a origem dos arquivos pode vim de outro seviço da aws
<!-- senha : [OcsbV6rTMn4RA[ -->

> Instalando CLI

# IAM

![IAM](Iam%20logo.png)

[Documentação](https://docs.aws.amazon.com/iam/index.html)

O AWS Identity and Access Management (IAM) é um serviço da web que ajuda você a controlar com segurança o acesso aos recursos da AWS. Você usa o IAM para controlar quem está autenticado (conectado) e autorizado (tem permissões) para usar recursos.

- faz o gerenciamento de acesos e recursos dos serviços ofertados na aws
- sempre quando for usar a ferramenta pegar todas as senha e credenciais pq depois nao da pra recuperar

# EC2

O Amazon Elastic Compute Cloud (Amazon EC2) fornece capacidade de computação escalável na nuvem Amazon Web Services (AWS). O uso do Amazon EC2 elimina a necessidade de investir em hardware antecipadamente, para que você possa desenvolver e implantar aplicativos com mais rapidez. Você pode usar o Amazon EC2 para iniciar quantos servidores virtuais precisar, configurar a segurança e a rede e gerenciar o armazenamento. O Amazon EC2 permite que você aumente ou diminua a escala para lidar com mudanças nos requisitos ou picos de popularidade, reduzindo sua necessidade de prever o tráfego.

[Documentação](https://docs.aws.amazon.com/ec2/index.html)

[Preço](https://aws.amazon.com/pt/ec2/pricing/on-demand/)
