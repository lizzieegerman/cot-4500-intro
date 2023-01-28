from __init__ import *
def array():
    arr = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    for i in range(0, 3):
        for j in range(0, 3):
            if i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = 0
    print(str(arr).replace(' [', '').replace('[', '').replace(']', ''))
    print()

    for i in range(0, 3):
        for j in range(0, 3):
            if i == j:
                arr[i][j] = 1
            else:
                arr[i][j] += 3
    print(str(arr).replace(' [', '').replace('[', '').replace(']', ''))
    print()

    arr = np.delete(arr, 2, 1)
    print(str(arr).replace(' [', '').replace('[', '').replace(']', ''))
    
if __name__ == "__main__":
    array()