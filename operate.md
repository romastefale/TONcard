# Atalho aceite: TON Storage

Objectivo: `romastefale.ton` servir o `index.html` do Pages.
Nao usar proxy, Docker, Railway nem Termux para isto.

## Ja feito

- HTML no ar: https://romastefale.github.io/TONcard/
- Dominio teu, carteira ligada
- Campo Site ainda vazio

## Passo 1 — pasta so com o cartao

Cria uma pasta, por exemplo `ton-site`, e mete la **apenas** `index.html` na raiz.
Copia o ficheiro de:
https://raw.githubusercontent.com/romastefale/TONcard/main/index.html

A pasta nao pode ter `server.js`, `Dockerfile` nem `node_modules`.

## Passo 2 — criar o Bag ID

Instala o TON Torrent:
https://github.com/xssnick/TON-Torrent/releases

Abre o programa → cria torrent/bag a partir da pasta `ton-site`.
Copia o Bag ID (64 caracteres hex).
Deixa o programa aberto a semear, ou contrata um storage provider.

Nao reutilizes o bag que ja esta no campo Storage do dominio, a menos que tenhas a certeza de que ele contem `index.html` na raiz.

## Passo 3 — gravar no DNS (carteira dona)

1. Abre https://dns.tonkeeper.com/manage?v=0:2cb928e06aee6ee66b8dbfcb657fa1cf4fbb581ff11fefcad95d9c40aa0d06f3
2. Liga a carteira dona do NFT `romastefale.ton`.
3. Campo **Site**.
4. Cola o Bag ID.
5. Marca **Host in TON Storage** (nao e ADNL).
6. Save / confirmar a transacao.
7. Espera 1–2 minutos.

Alternativa no Chrome: extensao MyTonWallet → https://dns.ton.org → romastefale → Edit → Site + checkbox Storage.

## Passo 4 — testar

- https://romastefale.ton.run
- https://romastefale.ton.website
- browser do Tonkeeper: `romastefale.ton`

Chrome normal sem gateway nao resolve `.ton`.

## Se der 502

- O campo Site ainda nao e do tipo Storage, ou ainda nao confirmaste a tx.
- O bag nao tem `index.html` na raiz.
- Ninguem esta a semear o bag.
