ROBOKOF 3.0 - PROTÓTIPO FLET

Este projeto contém apenas a interface visual.
Os callbacks dos botões estão vazios e nenhuma rotina de SAP, Outlook,
Excel, PDF ou fila é executada.

TESTAR NO COMPUTADOR
1. Abra o terminal nesta pasta.
2. Execute:

   python -m pip install -r requirements.txt
   flet run src/main.py

TESTAR NO NAVEGADOR

   flet run --web src/main.py

GERAR APK DE TESTE

   flet build apk

O build Android depende do ambiente Android configurado pelo Flet.
