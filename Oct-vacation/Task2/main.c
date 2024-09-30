#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap(int numbers[], int i, int j) {
    // C 语言不像 Python 那样支持 unpack，所以需要一个中间量
    int temp = numbers[i];
    numbers[i] = numbers[j];
    numbers[j] = temp;
}

void bubbleSort(int numbers[], int length) {
    for (int i = length - 1; i > 0; i--) {
        // 排序区间一开始是整个数组，之后逐渐缩小直到 1
        for (int j = 0; j < i; j++) {
            // 一轮冒泡
            if (numbers[j] > numbers[j + 1]) {
                // 如果前一个数比后一个数大，交换两个数
                swap(numbers, j, j + 1);
            }
        }
    }
}

int partition(int numbers[], int left, int right) {
    int l = left, r = right;
    while (l < r) {
        while (l < r && numbers[r] >= numbers[left]) {
            // 从右向左移动，找到第一个小于「哨兵」的数
            r--;
        }
        while (l < r && numbers[l] <= numbers[left]) {
            // 从左向右移动，找到第一个大于「哨兵」的数
            l++;
        }
        // 找到了
        swap(numbers, l, r);
    }
    swap(numbers, l, left);

    // 此时已经完成了一波「哨兵划分」
    return l;  // l 为「哨兵」，即两子数组的分界线
}

void quickSortRecur(int numbers[], int left, int right) {
    if (left >= right) {
        // 排序已经完成
        return;
    }
    // 进行划分，返回「哨兵」的位置（分界线）
    int pivot = partition(numbers, left, right);
    // 分别排序左半部分和右半部分
    quickSortRecur(numbers, left, pivot - 1);
    quickSortRecur(numbers, pivot + 1, right);
}

void quickSort(int numbers[], int length) {
    quickSortRecur(numbers, 0, length - 1);
}


void main() {
    // 测试数据，脸滚键盘瞎打出来的
    int numbers_bubblesort[] = {0, 1, 6, 12, 4, 6, 9, 29, 9, 5, 56, 8, 9, 3, 2, 1, 8, 33, 94};
    int length = sizeof(numbers_bubblesort) / sizeof(numbers_bubblesort[0]);
    int numbers_quicksort[length];
    memcpy(numbers_quicksort, numbers_bubblesort, sizeof(numbers_bubblesort));

    // 进行排序
    bubbleSort(numbers_bubblesort, length);
    printf("Bubble sort: [");

    for (int i = 0; i < length; i++) {
        printf("%d, ", numbers_bubblesort[i]);
    }
    printf("]\n");

    quickSort(numbers_quicksort, length);
    printf("Quick sort: [");

    for (int i = 0; i < length; i++) {
        printf("%d, ", numbers_quicksort[i]);
    }
    printf("]\n");
}