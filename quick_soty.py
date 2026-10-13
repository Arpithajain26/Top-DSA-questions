
def partition(a, low, high):
    pivot = a[low]
    i = low
    j = high

    while i < j:
        while a[i] <= pivot and i < high:
            i += 1

        while a[j] > pivot:
            j -= 1

        if i < j:
            a[i], a[j] = a[j], a[i]

    a[low], a[j] = a[j], a[low]
    return j


def quicksort(a, low, high):
    if low < high:
        p = partition(a, low, high)
        quicksort(a, low, p - 1)
        quicksort(a, p + 1, high)


a = [40, 20, 10, 50, 30]
quicksort(a, 0, len(a) - 1)
print(a)
