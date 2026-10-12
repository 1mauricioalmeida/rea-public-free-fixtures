# REA — laboratório público gratuito com fixtures sintéticas

Este repositório é um *executor público independente* para testar `rea-agents@6.4.0` em runners padrão do GitHub Actions, sem cobrar minutos de GitHub Actions conforme a política de repositórios públicos. **Não** contém projetos, credenciais, código, arquivos ou informações pessoais de terceiros.

## Como usar
1. Crie um repositório público novo e vazio no GitHub, por exemplo `rea-public-free-fixtures`.
2. Publique estes arquivos nesse novo repositório. Não mude o repositório privado atual para público.
3. Na aba Actions, selecione `REA | Public synthetic fixture free runner` > `Run workflow` > `macos`.
4. Consulte `evidence.json`, `inventory-capabilities.json`, `inventory-providers.json`, `evaluation.json` nos artefatos disponíveis para download.

## Segurança e limitações
- Executa **somente** sob `workflow_dispatch` (manual), sem cron, push ou pull request.
- O workflow declara `permissions: contents: read`, `persist-credentials: false`, sem `secrets`.
- Analisa somente o diretório de fixtures sintéticas incluído neste repositório.
- Não executa no computador local; cada job usa runner descartável hospedado pelo GitHub.
- Runners públicos possuem internet, portanto não são air-gapped. A instalação do pacote npm executa código de fornecedor em VM descartável; por isso não forneça secrets.
- Não execute com larger runners, em repositório privado ou com Cloud-hosted environment pago. Runners padrão em públicos são gratuitos segundo a documentação publicada.
- A execução pode continuar bloqueada por uma pendência de faturamento na conta, apesar da regra geral de gratuidade. Não há garantia de desbloqueio até testar.
- Um resultado JSON validado **não** significa precisão forense nem qualificação EFOA completa.

**Referência:** https://docs.github.com/en/actions/concepts/billing-and-usage
