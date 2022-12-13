# heap sort
input_list=[1.2, 0.22, 0.43, 0.36, 0.39, 0.27]
def Qsort(mass):
    if len(mass) <= 1:
        return mass
    else:
        pillar = mass[0]
        SmallerThanPillar = []
        EqualPillar = []
        BiggerThanPillar = []
        for el in mass:
            if el < pillar:
                SmallerThanPillar.append(el)
            elif el > pillar:
                BiggerThanPillar.append(el)
            else:
                EqualPillar.append(el)
        return Qsort(SmallerThanPillar) + EqualPillar + Qsort(BiggerThanPillar)


def bucket_sort(input_list):
    # Находим максимальное значение в списке. Затем используем длину списка, чтобы определить, какое значение в списке попадет в какой блок
    max_value = max(input_list)
    size = max_value / len(input_list)

    # Создаем n пустых блоков, где n равно длине входного списка
    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([])

        # Помещаем элементы списка в разные блоки на основе size
    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    # Сортируем элементы внутри блоков с помощью сортировки вставкой
    for z in range(len(input_list)):
        Qsort(buckets_list[z])

    # Объединяем блоки с отсортированными элементами в один список
    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]
    return final_output
print(bucket_sort(input_list))