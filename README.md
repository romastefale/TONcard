# ID.SYS - Web3 Profile & TON DNS Endpoint

Interface web ultraleve construída em Python (FastAPI), concebida para atuar como um cartão de visitas digital acoplado a domínios da rede TON. A arquitetura foi estruturada para orquestração em contentores (Railway) com integração nativa para tráfego reencaminhado via gateways Web3.

## Especificações Técnicas

* **Backend:** FastAPI, Uvicorn (ASGI).
* **Frontend:** HTML embutido de ficheiro único, motor de estilos TailwindCSS via CDN, design reativo e animações keyframe (Glitch/Neon).
* **Roteamento Web3:** O servidor Uvicorn encontra-se configurado (`--proxy-headers`, `--forwarded-allow-ips='*'`) para confiar nos cabeçalhos de rede emitidos por gateways públicos da infraestrutura TON (ex: `.ton.run`).

## Matriz de Segurança

* **Prevenção XSS:** Escapamento obrigatório de carateres (`html.escape`) em todas as variáveis injetadas no DOM.
* **CORS Restrito:** Permissão de interações limitadas estritamente a métodos `GET`.
* **Cabeçalhos HTTP (Middlewares):** Implementação de `Strict-Transport-Security` (HSTS preload), `X-Frame-Options` (DENY), `X-Content-Type-Options` (nosniff) e `Content-Security-Policy` (CSP) estrita, autorizando unicamente origens estáticas predefinidas.
* **Superfície de Reconhecimento:** Documentação automática (Swagger/ReDoc) desativada.

## Variáveis de Ambiente

O serviço consome parâmetros de ambiente para configuração dinâmica, eliminando dependências de dados imobilizados (hardcoded) no repositório:

| Variável | Descrição | Valor Padrão (Fallback) |
| :--- | :--- | :--- |
| `TON_WALLET` | Endereço da carteira na blockchain TON | `EQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM9c` |
| `TG_LINK` | URL do contacto Telegram | `https://t.me/` |
| `GITHUB_LINK` | URL do perfil GitHub | `https://github.com/` |
| `AVATAR_NAME` | Identificação principal apresentada na interface | `Nome Omitido` |

## Estrutura do Orquestrador (Nixpacks)

A implantação no Railway é regida pelo ficheiro `railway.toml`, que força a injeção dos parâmetros de rede adequados na inicialização do serviço e estabelece a rota de _healthcheck_ para monitorização de estabilidade do contentor.
