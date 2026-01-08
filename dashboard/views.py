from django.shortcuts import render

from dashboard.models import TitanicPassenger
from django.db.models import Count

# Create your views here.
def index(request):
    context = {}
 
    total_passenger = TitanicPassenger.objects.count()
    context["total_passenger"] = total_passenger

    total_male = TitanicPassenger.objects.filter(sex="male").count()
    context["total_male"] = total_male
    context["total_female"] = total_passenger - total_male

    total_fare = sum(TitanicPassenger.objects.values_list("fare", flat=True))
    context["total_fare"] = "$ " + str(int(total_fare // 1000)) + "K"

    total_survived = TitanicPassenger.objects.filter(survived=1).count()
    context["total_survived"] = total_survived
    context["survived_rate"] = round(total_survived / total_passenger * 100, 2)

    classes = [1, 2, 3]
    context["classes"] = classes

    counts = TitanicPassenger.objects.values('pclass').annotate(count=Count('pclass')).order_by('pclass')
    count_by_class = [c['count'] for c in counts]
    context["count_by_class"] = count_by_class

    survived_counts = TitanicPassenger.objects.filter(survived=1).values('pclass').annotate(count=Count('pclass')).order_by('pclass')
    survived_by_class = [s['count'] for s in survived_counts]
    context["survived_by_class"] = survived_by_class

    died_by_class = [total - survived for total, survived in zip(count_by_class, survived_by_class)]
    context["died_by_class"] = died_by_class

    top_10_fares_data = (TitanicPassenger.objects.order_by('-fare')[:10].values('name', 'fare'))
    context["top_10_fares"] = [{'Name': item['name'], 'Fare': float(item['fare'])}
    for item in top_10_fares_data
    ]

    embarked_data = (
        TitanicPassenger.objects
        .filter(survived=1) # Apenas sobreviventes
        .exclude(embarked__isnull=True) # Remove nulos
        .values('embarked', 'pclass')
        .annotate(count=Count('id'))
    )

    ports = sorted(list(set(item['embarked'] for item in embarked_data)))
    context["ports"] = ports

    embarked_by_class_matrix = []
    
    for port in ports:
        row = [port]
        for pclass in classes:
            # Encontra a contagem específica para aquele porto e classe
            try:
                count = next(item['count'] for item in embarked_data if item['embarked'] == port and item['pclass'] == pclass)
            except StopIteration:
                count = 0
            row.append(count)
        embarked_by_class_matrix.append(row)

    context["embarked_by_class"] = embarked_by_class_matrix[::-1]
    
    return render(request, "dashboard/index.html", context=context)
