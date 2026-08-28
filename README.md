# TONcard / ID.SYS

Cartao de visitas estatico ligado a `romastefale.ton`.

## URLs

- Web2 (ja no ar): https://romastefale.github.io/TONcard/
- Web3 (falta gravar o campo Site): https://romastefale.ton.run
- Gestao DNS: https://dns.tonkeeper.com/manage?v=0:2cb928e06aee6ee66b8dbfcb657fa1cf4fbb581ff11fefcad95d9c40aa0d06f3

## Como corre

```bash
python main.py
```

Serve `index.html` em `0.0.0.0:${PORT:-8080}`.
`/health` devolve `OK`.
Se o ficheiro local nao existir, busca `https://romastefale.github.io/TONcard/`.

Passos on-chain e de proxy: ver `operate.md`.
