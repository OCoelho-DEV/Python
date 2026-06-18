# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime

from dateutil.relativedelta import relativedelta

loan_value = 1_000_000
loan_ytime = relativedelta(years=5)
loan_start_date = datetime(2020, 12, 20)
loan_final_date = loan_start_date + loan_ytime

installments_date = []
installment_date = loan_start_date

while installment_date < loan_final_date:
    installments_date.append(installment_date)
    installment_date += relativedelta(months=1)

installments_number = len(installments_date)
installment_value = loan_value / installments_number

for date in installments_date:
    print(date.strftime('%d/%m/%Y'), f'R$ {installment_value:,.2f}')

print(30 * '-')

print(
    f'You paid R$ {loan_value:,}\n'
    f'In {loan_ytime.years} years ({installments_number} months)\n'
    f'For R$ {installment_value:,.2f} per installment\n'
)


