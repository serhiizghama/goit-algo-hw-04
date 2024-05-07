import random
import timeit
from tabulate import tabulate


class SortingPerformance:
    def __init__(self):
        self.fn_map = {
            "Insertion Sort": self.insertion_sort,
            "Merge Sort": self.merge_sort,
            "Quicksort": self.quick_sort,
            "Bubble Sort": self.bubble_sort,
            "Timsorted": sorted,
            "Timsort": lambda x: x[:].sort(),
        }
        self.headers = ["Algorithm", "Small", "Medium", "Large"]

    def insertion_sort(self, arr_):
        for i in range(1, len(arr_)):
            key = arr_[i]
            j = i - 1
            while j >= 0 and arr_[j] > key:
                arr_[j + 1] = arr_[j]
                j -= 1
            arr_[j + 1] = key
        return arr_

    def merge_sort(self, arr_):
        arr = arr_[:]
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        return self.merge(self.merge_sort(left), self.merge_sort(right))

    def merge(self, left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def bubble_sort(self, arr_):
        arr = arr_[:]
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def get_dataset(self, size):
        return [random.randint(0, 1000) for _ in range(size)]

    def run_tests(self):
        table = []
        dataset = [self.get_dataset(10), self.get_dataset(
            100), self.get_dataset(1000)]

        for name, fn in self.fn_map.items():
            row = [name]
            for data in dataset:
                row.append(timeit.timeit(lambda: fn(data), number=30))
            table.append(row)
        return table

    def display_results(self):
        data = self.run_tests()
        print(tabulate(data, self.headers, tablefmt="pipe"))


if __name__ == "__main__":
    sorter = SortingPerformance()
    sorter.display_results()
