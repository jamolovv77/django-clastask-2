from django.shortcuts import render
from django.http import HttpRequest


def home_task (request):
    context  = {
        'name' : 'Abdulloh',
        'age' : 16,
        'adres' : 'PRAFSAYUZZ',
        'number_phone' : '874751001',
        'gender' : 'man'


}
    return render(request, 'index.html', context)



def profile_task (request):
    context  = {
        'emomali_rahmon' : 'Эмомалӣ 👑',
        'full_name' : ' Эмомалӣ Раҳмон ❤️👑',
        'age' : 'Эмомалӣ Раҳмон 74-сола аст. Вай 5 октябри соли 1952 таваллуд шудааст 📆',
        'adres' : 'Муассисаи расмии Президенти Ҷумҳурии Тоҷикистон 📍'
        '— Қасри Миллат — дар шаҳри Душанбе, хиёбони Рудакӣ, '
        'рӯ ба рӯи Боғи устод Рӯдакӣ воқеъ аст.',
        'number' : '+992 (37) 221-69-15 ё +992 (37) 221-48-12 📱'
      


}
    return render(request, 'profile.html', context)




def sadi_task (request):
    context  = {
        'sadriddin_ayni' : 'Садриддин Айнӣ — Сардафтари адабиёти муосири тоҷик',
        'full_name' : '👤 Ному насаб: Садриддин Саидмуродзода Айнӣ',
        'age' : '🎂 Санаи таваллуд: 15 (27) апрели соли 1878',
        'adres' : '🏠 Ҷойи истиқомат дар солҳои охир: шаҳри Сталинобод (ҳоло Душанбе)',
        'chand_umrdid' : '⚰️ Санаи вафот: 15 июли соли 1954',



}
    return render(request, 'sadi.html', context)






def wirinwoh_task (request):
    context  = {
        'wirinwoh_wohtemur' : '👤 Ном: Шоҳтемур',
        'full_name' : '👤 Ному насаб: Шириншоҳ Шоҳтемур. ',
        'age' : '🎂 Санаи таваллуд: 1 декабри соли 1899.',
        'adres' : '🏠 Суроғаи зист: Зодаи деҳаи Поршинев, ноҳияи Шуғнон.',
        'chand_umrdid' : '⚰️ Санаи вафот: 27 октябри соли 1937.',



}
    return render(request, 'wirinwoh.html', context)

