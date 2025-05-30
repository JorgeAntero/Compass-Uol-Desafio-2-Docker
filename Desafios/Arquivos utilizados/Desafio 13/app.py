from datetime import datetime, timezone, timedelta

hoje = datetime.now()
fuso = timezone(timedelta(hours=-3))
fusodata = hoje.astimezone(fuso)
formatado = fusodata.strftime('%d/%m/%Y %H:%M')

print(formatado)