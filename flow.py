# coding: UTF-8
from graphviz import Digraph

dot = Digraph(format="png", comment='フロー')
# dot.attr("node", shape="square", style="filled")
# dot.edge("start","state1",label="0.8")

node_freebitcoin = "FreeBitco.in"
node_bitfun = 'Bit Fun'
node_bonus_bitcoin = 'Bonus Bitcoin'
node_moon_dash = 'Moon Dash'
node_moon_cash = 'Moon Cash'
node_moon_bitcoin = 'Moon Bitcoin'
node_moon_dogecoin = 'Moon Dogecoin'
node_moon_litecioin = 'Moon Litecoin'
node_coinpot = 'CoinPot'
node_grab = '暗号資産をもらう'
node_exchange_title = 'BTCに換金'

dot.node(node_freebitcoin, node_freebitcoin+"\n増やし方が複数ある", style="filled", color='pink', fontstyle="bold")
dot.node(node_grab, node_grab, style="filled", color='lightblue')
dot.node(node_coinpot, node_coinpot, style="filled", color='pink')
dot.node(node_bitfun, node_bitfun, style="filled", color='lightgray')
dot.node(node_bonus_bitcoin, node_bonus_bitcoin, style="filled", color='lightgray')
dot.node(node_moon_dash, node_moon_dash, style="filled", color='lightgray')
dot.node(node_moon_cash, node_moon_cash, style="filled", color='lightgray')
dot.node(node_moon_bitcoin, node_moon_bitcoin, style="filled", color='lightgray')
dot.node(node_moon_dogecoin, node_moon_dogecoin, style="filled", color='lightgray')
dot.node(node_moon_litecioin, node_moon_litecioin, style="filled", color='lightgray')

############### エッジ
dot.edge(node_freebitcoin, node_freebitcoin, label="もらって貯め続ける", fontsize="10")

dot.edge(node_grab, node_freebitcoin)
dot.edge(node_grab, node_bitfun)
dot.edge(node_grab, node_bonus_bitcoin)
dot.edge(node_grab, node_moon_dash)
dot.edge(node_grab, node_moon_cash)
dot.edge(node_grab, node_moon_bitcoin)
dot.edge(node_grab, node_moon_dogecoin)
dot.edge(node_grab, node_moon_litecioin)

dot.edge(node_bitfun, node_coinpot, label="自動送金", fontsize="10")
dot.edge(node_bonus_bitcoin, node_coinpot, label="自動送金", fontsize="10")
dot.edge(node_moon_dash, node_coinpot, label="自動送金", fontsize="10")
dot.edge(node_moon_cash, node_coinpot, label="自動送金", fontsize="10")
dot.edge(node_moon_bitcoin, node_coinpot, label="自動送金", fontsize="10")
dot.edge(node_moon_dogecoin, node_coinpot, label="自動送金", fontsize="10")
dot.edge(node_moon_litecioin, node_coinpot, label="自動送金", fontsize="10")

dot.edge(node_coinpot, node_exchange_title)
dot.edge(node_exchange_title, "出金可能？")
dot.edge("出金可能？", node_freebitcoin, label="送金", fontsize="10")
dot.edge("出金可能？", node_grab, label="繰り返す", fontsize="10", style="bold")


dot.render("flow")
