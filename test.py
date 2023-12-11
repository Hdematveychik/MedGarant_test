from typing import List, Dict
from datetime import date, datetime, time, timedelta


busy = [
    {'start': '10:30',
     'stop': '10:50'
     },
    {'start': '18:40',
     'stop': '18:50'
     },
    {'start': '14:40',
     'stop': '15:50'
     },
    {'start': '16:40',
     'stop': '17:20'
     },
    {'start': '20:05',
     'stop': '20:20'
     }
]


def get_window(busy_list: list, start_time='09:00', end_time='21:00', window_time=timedelta(minutes=30)) -> List[Dict]:
    open_window = []  # Список свободных окон
    start_time = datetime.combine(date.today(), time.fromisoformat(start_time))  # Начало рабочего дня
    current_end = (start_time + window_time)  # Текущее время конца свободного окна
    end_time = datetime.combine(date.today(), time.fromisoformat(end_time))  # Конец рабочего дня

    while current_end < end_time:

        for i_busy in busy_list:  # Проходим по списку занятого времени
            start_break = datetime.combine(date.today(), time.fromisoformat(i_busy['start']))  # Начало перерыва
            end_break = datetime.combine(date.today(), time.fromisoformat(i_busy['stop']))  # Конец перерыва
            # В случаи, если время следующего окна входит во время перерыва, время начала следующего окна равно времени
            # конца перерыва
            if start_time < start_break < current_end \
                    or start_time < end_break < current_end:
                start_time = end_break
                current_end = (start_time + window_time)

        open_window.append({
            'start': start_time.time().isoformat(timespec='minutes'),
            'stop': current_end.time().isoformat(timespec='minutes')
        })  # Добавляем в список время начала и время конца текущего окна

        start_time = current_end
        current_end = (start_time + window_time)

    return open_window


print(get_window(busy))
