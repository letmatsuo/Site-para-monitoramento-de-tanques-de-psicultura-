import os
import django
import asyncio
from django.utils import timezone
from pymodbus.client.tcp import AsyncModbusTcpClient
from asgiref.sync import sync_to_async

# CONFIGURA DJANGO
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
django.setup()

from peixonauta.models import LeituraAmonia, LeituraPh, LeituraTemperatura, LeituraTurbidez, LeituraO2

# CONFIGURAÇÕES DO ESP32
ESP32_IP = "10.162.157.120"
ESP32_TEMP_PH_IP = "10.162.157.35"
PORTA = 502
REG_AMONIA = 100
REG_TEMPERATURA = 100
REG_PH = 101
REG_TURBIDEZ = 102
REG_O2 = 103

async def ler_e_salvar(nome, client_ip, reg, modelo):
    client = AsyncModbusTcpClient(host=client_ip, port=PORTA, timeout=10)
    await client.connect()
      
    if not client.connected:
        print(f"❌ Não foi possível conectar ao ESP32 ({nome}).")
        return None

    try:
        result = await client.read_holding_registers(address=reg, count=1, device_id=1)
        if result.isError():
            print(f"⚠️ Erro ao ler {nome}.")
            return None

        valor = result.registers[0] / 100.0
        print(f"✅ {nome}: {valor:.2f}")
        await sync_to_async(modelo.objects.create)(valor=valor)
        print(f"💾 {nome} salvo no banco.")
        return valor
    finally:
        client.close()

async def main():
    print("📡 Iniciando leitura e salvamento dos dados...")
    
    await ler_e_salvar("Amônia", ESP32_IP, REG_AMONIA, LeituraAmonia)
    await ler_e_salvar("Temperatura", ESP32_TEMP_PH_IP, REG_TEMPERATURA, LeituraTemperatura)
    await ler_e_salvar("pH", ESP32_TEMP_PH_IP, REG_PH, LeituraPh)
    await ler_e_salvar("Turbidez", ESP32_TEMP_PH_IP, REG_TURBIDEZ, LeituraTurbidez)
    await ler_e_salvar("O2", ESP32_TEMP_PH_IP, REG_O2, LeituraO2)

async def loop_envio(intervalo_segundos=5):
    while True:
        await main()
        print(f"⏳ Esperando {intervalo_segundos} segundos...\n")
        await asyncio.sleep(intervalo_segundos)

if __name__ == "__main__":
    asyncio.run(loop_envio(5))  # roda de 5 em 5 segundos
