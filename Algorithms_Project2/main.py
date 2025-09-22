import time
class Case:

    def __init__(self):
        self.best_case = []
        self.worst_case= []
        self.average_case = []

    def bubble_sort(self, my_list):
        sorted = False
        for i in range(len(my_list) - 1):
            swap = False
        if not sorted:
            for j in range(len(my_list) - i - 1):
                if my_list[j] > my_list[j + 1]:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                    swap = True
                if not swap:
                    sorted = True
                    break

        return my_list

    def merge_sort(self, my_list):
        if len(my_list) <= 1:
            return my_list
        middle = len(m) // 2
        left = my_list[:middle]
        right = my_list[middle:]
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return list(self.merge(left, right))

    def merge(self, left, right):
        result = []

        left_idx, right_idx = 0, 0
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
        if left_idx < len(left):
            result.extend(left[left_idx:])
        if right_idx < len(right):
            result.extend(right[right_idx:])
        return result

    def insertionSort(self, my_list):
        n = len(my_list)
        pass_count = 0
        swap_count = 0
        comparison_count = 0

        for i in range(1, n):
            pass_count += 1
            key = my_list[i]
            j = i - 1

            # Move elements that are greater than key one position ahead
            while j >= 0:
                comparison_count += 1  # Each iteration is a comparison
                if my_list[j] > key:
                    my_list[j + 1] = my_list[j]
                    swap_count += 1  # Treat shifting as a swap
                else:
                    break  # No need for further comparisons
                j -= 1

            my_list[j + 1] = key  # Insert key in the correct position

        print("Passes:", pass_count)
        print("Swaps:", swap_count)
        print("Comparisons:", comparison_count)
        return list

def main_menu():
    print('Select the sorting algorithm')

if __name__ == '__main__':
    print("Welcome to the test suite of selected sorting algorithms!")