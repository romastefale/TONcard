# Operacao TONcard

Objectivo: `romastefale.ton` mostrar o mesmo HTML de `https://romastefale.github.io/TONcard/`.

## Ja feito

- Repositorio: `github.com/romastefale/TONcard` branch `main`
- GitHub Pages activo: `https://romastefale.github.io/TONcard/`
- `index.html` e o cartao
- `main.py` serve o HTML local e usa Pages como fallback
- Dominio `romastefale.ton` existe e a carteira ja esta ligada

## Estado on-chain agora

- Wallet: ligado
- Site / ADNL: vazio (`sites: []`)
- Por isso `https://romastefale.ton.run` e `https://romastefale.ton.website` devolvem 502
- Chrome normal nao resolve `.ton` sem gateway ou extensao TON

Gestao do NFT:
https://dns.tonkeeper.com/manage?v=0:2cb928e06aee6ee66b8dbfcb657fa1cf4fbb581ff11fefcad95d9c40aa0d06f3

## O que falta (so a carteira dona consegue gravar)

Nao existe CNAME de `.ton` para `github.io`. O campo Site tem de apontar para um ADNL ou para um bag de TON Storage.

### Opcao A — TON Storage (mais simples, sem VPS)

1. Empacota uma pasta cuja raiz tenha `index.html`.
2. Publica o bag no TON Storage.
3. No Tonkeeper / dns.tonkeeper.com: Site → Host in TON Storage → cola o Bag ID.
4. Confirma a transacao.
5. Testa `https://romastefale.ton.run`.

### Opcao B — continuar o proxy que ja comecaste

1. Servidor com IP publico ou tunel do `tonutils-reverse-proxy`.
2. Corre `python main.py` na porta 8080.
3. Corre o proxy com `proxy_pass` para `http://127.0.0.1:8080/`.
4. Copia o ADNL que o proxy mostrar.
5. No dns.tonkeeper.com grava esse ADNL no campo Site.
6. Confirma a transacao.
7. Testa `https://romastefale.ton.run`.

Gera um `config.json` novo na primeira execucao. Nao commits chaves.

## Seguranca

O ficheiro antigo `reverse-proxy/config.json` estava publico com chaves privadas.
Trata essas chaves como comprometidas e gera par novo.
