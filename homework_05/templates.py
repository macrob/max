TPL_HEADER = '| Квитки\t| Таксі\t\t| Їжа\t\t| Аерохокей\t| Всього\t| Скільки грошей з кожного\t|'
TPL_CONTENT = '| {tickets} грн\t| {taxi} грн\t| {food} грн\t| {game} грн\t| {total} грн\t| {per_person} грн\t\t\t|'

TAB_LENGTH = 5
TAB_COUNT = TPL_HEADER.count('\t')
TPL_HR = '-' * (len(TPL_HEADER) + TAB_COUNT * TAB_LENGTH)

TPL_OUTPUT = f'{TPL_HR}\n\r{TPL_HEADER}\n\r{TPL_CONTENT}\n\r{TPL_HR}'
