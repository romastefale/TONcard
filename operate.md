# Manual de Operação e Implantação (Root Access)

Este documento contém os procedimentos para executar a aplicação localmente e configurar o pipeline de produção.

## 1. Inicialização Local (Ambiente de Testes / Termux / Linux)

Para validar a integridade da aplicação antes do envio para a infraestrutura de nuvem:

1. **Extração:** Descomprima os ficheiros `main.py`, `requirements.txt` e `railway.toml` no seu diretório de trabalho.
2. **Dependências:** Instale os pacotes Python exigidos.
   ```bash
   pip install -r requirements.txt
   
