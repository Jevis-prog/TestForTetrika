def merge_intervals(intervals):
    """Объединяет пересекающиеся интервалы."""
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for current_start, current_end in intervals[1:]:
        last_start, last_end = merged[-1]
        if current_start <= last_end:
            merged[-1][1] = max(last_end, current_end)
        else:
            merged.append([current_start, current_end])
    return merged

def clip_intervals(intervals, start, end):
    """Обрезает интервалы границами урока."""
    result = []
    for i in range(0, len(intervals), 2):
        interval_start = max(intervals[i], start)
        interval_end = min(intervals[i + 1], end)
        if interval_start < interval_end:
            result.append([interval_start, interval_end])
    return result

def intersect_intervals(intervals1, intervals2):
    """Находит пересечения двух списков интервалов."""
    i = j = 0
    result = []
    while i < len(intervals1) and j < len(intervals2):
        a_start, a_end = intervals1[i]
        b_start, b_end = intervals2[j]
        start = max(a_start, b_start)
        end = min(a_end, b_end)
        if start < end:
            result.append([start, end])
        if a_end < b_end:
            i += 1
        else:
            j += 1
    return result

def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']

    pupil_intervals = clip_intervals(intervals['pupil'], lesson_start, lesson_end)
    tutor_intervals = clip_intervals(intervals['tutor'], lesson_start, lesson_end)

    merged_pupil = merge_intervals(pupil_intervals)
    merged_tutor = merge_intervals(tutor_intervals)

    intersection = intersect_intervals(merged_pupil, merged_tutor)

    return sum(end - start for start, end in intersection)

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]
c = 1
if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
       print(f'тест {c} пройден')
       c += 1