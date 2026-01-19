const plusBtn = document.getElementById('plus');
const minusBtn = document.getElementById('minus');
const resultEl = document.getElementById('result');
const messageEl = document.getElementById('message');

let count = 0;

function update() {
    resultEl.textContent = count;

    if (count > 0) {
        resultEl.style.backgroundColor = 'yellow';
    } else if (count < 0) {
        resultEl.style.backgroundColor = 'green';
    } else {
        resultEl.style.backgroundColor = 'red';
    }

    plusBtn.disabled = count >= 10;
    minusBtn.disabled = count <= -10;

    if (count === 10 || count === -10) {
        messageEl.textContent = 'Вы достигли экстремального значения';
    } else {
        messageEl.textContent = '';
    }
}

plusBtn.addEventListener('click', () => {
    count++;
    update();
});

minusBtn.addEventListener('click', () => {
    count--;
    update();
});

update();