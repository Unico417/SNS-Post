Write-Output 'クライアントをセットアップします。';
Set-Location '../viewer';
try {
    npm install;
}
catch {
    "インストールには、Node.js が必要です。";
    exit;
}

Write-Output 'サーバーをセットアップします。';
Set-Location '../server';
try {
    python -m venv venv;
    .\venv\Scripts\activate;
    python -m pip install -r ./venv/requirements.txt;
}
catch {
    "インストールには、Python が必要です。";
    exit;
}
pause;
