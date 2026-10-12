# Ground truth sintético
A aplicação declara Electron e cria `BrowserWindow` com `nodeIntegration: false` e `contextIsolation: true`.
`calculateFee` aplica 5% a um argumento convertido para número.
Trata-se de análise estática. O teste não executa a aplicação Electron.
