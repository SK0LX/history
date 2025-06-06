﻿let crosswordData = null;

async function init() {
    try {
        const response = await fetch('/crossword');
        if (!response.ok) throw new Error('Ошибка получения данных');
        crosswordData = await response.json();
        renderGrid();
        renderClues();
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Не удалось загрузить кроссворд');
    }
}

function renderGrid() {
    if (!crosswordData) return;
    const grid = document.getElementById('crossword-grid');
    const activeArea = getActiveArea();

    grid.style.gridTemplateColumns = `repeat(${activeArea.width}, 30px)`;
    grid.innerHTML = '';

    const startCells = new Map();
    crosswordData.clues.forEach((clue, idx) => {
        const key = `${clue.x - 1}-${clue.y - 1}`;
        startCells.set(key, idx + 1);
    });

    for (let y = activeArea.minY; y <= activeArea.maxY; y++) {
        for (let x = activeArea.minX; x <= activeArea.maxX; x++) {
            const cell = crosswordData.grid[y][x];
            const cellDiv = document.createElement('div');
            cellDiv.className = cell === '#' ? 'cell block' : 'cell';
            cellDiv.dataset.coords = `${x}-${y}`;

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
    return { minX, maxX, minY, maxY, width: maxX - minX + 1, height: maxY - minY + 1 };
}

function renderClues() {
    if (!crosswordData) return;

    const cluesH = crosswordData.clues.filter(c => c.direction === 'horizontal');
    const cluesV = crosswordData.clues.filter(c => c.direction === 'vertical');

    let hIndex = 1;
    let vIndex = 1;
    const startCells = new Map();

    crosswordData.clues.forEach(clue => {
        const key = `${clue.x - 1}-${clue.y - 1}`;
        const number = clue.direction === 'horizontal' ? hIndex++ : vIndex++;
        startCells.set(key, number);
    });

    document.getElementById('clues-horizontal').innerHTML = `
        <h3>Горизонтальные:</h3>
        ${cluesH.map((clue, idx) => `
            <div class="clue">
                <b>${idx + 1}</b>
                <div>${clue.clue}</div>
            </div>
        `).join('')}
    `;

    document.getElementById('clues-vertical').innerHTML = `
        <h3>Вертикальные:</h3>
        ${cluesV.map((clue, idx) => `
            <div class="clue">
                <b>${idx + 1}</b>
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
    if (!crosswordData) return;

    let allCorrect = true;
    const results = [];

    crosswordData.clues.forEach(clue => {
        let userWord = '';
        const startX = clue.x - 1;
        const startY = clue.y - 1;

        for (let i = 0; i < clue.word.length; i++) {
            const x = clue.direction === 'horizontal' ? startX + i : startX;
            const y = clue.direction === 'vertical' ? startY + i : startY;
            const input = document.querySelector(`input[data-x="${x}"][data-y="${y}"]`);
            userWord += input?.value.toUpperCase() || '';
        }

        const isCorrect = userWord === clue.word.toUpperCase();
        if (!isCorrect) allCorrect = false;
        results.push({ clue, isCorrect });
    });

    document.querySelectorAll('.cell').forEach(cell => {
        cell.classList.remove('correct', 'incorrect');
    });

    results.forEach(({ clue, isCorrect }) => {
        const className = isCorrect ? 'correct' : 'incorrect';
        for (let i = 0; i < clue.word.length; i++) {
            const x = clue.direction === 'horizontal' ? clue.x - 1 + i : clue.x - 1;
            const y = clue.direction === 'vertical' ? clue.y - 1 + i : clue.y - 1;
            const cell = document.querySelector(`.cell[data-coords="${x}-${y}"]`);
            if (cell) cell.classList.add(className);
        }
    });

    const existingMessage = document.getElementById('result-message');
    if (existingMessage) existingMessage.remove();

    const resultDiv = document.createElement('div');
    resultDiv.id = 'result-message';
    resultDiv.innerHTML = `
        <div class="result-box">
            ${allCorrect ? 'Секретное слово: Обезьяна Чичичи' : `Правильно: ${results.filter(r => r.isCorrect).length} из ${crosswordData.clues.length}`}
        </div>
    `;
    document.body.appendChild(resultDiv);
    setTimeout(() => resultDiv.remove(), allCorrect ? 5000 : 3000);
}

async function resetCrossword() {
    document.querySelectorAll('.cell input').forEach(input => {
        input.value = '';
        input.parentElement.classList.remove('correct', 'incorrect');
    });
    await init();
}

window.onload = init;