import json
from email.utils import parsedate
import matplotlib.pyplot as plt

with open('table.json', encoding='utf8') as f:
    table = json.loads(f.read())  # Таблица решений задач
with open('failed.json', encoding='utf8') as f:
    failed = json.loads(f.read())  # Данные по ошибкам
with open('messages.json', encoding='utf8') as f:
    messages = json.loads(f.read())  # Полученные сообщения
messages = [(m['subj'].upper(), parsedate(m['date'])) for m in messages]

#график распределения по часам
fig, axs0 = plt.subplots()
messages_hours = []
for i in range(len(messages)):
    messages_hours.append(messages[i][1][3])

axs0.set_title('Распределение по часам')
axs0.set_xlabel('часы отправки')
axs0.set_ylabel('количество отправлений')
axs0.hist(messages_hours, bins=24)
plt.savefig(fname='histograms/hours.png', bbox_inches='tight')
plt.show()
#график распределения отправлений по группам
fig, axs1 = plt.subplots()
messages_groups = []
for i in range (len(messages)):
    messages_groups.append(messages[i][0])
axs1.set_title('Распределение отправлений по группам')
axs1.set_xlabel('группа')
axs1.set_ylabel('количество отправлений')
axs1.hist(messages_groups, bins=50)
plt.savefig(fname='histograms/group_send.png', bbox_inches='tight')
plt.show()
#график распределения верных решений по группам
fig, axs2 = plt.subplots()
messages_right = []
for i in range(len(table['data'])):
    messages_right.append(table['data'][i][0])
axs2.set_title('Распределение верных решений по группам')
axs2.set_xlabel('группа')
axs2.set_ylabel('количество верных решений')
axs2.hist(messages_right, bins=46)
plt.savefig(fname='histograms/right.png', bbox_inches='tight')
plt.show()
#график сложных задач
fig, axs3 = plt.subplots()
tasks = []
for i in range(len(table['data'])):
    tasks.append(table['data'][i][2])
axs3.set_title('Сложность задач')
axs3.set_xlabel('задачи')
axs3.set_ylabel('количество верных решений')
axs3.hist(tasks, bins=6)
plt.savefig(fname='histograms/tasks.png', bbox_inches='tight')
plt.show()