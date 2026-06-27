from __future__ import annotations

import flet as ft


# =========================================================
# IDENTIDADE VISUAL
# =========================================================
COLOR_BG = "#FFF7F7"
COLOR_SURFACE = "#FFFFFF"
COLOR_SURFACE_ALT = "#FFF1F1"
COLOR_RED = "#E41E2B"
COLOR_RED_HOVER = "#B91620"
COLOR_RED_SOFT = "#FDE7E9"
COLOR_DARK = "#2A1013"
COLOR_TEXT = "#1F2937"
COLOR_MUTED = "#6F5D60"
COLOR_BORDER = "#F0C9CE"
COLOR_SUCCESS = "#1F8B4C"
COLOR_SUCCESS_BG = "#EAF7EF"
COLOR_WARNING = "#C98300"
COLOR_WARNING_BG = "#FFF6E5"
COLOR_INFO = "#2563EB"
COLOR_INFO_BG = "#EAF2FF"
COLOR_ERROR_BG = "#FDECEC"


# =========================================================
# CALLBACKS VAZIOS — APENAS PROTÓTIPO VISUAL
# =========================================================
def adicionar_arquivos(e=None):
    pass


def importar_outlook(e=None):
    pass


def selecionar_layout(e=None):
    pass


def selecionar_todos(e=None):
    pass


def limpar_selecao(e=None):
    pass


def aplicar_rastreabilidade(e=None):
    pass


def remover_selecionado(e=None):
    pass


def limpar_lista(e=None):
    pass


def limpar_trafego(e=None):
    pass


def processar_importacao(e=None):
    pass


def abrir_arquivo(e=None):
    pass


def abrir_pasta(e=None):
    pass


def atualizar_depara(e=None):
    pass


def atualizar_historico(e=None):
    pass


def adicionar_pdfs_bh(e=None):
    pass


def selecionar_pasta_bh(e=None):
    pass


def processar_bh(e=None):
    pass


def gerar_fila_bh(e=None):
    pass


def abrir_fila(e=None):
    pass


def gerar_pedidos(e=None):
    pass


def mover_historico(e=None):
    pass


def abrir_sap(e=None):
    pass


def contar_pedidos(e=None):
    pass


def validar_governanca(e=None):
    pass


def abrir_logs(e=None):
    pass


# =========================================================
# COMPONENTES VISUAIS
# =========================================================
def border_card(color: str = COLOR_BORDER) -> ft.Border:
    return ft.Border.all(1, color)


def card(
    content: ft.Control,
    *,
    padding: int = 16,
    bgcolor: str = COLOR_SURFACE,
    col: dict | int = 12,
    height: int | None = None,
) -> ft.Container:
    return ft.Container(
        content=content,
        bgcolor=bgcolor,
        border=border_card(),
        border_radius=12,
        padding=padding,
        col=col,
        height=height,
    )


def section_title(title: str, subtitle: str | None = None) -> ft.Column:
    controls: list[ft.Control] = [
        ft.Text(title, size=17, weight=ft.FontWeight.BOLD, color=COLOR_DARK)
    ]
    if subtitle:
        controls.append(ft.Text(subtitle, size=11, color=COLOR_MUTED))
    return ft.Column(controls=controls, spacing=3)


def primary_button(text: str, icon, callback, *, expand: bool = False) -> ft.FilledButton:
    return ft.FilledButton(
        content=text,
        icon=icon,
        on_click=callback,
        bgcolor=COLOR_RED,
        color="#FFFFFF",
        expand=expand,
        style=ft.ButtonStyle(
            padding=ft.Padding.symmetric(horizontal=16, vertical=14),
            shape=ft.RoundedRectangleBorder(radius=9),
        ),
    )


def secondary_button(text: str, icon, callback, *, expand: bool = False) -> ft.OutlinedButton:
    return ft.OutlinedButton(
        content=text,
        icon=icon,
        on_click=callback,
        expand=expand,
        style=ft.ButtonStyle(
            color=COLOR_TEXT,
            side=ft.BorderSide(1, COLOR_BORDER),
            padding=ft.Padding.symmetric(horizontal=14, vertical=13),
            shape=ft.RoundedRectangleBorder(radius=9),
        ),
    )


def action_buttons(buttons: list[ft.Control]) -> ft.Row:
    return ft.Row(
        controls=buttons,
        spacing=8,
        run_spacing=8,
        wrap=True,
    )


def metric_card(title: str, value: str, subtitle: str, *, highlight: bool = False) -> ft.Container:
    bg = COLOR_RED if highlight else COLOR_SURFACE
    title_color = "#FFE2E0" if highlight else COLOR_RED
    value_color = "#FFFFFF" if highlight else COLOR_DARK
    subtitle_color = "#FFF2F1" if highlight else COLOR_MUTED
    return ft.Container(
        col={"xs": 12, "sm": 6, "md": 4, "lg": 2},
        bgcolor=bg,
        border=ft.Border.all(1, COLOR_RED if highlight else COLOR_BORDER),
        border_radius=12,
        padding=14,
        content=ft.Column(
            controls=[
                ft.Text(title, size=10, weight=ft.FontWeight.BOLD, color=title_color),
                ft.Text(value, size=24, weight=ft.FontWeight.BOLD, color=value_color),
                ft.Text(subtitle, size=9, color=subtitle_color),
            ],
            spacing=2,
        ),
    )


def status_chip(text: str, bgcolor: str, color: str = COLOR_TEXT) -> ft.Container:
    return ft.Container(
        content=ft.Text(text, size=9, weight=ft.FontWeight.BOLD, color=color),
        bgcolor=bgcolor,
        border_radius=20,
        padding=ft.Padding.symmetric(horizontal=9, vertical=4),
    )


def log_box(title: str, lines: list[str], *, height: int = 210) -> ft.Container:
    return card(
        ft.Column(
            controls=[
                ft.Text(title, size=15, weight=ft.FontWeight.BOLD, color=COLOR_DARK),
                ft.Container(
                    bgcolor="#FBFCFD",
                    border_radius=8,
                    padding=12,
                    height=height,
                    content=ft.ListView(
                        controls=[ft.Text(line, size=10, color=COLOR_TEXT) for line in lines],
                        spacing=7,
                        auto_scroll=False,
                    ),
                ),
            ],
            spacing=10,
        )
    )


def table_container(table: ft.DataTable, *, height: int | None = None) -> ft.Container:
    return ft.Container(
        height=height,
        bgcolor=COLOR_SURFACE,
        border=border_card(),
        border_radius=10,
        padding=8,
        content=ft.Row(
            controls=[table],
            scroll=ft.ScrollMode.AUTO,
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
    )


def make_data_table(columns: list[str], rows: list[list[ft.Control | str]]) -> ft.DataTable:
    return ft.DataTable(
        columns=[
            ft.DataColumn(
                ft.Text(col, size=10, weight=ft.FontWeight.BOLD, color=COLOR_RED)
            )
            for col in columns
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(value if isinstance(value, ft.Control) else ft.Text(str(value), size=10))
                    for value in row
                ]
            )
            for row in rows
        ],
        heading_row_color=COLOR_RED_SOFT,
        heading_row_height=42,
        data_row_min_height=44,
        data_row_max_height=56,
        column_spacing=28,
        horizontal_margin=14,
        divider_thickness=0.6,
        border=ft.Border.all(1, COLOR_BORDER),
        border_radius=8,
    )


def detail_line(label: str, value: str, *, color: str = COLOR_TEXT) -> ft.Column:
    return ft.Column(
        controls=[
            ft.Text(label, size=9, weight=ft.FontWeight.BOLD, color=COLOR_MUTED),
            ft.Text(value, size=10, color=color, selectable=True),
        ],
        spacing=2,
    )


def page_column(controls: list[ft.Control]) -> ft.Column:
    return ft.Column(
        controls=controls,
        spacing=12,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )


# =========================================================
# CABEÇALHO E RESUMO
# =========================================================
def build_header() -> ft.Container:
    return ft.Container(
        bgcolor=COLOR_SURFACE,
        border=ft.Border.only(bottom=ft.BorderSide(1, COLOR_BORDER)),
        padding=ft.Padding.symmetric(horizontal=18, vertical=12),
        content=ft.ResponsiveRow(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    col={"xs": 12, "md": 8},
                    controls=[
                        ft.Container(
                            width=54,
                            height=46,
                            bgcolor=COLOR_RED,
                            border_radius=9,
                            alignment=ft.Alignment.CENTER,
                            content=ft.Text(
                                "RK",
                                color="#FFFFFF",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(
                                    "RoboKOF 3.0",
                                    color=COLOR_RED,
                                    size=22,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(
                                    "Central de importação, padronização e fila operacional",
                                    color=COLOR_MUTED,
                                    size=10,
                                ),
                            ],
                            spacing=0,
                        ),
                    ],
                    spacing=12,
                ),
                ft.Container(
                    col={"xs": 12, "md": 4},
                    alignment=ft.Alignment.CENTER_RIGHT,
                    content=status_chip("Ambiente Operacional", COLOR_RED_SOFT, COLOR_RED),
                ),
            ],
        ),
    )


def build_metrics() -> ft.ResponsiveRow:
    return ft.ResponsiveRow(
        controls=[
            metric_card("Arquivos na fila", "3", "Aguardando importação"),
            metric_card("Layouts vinculados", "2", "Arquivos prontos para processar"),
            metric_card("Processados com sucesso", "1", "Resultado consolidado", highlight=True),
            metric_card("Arquivos com erro", "1", "Itens que exigem revisão"),
            metric_card("Linhas inseridas", "284", "Entrada total na fila"),
        ],
        spacing=10,
        run_spacing=10,
        alignment=ft.MainAxisAlignment.CENTER,
    )


# =========================================================
# ABA 1 — VISÃO GERAL
# =========================================================
def build_overview() -> ft.Control:
    hero = card(
        ft.Column(
            controls=[
                ft.Text("Fluxo atual do RoboKOF", size=21, weight=ft.FontWeight.BOLD, color=COLOR_DARK),
                ft.Text(
                    "Excel/PDF do cliente → leitura inteligente → validação → fila do RoboKOF somente após aprovação.\n"
                    "A importação do Outlook aparece no fluxo geral e também na rotina isolada da Rede BH.",
                    size=11,
                    color=COLOR_MUTED,
                ),
                primary_button(
                    "Importar Outlook geral/BH",
                    ft.Icons.EMAIL,
                    importar_outlook,
                ),
            ],
            spacing=12,
        )
    )

    items = [
        ("Importação", "Recebe arquivos Excel, PDF e MSG de diferentes clientes.", ft.Icons.UPLOAD_FILE),
        ("Padronização", "Normaliza colunas, interpreta datas e aplica mapeamentos por layout.", ft.Icons.TUNE),
        ("Fila operacional", "Consolida a informação no padrão utilizado pelo RoboKOF.", ft.Icons.FORMAT_LIST_BULLETED),
        ("Escalabilidade", "Estrutura preparada para novos layouts, regras e processadores.", ft.Icons.AUTO_GRAPH),
    ]

    cards = ft.ResponsiveRow(
        controls=[
            card(
                ft.Column(
                    controls=[
                        ft.Icon(icon, color=COLOR_RED, size=28),
                        ft.Text(title, size=15, weight=ft.FontWeight.BOLD, color=COLOR_RED),
                        ft.Text(description, size=10, color=COLOR_TEXT),
                    ],
                    spacing=8,
                ),
                col={"xs": 12, "sm": 6},
                height=150,
            )
            for title, description, icon in items
        ],
        spacing=10,
        run_spacing=10,
    )

    return page_column([hero, cards])


# =========================================================
# ABA 2 — IMPORTAÇÃO DE CLIENTES
# =========================================================
def build_importacao() -> ft.Control:
    toolbar = action_buttons(
        [
            primary_button("Adicionar arquivos", ft.Icons.ADD, adicionar_arquivos),
            secondary_button("Outlook geral", ft.Icons.EMAIL, importar_outlook),
            secondary_button("Selecionar layout", ft.Icons.SETTINGS, selecionar_layout),
            secondary_button("Selecionar todos", ft.Icons.SELECT_ALL, selecionar_todos),
            secondary_button("Limpar seleção", ft.Icons.DESELECT, limpar_selecao),
            secondary_button("Rastreabilidade", ft.Icons.SEARCH, aplicar_rastreabilidade),
            secondary_button("Remover", ft.Icons.DELETE_OUTLINE, remover_selecionado),
            secondary_button("Limpar lista", ft.Icons.CLEANING_SERVICES, limpar_lista),
            primary_button("Processar importação", ft.Icons.PLAY_ARROW, processar_importacao),
        ]
    )

    upload = ft.Container(
        bgcolor=COLOR_SURFACE,
        border=ft.Border.all(2, COLOR_BORDER),
        border_radius=12,
        padding=18,
        on_click=adicionar_arquivos,
        content=ft.Row(
            controls=[
                ft.Container(
                    width=58,
                    height=58,
                    bgcolor=COLOR_RED_SOFT,
                    border_radius=12,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Icon(ft.Icons.CLOUD_UPLOAD, color=COLOR_RED, size=30),
                ),
                ft.Column(
                    controls=[
                        ft.Text("Anexe PDFs/Excels aqui", size=15, weight=ft.FontWeight.BOLD, color=COLOR_DARK),
                        ft.Text(
                            "Toque nesta área para selecionar arquivos. Aceita PDF, XLSX, XLS, XLSM e MSG.",
                            size=10,
                            color=COLOR_MUTED,
                        ),
                        ft.Text(
                            "Múltiplos arquivos permitidos por upload ou Importar do Outlook.",
                            size=9,
                            weight=ft.FontWeight.BOLD,
                            color=COLOR_INFO,
                        ),
                    ],
                    spacing=3,
                    expand=True,
                ),
            ],
            spacing=14,
        ),
    )

    status = card(
        ft.Column(
            controls=[
                ft.Text(
                    "Sistema pronto para receber arquivos de clientes.",
                    size=11,
                    weight=ft.FontWeight.BOLD,
                    color=COLOR_MUTED,
                ),
                ft.ProgressBar(value=0.36, color=COLOR_RED, bgcolor=COLOR_RED_SOFT, bar_height=7),
            ],
            spacing=8,
        )
    )

    fila_table = make_data_table(
        ["Sel", "Arquivo", "Tipo", "Layout", "Status", "Lidas", "Válidas", "Desc.", "Inseridas"],
        [
            ["☑", "pedido_miller_195526.pdf", "PDF", "Miller PDF", status_chip("Pronto", COLOR_INFO_BG, COLOR_INFO), "42", "40", "2", "0"],
            ["☑", "pedido_rede_vip.xlsx", "EXCEL", "Rede VIP Excel", status_chip("Sucesso", COLOR_SUCCESS_BG, COLOR_SUCCESS), "128", "128", "0", "128"],
            ["☐", "pedido_sem_layout.pdf", "PDF", "—", status_chip("Aviso", COLOR_WARNING_BG, COLOR_WARNING), "0", "0", "0", "0"],
            ["☐", "arquivo_invalido.xls", "EXCEL", "Layout legado", status_chip("Erro", COLOR_ERROR_BG, COLOR_RED), "16", "0", "16", "0"],
        ],
    )

    queue_panel = card(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        section_title("Fila de importação", "Cores por status para leitura rápida"),
                        ft.Container(expand=True),
                        action_buttons([
                            primary_button("Selecionar todos", ft.Icons.SELECT_ALL, selecionar_todos),
                            secondary_button("Limpar", ft.Icons.DESELECT, limpar_selecao),
                        ]),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        status_chip("Neutro", COLOR_SURFACE_ALT),
                        status_chip("Pronto", COLOR_INFO_BG, COLOR_INFO),
                        status_chip("Sucesso", COLOR_SUCCESS_BG, COLOR_SUCCESS),
                        status_chip("Aviso", COLOR_WARNING_BG, COLOR_WARNING),
                        status_chip("Erro", COLOR_ERROR_BG, COLOR_RED),
                    ],
                    wrap=True,
                    spacing=6,
                ),
                table_container(fila_table),
            ],
            spacing=12,
        ),
        col={"xs": 12, "lg": 8},
    )

    details = card(
        ft.Column(
            controls=[
                section_title("Detalhes do arquivo"),
                detail_line("Arquivo", "pedido_miller_195526.pdf"),
                detail_line("Tipo", "PDF"),
                detail_line("Layout", "Miller PDF"),
                detail_line("Mensagem", "Layout identificado; arquivo pronto para validação."),
                detail_line("Linhas lidas", "42"),
                detail_line("Linhas válidas", "40"),
                detail_line("Linhas descartadas", "2"),
                detail_line("Linhas inseridas", "0"),
                detail_line("Conversão", "possui conversão: SIM | convertidos: 38 | validar: 2"),
                detail_line("Alertas", "2 códigos precisam de conferência"),
                detail_line("Status", "PRONTO PARA PROCESSAR", color=COLOR_INFO),
            ],
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
        ),
        col={"xs": 12, "lg": 4},
        height=520,
    )

    output_table = make_data_table(
        ["Data/hora", "Layout", "Status", "Tipo", "Arquivo gerado"],
        [
            ["27/06/2026 09:42", "Rede VIP Excel", status_chip("Sucesso", COLOR_SUCCESS_BG, COLOR_SUCCESS), "Excel", "VALIDACAO_REDE_VIP.xlsx"],
            ["27/06/2026 09:42", "GERAL", status_chip("Finalizado", COLOR_INFO_BG, COLOR_INFO), "Log", "LOG_IMPORTACAO_094200.txt"],
        ],
    )

    outputs = card(
        ft.Column(
            controls=[
                section_title(
                    "Processamento das Importações dos Clientes",
                    "Arquivos copiados por data/layout para validação e reabertura rápida",
                ),
                action_buttons([
                    secondary_button("Abrir arquivo", ft.Icons.DESCRIPTION, abrir_arquivo),
                    secondary_button("Abrir pasta", ft.Icons.FOLDER_OPEN, abrir_pasta),
                    secondary_button("Atualizar CNPJ/GLN", ft.Icons.SYNC_ALT, atualizar_depara),
                    secondary_button("Atualizar", ft.Icons.REFRESH, atualizar_historico),
                    secondary_button("Limpar tráfego", ft.Icons.CLEANING_SERVICES, limpar_trafego),
                ]),
                table_container(output_table),
            ],
            spacing=12,
        ),
        col={"xs": 12, "lg": 8},
    )

    orientations = card(
        ft.Column(
            controls=[
                section_title("Orientações rápidas"),
                *[
                    ft.Text(text, size=10, color=COLOR_TEXT)
                    for text in [
                        "1. Adicione um ou mais arquivos do cliente.",
                        "2. Marque arquivos do mesmo tipo e aplique o layout em lote.",
                        "3. O seletor mantém PDF com PDF e Excel com Excel.",
                        "4. Gere o Excel de validação antes de TXT/fila.",
                        "5. Depois, siga na aba Operação RoboKOF.",
                    ]
                ],
            ],
            spacing=8,
        ),
        col={"xs": 12, "lg": 4},
    )

    log = log_box(
        "Log operacional",
        [
            "[09:40:01] Interface Flet iniciada com sucesso.",
            "[09:41:06] 3 arquivos adicionados à fila.",
            "[09:41:12] Rastreabilidade simulada concluída.",
            "[09:42:00] Exemplo visual: nenhuma rotina real foi executada.",
        ],
        height=150,
    )

    return page_column(
        [
            toolbar,
            upload,
            status,
            ft.ResponsiveRow(controls=[queue_panel, details], spacing=10, run_spacing=10),
            ft.ResponsiveRow(controls=[outputs, orientations], spacing=10, run_spacing=10),
            log,
        ]
    )


# =========================================================
# ABA 3 — REDE BH
# =========================================================
def build_bh() -> ft.Control:
    header = card(
        ft.ResponsiveRow(
            controls=[
                ft.TextField(
                    label="Data lote/remessa",
                    value="27.06.2026",
                    col={"xs": 12, "sm": 4},
                    border_color=COLOR_BORDER,
                    focused_border_color=COLOR_RED,
                ),
                ft.TextField(
                    label="Saída",
                    value="Resultados/Rede_BH/Pedidos_a_Validar",
                    read_only=True,
                    col={"xs": 12, "sm": 8},
                    border_color=COLOR_BORDER,
                ),
                ft.Text(
                    "Rede BH pronta para gerar pedidos a validar.",
                    col=12,
                    size=10,
                    weight=ft.FontWeight.BOLD,
                    color=COLOR_MUTED,
                ),
            ],
            spacing=10,
            run_spacing=10,
        )
    )

    toolbar = action_buttons(
        [
            primary_button("Adicionar PDFs BH", ft.Icons.ADD, adicionar_pdfs_bh),
            secondary_button("Outlook BH", ft.Icons.EMAIL, importar_outlook),
            secondary_button("Selecionar pasta", ft.Icons.FOLDER, selecionar_pasta_bh),
            secondary_button("Abrir PDF", ft.Icons.PICTURE_AS_PDF, abrir_arquivo),
            secondary_button("Abrir convertido", ft.Icons.DESCRIPTION, abrir_arquivo),
            secondary_button("Limpar", ft.Icons.CLEANING_SERVICES, limpar_lista),
            primary_button("Processar BH para validar", ft.Icons.PLAY_ARROW, processar_bh),
            secondary_button("Gerar fila KOF BH", ft.Icons.FORMAT_LIST_BULLETED, gerar_fila_bh),
        ]
    )

    metrics = ft.ResponsiveRow(
        controls=[
            metric_card("PDFs na fila", "12", "Lote selecionado"),
            metric_card("Pedidos identificados", "11", "Pré-leitura concluída"),
            metric_card("Regra", "BH + GLN", "Base BH e conferência"),
        ],
        spacing=10,
        run_spacing=10,
    )

    bh_table = make_data_table(
        ["Status", "Pedido", "Arquivo", "Alertas"],
        [
            [status_chip("Aguardando", COLOR_SURFACE_ALT), "195526", "BH_LOJA_01_195526.pdf", "—"],
            [status_chip("Processado", COLOR_SUCCESS_BG, COLOR_SUCCESS), "195527", "BH_LOJA_02_195527.pdf", "—"],
            [status_chip("Duplicado", COLOR_WARNING_BG, COLOR_WARNING), "195528", "BH_LOJA_03_195528.pdf", "Não enviar"],
            [status_chip("Fora do layout", COLOR_ERROR_BG, COLOR_RED), "A identificar", "arquivo_recebido.pdf", "Layout inválido"],
        ],
    )

    left = card(
        ft.Column(
            controls=[
                section_title("Pedidos/PDFs BH para validação"),
                table_container(bh_table),
            ],
            spacing=12,
        ),
        col={"xs": 12, "lg": 8},
    )

    right = ft.Column(
        col={"xs": 12, "lg": 4},
        controls=[
            card(
                ft.Column(
                    controls=[
                        section_title("Validação e saídas BH"),
                        secondary_button("Abrir pasta do último lote", ft.Icons.FOLDER_OPEN, abrir_pasta, expand=True),
                        secondary_button("Abrir main de pushes", ft.Icons.TABLE_VIEW, abrir_arquivo, expand=True),
                        secondary_button("Abrir duplicados", ft.Icons.CONTENT_COPY, abrir_pasta, expand=True),
                        secondary_button("Abrir fila KOF BH gerada", ft.Icons.FORMAT_LIST_BULLETED, abrir_arquivo, expand=True),
                    ],
                    spacing=9,
                )
            ),
            card(
                ft.Column(
                    controls=[
                        section_title("Proteções ativas"),
                        ft.Text("• PDF fora do layout BH é bloqueado.", size=10),
                        ft.Text("• Duplicados ficam separados antes da fila KOF.", size=10),
                        ft.Text("• Pedidos com alerta não entram automaticamente.", size=10),
                        ft.Text("• A quantidade BH não usa mapa de produtos.", size=10),
                    ],
                    spacing=7,
                )
            ),
        ],
        spacing=10,
    )

    log = log_box(
        "Log Rede BH",
        [
            "[09:30:00] Aba Rede BH carregada.",
            "[09:31:04] 12 PDFs adicionados ao lote visual.",
            "[09:31:12] 1 possível duplicidade identificada.",
            "[09:31:18] Protótipo: nenhum PDF foi realmente processado.",
        ],
        height=160,
    )

    return page_column(
        [
            header,
            toolbar,
            metrics,
            ft.ResponsiveRow(controls=[left, right], spacing=10, run_spacing=10),
            ft.ProgressBar(value=0.58, color=COLOR_RED, bgcolor=COLOR_RED_SOFT, bar_height=7),
            log,
        ]
    )


# =========================================================
# ABA 4 — OPERAÇÃO ROBOKOF
# =========================================================
def large_action(text: str, subtitle: str, icon, callback, *, primary: bool = True) -> ft.Container:
    button = primary_button(text, icon, callback, expand=True) if primary else secondary_button(text, icon, callback, expand=True)
    return ft.Container(
        col={"xs": 12, "md": 4},
        content=ft.Column(
            controls=[button, ft.Text(subtitle, size=9, color=COLOR_MUTED)],
            spacing=5,
        ),
    )


def build_operacao() -> ft.Control:
    main_actions = card(
        ft.Column(
            controls=[
                section_title(
                    "Ações do processo",
                    "Fluxo principal a partir da fila: abertura, geração e arquivamento no histórico.",
                ),
                ft.ResponsiveRow(
                    controls=[
                        large_action("Abrir arquivo da Fila", "Consulta o Excel operacional.", ft.Icons.DESCRIPTION, abrir_fila),
                        large_action("Gerar pedidos e TXTs", "Executa a geração dos arquivos finais.", ft.Icons.SETTINGS, gerar_pedidos),
                        large_action("Mover para histórico", "Arquiva os resultados e limpa a fila.", ft.Icons.HISTORY, mover_historico),
                    ],
                    spacing=10,
                    run_spacing=10,
                ),
            ],
            spacing=14,
        )
    )

    aux = card(
        ft.Column(
            controls=[
                section_title("Botões auxiliares", "Ações de apoio para consulta e preparação operacional."),
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            col={"xs": 12, "md": 6},
                            content=primary_button("Abrir SAP + transação EDI", ft.Icons.COMPUTER, abrir_sap, expand=True),
                        ),
                        ft.Container(
                            col={"xs": 12, "md": 6},
                            content=primary_button("Contar matrículas + pedidos", ft.Icons.NUMBERS, contar_pedidos, expand=True),
                        ),
                    ],
                    spacing=10,
                    run_spacing=10,
                ),
            ],
            spacing=14,
        )
    )

    progress = card(
        ft.Column(
            controls=[
                section_title("Acompanhamento operacional"),
                ft.Text("Sistema pronto para executar ações operacionais.", size=10, weight=ft.FontWeight.BOLD, color=COLOR_MUTED),
                ft.Row(
                    controls=[
                        ft.ProgressBar(value=0.0, color=COLOR_RED, bgcolor=COLOR_RED_SOFT, expand=True, bar_height=8),
                        ft.Text("0%", size=10, weight=ft.FontWeight.BOLD, color=COLOR_MUTED),
                    ]
                ),
                ft.Container(
                    bgcolor="#FBFCFD",
                    border_radius=8,
                    padding=12,
                    height=190,
                    content=ft.ListView(
                        controls=[
                            ft.Text("Fluxo operacional preservado na aba Operação RoboKOF.", size=10),
                            ft.Text("Protótipo visual: os botões não executam rotinas.", size=10),
                        ],
                        spacing=8,
                    ),
                ),
            ],
            spacing=10,
        )
    )

    return page_column([main_actions, aux, progress])


# =========================================================
# ABA 5 — GOVERNANÇA
# =========================================================
def build_governanca() -> ft.Control:
    body = card(
        ft.Column(
            controls=[
                section_title(
                    "Governança e saúde do Robô KOF",
                    "Validação técnica para ambiente corporativo: estrutura, cadastros CSV, regras de conversão, Excel enterprise, duplicidades e bloqueios de fila.",
                ),
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            col={"xs": 12, "md": 6},
                            content=primary_button("Validar integridade total", ft.Icons.VERIFIED_USER, validar_governanca, expand=True),
                        ),
                        ft.Container(
                            col={"xs": 12, "md": 6},
                            content=secondary_button("Abrir logs de validação", ft.Icons.FOLDER_OPEN, abrir_logs, expand=True),
                        ),
                    ],
                    spacing=10,
                    run_spacing=10,
                ),
                ft.Text("Pronto para validação corporativa.", size=10, weight=ft.FontWeight.BOLD, color=COLOR_MUTED),
                ft.ProgressBar(value=0.18, color=COLOR_RED, bgcolor=COLOR_RED_SOFT, bar_height=8),
                ft.Container(
                    bgcolor="#FBFCFD",
                    border_radius=8,
                    padding=14,
                    height=330,
                    content=ft.ListView(
                        controls=[
                            ft.Text("[09:00:00] Aba de governança iniciada.", size=10),
                            ft.Text("[09:00:01] Estrutura visual pronta para validações futuras.", size=10),
                            ft.Text("[09:00:02] Nenhum script técnico é executado neste protótipo.", size=10),
                        ],
                        spacing=8,
                    ),
                ),
            ],
            spacing=14,
        )
    )
    return page_column([body])


# =========================================================
# APP
# =========================================================
def main(page: ft.Page):
    page.title = "RoboKOF 3.0 — Protótipo Flet"
    page.bgcolor = COLOR_BG
    page.padding = 0
    page.spacing = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.adaptive = True
    page.window.width = 1280
    page.window.height = 820
    page.window.min_width = 380
    page.window.min_height = 640

    page.theme = ft.Theme(
        color_scheme_seed=COLOR_RED,
        font_family="Segoe UI",
        scaffold_bgcolor=COLOR_BG,
        tab_bar_theme=ft.TabBarTheme(
            label_color=COLOR_RED,
            unselected_label_color=COLOR_MUTED,
            indicator_color=COLOR_RED,
            divider_color=COLOR_BORDER,
        ),
    )

    header = build_header()
    metrics = ft.Container(
        padding=ft.Padding.only(left=12, right=12, top=10, bottom=8),
        content=build_metrics(),
    )

    tab_titles = [
        ("Visão geral", ft.Icons.HOME_OUTLINED),
        ("Importação", ft.Icons.UPLOAD_FILE),
        ("Rede BH", ft.Icons.STORE_OUTLINED),
        ("Operação", ft.Icons.SETTINGS_OUTLINED),
        ("Governança", ft.Icons.SECURITY_OUTLINED),
    ]

    tabs = ft.Tabs(
        length=len(tab_titles),
        expand=True,
        content=ft.Column(
            expand=True,
            controls=[
                ft.TabBar(
                    tabs=[ft.Tab(label=title, icon=icon) for title, icon in tab_titles],
                    scrollable=True,
                    tab_alignment=ft.TabAlignment.START,
                ),
                ft.TabBarView(
                    expand=True,
                    controls=[
                        ft.Container(padding=12, content=build_overview()),
                        ft.Container(padding=12, content=build_importacao()),
                        ft.Container(padding=12, content=build_bh()),
                        ft.Container(padding=12, content=build_operacao()),
                        ft.Container(padding=12, content=build_governanca()),
                    ],
                ),
            ],
        ),
    )

    footer = ft.Container(
        bgcolor=COLOR_SURFACE,
        border=ft.Border.only(top=ft.BorderSide(1, COLOR_BORDER)),
        padding=ft.Padding.symmetric(horizontal=16, vertical=9),
        content=ft.Text(
            "Arquivos na fila: 3  |  Layouts vinculados: 2  |  Sucesso: 1  |  Erros: 1  |  Linhas inseridas: 284",
            size=9,
            color=COLOR_MUTED,
        ),
    )

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Column(
                expand=True,
                spacing=0,
                controls=[header, metrics, tabs, footer],
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
