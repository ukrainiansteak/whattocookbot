
recipes_list = ['Шакшука', 'Рамен', 'Бургер', 'Боул', 'Борщ',
                'Котлета по-київські', 'Хачапурі', 'Брецель',
                'Китайська локшина з куркою', 'Лазанья', 'Запечена форель',
                'Хумус', 'Нагетси', 'Піца']


def create_recipe(session, model):
    for rec in recipes_list:
        recipe = model(name=rec)
        session.add(recipe)
        session.commit()
