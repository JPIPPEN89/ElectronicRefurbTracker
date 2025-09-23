import time
class Case:
##########
##################################################################
###########  Next is building and connecting the cases as modular as possible
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

    def insertion_sort(self, my_list):
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

    def partition(self, array, begin, end):
        pivot_idx = begin
        for i in range(begin + 1, end + 1):
            if array[i] <= array[begin]:
                pivot_idx += 1
                array[i], array[pivot_idx] = array[pivot_idx], array[i]
        array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
        return pivot_idx

    def quick_sort_recursion(self, array, begin, end):
        if begin >= end:
            return
        pivot_idx = self.partition(array, begin, end)
        self.quick_sort_recursion(array, begin, pivot_idx - 1)
        self.quick_sort_recursion(array, pivot_idx + 1, end)

    def quick_sort(self, array, begin=0, end=None):
        if end is None:
            end = len(array) - 1

        return self.quick_sort_recursion(array, begin, end)

    def new_n(self):
        choice = ''

        while choice != 'y' or 'Y' or 'n' or 'N':

            choice = input('Do you want to input another N (Y/N)? ')

            if choice == 'N' or choice == 'n':
                return
            elif choice == 'Y' or choice == 'y':


    def case_scenarios(self, choice):
        new_choice = input(f'Case Scenarios for {choice}\n'
                       f'--------------------------------------\n'
                       f'1.\tBest Case\n'
                       f'2.\tAverage Case\n'
                       f'3.\tWorst Case\n'
                       f'4.\tExit {choice} Test')


def main_menu():
    choice = input('Select the sorting algorithm you want to test\n'
          '--------------------------------------\n'
          '1.\tBubble Sort\n'
          '2.\tMerge Sort\n'
          '3.\tQuick Sort\n'
          '4.\tInsertion Sort\n'
          '5.\tExit\n')

    choices = {'1': 'Bubble Sort', '2': 'Merge Sort', '3': 'Quick Sort', '4': 'Insertion Sort', '5': 5}

    return choices[choice]





if __name__ == '__main__':
    print("Welcome to the test suite of selected sorting algorithms!")

    choice = 0
    while choice != 5:
        choice = main_menu()