Write-Output '�N���C�A���g���Z�b�g�A�b�v���܂��B';
Set-Location '../viewer';
try {
    npm install;
}
catch {
    "�C���X�g�[���ɂ́ANode.js ���K�v�ł��B";
    exit;
}

Write-Output '�T�[�o�[���Z�b�g�A�b�v���܂��B';
Set-Location '../server';
try {
    python -m venv venv;
    .\venv\Scripts\activate;
    python -m pip install -r ./venv/requirements.txt;
}
catch {
    "�C���X�g�[���ɂ́APython ���K�v�ł��B";
    exit;
}
pause;
