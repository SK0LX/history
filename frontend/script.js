// Данные кроссворда
const crosswordData = {
    "metadata": {
        "generated_at": "2025-04-30T10:57:51.680395",
        "width": 15,
        "height": 15,
        "total_words": 13,
        "attempted_words": 14
    },
    "grid": [
        [
            "Ф",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "А",
            "#",
            "#",
            "#"
        ],
        [
            "И",
            "#",
            "К",
            "У",
            "Н",
            "С",
            "Т",
            "К",
            "А",
            "М",
            "Е",
            "Р",
            "А",
            "#",
            "#"
        ],
        [
            "З",
            "#",
            "А",
            "#",
            "#",
            "#",
            "#",
            "Р",
            "#",
            "#",
            "#",
            "Т",
            "#",
            "#",
            "#"
        ],
        [
            "И",
            "#",
            "М",
            "Р",
            "И",
            "Х",
            "М",
            "А",
            "Н",
            "#",
            "#",
            "И",
            "#",
            "#",
            "#"
        ],
        [
            "К",
            "#",
            "Ч",
            "#",
            "#",
            "#",
            "#",
            "Ш",
            "#",
            "Э",
            "#",
            "Л",
            "#",
            "#",
            "#"
        ],
        [
            "А",
            "#",
            "А",
            "#",
            "#",
            "#",
            "#",
            "Е",
            "#",
            "К",
            "#",
            "Л",
            "#",
            "#",
            "#"
        ],
        [
            "С",
            "#",
            "Т",
            "#",
            "#",
            "#",
            "#",
            "Н",
            "#",
            "С",
            "#",
            "Е",
            "#",
            "Ш",
            "#"
        ],
        [
            "Т",
            "А",
            "К",
            "А",
            "Д",
            "Е",
            "М",
            "И",
            "Я",
            "П",
            "#",
            "Р",
            "#",
            "Р",
            "#"
        ],
        [
            "Р",
            "#",
            "А",
            "#",
            "#",
            "#",
            "#",
            "Н",
            "#",
            "Е",
            "Х",
            "И",
            "М",
            "И",
            "Я"
        ],
        [
            "О",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "Н",
            "#",
            "Д",
            "#",
            "Я",
            "#",
            "Ф",
            "#"
        ],
        [
            "Н",
            "Г",
            "И",
            "М",
            "Н",
            "А",
            "З",
            "И",
            "Я",
            "И",
            "#",
            "#",
            "#",
            "Т",
            "#"
        ],
        [
            "О",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "К",
            "#",
            "Ц",
            "#",
            "#",
            "#",
            "#",
            "#"
        ],
        [
            "М",
            "И",
            "Н",
            "Е",
            "Р",
            "А",
            "Л",
            "О",
            "Г",
            "И",
            "Я",
            "#",
            "#",
            "#",
            "#"
        ],
        [
            "И",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "В",
            "#",
            "Я",
            "#",
            "#",
            "#",
            "#",
            "#"
        ],
        [
            "Я",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#",
            "#"
        ]
    ],
    "clues": [
        {
            "word": "КРАШЕНИННИКОВ",
            "clue": "Учёный, описавший природу Камчатки в экспедиции Беринга.",
            "x": 8,
            "y": 2,
            "direction": "vertical",
            "length": 13
        },
        {
            "word": "КУНСТКАМЕРА",
            "clue": "Первый русский музей редкостей, открытый в 1719 г.   ",
            "x": 3,
            "y": 2,
            "direction": "horizontal",
            "length": 11
        },
        {
            "word": "МИНЕРАЛОГИЯ",
            "clue": "Наука о минералах; Ломоносов составил первый каталог коллекций.   ",
            "x": 1,
            "y": 13,
            "direction": "horizontal",
            "length": 11
        },
        {
            "word": "ЭКСПЕДИЦИЯ",
            "clue": " Научное путешествие, как Вторая Камчатская экспедиция Беринга.   ",
            "x": 10,
            "y": 5,
            "direction": "vertical",
            "length": 10
        },
        {
            "word": "АРТИЛЛЕРИЯ",
            "clue": "Род войск, ставший ключевым после победы под Полтавой.",
            "x": 12,
            "y": 1,
            "direction": "vertical",
            "length": 10
        },
        {
            "word": "АСТРОНОМИЯ",
            "clue": "Наука о небесных телах, развитая Брюсом и Рихманом.   ",
            "x": 1,
            "y": 6,
            "direction": "vertical",
            "length": 10
        },
        {
            "word": "ГИМНАЗИЯ",
            "clue": "Предуниверситетское учебное заведение при Петербургской академии.   ",
            "x": 2,
            "y": 11,
            "direction": "horizontal",
            "length": 8
        },
        {
            "word": "КАМЧАТКА",
            "clue": "Полуостров, изученный экспедицией Беринга.",
            "x": 3,
            "y": 2,
            "direction": "vertical",
            "length": 8
        },
        {
            "word": "АКАДЕМИЯ",
            "clue": "Научный центр, основанный Петром I в 1724 году.   ",
            "x": 2,
            "y": 8,
            "direction": "horizontal",
            "length": 8
        },
        {
            "word": "РИХМАН",
            "clue": "Физик, погибший во время экспериментов с атмосферным электричеством.",
            "x": 4,
            "y": 4,
            "direction": "horizontal",
            "length": 6
        },
        {
            "word": "ФИЗИКА",
            "clue": "Естественная наука; Ломоносов разработал молекулярно-кинетическую теорию тепла.   ",
            "x": 1,
            "y": 1,
            "direction": "vertical",
            "length": 6
        },
        {
            "word": "ХИМИЯ",
            "clue": "Наука, одним из основателей которой в России считается Ломоносов.   ",
            "x": 11,
            "y": 9,
            "direction": "horizontal",
            "length": 5
        },
        {
            "word": "ШРИФТ",
            "clue": "Новый гражданский стиль письма, введённый Петром I.   ",
            "x": 14,
            "y": 7,
            "direction": "vertical",
            "length": 5
        }
    ]
}

function init() {
    renderGrid();
    renderClues();
}

// Отрисовка сетки с активной зоной
function renderGrid() {
    const grid = document.getElementById('crossword-grid');
    const activeArea = getActiveArea();

    // Настройка grid
    grid.style.gridTemplateColumns = `repeat(${activeArea.width}, 30px)`;
    grid.innerHTML = '';

    // Нумерация стартовых клеток
    const startCells = new Map();
    crosswordData.clues.forEach((clue, idx) => {
        const key = `${clue.x - 1}-${clue.y - 1}`;
        startCells.set(key, idx + 1);
    });

    // Отрисовка только активной зоны
    for (let y = activeArea.minY; y <= activeArea.maxY; y++) {
        for (let x = activeArea.minX; x <= activeArea.maxX; x++) {
            const cell = crosswordData.grid[y][x];
            const cellDiv = document.createElement('div');
            cellDiv.className = cell === '#' ? 'cell block' : 'cell';
            cellDiv.dataset.coords = `${x}-${y}`;
            // Номер клетки
            const number = startCells.get(`${x}-${y}`);
            if (number) {
                const numDiv = document.createElement('div');
                numDiv.className = 'cell-number';
                numDiv.textContent = number;
                cellDiv.appendChild(numDiv);
            }

            if (cell !== '#') {
                const input = document.createElement('input');
                input.dataset.x = x;
                input.dataset.y = y;
                input.maxLength = 1;
                cellDiv.appendChild(input);
            }
            grid.appendChild(cellDiv);
        }
    }
}

// Определение границ активной зоны
function getActiveArea() {
    let minX = 14, maxX = 0, minY = 14, maxY = 0;
    crosswordData.grid.forEach((row, y) => {
        row.forEach((cell, x) => {
            if (cell !== '#') {
                minX = Math.min(minX, x);
                maxX = Math.max(maxX, x);
                minY = Math.min(minY, y);
                maxY = Math.max(maxY, y);
            }
        });
    });
    return {
        minX, maxX,
        minY, maxY,
        width: maxX - minX + 1,
        height: maxY - minY + 1
    };
}



function renderClues() {
    const cluesH = crosswordData.clues.filter(c => c.direction === 'horizontal');
    const cluesV = crosswordData.clues.filter(c => c.direction === 'vertical');

    // Раздельные счетчики
    let hIndex = 1;
    let vIndex = 1;

    // Обновляем номера в стартовых клетках
    const startCells = new Map();
    crosswordData.clues.forEach(clue => {
        const key = `${clue.x - 1}-${clue.y - 1}`;
        const number = clue.direction === 'horizontal' ? hIndex++ : vIndex++;
        startCells.set(key, number);
    });

    // Отрисовка подсказок
    document.getElementById('clues-horizontal').innerHTML = `
        <h3>Горизонтальные:</h3>
        ${cluesH.map((clue, idx) => `
            <div class="clue">
                <b>${idx + 1}. ${clue.word}</b>
                <div>${clue.clue}</div>
            </div>
        `).join('')}
    `;

    document.getElementById('clues-vertical').innerHTML = `
        <h3>Вертикальные:</h3>
        ${cluesV.map((clue, idx) => `
            <div class="clue">
                <b>${idx + 1}. ${clue.word}</b>
                <div>${clue.clue}</div>
            </div>
        `).join('')}
    `;

    document.querySelectorAll('.cell-number').forEach(el => {
        const coords = el.parentElement.dataset.coords;
        el.textContent = startCells.get(coords) || '';
    });
}

function checkAnswers() {
    let correctCount = 0;
    let totalCells = 0;

    crosswordData.grid.forEach((row, y) => {
        row.forEach((cell, x) => {
            if (cell !== '#') {
                totalCells++;
                const input = document.querySelector(`input[data-x="${x}"][data-y="${y}"]`);
                if (input && input.value.toUpperCase() === cell) {
                    correctCount++;
                    input.parentElement.classList.add('correct');
                } else if (input) {
                    input.parentElement.classList.add('incorrect');
                }
            }
        });
    });

    // Создаем или обновляем блок с результатами
    let resultDiv = document.getElementById('result-message');
    if (!resultDiv) {
        resultDiv = document.createElement('div');
        resultDiv.id = 'result-message';
        document.querySelector('.container').prepend(resultDiv);
    }

    resultDiv.innerHTML = `
        <div class="result-box">
            Правильных ответов: ${correctCount} из ${totalCells}
        </div>
    `;
    setTimeout(() => {
        resultDiv.remove();
    }, 3000);
}

function resetCrossword() {
    document.querySelectorAll('.cell input').forEach(input => {
        input.value = '';
        input.parentElement.classList.remove('correct', 'incorrect');
    });
}
window.onload = init;