from django.shortcuts import render

from . import cash_flow_db


def render_transaction(request):
    transaction_dict = {
        'id': 6,
        'income': 35000,
        'expense': 0,
        'description': 'Дохід від реалізації послуг',
        'company': 'Big Plus',
        'date_time': '13 July 2024 13:05',
    }
    return render(
        request,
        'example/template_transaction.html',
        context=transaction_dict,
    )


# render function looks into templates folder for a given template mane


def render_real_transactions(request):
    transactions_list = {'all': cash_flow_db.get_all_transaction_records()}
    return render(
        request,
        'example/template_real_transactions.html',
        context=transactions_list,
    )
