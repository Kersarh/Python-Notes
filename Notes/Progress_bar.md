TQDM

Эта библиотека отображает индикатор выполнения.

Устанавливаем с помощью pip:

pip install tqdm

Если у вас есть цикл for, использующий функцию range, просто замените его на trange из tqdm.

```python
from tqdm import trange
for i in trange(100):
	sleep(0.01)
```

В более общем случае можно легко зациклить список с помощью tqdm.

```python
from tqdm import tqdm
for e in tqdm([1,2,3,4,5,6,7,8,9]):
	sleep(0.5)
```