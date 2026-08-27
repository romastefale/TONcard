import os
import html
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

TON_WALLET = os.environ.get("TON_WALLET", "EQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM9c")
TG_LINK = os.environ.get("TG_LINK", "https://t.me/")
GITHUB_LINK = os.environ.get("GITHUB_LINK", "https://github.com/")
AVATAR_NAME = os.environ.get("AVATAR_NAME", "Nome Omitido")

app = FastAPI(title="Servico Web3 TON", docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains; preload"
    
    csp = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; "
        "font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; "
        "connect-src 'self'"
    )
    response.headers["Content-Security-Policy"] = csp
    return response

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-PT" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>ID.SYS | Cartão de Visitas</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --bg-color: #000000;
            --text-main: #f3f4f6;
            --text-highlight: #ffffff;
            --accent-red: #ff0033;
            --accent-cyan: #00ffff;
        }
        
        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: 'JetBrains Mono', monospace;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            overscroll-behavior-y: none; 
        }

        .scanlines::before {
            content: " ";
            display: block;
            position: fixed;
            top: 0; left: 0; bottom: 0; right: 0;
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
            z-index: 50;
            background-size: 100% 2px, 3px 100%;
            pointer-events: none;
        }

        ::selection {
            background: var(--accent-red);
            color: #ffffff;
            text-shadow: none;
        }

        .glitch-hover:hover {
            text-shadow: 2px 0 var(--accent-red), -2px 0 var(--accent-cyan);
            animation: glitch-anim 0.2s linear infinite;
        }
        
        @keyframes glitch-anim {
            0% { transform: translate(0) }
            20% { transform: translate(-2px, 1px) }
            40% { transform: translate(-1px, -1px) }
            60% { transform: translate(2px, 1px) }
            80% { transform: translate(1px, -1px) }
            100% { transform: translate(0) }
        }

        .cmd-prompt::before {
            content: "> ";
            color: var(--accent-red);
            font-weight: 900;
        }
        
        .box-border-glow {
            border: 1px solid rgba(255,255,255,0.2);
            background-color: #080808;
            transition: all 0.2s ease-in-out;
        }
        
        @media (hover: hover) {
            .box-border-glow:hover {
                border-color: var(--accent-red);
                background-color: #0a0000;
                box-shadow: inset 0 0 15px rgba(255, 0, 51, 0.1);
            }
        }
        .box-border-glow:active {
            border-color: var(--accent-red);
            background-color: #0a0000;
        }

        .safari-blur {
            -webkit-backdrop-filter: blur(8px);
            backdrop-filter: blur(8px);
        }
    </style>
</head>
<body class="scanlines relative selection:bg-red-600 selection:text-white pb-10 flex flex-col min-h-screen">

    <nav class="fixed top-0 w-full z-40 bg-black/90 border-b border-white/20 px-4 md:px-6 py-4 flex justify-between items-center text-[10px] md:text-xs tracking-[0.2em] uppercase shadow-lg safari-blur">
        <div class="flex items-center gap-2 md:gap-4 truncate">
            <span class="text-white font-extrabold tracking-widest cmd-prompt truncate">ID.SYS</span>
        </div>
        <div class="flex items-center gap-3 text-cyan-500 font-bold tracking-widest">
            <span class="w-2 h-2 rounded-sm bg-cyan-500 animate-pulse"></span>
            <span>STATUS: ONLINE</span>
        </div>
    </nav>

    <main class="flex-grow pt-32 md:pt-40 pb-12 px-4 md:px-12 flex flex-col items-center justify-center relative z-10">
        <div class="w-full max-w-md space-y-12">
            
            <div class="text-center space-y-6">
                <div class="w-24 h-24 mx-auto bg-[#080808] border border-white/20 flex items-center justify-center relative overflow-hidden group transition-all duration-300 hover:border-red-500">
                    <div class="absolute inset-0 bg-red-600/5 group-hover:bg-red-600/20 transition-colors"></div>
                    <i class="fa-solid fa-user-astronaut text-4xl text-white group-hover:text-red-500 transition-colors glitch-hover"></i>
                </div>
                
                <div>
                    <h1 class="text-3xl md:text-4xl font-extrabold tracking-tighter uppercase mb-2 glitch-hover text-white break-words">
                        {{AVATAR_NAME}}
                    </h1>
                    <p class="text-red-500 text-[10px] md:text-xs tracking-[0.2em] md:tracking-[0.3em] uppercase font-bold cmd-prompt">
                        Desenvolvedor Web3
                    </p>
                </div>
            </div>

            <div class="space-y-4 w-full">
                <a href="{{TG_LINK}}" target="_blank" rel="noopener noreferrer" class="block box-border-glow p-5 flex items-center justify-between group cursor-pointer">
                    <div class="flex items-center gap-4">
                        <i class="fa-brands fa-telegram text-2xl text-white group-hover:text-cyan-400 transition-colors"></i>
                        <span class="text-sm font-bold tracking-widest uppercase text-white group-hover:text-red-500 transition-colors">Telegram</span>
                    </div>
                    <i class="fa-solid fa-arrow-right text-white/20 group-hover:text-red-500 text-xs transition-colors"></i>
                </a>

                <a href="{{GITHUB_LINK}}" target="_blank" rel="noopener noreferrer" class="block box-border-glow p-5 flex items-center justify-between group cursor-pointer">
                    <div class="flex items-center gap-4">
                        <i class="fa-brands fa-github text-2xl text-white group-hover:text-cyan-400 transition-colors"></i>
                        <span class="text-sm font-bold tracking-widest uppercase text-white group-hover:text-red-500 transition-colors">GitHub</span>
                    </div>
                    <i class="fa-solid fa-arrow-right text-white/20 group-hover:text-red-500 text-xs transition-colors"></i>
                </a>

                <button onclick="copyWallet()" class="w-full text-left box-border-glow p-5 flex items-center justify-between group cursor-pointer focus:outline-none">
                    <div class="flex items-center gap-4 w-full overflow-hidden">
                        <i class="fa-solid fa-wallet text-2xl text-white group-hover:text-cyan-400 transition-colors shrink-0"></i>
                        <div class="flex flex-col overflow-hidden">
                            <span class="text-sm font-bold tracking-widest uppercase text-white group-hover:text-red-500 transition-colors cmd-prompt">Endereço TON</span>
                            <span class="text-[10px] text-gray-500 tracking-widest truncate mt-1">{{TON_WALLET}}</span>
                        </div>
                    </div>
                    <i class="fa-regular fa-copy text-white/20 group-hover:text-red-500 text-xs transition-colors shrink-0 ml-2"></i>
                </button>
                
                <div id="copy-notification" class="hidden text-center text-cyan-400 text-[10px] font-bold tracking-[0.2em] uppercase mt-2 transition-all">
                    > Hash copiada para a área de transferência <
                </div>
            </div>
        </div>
    </main>

    <footer class="py-10 border-t border-red-900/30 mt-auto relative z-10 w-full">
        <div class="flex justify-center">
            <div class="inline-flex items-center gap-2 md:gap-4 text-[10px] font-bold uppercase tracking-[0.2em] text-red-600">
                <span class="w-8 h-[2px] bg-red-600"></span>
                EOF_REACHED
                <span class="w-8 h-[2px] bg-red-600"></span>
            </div>
        </div>
    </footer>

    <script>
        function copyWallet() {
            const walletAddress = '{{TON_WALLET}}';
            navigator.clipboard.writeText(walletAddress).then(() => {
                const notification = document.getElementById('copy-notification');
                notification.classList.remove('hidden');
                notification.classList.add('fade-in');
                setTimeout(() => {
                    notification.classList.add('hidden');
                    notification.classList.remove('fade-in');
                }, 2500);
            }).catch(err => {
                console.error('Falha de execução [SYS.COPY]: ', err);
            });
        }
    </script>
</body>
</html>
"""

HTML_CONTENT = HTML_TEMPLATE.replace("{{TON_WALLET}}", html.escape(TON_WALLET))\
                            .replace("{{TG_LINK}}", html.escape(TG_LINK))\
                            .replace("{{GITHUB_LINK}}", html.escape(GITHUB_LINK))\
                            .replace("{{AVATAR_NAME}}", html.escape(AVATAR_NAME))

@app.get("/", response_class=HTMLResponse)
async def root():
    return HTML_CONTENT

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "cartao-visitas-ton"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port, proxy_headers=True, forwarded_allow_ips="*")
