import psutil
import matplotlib.pyplot as plt
import time

# Configurações iniciais
interval = 1  # Intervalo de tempo entre cada leitura (em segundos)
history_len = 60  # Número de pontos de dados para manter no histórico
net_io_counters = psutil.net_io_counters()  # Contadores iniciais
rx_history = [0] * history_len  # Histórico de recebimento de dados
tx_history = [0] * history_len  # Histórico de envio de dados

# Cria o gráfico
fig, ax = plt.subplots()
ax.set_ylim([0, max(net_io_counters.bytes_sent, net_io_counters.bytes_recv)])
line_rx, = ax.plot(rx_history)
line_tx, = ax.plot(tx_history)

# Atualiza o gráfico a cada intervalo de tempo
while True:
    # Coleta as informações de largura de banda
    net_io_counters = psutil.net_io_counters()
    rx_speed = net_io_counters.bytes_recv - rx_history[-1]
    tx_speed = net_io_counters.bytes_sent - tx_history[-1]
    
    # Adiciona as informações ao histórico
    rx_history.append(rx_speed)
    tx_history.append(tx_speed)
    
    # Remove os pontos de dados mais antigos do histórico
    rx_history = rx_history[-history_len:]
    tx_history = tx_history[-history_len:]
    
    # Atualiza o gráfico
    line_rx.set_ydata(rx_history)
    line_tx.set_ydata(tx_history)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.pause(interval)
