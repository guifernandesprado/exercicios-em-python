import sys
import requests
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class JanelaCotacao(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 1. Configurações da Janela Principal
        self.setWindowTitle("Cotação de Moedas")
        self.setFixedSize(360, 380)

        # Estilo Global da Janela (Fundo Escuro Elegante)
        self.setStyleSheet("background-color: #1E1E2E;")

        # Layout Principal com espaçamentos
        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(18)

        # 2. Título / Instrução
        self.texto_orientacao = QLabel("Cotação de Moedas em Tempo Real")
        self.texto_orientacao.setWordWrap(True)
        self.texto_orientacao.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.texto_orientacao.setStyleSheet("""
            QLabel {
                color: #A6ADC8;
                font-size: 15px;
                font-weight: bold;
            }
        """)
        layout.addWidget(self.texto_orientacao)

        # 3. Botão Estilizado
        self.botao = QPushButton("Buscar Cotações")
        self.botao.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao.setStyleSheet("""
            QPushButton {
                background-color: #89B4FA;
                color: #11111B;
                font-size: 14px;
                font-weight: bold;
                border-radius: 8px;
                padding: 12px;
            }
            QPushButton:hover {
                background-color: #B4BEFE;
            }
            QPushButton:pressed {
                background-color: #74C7EC;
            }
        """)
        self.botao.clicked.connect(self.pegar_cotacoes)
        layout.addWidget(self.botao)

        # 4. Cartão / Painel de Resultados (Container com borda e fundo diferenciado)
        self.card_resultado = QFrame()
        self.card_resultado.setStyleSheet("""
            QFrame {
                background-color: #313244;
                border-radius: 12px;
                border: 1px solid #45475A;
            }
        """)

        layout_card = QVBoxLayout(self.card_resultado)

        self.texto_cotacao = QLabel("Clique no botão para carregar")
        self.texto_cotacao.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.texto_cotacao.setStyleSheet("""
            QLabel {
                color: #CDD6F4;
                font-size: 16px;
                font-weight: 500;
                line-height: 1.5;
            }
        """)
        layout_card.addWidget(self.texto_cotacao)

        layout.addWidget(self.card_resultado)

        # Aplica o layout principal
        self.setLayout(layout)

    def pegar_cotacoes(self):
        try:
            requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
            requisicao_dic = requisicao.json()

            cotacao_dolar = float(requisicao_dic['USDBRL']['bid'])
            cotacao_euro = float(requisicao_dic['EURBRL']['bid'])
            cotacao_btc = float(requisicao_dic['BTCBRL']['bid'])

            texto = (
                f"<b>💵 Dólar:</b> R$ {cotacao_dolar:.2f}<br><br>"
                f"<b>💶 Euro:</b> R$ {cotacao_euro:.2f}<br><br>"
                f"<b>₿ BTC:</b> R$ {cotacao_btc:,.2f}"
            )

            # O PySide6 aceita formatação HTML básica no QLabel!
            self.texto_cotacao.setText(texto)
        except Exception:
            self.texto_cotacao.setText("<font color='#F38BA8'>Erro ao buscar cotações!</font>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaCotacao()
    janela.show()
    sys.exit(app.exec())