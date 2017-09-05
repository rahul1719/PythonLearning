class SelectionSort:
    unsorted_array = [ 23, 12, 45, 2, 67, 1 ]

    def selectionSort(un_array):
        for i in range (0, len (un_array) - 1):
            low_index = i
            for j in range (i + 1, len (un_array)):
                if un_array[ low_index ] > un_array[ j ]:
                    low_index = j
            temp = un_array[ low_index ]
            un_array[ low_index ] = un_array[ i ]
            un_array[ i ] = temp
        return un_array


print (SelectionSort ().unsorted_array)
