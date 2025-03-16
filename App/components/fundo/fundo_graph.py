import reflex as rx
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import yfinance as yf  # Importamos a biblioteca yfinance


class CryptoState(rx.State):
    df: pd.DataFrame = pd.DataFrame()
    figure: go.Figure = px.line()
    timeframe: str = "1m"  # Valor padrão
    loading: bool = False
    error_message: str = ""

    # Valor inicial do investimento
    initial_investment: float = 100000  # $100,000 USD

    # Alocação do portfolio (em porcentagem)
    btc_allocation: float = 0.40  # 40% em BTC
    eth_allocation: float = 0.30  # 30% em ETH
    bnb_allocation: float = 0.30  # 30% em BNB

    # Símbolos do Yahoo Finance para as criptomoedas
    btc_symbol: str = "BTC-USD"
    eth_symbol: str = "ETH-USD"
    bnb_symbol: str = "BNB-USD"

    @rx.var
    def get_period(self) -> str:
        """Converte o timeframe selecionado para o formato do Yahoo Finance"""
        mapping = {
            "1h": "1d",  # Yahoo não tem dados intra-dia para todas as criptos
            "1d": "1d",  # 1 dia
            "1w": "1wk",  # 1 semana
            "1m": "1mo",  # 1 mês
            "6m": "6mo",  # 6 meses
            "1y": "1y",  # 1 ano
        }
        return mapping.get(self.timeframe, "1mo")  # 1mo é o padrão

    @rx.var
    def get_interval(self) -> str:
        """Define o intervalo de acordo com o timeframe"""
        mapping = {
            "1h": "5m",  # 5 minutos para visualização de 1 hora
            "1d": "1h",  # 1 hora para visualização de 1 dia
            "1w": "1d",  # 1 dia para visualização de 1 semana
            "1m": "1d",  # 1 dia para visualização de 1 mês
            "6m": "1d",  # 1 dia para visualização de 6 meses
            "1y": "1wk",  # 1 semana para visualização de 1 ano
        }
        return mapping.get(self.timeframe, "1d")  # 1d é o padrão

    def update_timeframe(self, value: str):
        """Atualiza o timeframe e refaz o fetch dos dados"""
        self.timeframe = value
        self.fetch_crypto_data()

    def fetch_crypto_data(self):
        """Busca dados de criptomoedas usando Yahoo Finance"""
        self.loading = True
        self.error_message = ""

        try:
            period = self.get_period
            interval = self.get_interval

            print(f"Buscando dados para período: {period}, intervalo: {interval}")

            # Download de dados históricos usando yfinance
            btc_data = yf.download(
                self.btc_symbol,
                period=period,
                interval=interval,
                progress=False,
            )

            eth_data = yf.download(
                self.eth_symbol,
                period=period,
                interval=interval,
                progress=False,
            )

            bnb_data = yf.download(
                self.bnb_symbol,
                period=period,
                interval=interval,
                progress=False,
            )

            # Verificar se os dados foram carregados corretamente
            if btc_data.empty or eth_data.empty or bnb_data.empty:
                raise ValueError("Não foi possível obter dados para um ou mais ativos")

            # Usar a coluna 'Close' para os preços
            btc_prices = btc_data["Close"]
            eth_prices = eth_data["Close"]
            bnb_prices = bnb_data["Close"]

            # Alinhando as datas (usando apenas datas que existem em todos os datasets)
            common_dates = btc_prices.index.intersection(eth_prices.index).intersection(
                bnb_prices.index
            )
            btc_prices = btc_prices[btc_prices.index.isin(common_dates)]
            eth_prices = eth_prices[eth_prices.index.isin(common_dates)]
            bnb_prices = bnb_prices[bnb_prices.index.isin(common_dates)]

            # Calcular quantidades iniciais (baseado no primeiro preço do período)
            btc_qty = (self.initial_investment * self.btc_allocation) / btc_prices.iloc[
                0
            ]
            eth_qty = (self.initial_investment * self.eth_allocation) / eth_prices.iloc[
                0
            ]
            bnb_qty = (self.initial_investment * self.bnb_allocation) / bnb_prices.iloc[
                0
            ]

            # Calcular valor do portfolio ao longo do tempo
            portfolio_df = pd.DataFrame(index=common_dates)
            portfolio_df["BTC_Value"] = btc_prices * btc_qty
            portfolio_df["ETH_Value"] = eth_prices * eth_qty
            portfolio_df["BNB_Value"] = bnb_prices * bnb_qty
            portfolio_df["Total_Value"] = (
                portfolio_df["BTC_Value"]
                + portfolio_df["ETH_Value"]
                + portfolio_df["BNB_Value"]
            )

            # Convertendo para o formato esperado pelo nosso gráfico
            result_df = pd.DataFrame(
                {"date": portfolio_df.index, "value": portfolio_df["Total_Value"]}
            ).reset_index(drop=True)

            self.df = result_df

            # Calcular o retorno percentual
            initial_value = self.df["value"].iloc[0]
            current_value = self.df["value"].iloc[-1]
            return_pct = ((current_value - initial_value) / initial_value) * 100
            return_sign = "+" if return_pct >= 0 else ""

            title = f"Portfolio: {return_sign}{return_pct:.2f}% ({self.timeframe})"

            # Criar gráfico
            fig = px.line(
                self.df,
                x="date",
                y="value",
                title=title,
            )

            # Ajustar cores e estilo para modo claro/escuro
            fig.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font_color="#F7FAFC",
                title_font_size=20,
                xaxis_title="Data",
                yaxis_title="Valor (USD)",
                hovermode="x unified",
                xaxis={"showgrid": False},
                yaxis={"showgrid": True, "gridcolor": "rgba(128,128,128,0.1)"},
            )

            # Definir cor da linha com base no retorno
            line_color = "#4CAF50" if return_pct >= 0 else "#F44336"

            fig.update_traces(
                line=dict(width=3, color=line_color),
                hovertemplate="<b>Data:</b> %{x}<br><b>Valor:</b> $%{y:.2f}<extra></extra>",
            )

            self.figure = fig

        except Exception as e:
            import traceback

            print(f"Erro ao processar dados: {str(e)}")
            traceback.print_exc()
            self.error_message = f"Erro ao carregar dados: {str(e)}"

            # Criar um gráfico vazio em caso de erro
            fig = px.line(
                title="Não foi possível carregar os dados. Tente novamente mais tarde."
            )
            fig.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font_color="#F7FAFC",
            )
            self.figure = fig

        finally:
            self.loading = False


def graph_fundo():
    return rx.vstack(
        rx.heading(
            "Desempenho do Portfolio",
            size="5",
            style={
                "margin_bottom": "1rem",
            },
        ),
        rx.flex(
            rx.text(
                "Período:",
                style={
                    "font_weight": "500",
                    "margin_right": "0.5rem",
                    "align_self": "center",
                },
            ),
            rx.select(
                ["1h", "1d", "1w", "1m", "6m", "1y"],
                default_value="1m",
                on_change=CryptoState.update_timeframe,
                style={
                    "width": "100px",
                    "color": rx.color_mode_cond(light="#2D3748", dark="white"),
                    "background": rx.color_mode_cond(light="white", dark="#2D3748"),
                    "border": rx.color_mode_cond(
                        light="1px solid #E2E8F0", dark="1px solid #4A5568"
                    ),
                },
            ),
            justify_content="flex-end",
            width="100%",
        ),
        rx.cond(
            CryptoState.loading,
            rx.center(
                rx.spinner(size="2", color="orange"), height="400px", width="100%"
            ),
            rx.box(
                rx.cond(
                    CryptoState.error_message != "",
                    rx.text(CryptoState.error_message, color="red"),
                    rx.plotly(
                        data=CryptoState.figure,
                        on_mount=CryptoState.fetch_crypto_data,
                        layout={
                            "autosize": True,
                            "height": 500,
                        },
                        config={"responsive": True},
                    ),
                ),
                width="100%",
                height="500px",
                style={
                    "border_radius": "0.5rem",
                    "overflow": "hidden",
                    "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                    "box_shadow": rx.color_mode_cond(
                        light="0 4px 6px rgba(0,0,0,0.1)",
                        dark="0 4px 6px rgba(0,0,0,0.3)",
                    ),
                    "padding": "1rem",
                },
            ),
        ),
        spacing="4",
        width="100%",
    )
